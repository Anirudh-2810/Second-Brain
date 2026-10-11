import json, os, sys
sys.path.insert(0, '.')
import numpy as np
from PIL import Image
from glyphs import body_bottom_frac

lib = r'styles/user_001.glyphs'
man_path = os.path.join(lib, 'manifest.json')
man = json.load(open(man_path))
fns = ['p07_0022_tall.png','p06_0059_tall.png','p06_0347_tall.png','p06_0425_tall.png','p06_0494_tall.png']
for fn in fns:
    arr = np.array(Image.open(os.path.join(lib, fn)).convert('L'))
    man['metrics'][fn] = {'bb': body_bottom_frac(arr)}
    print(fn, man['metrics'][fn])
json.dump(man, open(man_path, 'w'), indent=1)

# re-apply labels so the labeled manifest picks up new bb
from cluster import apply_labels
cdir = 'styles/user_001.clusters'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
labman = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
for fn in labman['chars'].get('g', []):
    m = labman['metrics'][fn]
    print('labeled', fn, 'bb=%.3f q=%.3f' % (m.get('bb'), m.get('q', 0)))
