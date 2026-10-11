"""Round 3c: drop the two high-q a-like o's caught by pick-spying
(c55_o_007 bottom-right exit stem q=0.976; c55_o_031 stem below bowl).
Maps labeled names -> source filenames via array md5 -> cluster index.
"""
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

drops = {}
for lab_fn in ['c55_o_007.png', 'c55_o_031.png']:
    a = np.array(Image.open(os.path.join(lib, lab_fn)).convert('L'))
    sfn = src_by.get(amd5(a))
    if sfn is None:
        print('MISS', lab_fn)
        continue
    cid = lab_fn.split('_')[0][1:]
    idx = p['clusters'][cid].index(sfn)
    drops.setdefault(cid, []).append(idx)
    print(lab_fn, '-> c%s #%d %s' % (cid, idx, sfn))

for cid, idxs in drops.items():
    mem = p['clusters'][cid]
    keep = [m for i, m in enumerate(mem) if i not in set(idxs)]
    print('c%s: %d -> %d' % (cid, len(mem), len(keep)))
    p['clusters'][cid] = keep
json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
from cluster import apply_labels
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
print('o now', len(man['chars']['o']), 'total', man['n_glyphs'])
