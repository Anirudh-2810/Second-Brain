"""
HandwriteAI - glyph library: harvest REAL glyph crops from the user's sample pages,
so rendering reuses their ink instead of a font. This is the accuracy path:
font rendering ≈ 30-50% feature error; glyph retrieval ≈ 5-15%.

No transcription needed: glyphs are bucketed by shape class, and each input
character maps to its expected bucket (narrow / xheight / ascender / descender / wide).
"""
from __future__ import annotations
import os, json, shutil
from typing import List, Dict
import numpy as np
from PIL import Image

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

from features import load_sample_images, binarize, deskew


def extract_glyphs_from_page(gray: np.ndarray, min_area: int = 60,
                             max_area_frac: float = 0.004,
                             max_w: int = 130, max_h: int = 100,
                             pad: int = 3) -> List[Dict]:
    """Connected-component glyph crops with shape stats.
    HARD SIZE CAPS (the slab incident): joined-up handwriting yields
    line-long components; anything bigger than a large glyph is a
    word/line chunk and must never enter the library. Caps also apply
    relative to page size inside the loop."""
    h, w = gray.shape[:2]
    bw = binarize(gray)
    ink = (bw < 128).astype(np.uint8) * 255
    if not HAS_CV2:
        return []
    n, labels, stats, centroids = cv2.connectedComponentsWithStats(ink, connectivity=8)
    max_area = h * w * max_area_frac
    glyphs = []
    for i in range(1, n):
        x, y, gw, gh, area = (int(stats[i, 0]), int(stats[i, 1]), int(stats[i, 2]),
                              int(stats[i, 3]), int(stats[i, 4]))
        if area < min_area or area > max_area:
            continue
        if gw < 4 or gh < 8 or gw > w * 0.3 or gh > h * 0.5:
            continue
        if gw > max_w or gh > max_h:
            continue  # word/line chunk, not a glyph (see docstring)
        aspect = gw / max(1, gh)
        if aspect > 6.0 or aspect < 0.08:
            continue
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(w, x + gw + pad), min(h, y + gh + pad)
        crop = gray[y0:y1, x0:x1]
        mask = (binarize(crop) < 128)
        if mask.mean() < 0.02 or mask.mean() > 0.9:
            continue
        glyphs.append({"img": crop, "w": x1 - x0, "h": y1 - y0,
                       "area": int(area), "aspect": float(aspect)})
    return glyphs


def bucket_of(gw: int, gh: int, line_h: int) -> str:
    """Coarse shape bucket from geometry relative to line height."""
    r = gh / max(1, line_h)
    aspect = gw / max(1, gh)
    if r > 0.62:
        return "tall"      # ascenders/descenders, capitals
    if aspect < 0.42:
        return "narrow"    # i l t . , : ; ! | '
    if aspect > 1.35:
        return "wide"      # m w M W or joined pairs
    return "xheight"       # a c e n o s u v x z


# heuristic: which bucket each character usually lives in
CHAR_BUCKET = {}
for ch in "iljtfrI.,:;!'|1":
    CHAR_BUCKET[ch] = "narrow"
for ch in "mwMW":
    CHAR_BUCKET[ch] = "wide"
for ch in "bdfhkltABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    CHAR_BUCKET.setdefault(ch, "tall")
for ch in "gjpqy":
    CHAR_BUCKET.setdefault(ch, "tall")  # descenders are tall crops too
# everything else defaults to xheight


def build_library(sample_paths: List[str], out_dir: str,
                  line_h_ref: int = 60) -> Dict:
    # wipe previous harvest: appending across runs mixed stale crops in
    # (the dir once held 3000+ files against a 230-file manifest).
    if os.path.exists(out_dir):
        for fn in os.listdir(out_dir):
            if fn.endswith(".png") or fn == "manifest.json":
                try:
                    os.remove(os.path.join(out_dir, fn))
                except Exception:
                    pass
    os.makedirs(out_dir, exist_ok=True)
    images = load_sample_images(sample_paths)
    buckets: Dict[str, List[str]] = {"narrow": [], "xheight": [], "wide": [], "tall": []}
    widths, heights, areas = [], [], []
    total_cc = 0
    for pi, im in enumerate(images):
        fixed, _ = deskew(im)
        gh_list = extract_glyphs_from_page(fixed)
        total_cc += len(gh_list)
        for gi, g in enumerate(gh_list):
            b = bucket_of(g["w"], g["h"], line_h_ref)
            fname = f"p{pi:02d}_{gi:04d}_{b}.png"
            Image.fromarray(g["img"]).save(os.path.join(out_dir, fname))
            buckets[b].append(fname)
            widths.append(g["w"])
            heights.append(g["h"])
            areas.append(g["area"])
    widths = np.array(widths or [20])
    heights = np.array(heights or [30])
    manifest = {
        "version": "0.1",
        "n_glyphs": int(sum(len(v) for v in buckets.values())),
        "n_pages": len(images),
        "buckets": {k: len(v) for k, v in buckets.items()},
        "width_mean": float(widths.mean()), "width_std": float(widths.std()),
        "height_mean": float(heights.mean()), "height_std": float(heights.std()),
        "files": buckets,
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    return manifest


def load_library(lib_dir: str):
    manifest_path = os.path.join(lib_dir, "manifest.json")
    if not os.path.exists(manifest_path):
        return None, None
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    med_w = float(manifest.get("width_mean", 25) or 25)
    med_h = float(manifest.get("height_mean", 25) or 25)
    cache = {}
    for bucket, files in manifest.get("files", {}).items():
        cache[bucket] = []
        for fn in files:
            p = os.path.join(lib_dir, fn)
            if os.path.exists(p):
                try:
                    arr = np.array(Image.open(p).convert("L"))
                    gh, gw = arr.shape[:2]
                    # load-time guard: word/line chunks can never render,
                    # even if an old manifest references them (slab incident)
                    if gw > 5 * med_w or gh > 4 * med_h:
                        continue
                    cache[bucket].append(arr)
                except Exception:
                    continue
    return manifest, cache


def sanitize_library(lib_dir: str) -> Dict:
    """Rescue an existing library: delete monster crops + stale files,
    rewrite the manifest. Returns the new manifest."""
    manifest_path = os.path.join(lib_dir, "manifest.json")
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    med_w = float(manifest.get("width_mean", 25) or 25)
    med_h = float(manifest.get("height_mean", 25) or 25)
    keep: Dict[str, List[str]] = {}
    removed, widths, heights = 0, [], []
    referenced = set()
    for bucket, files in manifest.get("files", {}).items():
        keep[bucket] = []
        for fn in files:
            referenced.add(fn)
            p = os.path.join(lib_dir, fn)
            if not os.path.exists(p):
                removed += 1
                continue
            try:
                arr = np.array(Image.open(p).convert("L"))
                gh, gw = arr.shape[:2]
            except Exception:
                removed += 1
                continue
            if gw > 5 * med_w or gh > 4 * med_h or gw > 130 or gh > 100:
                os.remove(p)
                removed += 1
                continue
            keep[bucket].append(fn)
            widths.append(gw)
            heights.append(gh)
    # sweep stale files no manifest references (append-across-runs leftovers)
    stale = 0
    for fn in os.listdir(lib_dir):
        if fn.endswith(".png") and fn not in referenced:
            try:
                os.remove(os.path.join(lib_dir, fn))
                stale += 1
            except Exception:
                pass
    widths = np.array(widths or [20])
    heights = np.array(heights or [30])
    manifest["files"] = keep
    manifest["n_glyphs"] = int(sum(len(v) for v in keep.values()))
    manifest["buckets"] = {k: len(v) for k, v in keep.items()}
    manifest["width_mean"] = float(widths.mean())
    manifest["width_std"] = float(widths.std())
    manifest["height_mean"] = float(heights.mean())
    manifest["height_std"] = float(heights.std())
    manifest["sanitized"] = {"removed_monsters": removed, "removed_stale": stale}
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    return manifest


def pick_glyph(cache: Dict, bucket: str, rng) -> np.ndarray | None:
    opts = cache.get(bucket) or cache.get("xheight") or []
    if not opts:
        for v in cache.values():
            if v:
                opts = v
                break
    if not opts:
        return None
    return opts[int(rng.integers(0, len(opts)))]
