"""One-shot: full indexed sheets for Profile 2 clusters (agent labeling).

Usage: python _p2_sheet.py 14 24 8 37
Writes Test_input/p2_sheets/full_<cid>.png with index numbers under each crop.
"""
import os, sys, json, math
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_002.glyphs")
CDIR = os.path.join(BASE, "styles", "profile_002.clusters")
OUT = os.path.join(BASE, "Test_input", "p2_sheets")
os.makedirs(OUT, exist_ok=True)

payload = json.load(open(os.path.join(CDIR, "clusters.json"), encoding="utf-8"))
for cid in sys.argv[1:]:
    members = payload["clusters"].get(str(int(cid)), [])
    cols = 10
    rows = math.ceil(len(members) / cols)
    sheet = Image.new("RGB", (cols * 90, rows * 100), "white")
    d = ImageDraw.Draw(sheet)
    for i, fn in enumerate(members):
        try:
            im = Image.open(os.path.join(LIB, fn)).convert("RGB")
            im.thumbnail((84, 78))
        except Exception:
            continue
        x, y = (i % cols) * 90, (i // cols) * 100
        sheet.paste(im, (x + 3, y + 3))
        d.text((x + 3, y + 84), str(i), fill=(150, 150, 150))
    out = os.path.join(OUT, f"full_{int(cid):03d}.png")
    sheet.save(out)
    print(f"cid {cid}: n={len(members)} -> {os.path.basename(out)}")
print("OK sheets")
