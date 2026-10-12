"""One-shot: erase ruled-paper bottom lines from profile_002.labeled crops.

Ruling = rows in the bottom 35% with >70% ink fill (letter strokes never
span that wide down there; t-crossbars sit higher). Erased to paper white,
bb recomputed via body_bottom_frac. Manifest backed up (.bak-ruling).
"""
import os, json, shutil
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_002.labeled")
MAN = os.path.join(LIB, "manifest.json")
BAK = os.path.join(LIB, "manifest.json.bak-ruling")

from glyphs import body_bottom_frac as _bb

manifest = json.load(open(MAN, encoding="utf-8"))
if not os.path.exists(BAK):
    shutil.copy(MAN, BAK)
    print("backup:", os.path.basename(BAK))
mets = manifest.setdefault("metrics", {})
n_clean, n_rows = 0, 0
for ch, files in manifest.get("chars", {}).items():
    for fn in files:
        p = os.path.join(LIB, fn)
        a = np.array(Image.open(p).convert("L"))
        h = a.shape[0]
        y0 = int(h * 0.65)
        fill = (a[y0:] < 200).mean(axis=1)
        bad = np.nonzero(fill > 0.7)[0]
        if len(bad) == 0:
            continue
        a[y0 + bad, :] = 255  # blank only the ruling rows themselves
        Image.fromarray(a).save(p)
        entry = mets.setdefault(fn, {})
        entry["bb"] = _bb(a)
        n_clean += 1
        n_rows += len(bad)
json.dump(manifest, open(MAN, "w", encoding="utf-8"), indent=2)
print(f"cleaned {n_clean} crops, {n_rows} ruling rows erased (bb recomputed)")
print("OK derule")
