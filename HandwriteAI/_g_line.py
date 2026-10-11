import numpy as np
from PIL import Image
import os
lib = r'styles/user_001.glyphs'
for fn in ['p07_0022_tall.png','p06_0059_tall.png','p06_0347_tall.png','p06_0425_tall.png','p06_0494_tall.png']:
    arr = np.array(Image.open(os.path.join(lib, fn)).convert('L'))
    ink = arr < 200
    h, w = ink.shape
    roww = ink.sum(axis=1)
    # rows that are nearly full width
    full = np.where(roww > 0.8*w)[0]
    print(fn, 'h=%d w=%d fullwidth_rows=%s' % (h, w, full.tolist()))
    if len(full):
        # min pixel value on those rows (darkness of the line)
        vals = [int(arr[r].min()) for r in full]
        print('   line min-pixels:', vals)
