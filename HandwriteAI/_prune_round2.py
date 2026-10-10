"""Round 2: strict o/v prunes + g font fallback."""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
drops = {
    '55': [3, 20, 34, 40],          # o: tails that read a-like/6-like
    '0':  [1, 9, 16, 23, 24, 30, 31],  # v: specks, a-like tails, blob
    '45': list(range(len(p['clusters']['45']))),  # g: all read as 9/d -> font fallback
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
