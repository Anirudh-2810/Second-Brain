"""Re-harvest Profile 2 from the NEW alphabet sheet (2026-10-15 photo).

Sheet: C:\\Users\\Asus\\Pictures\\Screenshots\\Screenshot 2026-10-15 150355.png
(370x621 phone photo, blue ink on white paper; thr dark<140 -- the old
110 threshold was tuned for the 2026-10-13 screenshot).

Layout (probed 2026-10-15):
  R1 (14,51)   ABCDEFGHI    9   (R1/R2 boundary is clean at 51/52: J's and
                               R's top bars start at 52, A's true bottom 51)
  R2 (52,116)  JKLMNOPQR    9
  R3 (127,168) STUVWXYZ     8
  R4 (188,257) abcdefgh     8   (g tail reaches y256)
  R5 (258,301) ijklmnop     8   (starts below g tail / h stem overlap)
  R6 (300,357) qrstuvwxyz   9   (starts below j hook; q/y tails to 357)
  R7 (365,422) 12345678910 11   ('10' segments into 1 + 0, verified)
  R10(536,569) punct row: % , \\ , - , = , + , x  -- 11 cells, comma-separated
Rows '11,12,...,17,' (y~427-466) and '18,19,20' (y~477-502) are SKIPPED:
redundant multi-digit groups, all digits already come from R7.

Same pipeline as _p2_sheet_reharvest.py (column segmentation, ord-based
case-safe filenames, strip_edge_junk, left-expansion). Stage-only: writes
crops to styles/_p2_stage + prints counts for audit. Does NOT touch the
live manifest.
"""
import os, json
import numpy as np
from PIL import Image

SRC = r"C:\Users\Asus\Pictures\Screenshots\Screenshot 2026-10-15 150355.png"
STAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "styles", "_p2_stage")
os.makedirs(STAGE, exist_ok=True)

BANDS = [
    (14, 51, "ABCDEFGHI"),
    (52, 116, "JKLMNOPQR"),
    (127, 168, "STUVWXYZ"),
    (188, 257, "abcdefgh"),
    (258, 301, "ijklmnop"),
    (300, 357, "qrstuvwxyz"),
    (365, 422, "12345678910"),
    (536, 569, None),  # punctuation: read dynamically
]
LEFT = 0    # photo fills the frame; first letter starts at x~21
GAP = 3     # px of empty column that separates characters (3 bridges J's
            # internal 2px stem/hook split; all letter gaps are >= 4px)
GAP_PUNCT = 2  # symbol/comma gaps in the punct row are ~6px; 2 keeps every
               # symbol whole while splitting symbol+comma pairs (7 merged)
MIN_AREA = 8
# band 8 cells at GAP_PUNCT=7, ground truth (ASCII-art verified 2026-10-15):
#   % , \ , - , = , + , x   (commas are separators between the real symbols)
PUNCT_MAP = {0: "%", 1: ",", 2: "\\", 3: ",", 4: "-",
             5: ",", 6: "=", 7: ",", 8: "+", 9: ",", 10: "\u00d7"}

im = Image.open(SRC).convert("RGB")
g = np.array(im).astype(int).mean(axis=2)
dark = (g < 140)


def column_cells(y0, y1, x0=LEFT, gap=GAP, min_area=MIN_AREA):
    """Segment a band into character cells by column runs."""
    sub = dark[y0:y1, x0:]
    col = sub.sum(axis=0)
    runs = []
    inr = False
    for x in range(len(col)):
        if col[x] > 0 and not inr:
            inr = True; s = x
        elif col[x] == 0 and inr:
            inr = False; runs.append([s, x])
    if inr:
        runs.append([s, len(col)])
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] <= gap:
            merged[-1][1] = r[1]
        else:
            merged.append(r[:])
    cells = []
    for s, e in merged:
        region = sub[:, s:e]
        if region.sum() < min_area:
            continue
        ys = np.where(region.any(axis=1))[0]
        if ys.max() - ys.min() < 2:
            continue
        cells.append(dict(x0=s + x0, x1=e + x0,
                          y0=y0 + ys.min(), y1=y0 + ys.max(),
                          col=s, cole=e))
    # left-boundary clip repair (guard x0>0 so the probe can never wrap
    # to negative indices)
    prev_x1 = None
    for c in cells:
        while (c["x0"] > 0 and c["x0"] - 1 >= x0 - 6
               and (prev_x1 is None or c["x0"] - 1 > prev_x1)
               and dark[c["y0"]:c["y1"] + 1, c["x0"] - 1].any()):
            c["x0"] -= 1
        prev_x1 = c["x1"]
        reg = dark[y0:y1, c["x0"]:c["x1"] + 1]
        ys2 = np.where(reg.any(axis=1))[0]
        if len(ys2):
            c["y0"] = y0 + int(ys2.min())
            c["y1"] = y0 + int(ys2.max())
    return cells


def strip_edge_junk(arr):
    """Drop detached thin edge runs (pen specks, paper-texture bleed) at a
    crop's top/bottom edge, then retrim to the remaining ink bbox."""
    rows = np.where(arr.any(axis=1))[0]
    if len(rows) == 0:
        return arr
    rs = []
    s = rows[0]
    for i in range(1, len(rows)):
        if rows[i] != rows[i - 1] + 1:
            rs.append((int(s), int(rows[i - 1])))
            s = rows[i]
    rs.append((int(s), int(rows[-1])))
    h, w = arr.shape
    drop = set()
    if len(rs) >= 2:
        r0, r1 = rs[0]
        rh = r1 - r0 + 1
        rw = int(arr[r0:r1 + 1].sum(axis=1).max())
        if (r0 <= 2 and rs[1][0] - r1 >= 1
                and (rh <= 1 or (rh <= 2 and rw >= 0.6 * w))):
            drop.update(range(r0, r1 + 1))
        r0, r1 = rs[-1]
        rh = r1 - r0 + 1
        rw = int(arr[r0:r1 + 1].sum(axis=1).max())
        if (r1 >= h - 3 and r0 - rs[-2][1] >= 1
                and (rh <= 1 or (rh <= 2 and rw >= 0.6 * w))):
            drop.update(range(r0, r1 + 1))
    if not drop:
        return arr
    keep = np.ones(h, dtype=bool)
    keep[list(drop)] = False
    arr = arr[keep]
    rows = np.where(arr.any(axis=1))[0]
    cols = np.where(arr.any(axis=0))[0]
    if len(rows) == 0 or len(cols) == 0:
        return arr
    return arr[rows.min():rows.max() + 1, cols.min():cols.max() + 1]


# wipe the stage (regenerable) so old-sheet crops can't mix in
for f in os.listdir(STAGE):
    os.remove(os.path.join(STAGE, f))

report = []
staged = {}
for bi, (y0, y1, chars) in enumerate(BANDS):
    cells = column_cells(y0, y1, gap=GAP_PUNCT if chars is None else GAP)
    n = len(cells)
    expected = len(chars) if chars else None
    report.append((bi, y0, y1, chars, n, expected))
    if chars is None:
        if len(cells) != len(PUNCT_MAP):
            print("PUNCT MISMATCH got=%d expected=%d" % (len(cells), len(PUNCT_MAP)))
        for i, c in enumerate(cells):
            if i not in PUNCT_MAP:
                continue
            ch = PUNCT_MAP[i]
            sub = dark[c["y0"]:c["y1"] + 1, c["x0"]:c["x1"] + 1]
            staged.setdefault(ch, []).append((sub.astype(np.uint8) * 255, c))
        continue
    if n != expected:
        print("BAND %d MISMATCH got=%d expected=%d chars=%s" % (bi, n, expected, chars))
        for c in cells:
            print("    cell x=%d..%d y=%d..%d" % (c["x0"], c["x1"], c["y0"], c["y1"]))
        staged["_band%d" % bi] = cells
        continue
    for ch, c in zip(chars, cells):
        sub = dark[c["y0"]:c["y1"] + 1, c["x0"]:c["x1"] + 1]
        staged.setdefault(ch, []).append((sub.astype(np.uint8) * 255, c))

print("=== band report (idx, y0, y1, chars, got, expected) ===")
for r in report:
    print(" ", r)

saved = {}
for ch, items in staged.items():
    if ch.startswith("_"):
        continue
    for k, (sub, c) in enumerate(items):
        sub = strip_edge_junk(sub)
        # unicode-codepoint filenames: case-safe AND collision-free on
        # Windows (sheet_a_0 vs sheet_A_0), stable across re-harvests.
        fn = "sheet_%d_%d.png" % (ord(ch), k)
        Image.fromarray(255 - sub).save(os.path.join(STAGE, fn))
        saved.setdefault(ch, []).append(fn)
json.dump(saved, open(os.path.join(STAGE, "staged.json"), "w"), indent=2)
print("staged chars:", len(saved), "crops:", sum(len(v) for v in saved.values()))
print("->", STAGE)
