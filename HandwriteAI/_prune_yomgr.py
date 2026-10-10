"""Love-note round: prune y(r-lookalikes)/o(a-lookalikes)/m(squished)/g(9-lookalikes)/r(speck).
"""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
drops = {
    '30': list(range(len(p['clusters']['30']))),  # y: all gamma-style, reads as r
    '19': [0],                                     # r: near-invisible speck
    '55': [4, 15, 40, 64],                         # o: theta-double, junk, 6-like, a-like
    '59': [0, 3, 8, 12, 15, 17, 18, 19, 21, 23, 25, 28, 32, 33, 36, 39, 40],  # o: l-loops, 6s, a-likes
    '46': [0, 3, 5, 13, 20, 22],                   # m: squished, flat, mn-merged
    '45': [1, 2, 4, 5, 6],                         # g: 9-like/f-like, keep bowl+descender
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
