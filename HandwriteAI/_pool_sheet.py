"""Indexed contact sheet for a labeled char pool."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw
import profiles

info = profiles.resolve("")
lab = info["labeled"]
ch = sys.argv[1] if len(sys.argv) > 1 else 'l'
manifest = json.load(open(os.path.join(lab, "manifest.json")))
files = manifest['chars'][ch]
cols = 8
cell = 90
rows = (len(files) + cols - 1) // cols
sheet = Image.new('RGB', (cols*cell, rows*cell), 'white')
d = ImageDraw.Draw(sheet)
for i, fn in enumerate(files):
    im = Image.open(os.path.join(lab, fn)).convert('RGB')
    im = im.resize((70, 70), Image.NEAREST)
    x, y = (i%cols)*cell + 8, (i//cols)*cell + 18
    sheet.paste(im, (x, y))
    d.text((x, y-16), fn.split('_')[-1].replace('.png',''), fill='red')
sheet.save('Test_input/pool-%s.png' % ch)
print('pool-%s n=%d' % (ch, len(files)))
