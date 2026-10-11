"""Prune wrong-letter crops from the t/f/s/r harvest (pool-sheet eyeballing).
Operates directly on clusters.json by index (pool idx == cluster idx for
single-cluster letters; r = c19[0:14] + c29[0:64])."""
import json, os, sys
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from cluster import apply_labels

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))

# t: keep only clear-crossbar t's (drop f-loops, y-hooks, ruled artifacts, dotted)
T_KEEP = (4, 5, 9, 11, 15, 16, 19)
mem = p['clusters']['11']
print('t: %d -> %d' % (len(mem), len(T_KEEP)))
p['clusters']['11'] = [mem[i] for i in T_KEEP]

# f: drop p-dot(7), 5-shape(11), d-loops(13,18)
F_DROP = {7, 11, 13, 18}
mem = p['clusters']['64']
keep = [m for i, m in enumerate(mem) if i not in F_DROP]
print('f: %d -> %d' % (len(mem), len(keep)))
p['clusters']['64'] = keep

# s: drop ruled-line artifacts(7,11), J-thins(13,17,18,37,39), "of"(36), p(38)
S_DROP = {7, 11, 13, 17, 18, 36, 37, 38, 39}
mem = p['clusters']['65']
keep = [m for i, m in enumerate(mem) if i not in S_DROP]
print('s: %d -> %d' % (len(mem), len(keep)))
p['clusters']['65'] = keep

# r: drop e-loops, C-curves, ruled artifacts, t/p/8/1 intruders from c29.
# pool order = c19[0:14] then c29; pool idx - 14 = c29 idx.
R_C29_DROP = (18, 21, 22, 35, 36, 42, 47,
              51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63)
mem = p['clusters']['29']
keep = [m for i, m in enumerate(mem) if i not in set(R_C29_DROP)]
print('r c29: %d -> %d (c19 keeps 14)' % (len(mem), len(keep)))
p['clusters']['29'] = keep

json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
for ch in 'abdefgilmnoprstuvwy':
    print(ch, len(man['chars'].get(ch, [])), end='  ')
print()
qs = [m.get('q', 0) for m in man['metrics'].values()]
print('q stats: min=%.3f median=%.3f max=%.3f n=%d' % (
    min(qs), float(np.median(qs)), max(qs), len(qs)))
