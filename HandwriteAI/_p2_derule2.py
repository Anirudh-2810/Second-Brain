"""One-shot: erase full-width thin ruling lines anywhere in p2 labeled crops.

Pass 1 (derule) only handled bottom rows; the writer sits ON ruled lines so
ruling crosses mid-crop too. Rule: rows with fill > 0.92, thickness <= 3px,
count <= 6 per crop (hand strokes never span 92%+ width dead-straight;
t/e bars are shorter). Manifest backed up (.bak-ruling2). bb recomputed.
"""
import os, json, shutil
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_002.labeled")
MAN = os.path.join(LIB, "manifest.json")
BAK = os.path.join(LIB, "manifest.json.bak-ruling2")

from glyphs import body_bottom_frac as _bb

manifest = json.load(open(MAN, encoding="utf-8"))
if not os.path.exists(BAK):
    shutil.copy(MAN, BAK)
    print("backup:", os.path.basename(BAK))
mets = manifest.setdefault("metrics", {})
n_clean, n_rows, skipped = 0, 0, []
for ch, files in manifest.get("chars", {}).items():
    for fn in files:
        p = os.path.join(LIB, fn)
        a = np.array(Image.open(p).convert("L"))
        fill = (a < 200).mean(axis=1)
        bad = np.nonzero(fill > 0.92)[0]
        # keep only thin runs (<=3px): ruling, not stacked strokes
        runs, run, prev = [], [], -10
        for r in bad:
            if r == prev + 1:
                run.append(r)
            else:
                runs.append(run)
                run = [r]
            prev = r
        runs.append(run)
        thin = [r for run in runs for r in (run if len(run) <= 3 else [])]
        if not thin or len(thin) > 6:
            if len(thin) > 6:
                skipped.append(fn)
            continue
        a[thin, :] = 255
        Image.fromarray(a).save(p)
        mets.setdefault(fn, {})["bb"] = _bb(a)
        n_clean += 1
        n_rows += len(thin)
json.dump(manifest, open(MAN, "w", encoding="utf-8"), indent=2)
print(f"cleaned {n_clean} crops, {n_rows} ruling rows; skipped>6: {len(skipped)} {skipped[:6]}")
print("OK derule2")
