"""F5: apply pool prunes + rebuild .labeled with q-scores."""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
drops = {
    '45': [1],
    '21': [12, 13, 15, 25, 26, 29, 31, 39, 47, 56, 65, 77] + list(range(78, 98)),
    '46': [4, 5, 10, 30, 33, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    '15': [45, 66],
    '2': [55, 69, 72],
    '13': [27, 58, 63],
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
