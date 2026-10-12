"""One-shot: erase thin DETACHED bottom blocks (ruling) from p2 crops.

Passes 1-2 missed these: ruling segments spanning only ~60% of crop width.
Rule: from the bottom, skip blanks; if the bottom ink block is <=4px tall
AND separated by >=2 blank rows from ink above, erase it (once per crop).
y-tails survive (tall + connected). bb recomputed. Backup .bak-ruling3.
"""
import os, json, shutil
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_002.labeled")
MAN = os.path.join(LIB, "manifest.json")
BAK = os.path.join(LIB, "manifest.json.bak-ruling3")

from glyphs import body_bottom_frac as _bb

manifest = json.load(open(MAN, encoding="utf-8"))
if not os.path.exists(BAK):
    shutil.copy(MAN, BAK)
    print("backup:", os.path.basename(BAK))
mets = manifest.setdefault("metrics", {})
n_clean = 0
for ch, files in manifest.get("chars", {}).items():
    for fn in files:
        p = os.path.join(LIB, fn)
        a = np.array(Image.open(p).convert("L"))
        h = a.shape[0]
        inkrows = (a < 200).any(axis=1)
        y = h - 1
        while y >= 0 and not inkrows[y]:
            y -= 1
        if y < 0:
            continue
        bottom = y
        while y >= 0 and inkrows[y]:
            y -= 1
        block_h = bottom - y  # height of bottom ink block
        gap = 0
        while y >= 0 and not inkrows[y]:
            gap += 1
            y -= 1
        if block_h <= 4 and gap >= 2 and y >= 0:
            a[y + 1:bottom + 1, :] = 255
            Image.fromarray(a).save(p)
            mets.setdefault(fn, {})["bb"] = _bb(a)
            n_clean += 1
json.dump(manifest, open(MAN, "w", encoding="utf-8"), indent=2)
print(f"cleaned {n_clean} crops (thin detached bottom blocks erased)")
print("OK derule3")
