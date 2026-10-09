"""
HandwriteAI - ENROLLMENT: one sheet that teaches the system YOUR letters.

Problem it solves: shape-bucket retrieval pastes random lookalikes per position
('T' slot gets any tall crop), so output looks handwritten but reads as gibberish.
Enrollment fixes identity: you write each character once in a labeled box, and
every future render pastes the CORRECT letter in your ink.

Workflow:
  1. python enroll.py sheet --out enrollment-sheet.png   (print it, or copy to tablet)
  2. Write each character inside its box, naturally, black/blue pen. Stay inside.
     Empty boxes are fine (those chars fall back to font rendering).
  3. Photograph/scan the sheet (fill the frame, decent light, no shadows).
  4. python enroll.py build photo.jpg --out styles/mine.labeled
  5. python convert.py --style styles/user_001.style --glyphs styles/mine.labeled ...
     (UI: Generate tab -> mode "labeled")

Sheet geometry (fractions of page, A4 portrait @300dpi = 2480x3508):
  - 4 filled-square fiducials near corners -> perspective correction of photos
  - 8 cols x 10 rows = 80 boxes, 77 labeled + 3 spare
"""
from __future__ import annotations
import os, json, string, argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SHEET_W, SHEET_H = 2480, 3508
FID_FRAC = 0.035   # fiducial square size (fraction of width)
FID_INSET = 0.045  # fiducial center inset from edges
CX0, CX1, CY0, CY1 = 0.11, 0.89, 0.10, 0.93
COLS, ROWS = 8, 10

CHARS: list = (list(string.ascii_lowercase) + list(string.ascii_uppercase)
               + list(string.digits)
               + list(".,!?;:'\"()-+=/&"))
while len(CHARS) < COLS * ROWS:
    CHARS.append("")  # spare blanks


def _font(size: int):
    for name in ("arial.ttf", "DejaVuSans.ttf"):
        for d in ("", "C:\\Windows\\Fonts\\", "/usr/share/fonts/truetype/dejavu/"):
            try:
                return ImageFont.truetype(os.path.join(d, name) if d else name, size)
            except Exception:
                continue
    return ImageFont.load_default()


def cell_rect(ci: int, W: int = SHEET_W, H: int = SHEET_H):
    r, c = divmod(ci, COLS)
    cw = (CX1 - CX0) / COLS
    chh = (CY1 - CY0) / ROWS
    return (int((CX0 + c * cw) * W), int((CY0 + r * chh) * H),
            int((CX0 + (c + 1) * cw) * W), int((CY0 + (r + 1) * chh) * H))


def fiducial_centers(W: int = SHEET_W, H: int = SHEET_H):
    fx = [FID_INSET * W, (1 - FID_INSET) * W]
    fy = [FID_INSET * H, (1 - FID_INSET) * H]
    return [(fx[0], fy[0]), (fx[1], fy[0]), (fx[1], fy[1]), (fx[0], fy[1])]


def make_sheet(out_png: str, out_pdf: str = ""):
    img = Image.new("RGB", (SHEET_W, SHEET_H), "white")
    d = ImageDraw.Draw(img)
    # fiducials: filled black squares
    fs = int(FID_FRAC * SHEET_W)
    for (fx, fy) in fiducial_centers():
        d.rectangle([fx - fs // 2, fy - fs // 2, fx + fs // 2, fy + fs // 2],
                    fill="black")
    # header
    hf = _font(64)
    d.text((int(0.11 * SHEET_W), int(0.035 * SHEET_H)),
           "HandwriteAI enrollment — write EACH character in its box, stay inside.",
           font=hf, fill=(30, 30, 30))
    sf = _font(40)
    d.text((int(0.11 * SHEET_W), int(0.058 * SHEET_H)),
           "Black/blue pen, natural size. Empty boxes fall back to font rendering.",
           font=sf, fill=(90, 90, 90))
    # boxes
    lf = _font(44)
    for ci, ch in enumerate(CHARS):
        x0, y0, x1, y1 = cell_rect(ci)
        d.rectangle([x0, y0, x1, y1], outline=(120, 120, 120), width=3)
        # faint baseline guide at 68%
        by = int(y0 + (y1 - y0) * 0.68)
        d.line([(x0 + 8, by), (x1 - 8, by)], fill=(200, 205, 220), width=2)
        if ch:
            d.text((x0 + 10, y0 + 6), ch if ch != " " else "sp",
                   font=lf, fill=(150, 150, 150))
        else:
            d.text((x0 + 10, y0 + 6), "spare", font=lf, fill=(190, 190, 190))
    img.save(out_png, dpi=(300, 300))
    if out_pdf:
        img.save(out_pdf, "PDF", resolution=300.0)
    print(f"sheet -> {out_png}" + (f" + {out_pdf}" if out_pdf else ""))
    return out_png


def _find_fiducials(gray: np.ndarray):
    import cv2
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    _, bw = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ink = (bw < 128).astype(np.uint8) * 255
    cnts, _ = cv2.findContours(ink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    h, w = gray.shape[:2]
    cands = []
    for c in cnts:
        area = cv2.contourArea(c)
        if not (0.0004 * w * h < area < 0.01 * w * h):
            continue
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) != 4:
            continue
        x, y, cw, chh = cv2.boundingRect(approx)
        if min(cw, chh) / max(cw, chh) < 0.75:
            continue
        M = cv2.moments(c)
        if M["m00"] == 0:
            continue
        cands.append((M["m10"] / M["m00"], M["m01"] / M["m00"]))
    if len(cands) < 4:
        raise RuntimeError(f"found {len(cands)} fiducials, need 4 "
                           f"(retake photo: fill frame, flat, good light)")
    # nearest to each corner
    corners = [(0, 0), (w, 0), (w, h), (0, h)]
    used, ordered = set(), []
    for corner in corners:
        best, bi = None, -1
        for i, (px, py) in enumerate(cands):
            if i in used:
                continue
            dist = (px - corner[0]) ** 2 + (py - corner[1]) ** 2
            if best is None or dist < best:
                best, bi = dist, i
        used.add(bi)
        ordered.append(cands[bi])
    return ordered  # TL, TR, BR, BL


def warp_sheet(photo_path: str) -> np.ndarray:
    import cv2
    img = np.array(Image.open(photo_path).convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    src = np.float32(_find_fiducials(gray))
    dst = np.float32([(x * SHEET_W, y * SHEET_H) for (x, y) in
                      [(FID_INSET, FID_INSET), (1 - FID_INSET, FID_INSET),
                       (1 - FID_INSET, 1 - FID_INSET), (FID_INSET, 1 - FID_INSET)]])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (SHEET_W, SHEET_H))
    return cv2.cvtColor(warped, cv2.COLOR_RGB2GRAY)


def build_labeled(photo_paths: list, out_dir: str) -> dict:
    os.makedirs(out_dir, exist_ok=True)
    chars: dict = {}
    missing = []
    for photo in photo_paths:
        gray = warp_sheet(photo)
        for ci, ch in enumerate(CHARS):
            if not ch:
                continue
            x0, y0, x1, y1 = cell_rect(ci)
            # inset: ignore box borders + corner label zone
            ix0, iy0 = int(x0 + (x1 - x0) * 0.10), int(y0 + (y1 - y0) * 0.16)
            ix1, iy1 = int(x1 - (x1 - x0) * 0.06), int(y1 - (y1 - y0) * 0.06)
            crop = gray[iy0:iy1, ix0:ix1]
            if crop.size == 0:
                continue
            thr = min(200.0, float(crop.mean()) - 18.0)
            ink = crop < thr
            frac = float(ink.mean())
            if not (0.004 <= frac <= 0.45):
                continue  # empty or scribbled-out box
            ys, xs = np.where(ink)
            py0, py1, px0, px1 = ys.min(), ys.max(), xs.min(), xs.max()
            pad = 10
            crop2 = crop[max(0, py0 - pad):py1 + pad, max(0, px0 - pad):px1 + pad]
            safe = ch.replace("/", "slash").replace("\\", "back").replace(
                '"', "dquot").replace("'", "squot").replace(":", "colon").replace(
                "?", "qmark").replace("*", "star").replace("|", "pipe")
            fn = f"{ci:02d}_{safe}_v{len(chars.get(ch, []))}.png"
            Image.fromarray(crop2).save(os.path.join(out_dir, fn))
            chars.setdefault(ch, []).append(fn)
    for ci, ch in enumerate(CHARS):
        if ch and ch not in chars:
            missing.append(ch)
    manifest = {"version": "0.2-labeled", "chars": chars, "missing": missing,
                "n_pages": len(photo_paths),
                "n_glyphs": sum(len(v) for v in chars.values())}
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"labeled library: {manifest['n_glyphs']} glyphs, "
          f"{len(chars)} chars covered, {len(missing)} missing -> {out_dir}")
    if missing:
        print("  missing (font fallback):", "".join(missing))
    return manifest


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sheet")
    s.add_argument("--out", default="enrollment-sheet.png")
    s.add_argument("--pdf", default="enrollment-sheet.pdf")
    b = sub.add_parser("build")
    b.add_argument("photos", nargs="+")
    b.add_argument("--out", default="styles/mine.labeled")
    args = ap.parse_args()
    if args.cmd == "sheet":
        make_sheet(args.out, args.pdf)
    else:
        out = args.out if args.out.endswith(".labeled") else args.out
        build_labeled(args.photos, out)


if __name__ == "__main__":
    main()
