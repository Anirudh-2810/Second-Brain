"""Restore 5 clean g variants (closed bowl + descender) into c45."""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np

cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
keep = [
    'p07_0022_tall.png',   # labeled 002: closed bowl, hooked descender
    'p06_0059_tall.png',   # labeled 004: closed bowl, straight descender
    'p06_0347_tall.png',   # labeled 005: closed bowl, baseline rule visible
    'p06_0425_tall.png',   # labeled 006: closed bowl, left-hook descender
    'p06_0494_tall.png',   # labeled 013: closed bowl, hooked descender
]
lib = p['lib']
missing = [f for f in keep if not os.path.exists(os.path.join(lib, f))]
if missing:
    print('MISSING in lib:', missing); sys.exit(1)
p['clusters']['45'] = keep
json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
from cluster import apply_labels
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
for ch in 'abdegilmnopruvwy':
    print(ch, len(man['chars'].get(ch, [])), end='  ')
print()
qs = [m.get('q', 0) for m in man['metrics'].values()]
print('q stats: min=%.3f median=%.3f max=%.3f n=%d' % (
    min(qs), float(np.median(qs)), max(qs), len(qs)))
for fn in man['chars'].get('g', []):
    m = man['metrics'][fn]
    print(fn, 'bb=%.3f q=%.3f' % (m.get('bb', -1), m.get('q', 0)))
