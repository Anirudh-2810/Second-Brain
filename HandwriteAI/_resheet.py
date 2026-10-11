"""Regenerate contact sheets with MORE samples (48) for label verification.
Usage: python _resheet.py 8 15 19 30 45   (cluster ids)
Sheet order == clusters.json member order (i%6 col, i//6 row) -- same grid
rule as cluster.py, so keep indices map 1:1 to the JSON list.
"""
import sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from PIL import Image
from cluster import _resolve_lib

CID = sys.argv[1:] or []
cdir = 'styles/user_001.clusters'
payload = json.load(open(os.path.join(cdir, 'clusters.json')))
lib = _resolve_lib(cdir, payload['lib'])

for cid in CID:
    members = payload['clusters'].get(str(cid), [])
    n = min(132, len(members))
    rows = (n + 5) // 6
    sheet = Image.new('RGB', (64 * 6, 64 * rows), 'white')
    for i, fn in enumerate(members[:n]):
        try:
            im = Image.open(os.path.join(lib, fn)).convert('RGB')
            im.thumbnail((60, 60))
            sheet.paste(im, ((i % 6) * 64 + 2, (i // 6) * 64 + 2))
        except Exception:
            pass
    out = os.path.join(cdir, f'cluster_{int(cid):03d}_all.png')
    sheet.save(out)
    if os.path.exists(os.path.join(cdir, f'cluster_{int(cid):03d}_48.png')):
        os.remove(os.path.join(cdir, f'cluster_{int(cid):03d}_48.png'))
    print(f'{out}  n={len(members)} shown={n}')
