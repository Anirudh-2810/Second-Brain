"""One-shot: OCR the 3 prepped scan pages, keep best-PSM text per page.

Tries PSM 6/4/3 (LSTM, oem 1), scores by mean word confidence, writes
Test_input/scan_work/ocr_draft.txt with page separators + a conf report.
Handwriting source: expect draft quality, user corrects before render.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(BASE, "Test_input", "scan_work", "pages")
OUT = os.path.join(BASE, "Test_input", "scan_work", "ocr_draft.txt")

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocr(path, psm):
    cfg = f"--oem 1 --psm {psm}"
    text = pytesseract.image_to_string(Image.open(path), config=cfg)
    data = pytesseract.image_to_data(Image.open(path), config=cfg,
                                     output_type=pytesseract.Output.DATAFRAME)
    try:
        conf = data[data.conf > 0].conf
        mean = float(conf.mean()) if len(conf) else 0.0
        n = int(len(conf))
    except Exception:
        mean, n = 0.0, 0
    return text, mean, n


report = []
draft = []
for i in (1, 2, 3):
    path = os.path.join(PAGES, f"page{i}.png")
    cands = [(psm,) + ocr(path, psm) for psm in (6, 4, 3)]
    cands.sort(key=lambda c: c[2], reverse=True)
    psm, text, mean, n = cands[0]
    report.append(f"page{i}: psm={psm} mean_conf={mean:.1f} words={n} "
                  f"chars={len(text.strip())}")
    draft.append(f"===== PAGE {i} (psm {psm}, conf {mean:.0f}) =====")
    draft.append(text.strip() or "[no text recognized]")
    print(report[-1])

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n\n".join(report) + "\n\n" + "\n\n".join(draft) + "\n")
print("draft ->", os.path.relpath(OUT, BASE))
print("OK ocr")
