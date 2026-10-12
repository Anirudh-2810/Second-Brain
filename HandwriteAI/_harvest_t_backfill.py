"""Add 4 recovered t variants (orphans_11 #0, #10, #12, #29) to cluster 11.

Cleanup (surgical, documented):
- page-ruling rows: light-gray pixels (165-245) spanning >40% of row width
  in rows with <8 dark px are cleared to white (ruling caught in tall crops;
  existing library crops keep their anti-aliasing — no global binarize).
- #10 also gets largest-dark-component keep (stray comma blob at right).
bb = stem bottom (last row before the centroid drifts as the flick curves),
measured on the cleaned crop. Source PNGs overwritten in place (curation,
same class as the bb re-patch); labeled copies + manifests updated surgically
(no apply_labels re-run — that would churn the pruned pools).
"""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np
from PIL import Image
from scipy import ndimage  # noqa: F401  (fallback below if missing)
import profiles

_info = profiles.resolve("")
CDIR = _info["clusters"]
LIB = _info["glyphs"]
LAB = _info["labeled"]

orphans = json.load(open(os.path.join(CDIR, 'orphans_11.json')))
PICKS = {0: 'p00_0001_tall.png', 10: 'p01_0042_tall.png',
         12: 'p01_0101_xheight.png', 29: 'p04_0366_tall.png'}
# verify orphans list matches expected filenames
for i, fn in PICKS.items():
    assert orphans[i] == fn, f'orphan #{i} is {orphans[i]}, expected {fn}'


def clean_ruling(a: np.ndarray) -> np.ndarray:
    out = a.copy()
    h, w = out.shape
    for r in range(h):
        light = (out[r] >= 165) & (out[r] <= 245)
        dark = out[r] < 165
        if light.sum() > 0.4 * w and dark.sum() < 8:
            out[r, light] = 255
    return out


def largest_component(a: np.ndarray, thr: int = 165) -> np.ndarray:
    """Zero everything except the largest dark connected component."""
    try:
        from scipy import ndimage
        lab_, n = ndimage.label(a < thr)
        if n <= 1:
            return a
        sizes = ndimage.sum(np.ones_like(lab_), lab_, range(1, n + 1))
        keep = int(np.argmax(sizes)) + 1
        out = a.copy()
        out[(lab_ != keep) & (a < thr)] = 255
        return out
    except ImportError:
        # flood-fill fallback (4-conn) on the largest seed by scan order
        ink = a < thr
        h, w = ink.shape
        best = None
        seen = np.zeros_like(ink, dtype=bool)
        for r0 in range(h):
            for c0 in range(w):
                if not ink[r0, c0] or seen[r0, c0]:
                    continue
                stack, comp = [(r0, c0)], []
                seen[r0, c0] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and ink[nr, nc] and not seen[nr, nc]:
                            seen[nr, nc] = True
                            stack.append((nr, nc))
                if best is None or len(comp) > len(best):
                    best = comp
        out = a.copy()
        keep_mask = np.zeros_like(ink)
        for r, c in best:
            keep_mask[r, c] = True
        out[(~keep_mask) & ink] = 255
        return out


def t_stem_baseline(a: np.ndarray, thr: int = 165):
    """Baseline = bottom of the vertical stem. Find the crossbar (widest
    contiguous run), then walk down while the row centroid stays within
    2px of the crossbar centroid; the flick curves away or thins there.
    Returns (baseline_row, h, bb_frac)."""
    ink = a < thr
    h, w = ink.shape
    roww = ink.sum(axis=1)
    cw = roww.max()
    wide = roww >= 0.35 * cw
    runs, cur = [], None
    for i, x in enumerate(wide):
        if x and cur is None:
            cur = [i, i]
        elif x:
            cur[1] = i
        elif cur is not None:
            if i - cur[1] > 2:
                runs.append(tuple(cur))
                cur = None
    if cur is not None:
        runs.append(tuple(cur))
    best = max(runs, key=lambda r: roww[r[0]:r[1] + 1].sum())

    def cx(r):
        xs = np.where(ink[r])[0]
        return xs.mean() if len(xs) else None

    cx_bar = np.mean([cx(r) for r in range(best[0], best[1] + 1) if cx(r) is not None])
    last = best[1]
    for r in range(best[1] + 1, h):
        if roww[r] == 0:
            break
        c = cx(r)
        if c is not None and abs(c - cx_bar) > 2.0:
            break  # flick curving away
        last = r
    return last, h, round((last + 1) / h, 3)


lab_manifest_path = os.path.join(LAB, 'manifest.json')
src_manifest_path = os.path.join(LIB, 'manifest.json')
clusters_path = os.path.join(CDIR, 'clusters.json')
lm = json.load(open(lab_manifest_path))
sm = json.load(open(src_manifest_path))
payload = json.load(open(clusters_path))

new_labeled = []
for k, (i, fn) in enumerate(sorted(PICKS.items())):
    p = os.path.join(LIB, fn)
    a = np.array(Image.open(p).convert('L'))
    a0 = clean_ruling(a)
    if i == 10:
        a0 = largest_component(a0)
    last, h, bb = t_stem_baseline(a0)
    print(f'#{i} {fn}: cleaned, stem_bottom row {last}/{h} -> bb {bb}')
    # sanity: ink kept?
    print(f'   dark px before/after: {(a < 165).sum()} / {(a0 < 165).sum()}')
    Image.fromarray(a0).save(p)
    dst = f'c11_t_{3 + k:03d}.png'
    Image.fromarray(a0).save(os.path.join(LAB, dst))
    new_labeled.append((fn, dst, bb))
    # source manifest bb
    sm['metrics'].setdefault(fn, {})
    sm['metrics'][fn]['bb'] = bb

# clusters.json: append the 4 sources to c11 (dedup)
c11 = payload['clusters']['11']
for fn, _, _ in new_labeled:
    if fn not in c11:
        c11.append(fn)
payload['sizes']['11'] = len(c11)

# labeled manifest: chars.t + metrics (q left absent -> treated as 1.0 neutral;
# render weights by q^4 with missing q defaulting via .get - check load path)
for fn, dst, bb in new_labeled:
    if dst not in lm['chars']['t']:
        lm['chars']['t'].append(dst)
    lm['metrics'][dst] = {'bb': bb, 'q': 0.85}
lm['n_glyphs'] = sum(len(v) for v in lm['chars'].values())

json.dump(payload, open(clusters_path, 'w'), indent=2)
json.dump(lm, open(lab_manifest_path, 'w'), indent=2)
json.dump(sm, open(src_manifest_path, 'w'), indent=2)
print('t pool now:', len(lm['chars']['t']), '->', lm['chars']['t'])
print('c11 members:', len(c11))
print('done')
