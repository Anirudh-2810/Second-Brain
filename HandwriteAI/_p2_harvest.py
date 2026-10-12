"""One-shot: Profile 2 harvest - 9 ruled-notebook pages -> glyph library.

Scope: ONLY the 3 same-hand PDFs (answer-sheet excluded by user decision).
Extracts page PNGs, builds styles/profile_002.glyphs/, sanitizes, reports.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PDFS = [
    "Test_input/DocScanner 07-Oct-2026 01-17 AM (1).pdf",
    "Test_input/DocScanner 07-Oct-2026 01-21 AM.pdf",
    "Test_input/DocScanner 07-Oct-2026 01-23 AM.pdf",
]
PAGEDIR = os.path.join(BASE, "Test_input", "profile2_pages")
os.makedirs(PAGEDIR, exist_ok=True)

import fitz
from glyphs import build_library, sanitize_library
import profiles

paths = []
for pdf in PDFS:
    doc = fitz.open(os.path.join(BASE, pdf))
    tag = os.path.basename(pdf).replace(".pdf", "").replace(" ", "_")
    for i, page in enumerate(doc):
        out = os.path.join(PAGEDIR, f"{tag}_p{i + 1}.png")
        page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5)).save(out)
        paths.append(out)
print(f"pages: {len(paths)}")

info = profiles.resolve("Profile 2")
man = build_library(paths, info["glyphs"])
print(f"harvest: n={man['n_glyphs']} pages={man['n_pages']} "
      f"line_h_ref={man['line_h_ref']} buckets={man['buckets']}")
rep = sanitize_library(info["glyphs"])
print("sanitize:", rep)
print("OK p2 harvest")
