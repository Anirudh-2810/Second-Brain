"""
HandwriteAI - feature extraction (CPU-only, offline).
Covers: deskew, binarize, line extraction, slant, thickness, baseline, ligatures.
All functions work without torch so the Gradio UI runs before any training.
"""
from __future__ import annotations
import os
import math
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
import numpy as np
from PIL import Image

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

TARGET_GLYPH_H = 48


def load_gray(path_or_image) -> np.ndarray:
    if isinstance(path_or_image, np.ndarray):
        arr = path_or_image
        if arr.ndim == 3:
            if HAS_CV2:
                return cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
            return np.mean(arr, axis=2).astype(np.uint8)
        return arr
    img = Image.open(path_or_image).convert("L")
    return np.array(img)


def pdf_to_images(pdf_path: str, dpi: int = 200) -> List[Image.Image]:
    """Convert PDF pages to PIL images. Uses PyMuPDF if available, else raises."""
    try:
        import fitz  # PyMuPDF
    except ImportError as e:
        raise RuntimeError("PyMuPDF not installed: pip install PyMuPDF") from e
    doc = fitz.open(pdf_path)
    out = []
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        out.append(img.convert("L"))
    return out


def load_sample_images(paths: List[str]) -> List[np.ndarray]:
    images: List[np.ndarray] = []
    for p in paths:
        if p.lower().endswith(".pdf"):
            for pil_img in pdf_to_images(p):
                images.append(np.array(pil_img))
        else:
            images.append(load_gray(p))
    return images


def binarize(gray: np.ndarray) -> np.ndarray:
    if HAS_CV2:
        _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # ensure ink = 255, paper = 0 for downstream? keep paper=255 convention
        return bw
    # fallback: simple mean threshold
    thr = float(np.mean(gray))
    return np.where(gray < thr, 0, 255).astype(np.uint8)


def deskew(gray: np.ndarray) -> Tuple[np.ndarray, float]:
    """Estimate skew via minAreaRect on ink pixels, rotate upright. Returns (fixed, angle)."""
    bw = binarize(gray)
    ink = (bw < 128).astype(np.uint8) * 255
    if not HAS_CV2:
        return gray, 0.0
    coords = np.column_stack(np.where(ink > 0))
    if len(coords) < 100:
        return gray, 0.0
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = gray.shape[:2]
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    fixed = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return fixed, float(angle)


def normalize_height(gray: np.ndarray, target_h: int = TARGET_GLYPH_H) -> np.ndarray:
    h, w = gray.shape[:2]
    if h == target_h:
        return gray
    scale = target_h / float(h)
    new_w = max(1, int(w * scale))
    if HAS_CV2:
        return cv2.resize(gray, (new_w, target_h), interpolation=cv2.INTER_AREA)
    img = Image.fromarray(gray).resize((new_w, target_h), Image.BILINEAR)
    return np.array(img)


def estimate_slant(gray: np.ndarray) -> float:
    """
    Slant in degrees, positive = leaning right (like italic /).
    Method: Sobel vertical edges -> Hough lines -> median deviation from vertical.
    Fallback to image moments if no lines found.
    """
    bw = binarize(gray)
    if not HAS_CV2:
        return 0.0
    edges = cv2.Canny(bw, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=120,
                            minLineLength=50, maxLineGap=10)
    angles = []
    if lines is not None:
        for x1, y1, x2, y2 in np.reshape(lines, (-1, 4)):
            dx, dy = (x2 - x1), (y2 - y1)
            if abs(dy) < 8:
                continue
            # angle from vertical
            ang = math.degrees(math.atan2(dx, -dy)) if dy != 0 else 0.0
            if -45 < ang < 45:
                angles.append(ang)
    if len(angles) >= 20:
        return float(np.median(angles))
    # fallback: moments of ink (clamped: near-vertical hands measure noisy)
    ink = (bw < 128).astype(np.uint8)
    m = cv2.moments(ink)
    if m["mu02"] is None or abs(m["mu02"]) < 1e-6:
        return 0.0
    skew = m["mu11"] / m["mu02"]
    return float(max(-15, min(15, math.degrees(math.atan(skew)))))


def estimate_thickness(gray: np.ndarray) -> float:
    """Median stroke width in px via distance transform on ink mask."""
    bw = binarize(gray)
    ink = (bw < 128).astype(np.uint8) * 255
    if not HAS_CV2:
        # fallback: fraction of ink pixels
        return float(np.mean(bw < 128) * 10.0)
    dist = cv2.distanceTransform(ink, cv2.DIST_L2, 3)
    vals = dist[ink > 0]
    if len(vals) == 0:
        return 0.0
    # distance = half-width, so x2
    return float(np.median(vals) * 2.0)


def extract_lines(gray: np.ndarray, min_gap: int = 8) -> List[np.ndarray]:
    """Split a page into line strips via horizontal projection."""
    bw = binarize(gray)
    ink_rows = np.mean(bw < 128, axis=1)  # ink density per row
    lines, in_line, start = [], False, 0
    for i, v in enumerate(ink_rows):
        if not in_line and v > 0.01:
            in_line, start = True, i
        elif in_line and v <= 0.01:
            if i - start > 10:
                # require small gap to close
                gap = 0
                j = i
                while j < len(ink_rows) and ink_rows[j] <= 0.01 and gap < min_gap:
                    gap += 1
                    j += 1
                if gap >= min_gap:
                    lines.append(gray[start:i, :])
                    in_line = False
    if in_line:
        lines.append(gray[start:, :])
    return lines if lines else [gray]


def estimate_baseline(gray: np.ndarray) -> Dict:
    """
    Fit a 2nd-degree curve to line bottoms across columns.
    Returns {coeffs:[a,b,c], sag_px, visualization strip}.
    """
    lines = extract_lines(gray)
    bottoms = []
    for ln in lines:
        bw = binarize(ln)
        # bottom ink pixel per column (sampled every 8px for speed)
        h, w = bw.shape
        for x in range(0, w, 8):
            col = np.where(bw[:, x] < 128)[0]
            if len(col):
                bottoms.append((x, int(col.max())))
    if len(bottoms) < 20:
        return {"coeffs": [0.0, 0.0, 0.0], "sag_px": 0.0, "n_lines": len(lines)}
    xs = np.array([b[0] for b in bottoms], dtype=float)
    ys = np.array([b[1] for b in bottoms], dtype=float)
    try:
        coeffs = np.polyfit(xs, ys, 2).tolist()
        sag = float(np.max(ys) - np.min(ys))
    except Exception:
        coeffs, sag = [0.0, 0.0, 0.0], 0.0
    return {"coeffs": [float(c) for c in coeffs], "sag_px": sag, "n_lines": len(lines)}


def ligature_stats(gray: np.ndarray) -> Dict:
    """Heuristic: wide connected components = likely ligatures/joined letters."""
    bw = binarize(gray)
    if not HAS_CV2:
        return {"ligature_pct": 0.0, "n_components": 0}
    ink = (bw < 128).astype(np.uint8) * 255
    n, _, stats, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
    widths, heights = [], []
    for i in range(1, n):
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        if area < 30 or h < 8:
            continue
        widths.append(w)
        heights.append(h)
    if not widths:
        return {"ligature_pct": 0.0, "n_components": 0,
                "median_glyph_w": 0.0, "median_glyph_h": 0.0}
    med = float(np.median(widths))
    med_h = float(np.median(heights))
    wide = sum(1 for w in widths if w > med * 1.8)
    pct = 100.0 * wide / max(1, len(widths))
    return {"ligature_pct": float(pct), "n_components": int(len(widths)),
            "median_glyph_w": med, "median_glyph_h": med_h}


@dataclass
class StyleFeatures:
    slant_deg: float = 0.0
    thickness_px: float = 3.0
    baseline_sag_px: float = 0.0
    baseline_coeffs: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    ligature_pct: float = 0.0
    n_lines: int = 0
    n_components: int = 0
    deskew_deg: float = 0.0
    glyph_h_median: float = 0.0  # DPI-anchored size ref: thickness TASK is
    glyph_w_median: float = 0.0  # compared as thickness/height RATIO, never raw px

    def to_dict(self) -> Dict:
        d = asdict(self)
        d["baseline_coeffs"] = list(self.baseline_coeffs)
        return d

    @classmethod
    def from_dict(cls, d: Dict) -> "StyleFeatures":
        bc = tuple(d.get("baseline_coeffs", (0.0, 0.0, 0.0)))
        return cls(slant_deg=d.get("slant_deg", 0.0),
                   thickness_px=d.get("thickness_px", 3.0),
                   baseline_sag_px=d.get("baseline_sag_px", 0.0),
                   baseline_coeffs=bc,  # type: ignore
                   ligature_pct=d.get("ligature_pct", 0.0),
                   n_lines=d.get("n_lines", 0),
                   n_components=d.get("n_components", 0),
                   deskew_deg=d.get("deskew_deg", 0.0),
                   glyph_h_median=d.get("glyph_h_median", 0.0),
                   glyph_w_median=d.get("glyph_w_median", 0.0))


def analyze_pages(images: List[np.ndarray]) -> StyleFeatures:
    slants, thick, ligs, nlines, ncomp, sags, skews = [], [], [], 0, 0, [], []
    heights, widths = [], []
    base_coeffs = []
    for img in images:
        fixed, skew = deskew(img)
        skews.append(skew)
        norm = normalize_height(fixed)
        slants.append(estimate_slant(fixed))
        thick.append(estimate_thickness(fixed))
        b = estimate_baseline(fixed)
        sags.append(b["sag_px"])
        nlines += b["n_lines"]
        base_coeffs.append(b["coeffs"])
        lg = ligature_stats(fixed)
        ligs.append(lg["ligature_pct"])
        ncomp += lg["n_components"]
        if lg.get("median_glyph_h"):
            heights.append(lg["median_glyph_h"])
        if lg.get("median_glyph_w"):
            widths.append(lg["median_glyph_w"])
    bc = np.mean(base_coeffs, axis=0).tolist() if base_coeffs else [0.0, 0.0, 0.0]
    return StyleFeatures(
        slant_deg=float(np.median(slants)) if slants else 0.0,
        thickness_px=float(np.median(thick)) if thick else 3.0,
        baseline_sag_px=float(np.median(sags)) if sags else 0.0,
        baseline_coeffs=(float(bc[0]), float(bc[1]), float(bc[2])),
        ligature_pct=float(np.median(ligs)) if ligs else 0.0,
        n_lines=int(nlines),
        n_components=int(ncomp),
        deskew_deg=float(np.median(skews)) if skews else 0.0,
        glyph_h_median=float(np.median(heights)) if heights else 0.0,
        glyph_w_median=float(np.median(widths)) if widths else 0.0,
    )
