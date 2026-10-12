"""One-shot audit (read-only): e-closure scores + q distribution, r-pool stats.

Closure metric for 'e': fill fraction in the mid-right band
(rows 35-65%, cols 60-92%). A closed e carries its crossbar/loop
through that band; an open (c-like) e leaves it empty.
"""
import os, json
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_001.labeled")
manifest = json.load(open(os.path.join(LIB, "manifest.json"), encoding="utf-8"))
mets = manifest.get("metrics", {})


def closure(arr):
    h, w = arr.shape[:2]
    ink = arr < 200
    band = ink[int(h * 0.35):int(h * 0.65), int(w * 0.60):int(w * 0.92)]
    return float(band.mean()) if band.size else 0.0


for ch in ["e", "r"]:
    files = manifest["chars"].get(ch, [])
    qs, scores, degen = [], [], []
    for fn in files:
        p = os.path.join(LIB, fn)
        if not os.path.exists(p):
            degen.append((fn, "missing-file")); continue
        arr = np.array(Image.open(p).convert("L"))
        if arr.size == 0 or (arr < 200).mean() < 0.01:
            degen.append((fn, "near-blank")); continue
        qs.append(float((mets.get(fn) or {}).get("q", 1.0)))
        if ch == "e":
            scores.append((closure(arr), fn))
    print(f"== {ch}: n={len(files)} qmin={min(qs):.2f} qmed={sorted(qs)[len(qs)//2]:.2f} "
          f"qmax={max(qs):.2f} degenerate={len(degen)} {degen[:4]}")
    if scores:
        scores.sort()
        print(f"   closure: min={scores[0][0]:.3f} med={scores[len(scores)//2][0]:.3f} "
              f"max={scores[-1][0]:.3f}")
        print("   bottom-12:", [(fn, round(s, 3)) for s, fn in scores[:12]])
print("OK audit")
