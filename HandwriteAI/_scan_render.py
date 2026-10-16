"""One-shot: render scan segments + compose scan-handwritten.pdf (A4 flow)."""
import os, io, time

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(BASE, "Test_input", "scan_work")
OUT = os.path.join(BASE, "outputs", "scan-handwritten.pdf")
os.makedirs(os.path.join(BASE, "outputs"), exist_ok=True)

import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import profiles
from inference import load_style, render_labeled

info = profiles.resolve("Profile 1")
style = load_style(info["style"])

imgs = []
for name in ["seg_scan1", "seg_scan2", "seg_scan3"]:
    with open(os.path.join(WORK, name + ".txt"), encoding="utf-8") as f:
        text = f.read()
    t0 = time.time()
    img = render_labeled(text, style, info["labeled"], width=1600, seed=7,
                         target_h=32, page_h=None)[0]
    img.save(os.path.join(WORK, name + ".png"), dpi=(300, 300))
    print(f"{name}: {len(text)} chars -> {img.size[0]}x{img.size[1]} "
          f"in {time.time()-t0:.1f}s")
    imgs.append(img)

PAGE_W, PAGE_H = 595.27, 841.89
MARGIN, CONTENT_W, MAX_H, GAP = 36.0, 595.27 - 72.0, 841.89 - 92.0, 10.0
BG = np.array([253, 252, 247])


def slices(img):
    px_per_pt = img.size[0] / CONTENT_W
    target = int(MAX_H * px_per_pt)
    if img.size[1] <= target:
        return [img]
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    blank = (np.abs(a - BG).max(axis=(1, 2)) < 12)
    H, y, out = img.size[1], 0, []
    while H - y > target:
        lo, hi = y + target - 250, min(H - 8, y + target + 250)
        cands = np.nonzero(blank[max(y + 200, lo):hi + 1])[0]
        cut = (y + target) if len(cands) == 0 else (max(y + 200, lo) + int(cands[len(cands) // 2]))
        if H - cut < 500:
            break
        out.append(img.crop((0, y, img.size[0], cut)))
        y = cut
    out.append(img.crop((0, y, img.size[0], H)))
    return out


c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))
c.setTitle("DocScanner notes — handwritten (Profile 1)")
c.setFont("Helvetica-Bold", 7)
c.setFillColorRGB(0.45, 0.45, 0.45)
c.drawString(MARGIN, PAGE_H - 28, "DocScanner 07-Oct-2026 — handwritten transcription (Profile 1)")
y, npages = PAGE_H - 48, 1
for si, img in enumerate(imgs):
    c.setFont("Helvetica-Bold", 7)
    c.setFillColorRGB(0.55, 0.55, 0.55)
    if y - 14 < MARGIN:
        c.showPage(); npages += 1; y = PAGE_H - MARGIN
    c.drawString(MARGIN, y - 10, f"— source p. {si + 1} —")
    y -= 16
    for s in slices(img):
        h = s.size[1] * CONTENT_W / s.size[0]
        if y - h < MARGIN:
            c.showPage(); npages += 1; y = PAGE_H - MARGIN
        buf = io.BytesIO()
        s.convert("RGB").save(buf, format="JPEG", quality=85)
        buf.seek(0)
        c.drawImage(ImageReader(buf), MARGIN, y - h, width=CONTENT_W, height=h)
        y -= h + GAP
c.save()
print(f"saved: {OUT} ({npages} pages, {os.path.getsize(OUT)/1e6:.1f} MB)")
print("OK scan render+compose")
