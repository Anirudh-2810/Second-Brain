"""Full indexed sheets for harvest clusters."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from PIL import Image, ImageDraw
from cluster import _resolve_lib

cdir = 'styles/user_001.clusters'
payload = json.load(open(os.path.join(cdir, 'clusters.json')))
lib = _resolve_lib(cdir, payload['lib'])
for cid in ('11', '29', '44', '47'):
    members = payload['clusters'][cid]
    n = len(members)
    cols = 12
    cell = 64
    rows = (n + cols - 1) // cols
    sheet = Image.new('RGB', (cols*cell, rows*cell), 'white')
    d = ImageDraw.Draw(sheet)
    for i, fn in enumerate(members):
        try:
            im = Image.open(os.path.join(lib, fn)).convert('RGB')
            im.thumbnail((50, 50))
            x, y = (i%cols)*cell+6, (i//cols)*cell+12
            sheet.paste(im, (x, y))
            d.text((x, y-11), str(i), fill='red')
        except Exception:
            pass
    sheet.save(os.path.join(cdir, 'full_%s.png' % cid))
    print('full_%s n=%d' % (cid, n))
