"""Rebuild profile_002.labeled manifest with VERIFIED glyph pools.

Fix (root cause): the original screenshot harvester mis-assigned rows, so 15
lowercase pools (a b f g h j k m p q s v w x z) held uppercase letterforms,
digits were mislabeled, and enr_A_* collided with enr_a_* on Windows' case-
insensitive FS (same file served both cases).

Merge rules:
  * KEEP  cNN_* cluster crops  -> correct, main variation source
  * DROP  enr_* crops          -> unreliable (case-collision)
  * ADD   sheet_* crops        -> verified correct row->char re-harvest

Stage-only for the crops (they're already in _p2_stage); this writes the
manifest after backing up the old one. Unreferenced enr_* files stay on disk.
"""
import os, json, shutil
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
STAGE = os.path.join(ROOT, "styles", "_p2_stage")
LIB = os.path.join(ROOT, "styles", "profile_002.labeled")
MAN = os.path.join(LIB, "manifest.json")

import sys
sys.path.insert(0, ROOT)
from glyphs import body_bottom_frac  # noqa: F401  (kept for reference)

SHEET_Q = 0.5  # moderate: lets clusters dominate variation for shared chars

DESCENDERS = set("gjpqy")


def baseline_frac(ch: str, arr) -> float:
    """Baseline (body-bottom) as a fraction of crop height, robust for tight
    single-glyph crops harvested off the alphabet sheet.

    body_bottom_frac() mis-picks thin-stroke letters (J/C/F/I/S): its
    0.35*width threshold excludes the thin stem, so the wide TOP bar wins as
    the "largest run" and bb lands near 0.09 -> glyph floats. Here the crop is
    known-tight (y-extent == ink extent), so:
      * non-descender -> lowest ink row IS the baseline  -> ~1.0
      * descender     -> baseline sits above the tail; take the body mass bottom
    """
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
    # descender: baseline = bottom of the x-height body mass, tail excluded
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

staged = json.load(open(os.path.join(STAGE, "staged.json"), encoding="utf-8"))
old = json.load(open(MAN, encoding="utf-8"))
old_chars = old.get("chars", {})
old_mets = old.get("metrics", {})

# 1. copy staged sheet crops into the library
copied = {}
for ch, files in staged.items():
    keep = []
    for fn in files:
        src = os.path.join(STAGE, fn)
        dst = os.path.join(LIB, fn)
        shutil.copy2(src, dst)
        keep.append(fn)
    copied[ch] = keep

# 2. build new chars: clusters kept + sheet added, enr dropped
new_chars = {}
added = dropped = 0
for ch, ofiles in old_chars.items():
    cluster = [f for f in ofiles if f.startswith("c")]
    enr = [f for f in ofiles if f.startswith("enr_")]
    dropped += len(enr)
    pool = list(cluster)
    pool += copied.get(ch, [])
    added += len(copied.get(ch, []))
    new_chars[ch] = pool
# ensure every staged char exists even if absent from old manifest
for ch, files in copied.items():
    if ch not in new_chars:
        new_chars[ch] = list(files)
        added += len(files)

# 3. metrics: keep cluster (immutable), ALWAYS recompute sheet (content changes
#    whenever the sheet re-harvests even though the filename is stable).
new_mets = {}
for ch, files in new_chars.items():
    for fn in files:
        if fn in old_mets and not fn.startswith("sheet_"):
            new_mets[fn] = old_mets[fn]
        else:
            arr = np.array(Image.open(os.path.join(LIB, fn)).convert("L"))
            bb = baseline_frac(ch, arr)
            new_mets[fn] = {"bb": round(float(bb), 3), "q": SHEET_Q}

# 4. recompute bookkeeping
missing = sorted([ch for ch, v in new_chars.items() if not v])
n_glyphs = sum(len(v) for v in new_chars.values())
new = dict(old)
new["chars"] = new_chars
new["metrics"] = new_mets
new["missing"] = missing
new["n_glyphs"] = n_glyphs

bak = MAN + ".bak-rebuild"
if not os.path.exists(bak):
    shutil.copy2(MAN, bak)
json.dump(new, open(MAN, "w", encoding="utf-8"), indent=2)

print("dropped enr_ refs:", dropped)
print("added sheet_ refs :", added)
print("chars:", len(new_chars), "n_glyphs:", n_glyphs, "missing:", missing)
print("metrics:", len(new_mets))
print("chars w/ clusters:", sum(1 for v in new_chars.values() if any(f.startswith('c') for f in v)))
