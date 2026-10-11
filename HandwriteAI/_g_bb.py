import numpy as np
from PIL import Image
import os
lib = r'styles/user_001.glyphs'
for fn in ['p07_0022_tall.png','p06_0059_tall.png','p06_0347_tall.png','p06_0425_tall.png','p06_0494_tall.png']:
    arr = np.array(Image.open(os.path.join(lib, fn)).convert('L'))
    ink = arr < 200
    h, w = ink.shape
    roww = ink.sum(axis=1)
    # print profile compactly: every row bucket of 4
    prof = [int(roww[i:i+4].mean()) for i in range(0, h, 4)]
    print(fn, 'h=%d w=%d' % (h, w))
    print('  prof(4-row avg):', prof)
    # valley search: bowl bottom should be local min between two humps
    # hump1 = bowl (top 30-70%), hump2 may be descender hook
    mx = roww.max()
    wide = roww >= 0.35*mx
    print('  wide rows:', np.where(wide)[0].min(), '-', np.where(wide)[0].max(), 'of', h)
