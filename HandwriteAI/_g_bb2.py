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
    new_bb = body_bottom_frac(arr)
    old_bb = (man['metrics'].get(fn) or {}).get('bb')
    print(fn, 'old=%.3f new=%.3f' % (old_bb, new_bb))
