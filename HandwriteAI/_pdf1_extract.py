"""One-shot: extract text segments + figure assets from file-example_PDF_1MB.pdf.

Layout (5-page cycle x6 = 30 pages):
  type C chart-page : headings + paras + 6 bullets + vector bar chart (last)
  type T table-page : paras + heading + table grid + closing para
  type X text-page  : body text only
  type P photo-page : keyboard photo on top + body text (2 variants: p4, p5)

Outputs (Test_input/pdf1_work/, gitignored):
  photo.jpg, chart_A.png, chart_B.png, table.png
  seg_chart.txt, seg_table_pre.txt, seg_table_post.txt, seg_p3.txt, seg_p4.txt, seg_p5.txt
  manifest.json  (ordered blocks for all 30 source pages)
"""
import os, json, hashlib

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "Test_input", "file-example_PDF_1MB.pdf")
WORK = os.path.join(BASE, "Test_input", "pdf1_work")
os.makedirs(WORK, exist_ok=True)

import fitz  # PyMuPDF (requirements.txt)

BULLETS = {"\uf0b7", "\u2022", "\u00b7", "-", "\u2013"}
TERMINAL = (".", ":", "!", "?", ";")


def is_bullet(line):
    return line.strip() in BULLETS


def reflow(lines):
    """Join hard-wrapped lines; keep headings/bullets/numbers on own lines."""
    out, cur = [], ""
    for ln in lines:
        s = ln.strip()
        if not s:
            if cur:
                out.append(cur); cur = ""
            continue
        if is_bullet(s):
            if cur:
                out.append(cur); cur = ""
            out.append("\u2022")
            continue
        if cur and len(cur) >= 60 and not cur.endswith(TERMINAL):
            cur = cur + " " + s
        else:
            if cur:
                out.append(cur)
            cur = s
    if cur:
        out.append(cur)
    # fold lone bullets into '- text'
    folded = []
    i = 0
    while i < len(out):
        if out[i] == "\u2022" and i + 1 < len(out):
            folded.append("- " + out[i + 1])
            i += 2
        else:
            folded.append(out[i])
            i += 1
    return "\n".join(folded)


def chart_bbox(page):
    rects = [d["rect"] for d in page.get_drawings()
             if d["rect"].y0 > 550 and (d["rect"].width > 10 or d["rect"].height > 10)]
    if not rects:
        return fitz.Rect(40, 556, 555, 800)
    u = rects[0]
    for r in rects[1:]:
        u = u | r
    # keep y-axis tick labels (x~150) and row/column text labels
    u.x0 = max(30, u.x0 - 25); u.y0 = max(0, u.y0 - 10)
    u.x1 = min(565, u.x1 + 10); u.y1 = min(830, u.y1 + 10)
    return u


def table_bbox(page):
    rules = [d["rect"] for d in page.get_drawings()
             if d["rect"].width > 200 and d["rect"].height < 3]
    if not rules:
        return fitz.Rect(40, 365, 555, 608)
    y0 = min(r.y0 for r in rules) - 16
    y1 = max(r.y1 for r in rules) + 9
    return fitz.Rect(48, max(0, y0), 547, min(830, y1))


def clip_png(page, rect, out, zoom=2.5):
    pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(zoom, zoom))
    pix.save(out)
    return out


doc = fitz.open(SRC)
assert doc.page_count == 30, doc.page_count

# ---- assets ----
p4 = doc[3]
placed = [img for img in p4.get_images(full=True) if p4.get_image_rects(img)]
assert placed, "no placed image on pdf p4"
photo_xref = placed[0][0]
with open(os.path.join(WORK, "photo.jpg"), "wb") as f:
    f.write(doc.extract_image(photo_xref)["image"])
print("photo.jpg <- xref", photo_xref)

ca = chart_bbox(doc[0]); cb = chart_bbox(doc[5])
print("chart clip A:", ca, " B:", cb)
clip_png(doc[0], ca, os.path.join(WORK, "chart_A.png"))
clip_png(doc[5], cb, os.path.join(WORK, "chart_B.png"))
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
print("chart md5:", md5(os.path.join(WORK, "chart_A.png")),
      md5(os.path.join(WORK, "chart_B.png")))

tb = table_bbox(doc[1])
print("table clip:", tb)
clip_png(doc[1], tb, os.path.join(WORK, "table.png"))

# ---- texts ----
def lines(pn):
    return doc[pn].get_text().splitlines()

# chart page (pdf idx 0; idx 5 is reflow twin)
c = lines(0)
assert c[26].strip() == "Row 1" and c[39].strip() == "Column 3", c[26:40]
c2 = lines(5)
seg_chart = reflow(c[:26])
seg_chart_b = reflow([l for l in c2 if l.strip() not in
                      ("Row 1", "Row 2", "Row 3", "Row 4", "0", "2", "4", "6",
                       "8", "10", "12", "Column 1", "Column 2", "Column 3")])
print("chart-text twin identical after reflow:", seg_chart == seg_chart_b)

# table page (pdf idx 1)
t = lines(1)
assert t[13].strip() == "Lorem ipsum" and t[31].strip() == "Ipsum", (t[13], t[31])
seg_table_pre = reflow(t[:13])
seg_table_post = reflow(t[32:])

seg_p3 = reflow(lines(2))
seg_p4 = reflow(lines(3))
seg_p5 = reflow(lines(4))

segs = {"seg_chart": seg_chart, "seg_table_pre": seg_table_pre,
        "seg_table_post": seg_table_post, "seg_p3": seg_p3,
        "seg_p4": seg_p4, "seg_p5": seg_p5}
for name, text in segs.items():
    with open(os.path.join(WORK, name + ".txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{name}: {len(text)} chars")

# ---- manifest: inline blocks for all 30 pages ----
hashA = hashlib.md5(doc[0].get_text().encode()).hexdigest()
pages = []
for i in range(30):
    kind = i % 5
    if kind == 0:
        h = hashlib.md5(doc[i].get_text().encode()).hexdigest()
        chart = "chart_A" if h == hashA else "chart_B"
        pages.append({"src": i + 1, "blocks": [
            {"kind": "text", "seg": "seg_chart"},
            {"kind": "fig", "asset": chart, "caption": "Bar chart (original figure)"}]})
    elif kind == 1:
        pages.append({"src": i + 1, "blocks": [
            {"kind": "text", "seg": "seg_table_pre"},
            {"kind": "fig", "asset": "table", "caption": "Table (original grid)"},
            {"kind": "text", "seg": "seg_table_post"}]})
    elif kind == 2:
        pages.append({"src": i + 1, "blocks": [{"kind": "text", "seg": "seg_p3"}]})
    elif kind == 3:
        pages.append({"src": i + 1, "blocks": [
            {"kind": "fig", "asset": "photo", "caption": "Keyboard photo (original)"},
            {"kind": "text", "seg": "seg_p4"}]})
    else:
        pages.append({"src": i + 1, "blocks": [
            {"kind": "fig", "asset": "photo", "caption": "Keyboard photo (original)"},
            {"kind": "text", "seg": "seg_p5"}]})
with open(os.path.join(WORK, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump({"pages": pages}, f, indent=1)
print("manifest: 30 pages,", sum(len(p["blocks"]) for p in pages), "blocks")
print("OK extract")
