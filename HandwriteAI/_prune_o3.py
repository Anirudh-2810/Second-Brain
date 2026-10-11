"""Round 3: o pool de-a/θ pass.
c55: theta bars (0,28,36), open-top a-likes (17,21), C-shape (53), crop junk (41).
c59: keep only clean closed o's; loop-crossers read theta/a in words.
"""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
drops = {
    '55': [0, 17, 21, 28, 36, 41, 53],
    '59': [0, 1, 2, 4, 6, 7, 9, 11, 12, 14, 17, 18, 19, 20, 22, 23, 24],
}
for cid, idxs in drops.items():
    mem = p['clusters'][cid]
    keep = [m for i, m in enumerate(mem) if i not in set(idxs)]
    print(f"c{cid} ({p['labels'][cid]}): {len(mem)} -> {len(keep)}")
    p['clusters'][cid] = keep
json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
from cluster import apply_labels
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
qs = [m.get('q', 0) for m in man['metrics'].values()]
print('q stats: min=%.3f median=%.3f max=%.3f n=%d' % (
    min(qs), float(np.median(qs)), max(qs), len(qs)))
for ch in 'abdegilmnopruvwy':
    print(ch, len(man['chars'].get(ch, [])), end='  ')
print()
