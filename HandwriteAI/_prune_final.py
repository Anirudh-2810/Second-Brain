"""Final quality prune: worst t/s offenders from pool-sheet review."""
import json, os, sys
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from cluster import apply_labels

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))

# t: drop 003 (f-like bottom curl). Current 4 -> 3.
mem = p['clusters']['11']
print('t: %d -> 3' % len(mem))
p['clusters']['11'] = [mem[i] for i in (0, 1, 2)]

# s: drop thin j-reads(11,12), cut(15), a-like(23), odd(26), underlined(7)
S_DROP = {7, 11, 12, 15, 23, 26}
mem = p['clusters']['65']
keep = [m for i, m in enumerate(mem) if i not in S_DROP]
print('s: %d -> %d' % (len(mem), len(keep)))
p['clusters']['65'] = keep

json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
for ch in 'abdefgilmnoprstuvwy':
    print(ch, len(man['chars'].get(ch, [])), end='  ')
print()
