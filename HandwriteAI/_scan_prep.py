"""One-shot: extract + preprocess DocScanner pages for OCR.

Zoom-3 render -> grayscale -> autocontrast -> save PNG.
Outputs: Test_input/scan_work/pages/pageN.png (+ pageN_raw.png for reference).
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "Test_input", "DocScanner 07-Oct-2026 01-17 AM (1).pdf")
WORK = os.path.join(BASE, "Test_input", "scan_work", "pages")
os.makedirs(WORK, exist_ok=True)

import fitz
from PIL import Image, ImageOps

doc = fitz.open(SRC)
print("pages:", doc.page_count)
for i, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
    raw = os.path.join(WORK, f"page{i + 1}_raw.png")
    pix.save(raw)
    img = Image.open(raw).convert("L")
    img = ImageOps.autocontrast(img, cutoff=1)
    out = os.path.join(WORK, f"page{i + 1}.png")
    img.save(out)
    print(f"page{i + 1}: {img.size[0]}x{img.size[1]} -> {os.path.basename(out)}")
print("OK prep")
