"""Second t prune: keep only clean-stem t's (drop bottom-curl -> f, blobby -> p)."""
import json, os, sys
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from cluster import apply_labels

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
T_KEEP = (0, 1, 2, 5)  # within current 7: pool-t 004,005,009,016 (drop curl-bottom 015,019 and blobby 011)
mem = p['clusters']['11']
print('t: %d -> %d' % (len(mem), len(T_KEEP)))
p['clusters']['11'] = [mem[i] for i in T_KEEP]
json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
print('t', len(man['chars'].get('t', [])), 'total', sum(len(v) for v in man['chars'].values()))
