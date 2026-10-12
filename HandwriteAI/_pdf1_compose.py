"""One-shot: assemble inline final PDF for file-example_PDF_1MB.pdf.

Flow: handwritten segment PNGs (sliced at whitespace rows) + original
figure assets inline in manifest order, packed onto A4 pages.
Figure captions + section labels are printed (Helvetica), body is ink.

Output: outputs/pdf1-handwritten.pdf
"""
import os, json, io

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(BASE, "Test_input", "pdf1_work")
OUT = os.path.join(BASE, "outputs", "pdf1-handwritten.pdf")
os.makedirs(os.path.join(BASE, "outputs"), exist_ok=True)

import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

PAGE_W, PAGE_H = 595.27, 841.89  # A4 pt
MARGIN = 36.0
CONTENT_W = PAGE_W - 2 * MARGIN          # 523.27
MAX_H = PAGE_H - 2 * MARGIN - 20         # headroom for section label
GAP, FIG_GAP, CAP_GAP = 10.0, 6.0, 4.0
BG = np.array([253, 252, 247])
CAPTION_FONT = ("Helvetica", 8)
LABEL_FONT = ("Helvetica-Bold", 7)


def blank_rows(img):
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    return (np.abs(a - BG).max(axis=(1, 2)) < 12)


def slice_to_height(img, max_h_pt, content_w_pt=CONTENT_W):
    """Split tall image into slices fitting max_h_pt when scaled to content width."""
    px_per_pt = img.size[0] / content_w_pt
    target = int(max_h_pt * px_per_pt)
    if img.size[1] <= target:
        return [img]
    blank = blank_rows(img)
    H = img.size[1]
    slices, y = [], 0
    while H - y > target:
        lo, hi = max(y + 200, y + target - 250), min(H - 8, y + target + 250)
        cands = np.nonzero(blank[lo:hi + 1])[0]
        cut = (y + target) if len(cands) == 0 else (lo + int(cands[len(cands) // 2]))
        if H - cut < 500:  # avoid sliver tail
            break
        slices.append(img.crop((0, y, img.size[0], cut)))
        y = cut
    slices.append(img.crop((0, y, img.size[0], H)))
    return slices


def scaled_h(img, w_pt=CONTENT_W):
    return img.size[1] * w_pt / img.size[0]


with open(os.path.join(WORK, "manifest.json"), encoding="utf-8") as f:
    manifest = json.load(f)

ASSET_FILE = {"photo": "photo.jpg", "chart_A": "chart_A.png",
              "chart_B": "chart_B.png", "table": "table.png"}

# build ordered item list: ("img", PIL) / ("caption", str) / ("label", str)
items = []
for pg in manifest["pages"]:
    items.append(("label", "source p. %d" % pg["src"]))
    for b in pg["blocks"]:
        if b["kind"] == "text":
            img = Image.open(os.path.join(WORK, b["seg"] + ".png"))
            for s in slice_to_height(img, MAX_H):
                items.append(("img", s, "JPEG"))
        else:
            img = Image.open(os.path.join(WORK, ASSET_FILE[b["asset"]]))
            fmt = "JPEG" if b["asset"] == "photo" else "PNG"
            for s in slice_to_height(img, MAX_H - 20):
                items.append(("img", s, fmt))
            items.append(("caption", b["caption"] + " — src p. %d" % pg["src"]))

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))
c.setTitle("file-example_PDF_1MB — handwritten (Profile 1) + original figures")
c.setFont(*LABEL_FONT); c.setFillColorRGB(0.45, 0.45, 0.45)
c.drawString(MARGIN, PAGE_H - 28, "file-example_PDF_1MB.pdf — handwritten transcription (Profile 1) + original figures inline")
y = PAGE_H - 48
npages = 1


def new_page():
    global y, npages
    c.showPage(); npages += 1; y = PAGE_H - MARGIN


for item in items:
    kind = item[0]
    if kind == "label":
        val = item[1]
        if y < PAGE_H - MARGIN - 14:
            y -= 6
        c.setFont(*LABEL_FONT); c.setFillColorRGB(0.55, 0.55, 0.55)
        if y - 12 < MARGIN:
            new_page()
        c.drawString(MARGIN, y - 10, "— %s —" % val)
        y -= 14
    elif kind == "caption":
        val = item[1]
        c.setFont(*CAPTION_FONT); c.setFillColorRGB(0.4, 0.4, 0.4)
        if y - 12 < MARGIN:
            new_page()
        c.drawString(MARGIN + 2, y - 10, val)
        y -= 12 + CAP_GAP
    else:
        img, fmt = item[1], item[2]
        h = scaled_h(img)
        if y - h < MARGIN:
            new_page()
        buf = io.BytesIO()
        rgb = img.convert("RGB") if img.mode != "RGB" else img
        if fmt == "JPEG":
            rgb.save(buf, format="JPEG", quality=85)
        else:
            rgb.save(buf, format="PNG")
        buf.seek(0)
        c.drawImage(ImageReader(buf), MARGIN, y - h, width=CONTENT_W, height=h)
        y -= h + GAP

c.save()
size_mb = os.path.getsize(OUT) / 1e6
print(f"saved: {OUT} ({npages} pages, {size_mb:.1f} MB, {len(items)} items)")
print("OK compose")
