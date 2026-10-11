"""Flag structural junk in labeled clusters: fragments (tiny ink area),
multi-letter crops (overwide), wrong-shape members (aspect outliers).
Draws flagged cells with 'cid/idx' labels for human confirmation.
Usage: python _suspect.py            -> all labeled clusters
       python _suspect.py 21 25      -> subset
"""
import sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np
from PIL import Image, ImageDraw
from cluster import _resolve_lib

cdir = 'styles/user_001.clusters'
payload = json.load(open(os.path.join(cdir, 'clusters.json')))
lib = _resolve_lib(cdir, payload['lib'])
cids = sys.argv[1:] or [c for c, ch in payload['labels'].items() if ch]

def ink_stats(fn):
    a = np.array(Image.open(os.path.join(lib, fn)).convert('L'))
    ys, xs = np.where(a < 200)
    if not len(ys):
        return None
    h = ys.max() - ys.min() + 1
    w = xs.max() - xs.min() + 1
    return w, h, len(ys), a.shape

rows = []
for cid in sorted(cids, key=int):
    members = payload['clusters'].get(str(cid), [])
    st = [ink_stats(fn) for fn in members]
    st = [(i, s) for i, s in enumerate(st) if s]
    if len(st) < 4:
        continue
    med_w = float(np.median([s[0] for _, s in st]))
    med_h = float(np.median([s[1] for _, s in st]))
    med_a = float(np.median([s[2] for _, s in st]))
    med_aspect = med_w / max(1.0, med_h)
    for i, (w, h, area, shape) in st:
        why = []
        if area < 0.40 * med_a:
            why.append('tiny')
        if w > 2.0 * med_w:
            why.append('wide')
        aspect = w / max(1.0, h)
        if med_aspect > 0 and (aspect > 1.6 * med_aspect or aspect < 0.4 * med_aspect):
            why.append('aspect')
        if why:
            rows.append((cid, i, members[i], '+'.join(why), shape))

print(f'{len(rows)} suspects')
# draw sheets: 6 cells/row, cell 72px wide (thumb 60 + label)
per_sheet = 48
font = None
try:
    from PIL import ImageFont
    font = ImageFont.load_default()
except Exception:
    pass
for page in range(0, len(rows), per_sheet):
    chunk = rows[page:page + per_sheet]
    nrow = (len(chunk) + 5) // 6
    sheet = Image.new('RGB', (6 * 76, nrow * 92), 'white')
    d = ImageDraw.Draw(sheet)
    for j, (cid, i, fn, why, shape) in enumerate(chunk):
        x, y = (j % 6) * 76, (j // 6) * 92
        try:
            im = Image.open(os.path.join(lib, fn)).convert('RGB')
            im.thumbnail((60, 60))
            sheet.paste(im, (x + 2, y + 2))
        except Exception:
            pass
        d.text((x + 2, y + 66), f'{cid}:{i} {why}', fill='black', font=font)
        d.text((x + 2, y + 76), fn[:11], fill='gray', font=font)
    out = f'outputs/SUSPECTS-{page // per_sheet}.png'
    sheet.save(out)
    print(out, len(chunk))
