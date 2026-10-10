"""Indexed contact sheet: stamps cluster-local index (clusters.json order) on each cell.
Usage: python _isheet.py 19 55 59 46 45
"""
import sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from PIL import Image, ImageDraw
from cluster import _resolve_lib

CID = sys.argv[1:]
cdir = 'styles/user_001.clusters'
payload = json.load(open(os.path.join(cdir, 'clusters.json')))
lib = _resolve_lib(cdir, payload['lib'])

CELL, PAD, COLS = 96, 4, 8
for cid in CID:
    members = payload['clusters'].get(str(cid), [])
    n = min(160, len(members))
    rows = (n + COLS - 1) // COLS
    sheet = Image.new('RGB', (CELL * COLS, CELL * rows), 'white')
    dr = ImageDraw.Draw(sheet)
    for i, fn in enumerate(members[:n]):
        x, y = (i % COLS) * CELL, (i // COLS) * CELL
        try:
            im = Image.open(os.path.join(lib, fn)).convert('RGB')
            im.thumbnail((CELL - 18, CELL - 18))
            sheet.paste(im, (x + PAD + 12, y + PAD + 12))
        except Exception:
            pass
        dr.text((x + 3, y + 2), str(i), fill=(200, 0, 0))
    out = os.path.join(cdir, f'cluster_{int(cid):03d}_idx.png')
    sheet.save(out)
    print(f'{out}  n={len(members)} shown={n}')
