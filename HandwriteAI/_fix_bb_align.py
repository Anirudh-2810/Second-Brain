"""One-shot bb alignment fix (2026-10-12).

Root cause: body_bottom_frac thresholds at 0.35*max_row_width — set by the
WIDEST feature (r shoulder, f crossbar, a bowl). Narrow stems fall below the
threshold, the run stops at the wide feature, and bb anchors too high. The
stem then hangs BELOW the baseline at render time ('r at the bottom',
'again' dipping, f same height as o).

Fix per letter class:
- no-descender letters (r, a, and any other non-descender with the same
  cut-off bug): bb = ink bottom (the stem bottom IS the baseline).
- cursive f: baseline = stem bottom, found where the ink centroid starts
  shifting after the crossbar (tail curve begins). Keeps the descender
  below the line while lifting the crossbar+ascender above it.
- real descenders (g j p q y): untouched — body_bottom_frac is correct.

Updates BOTH manifests (labeled + source glyphs) so future apply_labels
runs inherit the fix.
"""
import json
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LAB = "styles/profile_001.labeled"
SRC = "styles/profile_001.glyphs"

# letters with NO descender whose bb must sit at ink bottom
NO_DESC = set("arnmuivwxzoesc")
# f handled separately (has a real descender but bb was at crossbar)


def ink_bottom(arr):
    ink = np.asarray(arr) < 200
    if not ink.any():
        return None
    ys = np.where(ink.any(axis=1))[0]
    return int(ys.max()) + 1, ink.shape[0]


def f_stem_baseline(arr):
    """Cursive f: baseline = stem bottom = where centroid shifts (tail
    curve begins) after the crossbar. Returns bb fraction or None."""
    a = np.asarray(arr)
    ink = a < 200 if a.ndim == 2 else a[..., 0] < 200
    h, w = ink.shape
    roww = ink.sum(axis=1)
    if roww.max() < 3:
        return None
    thr = 0.35 * float(roww.max())
    wide = roww >= thr
    runs, cur = [], None
    for i, flag in enumerate(wide):
        if flag and cur is None:
            cur = [i, i]
        elif flag:
            cur[1] = i
        elif cur is not None:
            runs.append(tuple(cur))
            cur = None
    if cur is not None:
        runs.append(tuple(cur))
    if not runs:
        return None
    xb_bot = runs[-1][1]  # crossbar (widest run) bottom
    stem_c = None
    last_stem = xb_bot
    for r in range(xb_bot + 1, h):
        xs = np.where(ink[r])[0]
        if len(xs) == 0:
            break
        c = float(xs.mean())
        if stem_c is None:
            stem_c = c
        elif abs(c - stem_c) > max(2.0, 0.15 * w):
            break  # centroid shifted => tail curve began
        last_stem = r
    bb = (last_stem + 1) / float(h)
    return round(min(max(bb, 0.05), 0.98), 3)


def fix_manifest(man, label):
    metrics = man["metrics"]
    n_fixed = 0
    report = []
    for fn, m in metrics.items():
        base = os.path.basename(fn)
        # detect char from filename pattern cNN_<ch>_NNN.png
        parts = base.split("_")
        if len(parts) < 3:
            continue
        ch = parts[1]
        if len(ch) != 1 or not ch.isalpha():
            continue
        p = os.path.join(man.get("_dir", LAB), base)
        # resolve path: labeled dir or source bucket dir
        if not os.path.exists(p):
            for sub in ("narrow", "xheight", "wide", "tall"):
                p2 = os.path.join(man.get("_dir", SRC), sub, base)
                if os.path.exists(p2):
                    p = p2
                    break
            else:
                continue
        try:
            arr = np.array(Image.open(p).convert("L"))
        except Exception:
            continue
        ib = ink_bottom(arr)
        if ib is None:
            continue
        ib_row, h = ib
        ib_frac = round(ib_row / float(h), 3)
        old = float(m.get("bb", 0.5))
        new = old
        if ch == "f":
            fb = f_stem_baseline(arr)
            if fb is not None and abs(fb - old) > 0.03:
                new = fb
        elif ch in NO_DESC:
            if abs(ib_frac - old) > 0.05:
                new = ib_frac
        # real descenders g j p q y: leave untouched
        if abs(new - old) > 0.001:
            m["bb"] = new
            n_fixed += 1
            if len(report) < 40:
                report.append(f"  {base}: {old:.3f} -> {new:.3f} (ib={ib_frac})")
    print(f"[{label}] fixed {n_fixed} bb values")
    for line in report:
        print(line)
    return n_fixed


def main():
    total = 0
    # only the LABELED manifest carries per-char identity; the source
    # glyphs manifest is unlabeled (pNN_NNNN_bucket.png) so per-char bb
    # correction is impossible there. render_labeled reads labeled only.
    for path, label in ((LAB, "labeled"),):
        mp = os.path.join(path, "manifest.json")
        if not os.path.exists(mp):
            print(f"skip {mp} (missing)")
            continue
        with open(mp) as f:
            man = json.load(f)
        man["_dir"] = path
        total += fix_manifest(man, label)
        man.pop("_dir", None)
        with open(mp, "w") as f:
            json.dump(man, f, indent=1)
    print(f"total fixed: {total}")


if __name__ == "__main__":
    main()
