"""One-shot: normalize every crop in profile_002.labeled to uniform native
stroke width (= the writer's measured pen, styles/profile_002.style
features.thickness_px, 1.91px).

Why: the pool mixes pure-binary sheet crops (1.91px) with soft-grayscale
cluster crops (2.74-3.82px, bimodal). At render scale (_k=3) every pick
pastes a different weight: 3.8px vs 7.4px strokes in one page. Normalizing
at NATIVE scale makes every pick uniform; the renderer then applies one
fixed correction (inference._match_thickness).

Per crop: binarize at <200 (kills grayscale softness so 3x upscale
behavior is identical for every crop), then erode/dilate on a 4x
supersampled mask (one 3x3-ellipse ring = 0.25px per side) until
2*median(dt) ~= target, max 3 passes. Blobby degenerate variants get
boundary-thinned like everything else (they're small at native scale,
so boundary erosion is reliable there -- unlike at render scale).

Run AFTER _p2_manifest_rebuild.py (which copies raw stage crops back into
the library). Backs the library up to styles/profile_002.labeled.bak-normalize.
"""
import os, json, shutil
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(ROOT, "styles", "profile_002.labeled")
MAN = os.path.join(LIB, "manifest.json")
STYLE = os.path.join(ROOT, "styles", "profile_002.style")
BAK = LIB + ".bak-normalize"

DESCENDERS = set("gjpqy")


def baseline_frac(ch, arr):
    ink = (np.array(arr) < 200)
    if ink.ndim == 3:
        ink = ink[..., 0]
    h = ink.shape[0]
    if h < 4 or not ink.any():
        return 0.62
    roww = ink.sum(axis=1)
    rows = np.where(roww > 0)[0]
    if ch not in DESCENDERS:
        return round(float(rows.max() + 1) / float(h), 3)
    thr = max(1.0, 0.4 * float(roww.max()))
    wide = roww >= thr
    runs, cur = [], None
    for i, w in enumerate(wide):
        if w and cur is None:
            cur = [i, i]
        elif w:
            cur[1] = i
        elif cur is not None and i - cur[1] > 2:
            runs.append(tuple(cur)); cur = None
    if cur is not None:
        runs.append(tuple(cur))
    if not runs:
        return round(float(rows.max() + 1) / float(h), 3)
    best = max(runs, key=lambda r: float(roww[r[0]:r[1] + 1].sum()))
    return round(float(best[1] + 1) / float(h), 3)


def cur_width(a):
    ink = (a > 127).astype(np.uint8)
    if int(ink.sum()) < 10:
        return None
    import cv2
    dt = cv2.distanceTransform(ink, cv2.DIST_L2, 3)
    v = dt[ink > 0]
    return float(np.median(v)) * 2.0


def step_mask(mask, k, erode):
    """Grow/shrink a 0/1 mask by k rings of 0.25px (supersample x4)."""
    import cv2
    h, w = mask.shape
    kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    sup = cv2.resize(mask * 255, None, fx=4.0, fy=4.0,
                     interpolation=cv2.INTER_NEAREST)
    op = cv2.erode if erode else cv2.dilate
    for _ in range(k):
        sup = op(sup, kern)
    return (cv2.resize(sup, (w, h), interpolation=cv2.INTER_AREA) > 127).astype(np.uint8)


def normalize(arr, tgt):
    bw = ((arr < 200) * 255).astype(np.uint8)
    n0 = int((bw > 0).sum())
    if n0 < 12:
        return bw, 0.0, 0.0
    c0 = cur_width(bw)
    cur_mask = (bw > 0).astype(np.uint8)
    cur = c0
    for _ in range(3):
        diff = cur - tgt
        if abs(diff) <= 0.25:
            break
        k = int(round(abs(diff) * 2.0))
        if k < 1:
            break
        nxt = step_mask(cur_mask, k, diff > 0)
        if int(nxt.sum()) < int(0.35 * n0):
            break
        cur_mask = nxt
        cur = cur_width(cur_mask * 255)
        if cur is None:
            break
    return cur_mask * 255, c0, cur


def main():
    tgt = float(json.load(open(STYLE, encoding="utf-8"))
               ["features"].get("thickness_px", 1.91))
    print("target native width: %.2f px" % tgt)
    if not os.path.exists(BAK):
        shutil.copytree(LIB, BAK)
        print("backup ->", BAK)
    man = json.load(open(MAN, encoding="utf-8"))
    chars = man.get("chars", {})
    mets = man.get("metrics", {})
    before, after = [], []
    n_changed = 0
    for ch, fns in chars.items():
        for fn in fns:
            p = os.path.join(LIB, fn)
            if not os.path.exists(p):
                continue
            arr = np.array(Image.open(p).convert("L"))
            out, c0, c1 = normalize(arr, tgt)
            # library convention: ink = 0 (black) on white; normalize() works
            # ink=255 internally, so flip on the way out
            save = 255 - out
            Image.fromarray(save).save(p)
            mets[fn] = {"bb": baseline_frac(ch, save),
                        "q": float((mets.get(fn) or {}).get("q", 1.0))}
            if c0 is not None and abs((c1 or c0) - c0) > 0.25:
                n_changed += 1
            if c0 is not None:
                before.append(c0)
                after.append(c1 if c1 else c0)
    man["metrics"] = mets
    json.dump(man, open(MAN, "w", encoding="utf-8"), indent=2)
    b = np.array(before)
    a = np.array(after)
    print("crops changed: %d / %d" % (n_changed, len(b)))
    print("width before: med=%.2f p10=%.2f p90=%.2f" %
          (np.median(b), np.percentile(b, 10), np.percentile(b, 90)))
    print("width after : med=%.2f p10=%.2f p90=%.2f std=%.3f" %
          (np.median(a), np.percentile(a, 10), np.percentile(a, 90), a.std()))


if __name__ == "__main__":
    main()
