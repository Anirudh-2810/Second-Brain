"""One-shot: drop small DETACHED components (ruling ticks) from p2 crops.

Keeps the largest CC + any CC >= 25% of it. Safe for our 11 letters
(o,n,u,t,e,c,l,d,y,r,+): none has legitimately detached small parts
(no i-dots/colon enrolled). Manifest backed up (.bak-decc). bb recomputed.
"""
import os, json, shutil
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_002.labeled")
MAN = os.path.join(LIB, "manifest.json")
BAK = os.path.join(LIB, "manifest.json.bak-decc")

import cv2
from glyphs import body_bottom_frac as _bb

manifest = json.load(open(MAN, encoding="utf-8"))
if not os.path.exists(BAK):
    shutil.copy(MAN, BAK)
    print("backup:", os.path.basename(BAK))
mets = manifest.setdefault("metrics", {})
n_clean, n_rm = 0, 0
for ch, files in manifest.get("chars", {}).items():
    for fn in files:
        p = os.path.join(LIB, fn)
        a = np.array(Image.open(p).convert("L"))
        ink = (a < 200).astype(np.uint8)
        nl, lab, stats, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
        if nl <= 2:
            continue  # single component (+background): nothing detached
        areas = stats[1:, cv2.CC_STAT_AREA]
        big = areas.max()
        keep = {i + 1 for i, ar in enumerate(areas) if ar >= 0.25 * big}
        if len(keep) == nl - 1:
            continue
        mask = np.isin(lab, list(keep))
        a = np.where(mask, a, 255).astype(np.uint8)
        Image.fromarray(a).save(p)
        mets.setdefault(fn, {})["bb"] = _bb(a)
        n_clean += 1
        n_rm += (nl - 1) - len(keep)
json.dump(manifest, open(MAN, "w", encoding="utf-8"), indent=2)
print(f"cleaned {n_clean} crops, {n_rm} detached components removed")
print("OK decc")
