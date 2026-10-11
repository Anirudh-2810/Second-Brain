"""Contact sheets for all unlabeled clusters."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from PIL import Image, ImageDraw
from cluster import _resolve_lib

cdir = 'styles/user_001.clusters'
payload = json.load(open(os.path.join(cdir, 'clusters.json')))
lib = _resolve_lib(cdir, payload['lib'])
lab = payload['labels']
unlabeled = [k for k in sorted(payload['clusters'], key=int)
             if k not in lab or not lab[k]]
cell, cols = 70, 10
for cid in unlabeled:
    members = payload['clusters'][cid]
    n = min(50, len(members))
    rows = (n + cols - 1) // cols
    sheet = Image.new('RGB', (cols*cell, rows*cell+16), 'white')
    d = ImageDraw.Draw(sheet)
    d.text((4, 2), 'c%s n=%d' % (cid, len(members)), fill='red')
    for i, fn in enumerate(members[:n]):
        try:
            im = Image.open(os.path.join(lib, fn)).convert('RGB')
            im.thumbnail((56, 56))
            sheet.paste(im, ((i%cols)*cell+6, (i//cols)*cell+18))
        except Exception:
            pass
    sheet.save(os.path.join(cdir, 'unlab_%03d.png' % int(cid)))
print('sheets written for', len(unlabeled), 'clusters')
print('ids:', ','.join(unlabeled))
