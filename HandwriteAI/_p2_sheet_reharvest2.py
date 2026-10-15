"""Re-harvest Profile 2 from the NEW alphabet sheet (2026-10-15 photo).

Sheet: C:\\Users\\Asus\\Pictures\\Screenshots\\Screenshot 2026-10-15 150355.png
(370x621 phone photo, blue ink on white paper; thr dark<140 -- the old
110 threshold was tuned for the 2026-10-13 screenshot).

Layout (rows located from the sheet's horizontal ink profile):
  R1 ABCDEFGHI  R2 JKLMNOPQR  R3 STUVWXYZ
  R4 abcdefgh   R5 ijklmnop   R6 qrstuvwxyz
  R7 12345678910
  R10 punct row: % , \\ , - , = , + , x  (comma-separated)
Rows '11..17' and '18..20' (y~427-502) are SKIPPED: redundant multi-digit
groups, all digits already come from R7.

v3 (2026-10-15) -- COMPONENT-BASED. The rows overlap vertically (descenders
and ascenders cross the nominal row gaps), so a fixed y-band clips letters
(p's bowl pokes up into R4, j's hook reaches down into R6) and expanding the
band grabs the neighbouring row's letter at the same x. Instead:
  1. label connected components on the whole sheet,
  2. segment each row into letter columns (column_cells) as before,
  3. for each letter pick the component with the most ink inside that
     column x the band's CORE (the band only says WHICH component is the
     letter), then take that component's FULL vertical extent,
  4. add nearby small components in the same columns (i/j dots, E/F bars).
Baseline fraction is derived from a per-row least-squares fit of the
non-descender bottoms (the photo is rotated, ~ -0.12 row/px): a descender's
body-bottom is the fitted baseline at its x; non-descenders keep their own
ink bottom. Stage-only: writes crops to styles/_p2_stage + staged.json +
staged_meta.json (per-crop top, cx, band, bb). Does NOT touch the manifest.
"""
import os, json
import numpy as np
import cv2
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
GAP_PUNCT = 2
MIN_AREA = 8
COMP_MIN = 4          # components smaller than this are noise (dots are ~7)
DOT_ABOVE = 14        # a dot/crossbar comp must centre within this many rows
                      # above the body top (i/j dot gap is 5-9)
DOT_BELOW = 4
DESC = set("gjpqyfJQ")  # glyphs whose ink descends below the baseline
# band 8 cells at GAP_PUNCT=2, ground truth (ASCII-art verified 2026-10-15):
#   % , \ , - , = , + , x   (commas are separators between the real symbols)
PUNCT_MAP = {0: "%", 1: ",", 2: "\\", 3: ",", 4: "-",
             5: ",", 6: "=", 7: ",", 8: "+", 9: ",", 10: "\u00d7"}

g = np.array(Image.open(SRC).convert("RGB")).astype(int).mean(axis=2)
dark = g < 140

_n, lab, _stats, _cent = cv2.connectedComponentsWithStats(
    dark.astype(np.uint8), connectivity=8)
COMP = {}
for i in range(1, _n):
    x, y, w, h, area = _stats[i]
    if area < COMP_MIN:
        continue
    COMP[i] = (int(x), int(y), int(w), int(h), int(area),
               int(_cent[i][0]), int(_cent[i][1]))


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
        cells.append(dict(x0=s + x0, x1=e - 1 + x0,
                          y0=y0 + int(ys.min()), y1=y0 + int(ys.max())))
    # left-boundary clip repair (guard x0>0 so the probe can never wrap)
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


def pick_comp(cell, y0, y1):
    """Component holding the most ink inside the cell columns x band rows."""
    best, bestink = None, 0
    for cid, (x, y, w, h, area, ccx, ccy) in COMP.items():
        ox0, ox1 = max(cell["x0"], x), min(cell["x1"], x + w - 1)
        oy0, oy1 = max(y0, y), min(y1, y + h - 1)
        if ox1 < ox0 or oy1 < oy0:
            continue
        ink = int((lab[oy0:oy1 + 1, ox0:ox1 + 1] == cid).sum())
        if ink > bestink:
            bestink, best = ink, cid
    return best, bestink


def gather(cell, main):
    """Main component + nearby smaller ones in the same columns (dots/bars)."""
    mx, my, mw, mh, marea, mcx, mcy = COMP[main]
    body_top, body_bot = my, my + mh - 1
    keep = [main]
    for cid, (x, y, w, h, area, ccx, ccy) in COMP.items():
        if cid == main or area >= marea:
            continue
        if min(cell["x1"], x + w - 1) < max(cell["x0"], x):
            continue
        if body_top - DOT_ABOVE <= ccy <= body_bot + DOT_BELOW:
            keep.append(cid)
    return keep


def crop_of(cids):
    sel = np.zeros_like(dark, dtype=bool)
    for cid in cids:
        sel |= (lab == cid)
    ys, xs = np.where(sel)
    return (sel[ys.min():ys.max() + 1, xs.min():xs.max() + 1],
            int(ys.min()), int((xs.min() + xs.max()) // 2))


report = []
staged = {}   # ch -> list of (crop, top, cx, band)
for bi, (y0, y1, chars) in enumerate(BANDS):
    cells = column_cells(y0, y1, gap=GAP_PUNCT if chars is None else GAP)
    n = len(cells)
    expected = len(chars) if chars else len(PUNCT_MAP)
    report.append((bi, y0, y1, chars, n, expected))
    if n != expected:
        print("BAND %d MISMATCH got=%d expected=%d chars=%s"
              % (bi, n, expected, chars))
    for i, c in enumerate(cells):
        if chars is None:
            if i not in PUNCT_MAP:
                continue
            ch = PUNCT_MAP[i]
        else:
            if n != expected:
                break
            ch = chars[i]
        main, ink = pick_comp(c, y0, y1)
        if main is None:
            print("  no component for", repr(ch))
            continue
        crop, top, cx = crop_of(gather(c, main))
        staged.setdefault(ch, []).append((crop, top, cx, bi))

print("=== band report (idx, y0, y1, chars, got, expected) ===")
for r in report:
    print(" ", r)

# per-row least-squares baseline from non-descender ink bottoms
band_pts = {}
for ch, items in staged.items():
    if ch in DESC:
        continue
    for (crop, top, cx, bi) in items:
        band_pts.setdefault(bi, []).append((cx, top + crop.shape[0] - 1))
FIT = {}
for bi, pts in band_pts.items():
    if len(pts) >= 3:
        m, c = np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1)
        FIT[bi] = (float(m), float(c))
    elif pts:
        FIT[bi] = (0.0, float(np.median([p[1] for p in pts])))
print("=== row baseline fits (slope, intercept) ===")
for bi in sorted(FIT):
    print("  band %d: %.4f * x + %.1f" % (bi, FIT[bi][0], FIT[bi][1]))


def baseline_frac(ch, crop, top, cx, bi):
    h = crop.shape[0]
    if ch in DESC and bi in FIT:
        m, c = FIT[bi]
        bb = (m * cx + c - top) / h
    else:
        rows = np.where((crop > 0).any(axis=1))[0]
        bb = (rows.max() + 1) / h
    return round(float(min(1.0, max(0.15, bb))), 3)


for f in os.listdir(STAGE):
    os.remove(os.path.join(STAGE, f))

saved = {}
meta = {}
for ch, items in staged.items():
    for k, (crop, top, cx, bi) in enumerate(items):
        fn = "sheet_%d_%d.png" % (ord(ch), k)
        Image.fromarray(255 - crop.astype(np.uint8) * 255).save(
            os.path.join(STAGE, fn))
        saved.setdefault(ch, []).append(fn)
        meta[fn] = {"top": int(top), "cx": int(cx), "band": int(bi),
                    "h": int(crop.shape[0]),
                    "bb": baseline_frac(ch, crop, top, cx, bi)}
json.dump(saved, open(os.path.join(STAGE, "staged.json"), "w"), indent=2)
json.dump(meta, open(os.path.join(STAGE, "staged_meta.json"), "w"), indent=2)
print("staged chars:", len(saved), "crops:", sum(len(v) for v in saved.values()))
print("->", STAGE)
