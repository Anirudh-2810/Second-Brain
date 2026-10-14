"""Re-harvest Profile 2 alphabet sheet with CORRECT row->char mapping.

Root fix: the original harvest mis-assigned rows (uppercase shapes landed in
lowercase pools). Reads the 9 known content bands and maps each to its
ground-truth character sequence using COLUMN segmentation (robust to i/j dots
and split digits, which connected-components mishandles).

Stage-only: writes crops to styles/_p2_stage + prints counts for audit.
Does NOT touch the live manifest.
"""
import os, json
import numpy as np
from PIL import Image

SRC = r"C:\Users\Asus\Pictures\Screenshots\Screenshot 2026-10-13 134208.png"
STAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "styles", "_p2_stage")
os.makedirs(STAGE, exist_ok=True)

# (y0, y1, char sequence) -- TIGHT ink bands detected from the source
# (dark<110 over x[40:], gap tol 3). MUST stay non-overlapping: loose bands
# let a cell bleed ink from the row below, which corrupts body_bottom_frac bb.
BANDS = [
    (63, 100, "abcdefghij"),
    (106, 141, "klmnopqrst"),
    (161, 190, "uvwxyz"),
    (221, 253, "ABCDEFGHIJ"),
    (270, 299, "KLMNOPQRST"),
    (315, 341, "UVWXYZ"),
    (365, 390, "12345678"),
    (413, 438, "910"),
    (462, 495, None),  # punctuation: read dynamically
]
LEFT = 40   # exclude left-side UI chrome
GAP = 2     # px of empty column that separates characters (tuned: all
            # letter+digit bands hit exact expected counts)
GAP_PUNCT = 7  # keep symbols like % and = whole
MIN_AREA = 8
# band 8 cells at GAP_PUNCT=7, ground-truth read from p2_punct.png:
#   + , - , % , / , = ,
PUNCT_MAP = {0: "+", 1: ",", 2: "-", 3: ",", 4: "%",
             5: ",", 6: "/", 7: ",", 8: "=", 9: ","}

im = Image.open(SRC).convert("RGB")
g = np.array(im).astype(int).mean(axis=2)
dark = (g < 110)


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
    # bridge small gaps
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] <= gap:
            merged[-1][1] = r[1]
        else:
            merged.append(r[:])
    # drop tiny specks (ruled-line fragments)
    cells = []
    for s, e in merged:
        region = sub[:, s:e]
        if region.sum() < min_area:
            continue
        ys = np.where(region.any(axis=1))[0]
        if ys.max() - ys.min() < 2:
            continue  # height-0 speck (ruled-line fragment)
        cells.append(dict(x0=s + x0, x1=e + x0,
                          y0=y0 + ys.min(), y1=y0 + ys.max(),
                          col=s, cole=e))
    # left-boundary clip repair: ink at x < x0 was invisible to the scan
    # (the 9 loop lives at x38-39 and the + left arm at x37-39; LEFT=40
    # cut both). Grow x0 leftward while the adjacent column has ink in the
    # cell's y-range, max 6px, never crossing the previous cell. Internal
    # cells can't trigger this (they're separated by empty columns), so
    # bands/counts are unaffected.
    prev_x1 = None
    for c in cells:
        while (c["x0"] - 1 >= x0 - 6
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
    """Drop detached thin edge runs (pen specks, ruled-line bleed) at a
    crop's top/bottom edge, then retrim to the remaining ink bbox. Rules
    validated against all 73 staged crops: catches the 8's top speck +
    bottom rule line and the W's 1px dot; the 5's two strokes, = bars,
    i/j dots and 9 loop are legitimate (h>=3 or narrow) and survive."""
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
        # NOTE: Windows FS is case-insensitive -> "sheet_a_0" and "sheet_A_0"
        # are the SAME file (uppercase band overwrote every lowercase crop).
        # Use the unicode codepoint so every char gets a unique, case-safe name.
        fn = "sheet_%d_%d.png" % (ord(ch), k)
        Image.fromarray(255 - sub).save(os.path.join(STAGE, fn))
        saved.setdefault(ch, []).append(fn)
json.dump(saved, open(os.path.join(STAGE, "staged.json"), "w"), indent=2)
print("staged chars:", len(saved), "crops:", sum(len(v) for v in saved.values()))
print("->", STAGE)
