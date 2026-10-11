"""
HandwriteAI - glyph library: harvest REAL glyph crops from the user's sample pages,
so rendering reuses their ink instead of a font. This is the accuracy path:
font rendering ≈ 30-50% feature error; glyph retrieval ≈ 5-15%.

No transcription needed: glyphs are bucketed by shape class, and each input
character maps to its expected bucket (narrow / xheight / ascender / descender / wide).
"""
from __future__ import annotations
import os, json, shutil
from typing import List, Dict, Tuple
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


def body_bottom_frac(arr: np.ndarray) -> float:
    """Baseline anchor of a glyph crop as a fraction of its height.

    Lowest substantial-ink run by AREA (not the first, not the last).
    For `a`/`h` that is the ink bottom (= the writing baseline); for
    `g`/`y` the descender tail is a separate thinner run below a long gap
    and the tail's end-hook is wide, so a naive "lowest wide row" rule
    anchored y at the tail tip (bb~0.96) — 'you' rendered as a giant J.
    Largest-area beats first-run: a detached i-dot is a tiny run above the
    stem and must not steal the anchor. 2-row gap tolerance bridges
    body-internal dips without swallowing tails. Neutral 0.62 when
    degenerate.
    """
    try:
        ink = (np.array(arr) < 200)
        if ink.ndim == 3:
            ink = ink[..., 0]
        h = ink.shape[0]
        if h < 4 or not ink.any():
            return 0.62
        roww = ink.sum(axis=1)
        thr = max(1.0, 0.35 * float(roww.max()))
        wide = roww >= thr
        runs, cur = [], None
        for i, w in enumerate(wide):
            if w and cur is None:
                cur = [i, i]
            elif w:
                cur[1] = i
            elif cur is not None:
                if i - cur[1] > 2:
                    runs.append(tuple(cur))
                    cur = None
        if cur is not None:
            runs.append(tuple(cur))
        if not runs:
            return 0.62
        best = max(runs, key=lambda r: float(roww[r[0]:r[1] + 1].sum()))
        return round(float(best[1] + 1) / float(h), 3)
    except Exception:
        return 0.62


def estimate_page_line_h(gray: np.ndarray) -> float:
    """Ruled-line height of one sample page: median line-strip height.
    This is the reference bucket_of() thresholds are relative to, so a
    phone photo at 150dpi and a scan at 300dpi classify identically (D3).
    Returns 0.0 when no line structure is found (caller falls back)."""
    from features import extract_lines, deskew as _deskew
    try:
        fixed, _ = _deskew(gray)
        strips = extract_lines(fixed)
        hs = [s.shape[0] for s in strips if s.shape[0] >= 12]
        if len(hs) >= 2:
            return float(np.median(hs))
    except Exception:
        pass
    return 0.0


def build_library(sample_paths: List[str], out_dir: str,
                  line_h_ref: int | None = None) -> Dict:
    # line_h_ref=None (default) derives the reference from the pages
    # themselves: median per-page line-strip height. A fixed 60px assumed
    # one DPI; per-page derivation keeps tall/narrow/xheight/wide honest
    # across phone photos and scans (D3). Pass an int to force a value.
    if os.path.exists(out_dir):
        for fn in os.listdir(out_dir):
            if fn.endswith(".png") or fn == "manifest.json":
                try:
                    os.remove(os.path.join(out_dir, fn))
                except Exception:
                    pass
    os.makedirs(out_dir, exist_ok=True)
    images = load_sample_images(sample_paths)
    if line_h_ref is None:
        per_page = [estimate_page_line_h(im) for im in images]
        per_page = [v for v in per_page if v >= 24]
        line_h_ref = int(round(float(np.median(per_page)))) if per_page else 60
    buckets: Dict[str, List[str]] = {"narrow": [], "xheight": [], "wide": [], "tall": []}
    metrics: Dict[str, Dict] = {}
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
            metrics[fname] = {"bb": body_bottom_frac(g["img"])}
            widths.append(g["w"])
            heights.append(g["h"])
            areas.append(g["area"])
    widths = np.array(widths or [20])
    heights = np.array(heights or [30])
    manifest = {
        "version": "0.2-glyph",
        "n_glyphs": int(sum(len(v) for v in buckets.values())),
        "n_pages": len(images),
        "line_h_ref": int(line_h_ref),
        "buckets": {k: len(v) for k, v in buckets.items()},
        "width_mean": float(widths.mean()), "width_std": float(widths.std()),
        "height_mean": float(heights.mean()), "height_std": float(heights.std()),
        "files": buckets,
        "metrics": metrics,
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
    mets = manifest.get("metrics", {}) or {}
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
                    bb = float((mets.get(fn) or {}).get("bb", 0.0)) or 0.0
                    if not (0.0 < bb <= 1.0):
                        bb = body_bottom_frac(arr)
                    cache[bucket].append((arr, bb))
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


def pick_glyph(cache: Dict, bucket: str, rng) -> Tuple[np.ndarray | None, float]:
    """Random crop from a bucket. Returns (array, body_bottom_frac);
    (None, 0.62) when empty."""
    opts = cache.get(bucket) or cache.get("xheight") or []
    if not opts:
        for v in cache.values():
            if v:
                opts = v
                break
    if not opts:
        return None, 0.62
    pick = opts[int(rng.integers(0, len(opts)))]
    if isinstance(pick, tuple):
        return pick
    return pick, body_bottom_frac(pick)
