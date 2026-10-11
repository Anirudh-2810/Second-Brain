"""Harvest t/f/s/r from unlabeled clusters c11/c29/c44/c47.
c11 -> split: t stays (label '11'='t'), f moves to new cluster '64' (label 'f').
c29 -> prune thin/junk, label '29'='r' (fattens r 14 -> ~78).
c44+c47 -> clear s's merge into new cluster '65' (label 's'), leftovers
stay unlabeled in 44/47. bb re-patched with current body_bottom_frac rule
for every file in the four labeled clusters (stale source-rule anchors
were the g disaster; x-height letters are near-neutral but f descenders
must anchor on the body, not the loop tip)."""
import json, os, sys
import numpy as np
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from cluster import _resolve_lib, apply_labels
from glyphs import body_bottom_frac

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
srclib = _resolve_lib(cdir, p['lib'])

# --- c11: t (crossbar) vs f (descender loop). Rest = junk/thin -> dropped.
T11 = (2, 5, 8, 10, 11, 15, 27, 28, 29, 45, 46, 48, 50, 54, 55, 58, 61, 63, 64, 65)
F11 = (12, 13, 17, 18, 19, 20, 24, 25, 33, 34, 35, 39, 40, 41, 47, 49, 51, 53, 57)
mem11 = p['clusters']['11']
p['clusters']['64'] = [mem11[i] for i in F11]
p['clusters']['11'] = [mem11[i] for i in T11]

# --- c29: clean shoulder-r's only (drop thin i-like, 2/5/p/t/C junk).
R29 = (2, 3, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 24, 25, 26,
       27, 28, 31, 33, 34, 35, 36, 37, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 63, 66, 67, 69, 74, 76, 77, 81,
       83, 86, 87, 88, 89, 90, 93, 94, 104)
mem29 = p['clusters']['29']
p['clusters']['29'] = [mem29[i] for i in R29]

# --- c44/c47: clear s's -> new cluster 65.
S44 = (3, 4, 5, 6, 7, 13, 18, 21, 23, 27, 32, 38, 39)
S47 = (0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22,
       25, 26, 27, 33, 34, 38, 39, 44)
mem44, mem47 = p['clusters']['44'], p['clusters']['47']
p['clusters']['65'] = ([mem44[i] for i in S44] + [mem47[i] for i in S47])
p['clusters']['44'] = [m for i, m in enumerate(mem44) if i not in set(S44)]
p['clusters']['47'] = [m for i, m in enumerate(mem47) if i not in set(S47)]

p['labels']['11'] = 't'
p['labels']['64'] = 'f'
p['labels']['29'] = 'r'
p['labels']['65'] = 's'

json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
print('clusters: 11(t)=%d 64(f)=%d 29(r)=%d 65(s)=%d' % (
    len(p['clusters']['11']), len(p['clusters']['64']),
    len(p['clusters']['29']), len(p['clusters']['65'])))

# --- bb re-patch (current rule) for every file in the four labeled clusters.
mpath = os.path.join(srclib, 'manifest.json')
sm = json.load(open(mpath))
mets = sm.setdefault('metrics', {})
n_patch = 0
for cid in ('11', '64', '29', '65'):
    for fn in p['clusters'][cid]:
        fp = os.path.join(srclib, fn)
        if not os.path.exists(fp):
            print('MISSING src', fn)
            continue
        bb = float(body_bottom_frac(np.array(Image.open(fp).convert('L'))))
        ent = mets.setdefault(fn, {})
        if abs(float(ent.get('bb', -1)) - bb) > 0.005:
            ent['bb'] = round(bb, 4)
            n_patch += 1
json.dump(sm, open(mpath, 'w'), indent=1)
print('bb patched:', n_patch)

man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
for ch in 'abdefgilmnoprstuvwy':
    print(ch, len(man['chars'].get(ch, [])), end='  ')
print()
qs = [m.get('q', 0) for m in man['metrics'].values()]
print('q stats: min=%.3f median=%.3f max=%.3f n=%d' % (
    min(qs), float(np.median(qs)), max(qs), len(qs)))
