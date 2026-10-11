"""Prune l/b/v/o/g crops caught by smoking-paragraph pick-spying.
labeled name -> source filename via array md5 -> cluster index drop."""
import json, os, sys, hashlib
import numpy as np
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from cluster import _resolve_lib

lib = 'styles/user_001.labeled'
cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
srclib = _resolve_lib(cdir, p['lib'])

def amd5(a):
    return hashlib.md5(np.ascontiguousarray(a).tobytes()).hexdigest()

src_by = {}
for fn in os.listdir(srclib):
    if fn.endswith('.png'):
        a = np.array(Image.open(os.path.join(srclib, fn)).convert('L'))
        src_by[amd5(a)] = fn

drop_names = []
# l: t-crossbars, e/o/s intruders, fragments
drop_names += ['c43_l_%03d.png' % i for i in
    (8, 10, 11, 16, 17, 19, 22, 27, 28, 29, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 44, 45)]
# b: z/2/c-open/p/y/t/5 shapes + 6-hook + lined
drop_names += ['c42_b_%03d.png' % i for i in
    (3, 4, 5, 6, 10, 11, 15, 20, 22, 34, 38, 40, 42, 45, 52)]
# v: u-rounded + ruled-line artifacts
drop_names += ['c0_v_%03d.png' % i for i in (8, 20, 21, 22, 23)]
# o: inner-mark a-like
drop_names += ['c55_o_038.png']
# g: ruled-line streaks (keep p07_0022 + p06_0059 only)
drop_names += ['c45_g_002.png', 'c45_g_003.png', 'c45_g_004.png']

drops = {}
miss = []
for lab_fn in drop_names:
    pth = os.path.join(lib, lab_fn)
    if not os.path.exists(pth):
        miss.append(lab_fn); continue
    a = np.array(Image.open(pth).convert('L'))
    sfn = src_by.get(amd5(a))
    if sfn is None:
        miss.append(lab_fn); continue
    cid = lab_fn.split('_')[0][1:]
    if sfn not in p['clusters'].get(cid, []):
        miss.append(lab_fn + '(not in cluster)'); continue
    idx = p['clusters'][cid].index(sfn)
    drops.setdefault(cid, []).append(idx)

if miss:
    print('MISS:', miss)
for cid, idxs in sorted(drops.items()):
    mem = p['clusters'][cid]
    keep = [m for i, m in enumerate(mem) if i not in set(idxs)]
    print('c%s (%s): %d -> %d' % (cid, p['labels'][cid], len(mem), len(keep)))
    p['clusters'][cid] = keep
json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
from cluster import apply_labels
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
for ch in 'abdegilmnopruvwy':
    print(ch, len(man['chars'].get(ch, [])), end='  ')
print()
qs = [m.get('q', 0) for m in man['metrics'].values()]
print('q stats: min=%.3f median=%.3f max=%.3f n=%d' % (
    min(qs), float(np.median(qs)), max(qs), len(qs)))
