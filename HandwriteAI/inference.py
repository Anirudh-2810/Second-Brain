"""
HandwriteAI - inference: text -> handwriting image.
Paths (best first):
  1. GLYPH RETRIEVAL (render_with_glyphs): pastes YOUR real ink crops from
     styles/<user>.glyphs/ — lowest feature error, real pen texture.
  2. FONT RENDERER v2 (render_text_image): per-glyph jitter + ink variation.
Exports PNG / PDF / SVG into outputs/.
Accuracy: eval_style_error() reports feature MSE vs the .style profile.
"""
from __future__ import annotations
import os, json, math, datetime
from typing import Dict, Tuple, List
import numpy as np
from PIL import Image, ImageDraw, ImageFont

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


def load_style(style_path: str) -> Dict:
    if style_path and os.path.exists(style_path):
        with open(style_path, encoding="utf-8") as f:
            return json.load(f)
    return {"z": [0.0]*128, "features": {
        "slant_deg": 8.0, "thickness_px": 3.0, "baseline_sag_px": 2.0,
        "ligature_pct": 25.0, "n_lines": 0}}


def _font(size: int):
    # Prefer real handwriting fonts on Windows, then clean fallbacks.
    candidates = (
        "segoepr.ttf",    # Segoe Print
        "segoeprb.ttf",   # Segoe Print Bold
        "bradhitc.ttf",   # Bradley Hand ITC
        "inkfree.ttf",    # Ink Free
        "mvboli.ttf",     # MV Boli
        "segoesc.ttf",    # Segoe Script
        "segoescb.ttf",
        "comic.ttf",      # Comic Sans
        "comicbd.ttf",
        "arial.ttf", "DejaVuSans.ttf",
    )
    import os as _os
    search_dirs = ("", "C:\\Windows\\Fonts\\", "/usr/share/fonts/truetype/dejavu/")
    for d in search_dirs:
        for name in candidates:
            try:
                return ImageFont.truetype(_os.path.join(d, name) if d else name, size)
            except Exception:
                continue
    return ImageFont.load_default()


def render_text_image(text: str, style: Dict, slant_adj: float = 0.0,
                      style_strength: float = 1.0, lined: bool = False,
                      width: int = 1600, font_size: int = 58,
                      seed: int = 7) -> Image.Image:
    """Natural-handwriting renderer v2: per-glyph jitter, ink variation, ligatures."""
    feats = style.get("features", {})
    base_slant = float(feats.get("slant_deg", 2.0)) + float(slant_adj)
    slant = max(-15, min(15, base_slant * float(style_strength)))
    thick_raw = float(feats.get("thickness_px", 2.0))
    thick = max(1, min(4, thick_raw))
    raw_sag = float(feats.get("baseline_sag_px", 3.0))
    sag = min(raw_sag, 7.0) * float(style_strength)
    lig = float(feats.get("ligature_pct", 25.0))
    lig_prob = max(0.0, min(0.85, lig / 100.0)) * float(style_strength)

    font = _font(font_size)
    line_h = int(font_size * 1.9)  # dense but non-colliding page rhythm
    # wrap (measure with base font)
    words, lines, cur = text.split(), [], ""
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    try:
        meas_font = font
    except Exception:
        meas_font = font
    for w in words:
        trial = (cur + " " + w).strip()
        try:
            bbox = tmp.textbbox((0, 0), trial, font=meas_font)
            tw = bbox[2]
        except Exception:
            tw = len(trial) * font_size * 0.55
        if tw > width - 160:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    if not lines:
        lines = [""]

    H = line_h * len(lines) + 140
    # warm paper, not pure white
    img = Image.new("RGB", (width, H), (253, 252, 247))
    d = ImageDraw.Draw(img)

    if lined:
        for i in range(len(lines)):
            y = 70 + (i + 1) * line_h - 22
            d.line([(50, y), (width - 50, y)], fill=(180, 195, 225), width=2)

    rng = np.random.default_rng(seed)
    base_shear = math.tan(math.radians(slant))
    # slow drift of baseline across the page (like a real hand tiring)
    page_drift = rng.normal(0, 4)

    for li, line in enumerate(lines):
        line_seed = int(rng.integers(0, 10_000))
        lrng = np.random.default_rng(seed * 1000 + line_seed + li * 77)
        yb = 70 + li * line_h + lrng.normal(0, 2.0) + page_drift * (li / max(1, len(lines)))
        cx = 60 + lrng.normal(0, 6.0)  # line-start never exactly aligned
        # per-line slant drift
        line_shear = base_shear + lrng.normal(0, 0.03)
        prev_exit = None  # (x, y) of previous char exit for ligature stroke
        for ci, ch in enumerate(line):
            if ch == " ":
                # word gaps swing wildly in real hands: sometimes airy, sometimes
                # words nearly collide. Uniform gaps are a top AI tell.
                # (KeptSacred: never merged — density lives inside words.)
                cx += font_size * max(0.25, float(lrng.normal(0.45, 0.18)))
                prev_exit = None
                continue
            word_start = prev_exit is None
            word_end = (ci == len(line) - 1) or (line[ci + 1] == " ")
            if word_start:
                word_pos = 0
                word_drift = float(lrng.normal(0, 3.5))  # whole word rides up/down
            else:
                word_pos += 1
            # --- per-glyph jitter, BUCKETS DENSITY: collide like real fast ink ---
            gsize = int(font_size * (1.0 + lrng.normal(0, 0.14)))  # size swings ±14%
            gsize = max(28, min(90, gsize))
            try:
                gfont = _font(gsize)
            except Exception:
                gfont = font
            rot = float(lrng.normal(0, 6.0))  # wild hands tilt ±6deg
            wob = (math.sin((cx / 110.0) + li * 1.7) * (sag * 0.5)
                   + lrng.normal(0, 3.5))
            gy = yb + wob + word_drift
            kern = float(lrng.normal(-0.2, 4.0))  # collisions welcome in-word
            # glyph cell, BASELINE-ANCHORED (never bbox-sized).
            # Root-cause fix: sizing the cell from the ink bbox ignored the
            # glyph's top bearing, so every lowercase body overflowed the cell
            # and PIL clipped it -> only ascender-zone scraps pasted (the
            # dot-soup). Cell now spans full ascent+descent; text is placed
            # by baseline anchor, which cannot overflow by construction.
            try:
                bb = ld_tmp_bbox(ch, gfont)
                gw = max(10, bb[0])
            except Exception:
                gw = int(gsize * 0.6)
            try:
                asc, desc = gfont.getmetrics()
            except Exception:
                asc, desc = int(gsize * 0.8), int(gsize * 0.25)
            pad = 16
            cell = Image.new("RGB", (gw + 2 * pad, asc + desc + 2 * pad),
                             (255, 255, 255))
            cd = ImageDraw.Draw(cell)
            # ink colour: ballpoint varies stroke to stroke, sometimes running dry
            ink_r = int(25 + lrng.normal(0, 12))
            ink_g = int(32 + lrng.normal(0, 12))
            ink_b = int(75 + lrng.normal(0, 18))
            ink_r, ink_g, ink_b = (max(10, min(85, ink_r)),
                                   max(15, min(90, ink_g)),
                                   max(45, min(135, ink_b)))
            # pen pressure for THIS glyph: hard presses and feather kisses.
            # Plus word-fade: pens run dry along a word, re-dip at the next start.
            pressure = float(lrng.uniform(0.60, 1.10))
            pressure *= max(0.70, 1.12 - 0.05 * word_pos)
            baseline_y = pad + asc + int(lrng.normal(0, 1.2))
            try:
                cd.text((pad, baseline_y), ch, font=gfont,
                        fill=(ink_r, ink_g, ink_b), anchor="ls")
            except TypeError:
                cd.text((pad, baseline_y - asc), ch, font=gfont,
                        fill=(ink_r, ink_g, ink_b))
            # per-glyph shear + rotation on OPAQUE cell (white fill, stays connected).
            # Each letter gets its OWN slant wobble on top of the line slant:
            # fast hands never hold one angle through a word.
            glyph_shear = line_shear + lrng.normal(0, 0.05)
            if abs(glyph_shear) > 0.005:
                try:
                    cell = cell.transform(
                        cell.size, Image.AFFINE,
                        (1, glyph_shear, 0, 0, 1, 0),
                        resample=Image.BICUBIC, fillcolor=(255, 255, 255))
                except TypeError:
                    cell = cell.transform(
                        cell.size, Image.AFFINE,
                        (1, glyph_shear, 0, 0, 1, 0),
                        resample=Image.BICUBIC)
            if abs(rot) > 0.2:
                try:
                    cell = cell.rotate(rot, resample=Image.BICUBIC, expand=True,
                                        fillcolor=(255, 255, 255))
                except TypeError:
                    cell = cell.rotate(rot, resample=Image.BICUBIC, expand=True)
            # CURSIVE DRIVE: join letters INSIDE words hard, respect spaces.
            # The scribble looked human because everything flowed; it died
            # because joins crossed word gaps. Rule: flow within words (fast,
            # tight, flicked), clean breaks at spaces (readability lives here).
            drew_lig = False
            join_p = min(0.90, lig_prob * 3.2)
            if not word_start and lrng.random() < join_p and ch.isalpha():
                drew_lig = True
                co = ImageDraw.Draw(cell)
                mid_y = baseline_y - max(6, asc // 3) + int(lrng.normal(0, 3))
                co.line([(0, mid_y), (12, mid_y - 5), (24, mid_y + 1)],
                        fill=(ink_r, ink_g, ink_b), width=3, joint="curve")
            # entry stroke: pen swoops in at word starts (30% of words).
            # Kept INSIDE the cell: reaching into the gap fuses words.
            if word_start and lrng.random() < 0.30 and ch.isalpha():
                co = ImageDraw.Draw(cell)
                ey = baseline_y - max(6, asc // 3) + int(lrng.normal(0, 3))
                co.line([(6, ey + 5), (12, ey + 1), (18, ey)],
                        fill=(ink_r, ink_g, ink_b), width=3, joint="curve")
            # vertical swell: tall-narrow vs short-wide letters. Real hands vary
            # height 2x inside a word; uniform cap-height is a top AI tell.
            # Applied to the opaque cell (connectivity-safe), baseline re-anchored.
            yscale = float(lrng.uniform(0.85, 1.20))
            if abs(yscale - 1.0) > 0.02:
                nw2 = cell.size[0]
                nh2 = max(8, int(cell.size[1] * yscale))
                cell = cell.resize((nw2, nh2), Image.LANCZOS)
                baseline_y = int(baseline_y * yscale)
            # mask from DARKNESS after all warps (strokes stay connected)
            mask = cell.convert("L").point(lambda v: 255 if v < 200 else 0)
            # HUMAN INK: textured fill with dry-pen skips, built per glyph.
            # - per-pixel tooth: ink density varies along the stroke
            # - dry-pen speckle: paper shows through INSIDE wide strokes only
            #   (edges untouched, so strokes can never disconnect -> the
            #   shabbiness of real ballpoint without the dot-soup failure)
            # baseline lands a touch below gy so bodies ride the line like real writing
            paste_y = int(gy + 8 - baseline_y)
            try:
                import cv2 as _cv2t
                m_arr = (np.array(mask) > 0)
                chh, cww = m_arr.shape
                tex = 1.0 + lrng.normal(0, 0.09, (chh, cww))
                fill = np.empty((chh, cww, 3), dtype=np.float32)
                fill[..., 0] = np.clip(ink_r * pressure * tex, 0, 255)
                fill[..., 1] = np.clip(ink_g * pressure * tex, 0, 255)
                fill[..., 2] = np.clip(ink_b * pressure * tex, 0, 255)
                dist = _cv2t.distanceTransform(
                    (m_arr * 255).astype(np.uint8), _cv2t.DIST_L2, 3)
                # dry pen, pushed: skips pepper wide strokes, edges sacred
                skips = (lrng.random((chh, cww)) < 0.08) & (dist > 1.5) & m_arr
                fill[skips] = (253, 252, 247)  # paper grinning through dry strokes
                # edge wobble: nibble/extend the stroke boundary by 1px in patches.
                # Core (dist>=2) never touched -> connectivity cannot break.
                edge_out = (_cv2t.dilate((m_arr * 255).astype(np.uint8),
                                         np.ones((3, 3), np.uint8)) > 0) & (~m_arr)
                sprout = (lrng.random((chh, cww)) < 0.22) & edge_out
                edge_in = m_arr & (dist <= 1.0)
                nibble = (lrng.random((chh, cww)) < 0.18) & edge_in
                wob_mask = (m_arr & (~nibble)) | sprout
                wob_pil = Image.fromarray((wob_mask * 255).astype(np.uint8))
                fill[~wob_mask & m_arr] = (253, 252, 247)
                fill[sprout] = np.clip(
                    np.array([ink_r, ink_g, ink_b], np.float32) * pressure * 0.9,
                    0, 255)
                img.paste(Image.fromarray(np.clip(fill, 0, 255).astype(np.uint8)),
                          (int(cx), paste_y), wob_pil)
            except Exception:
                img.paste(Image.new("RGB", cell.size, (ink_r, ink_g, ink_b)),
                          (int(cx), paste_y), mask)
            if lrng.random() < 0.18:  # heavier pens re-touch strokes more often
                ox, oy = int(lrng.normal(0, 1.4)), int(lrng.normal(0, 1.4))
                soft = mask.point(lambda v: int(v * 0.35))
                img.paste(Image.new("RGB", cell.size, (ink_r, ink_g, ink_b)),
                          (int(cx) + ox, paste_y + oy), soft)
            # advance by true glyph width + kerning (padding excluded).
            # Joined letters ride tight so joins touch; unjoined keep air.
            adv = gw + kern
            glyph_mid = int(paste_y + baseline_y - max(6, asc // 3))
            # post-paste weld: sweep reaches BACK into the previous glyph and
            # throws forward into this one, arched like a real pen join. This
            # is what fuses print letters into flowing words (in-cell stubs
            # alone never cross the seam).
            if drew_lig and prev_exit is not None:
                ex0, ey0 = prev_exit
                ex1 = int(cx + 14)
                ImageDraw.Draw(img).line(
                    [(ex0 - 6, ey0), ((ex0 + ex1) // 2, (ey0 + glyph_mid) // 2 - 6),
                     (ex1 + 10, glyph_mid)],
                    fill=(ink_r, ink_g, ink_b), width=4, joint="curve")
            prev_exit = (int(cx + adv * 0.95), glyph_mid)
            # BUCKETS DENSITY: deep overlap inside words, word gaps stay sacred.
            pull = 0.52 if drew_lig else 0.78
            cx += max(8, adv * pull)
            base_img_y = paste_y + baseline_y
            # exit flick: pen lifts off with a tail at word ends (55% of words).
            # Kept SHORT: long tails cross word gaps and fuse words (soup).
            if word_end and lrng.random() < 0.55 and ch.isalpha():
                fx0 = int(cx - adv * 0.15)
                fy0 = int(base_img_y - max(6, asc // 3))
                flen = int(lrng.uniform(6, 12))
                rise = int(lrng.uniform(3, 9)) * (1 if lrng.random() < 0.7 else -1)
                ImageDraw.Draw(img).line(
                    [(fx0, fy0), (fx0 + flen // 2, fy0 - rise // 2),
                     (fx0 + flen, fy0 - rise)],
                    fill=(ink_r, ink_g, ink_b), width=3, joint="curve")
            # touchdown blob: pen lands heavier at some word starts (15%)
            if word_start and lrng.random() < 0.15 and ch.isalpha():
                bx0 = int(cx + 3)
                by0 = int(base_img_y - max(6, asc // 3))
                br = int(lrng.uniform(2, 3.5))
                ImageDraw.Draw(img).ellipse(
                    [bx0 - br, by0 - br, bx0 + br, by0 + br],
                    fill=(max(8, ink_r - 8), max(10, ink_g - 8),
                          max(30, ink_b - 10)))

    # NOTE (scribble incident): NO erosion and NO post-hoc bridge passes here.
    # Erosion shattered glyphs into dot-soup while reporting perfect thickness;
    # bridge loops joined everything into wavy scribble while reporting perfect
    # ligatures. Both optimized px metrics that are invalid across scan-vs-render
    # DPIs. Closeness now comes ONLY from the glyph-retrieval path (real ink),
    # never from mutilating font output. This function must stay readable.

    # --- paper + ink finishing: subtle grain, no plastic smoothness ---
    arr = np.array(img).astype(np.float32)
    grain = rng.normal(0, 2.2, arr.shape[:2])[..., None]
    arr = np.clip(arr + grain, 0, 255)
    # faint ink bleed: darken near-ink pixels a touch (cheap morphological feel)
    gray = arr.mean(axis=2)
    near_ink = (gray < 210).astype(np.float32)[..., None]
    arr = arr - near_ink * rng.uniform(2, 5)
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    return img


def ld_tmp_bbox(ch: str, fnt) -> tuple:
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    try:
        b = tmp.textbbox((0, 0), ch, font=fnt)
        return (b[2] - b[0] + 1, b[3] - b[1] + 1)
    except Exception:
        return (30, 40)


def render_with_glyphs(text: str, style: Dict, lib_dir: str,
                       lined: bool = False, width: int = 1600,
                       target_h: int = 56, seed: int = 7,
                       style_strength: float = 1.0) -> Image.Image:
    """Retrieval renderer: paste user's REAL glyph crops. Lowest error path."""
    from glyphs import load_library, pick_glyph, CHAR_BUCKET
    feats = style.get("features", {})
    slant = max(-15, min(15, float(feats.get("slant_deg", 2.0)) * float(style_strength)))
    sag = min(float(feats.get("baseline_sag_px", 3.0)), 7.0) * float(style_strength)
    shear = math.tan(math.radians(slant))
    manifest, cache = load_library(lib_dir)
    if manifest is None or sum(len(v) for v in cache.values()) < 50:
        raise RuntimeError(f"glyph library missing/sparse at {lib_dir} "
                           f"(need 50+, have {sum(len(v) for v in cache.values()) if cache else 0}). "
                           f"Re-run training with sample pages, or use font mode.")
    rng = np.random.default_rng(seed)
    # scale real glyphs (scanned px) to target line height
    ref_h = float(manifest.get("height_mean", 30))
    scale = target_h / max(8.0, ref_h)
    ref_w = float(manifest.get("width_mean", 20) or 20) * scale
    line_h = int(target_h * 2.5)  # air between lines: ascenders must never
    # collide with the previous line's descenders (the cram failure)
    # LAYOUT (readability rules — the soup incident):
    # - user's own newlines are preserved (paragraphs), never invented
    # - wrap breaks at word boundaries only, words never split
    # - word gaps are WIDE and unconditional (merging words killed readability)
    paras = [p for p in text.split("\n")]
    lines: List[str] = []
    for para in paras:
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            est = len(trial) * ref_w
            if cur and est > width - 160:
                lines.append(cur)
                cur = w
            else:
                cur = trial
        if cur:
            lines.append(cur)
        lines.append("")  # paragraph break (collapsed below if trailing)
    while len(lines) > 1 and lines[-1] == "":
        lines.pop()
    if not lines:
        lines = [""]
    H = line_h * len(lines) + 140
    img = Image.new("RGB", (width, H), (253, 252, 247))
    d = ImageDraw.Draw(img)
    if lined:
        for i in range(len(lines)):
            y = 70 + (i + 1) * line_h - 22
            d.line([(50, y), (width - 50, y)], fill=(180, 195, 225), width=2)
    for li, line in enumerate(lines):
        if not line.strip():
            continue  # paragraph gap: vertical space, no ink
        lrng = np.random.default_rng(seed * 1000 + li * 77 + 5)
        yb = 70 + li * line_h + lrng.normal(0, 1.0)
        cx = 60 + lrng.normal(0, 4.0)
        prev_exit = None  # right-edge midpoint of previous crop (in-word only)
        for ci, ch in enumerate(line):
            if ch == " ":
                # WORD GAPS ARE SACRED: wide, always, no exceptions.
                # Narrow/merged word gaps were the readability killer.
                cx += max(target_h * 0.55, ref_w * 1.1 + lrng.normal(0, 4.0))
                prev_exit = None
                continue
            word_start = prev_exit is None
            word_end = (ci == len(line) - 1) or (line[ci + 1] == " ")
            # DENSE FLOW (reference look): most pairs join and overlap deep.
            # Letters are lookalikes, not true letters (user chose look first);
            # monsters/joins-across-spaces stay banned (slab + soup incidents).
            join_p = min(0.80, float(feats.get("ligature_pct", 25.0)) / 100.0 * 3.0)
            joining = (not word_start) and ch.isalpha() and lrng.random() < join_p
            bucket = CHAR_BUCKET.get(ch, "xheight")
            g = None
            # render guard: reject monster crops (word/line chunks) at pick
            # time; after 3 bad draws skip the character (slab incident).
            # Plus rhythm match: prefer crops near the library's typical
            # width so words don't lurch between giant and tiny glyphs.
            for _try in range(4):
                cand = pick_glyph(cache, bucket, lrng)
                if cand is None:
                    break
                chh, cww = cand.shape[:2]
                if cww * scale <= 4 * target_h and chh * scale <= 2.2 * target_h:
                    if _try < 2 and not (0.35 * ref_w <= cww * scale <= 2.2 * ref_w):
                        continue  # rhythm mismatch: draw again (2 chances)
                    g = cand
                    break
            if g is None:
                cx += target_h * 0.5
                continue
            gh, gw = g.shape[:2]
            # living size: ±6% per placement so repeats never march identical
            _sz = float(lrng.uniform(0.94, 1.06))
            nw, nh = max(6, int(gw * scale * _sz)), max(8, int(gh * scale * _sz))
            pil = Image.fromarray(g).resize((nw, nh), Image.LANCZOS)
            # writer's slant only (kept tiny: crops carry their own slant)
            if abs(shear) > 0.005:
                pil_rgba = pil.convert("RGBA")
                try:
                    pil_rgba = pil_rgba.transform(
                        pil_rgba.size, Image.AFFINE, (1, shear, 0, 0, 1, 0),
                        resample=Image.BICUBIC, fillcolor=(255, 255, 255, 0))
                except TypeError:
                    pil_rgba = pil_rgba.transform(
                        pil_rgba.size, Image.AFFINE, (1, shear, 0, 0, 1, 0),
                        resample=Image.BICUBIC)
                pil = pil_rgba.convert("L")
            else:
                pil = pil.convert("L") if not isinstance(pil, Image.Image) else pil
            if not isinstance(pil, Image.Image):
                pil = Image.fromarray(np.array(pil))
            # whisper of rotation: pens never land twice at the same angle
            _rot = float(lrng.normal(0, 1.5))
            if abs(_rot) > 0.4:
                try:
                    pil = pil.rotate(_rot, resample=Image.BICUBIC, expand=True,
                                     fillcolor=255)
                except TypeError:
                    pil = pil.rotate(_rot, resample=Image.BICUBIC, expand=True)
                nw, nh = pil.size
            wob = math.sin((cx / 110.0) + li * 1.7) * (sag * 0.4) + lrng.normal(0, 1.0)
            # recolor toward paper-ink: keep glyph's own shading, tint to ballpoint.
            # Per-glyph pressure breathes (0.85-1.05): real inkwork fades and bites.
            press = float(lrng.uniform(0.85, 1.05))
            arr = np.array(pil.convert("L")).astype(np.float32)
            ink = (arr < 200)
            tint = np.ones((arr.shape[0], arr.shape[1], 3), dtype=np.float32) * 253
            shade = (arr / 255.0)[..., None]
            tint = tint * (0.25 + 0.75 * shade)  # preserve stroke shading
            tint[..., 0] = np.clip(tint[..., 0] * 0.55 * press, 0, 255)
            tint[..., 1] = np.clip(tint[..., 1] * 0.60 * press, 0, 255)
            tint[..., 2] = np.clip(tint[..., 2] * 0.95 * press, 0, 255)
            cell = Image.fromarray(np.clip(tint, 0, 255).astype(np.uint8))
            mask_arr = (ink * 255).astype(np.uint8)
            # thickness match: upscaling fattens strokes, so erode the mask
            # back toward the writer's measured thickness before pasting
            try:
                import cv2 as _cv2
                if scale > 2.2:
                    mask_arr = _cv2.erode(mask_arr, _cv2.getStructuringElement(_cv2.MORPH_ELLIPSE, (3, 3)), iterations=1)
                elif scale > 1.35:
                    # 1-px cross erode: thins without eating thin strokes entirely
                    kern = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
                    mask_arr = _cv2.erode(mask_arr, kern, iterations=1)
            except Exception:
                pass
            mask = Image.fromarray(mask_arr)
            # bodies share a seating line: paste top anchored so x-height zones
            # align across glyphs instead of centering (centering lets tall and
            # short crops seesaw, which reads as soup, not handwriting).
            # Joined glyphs tuck 18% under the previous crop so the seam can fuse.
            if joining:
                cx -= nw * 0.32
            paste_top = int(yb + wob - nh * 0.62)
            img.paste(cell, (int(cx), paste_top), mask)
            # fuse the seam: short pen stroke from previous exit to this entry.
            # Spans past both edges so the weld always crosses the seam visibly.
            if joining and prev_exit is not None:
                ex0, ey0 = prev_exit
                ex1 = int(cx + 10)
                ey1 = int(paste_top + nh * 0.55 + lrng.normal(0, 2.0))
                ImageDraw.Draw(img).line(
                    [(ex0 - 6, ey0), ((ex0 + ex1) // 2, (ey0 + ey1) // 2 - 4),
                     (ex1 + 8, ey1)],
                    fill=(30, 35, 80), width=4, joint="curve")
            # exit flick: pen lifts with a tail at word ends
            if word_end and ch.isalpha() and lrng.random() < 0.55:
                fx0 = int(cx + nw * 0.85)
                fy0 = int(paste_top + nh * 0.55)
                flen = int(lrng.uniform(9, 18))
                rise = int(lrng.uniform(2, 7))
                ImageDraw.Draw(img).line(
                    [(fx0, fy0), (fx0 + flen // 2, fy0 - rise // 2),
                     (fx0 + flen, fy0 - rise)],
                    fill=(30, 35, 80), width=3, joint="curve")
            prev_exit = (int(cx + nw - 2), int(paste_top + nh * 0.55))
            # ADVANCE: pile deep inside words (reference density), gaps sacred.
            cx += max(nw * 0.45, nw * 0.85 + lrng.normal(1.0, 1.4))
    arr = np.array(img).astype(np.float32)
    arr = np.clip(arr + rng.normal(0, 1.6, arr.shape[:2])[..., None], 0, 255)
    return Image.fromarray(arr.astype(np.uint8))


def load_labeled(lib_dir: str):
    """Labeled library: {char: [crop arrays]}. Built by enroll.py from the
    user's own alphabet sheet, so each position pastes the CORRECT letter."""
    manifest_path = os.path.join(lib_dir, "manifest.json")
    if not os.path.exists(manifest_path):
        return None, None
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    if manifest.get("version") != "0.2-labeled":
        return None, None
    cache: Dict[str, list] = {}
    for ch, files in manifest.get("chars", {}).items():
        cache[ch] = []
        for fn in files:
            p = os.path.join(lib_dir, fn)
            if os.path.exists(p):
                try:
                    cache[ch].append(np.array(Image.open(p).convert("L")))
                except Exception:
                    continue
        if not cache[ch]:
            del cache[ch]
    return manifest, cache


def _font_fallback_cell(ch: str, target_h: int, lrng) -> Image.Image:
    """Rare chars missing from enrollment: clean font cell, same paper."""
    from features import binarize as _bin
    fnt = _font(int(target_h * 1.35))
    try:
        asc, desc = fnt.getmetrics()
    except Exception:
        asc, desc = int(target_h), int(target_h * 0.3)
    pad = 12
    cell = Image.new("RGB", (target_h + 2 * pad, asc + desc + 2 * pad), (255, 255, 255))
    cd = ImageDraw.Draw(cell)
    try:
        cd.text((pad, pad + asc), ch, font=fnt, fill=(28, 33, 75), anchor="ls")
    except TypeError:
        cd.text((pad, pad), ch, font=fnt, fill=(28, 33, 75))
    return cell


def render_labeled(text: str, style: Dict, lib_dir: str,
                   lined: bool = False, width: int = 1600,
                   target_h: int = 56, seed: int = 7,
                   style_strength: float = 1.0) -> Image.Image:
    """Exact-letter renderer: each character pastes one of YOUR enrolled
    variants of THAT character (random variant per occurrence for natural
    non-repetition). Layout engine mirrors render_with_glyphs: sacred word
    gaps, in-word welds, flicks, wobble. Missing chars -> font fallback."""
    feats = style.get("features", {})
    sag = min(float(feats.get("baseline_sag_px", 3.0)), 7.0) * float(style_strength)
    manifest, cache = load_labeled(lib_dir)
    if manifest is None or sum(len(v) for v in cache.values()) < 20:
        have = sum(len(v) for v in cache.values()) if cache else 0
        raise RuntimeError(f"labeled library missing/sparse at {lib_dir} ({have} glyphs). "
                           f"Run: python enroll.py sheet, fill it, then "
                           f"python enroll.py build photo.jpg --out {lib_dir}")
    cap_h = int(target_h * 1.15)  # normalize every variant to ~cap height
    rng = np.random.default_rng(seed)
    line_h = int(target_h * 2.5)
    paras = [p for p in text.split("\n")]
    lines: List[str] = []
    for para in paras:
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if cur and len(trial) * target_h * 0.62 > width - 160:
                lines.append(cur)
                cur = w
            else:
                cur = trial
        if cur:
            lines.append(cur)
        lines.append("")
    while len(lines) > 1 and lines[-1] == "":
        lines.pop()
    if not lines:
        lines = [""]
    H = line_h * len(lines) + 140
    img = Image.new("RGB", (width, H), (253, 252, 247))
    for li, line in enumerate(lines):
        if not line.strip():
            continue
        lrng = np.random.default_rng(seed * 1000 + li * 77 + 11)
        yb = 70 + li * line_h + lrng.normal(0, 1.0)
        cx = 60 + lrng.normal(0, 4.0)
        prev_exit = None
        for ci, ch in enumerate(line):
            if ch == " ":
                cx += max(target_h * 0.55, target_h * 0.75 + lrng.normal(0, 4.0))
                prev_exit = None
                continue
            word_start = prev_exit is None
            word_end = (ci == len(line) - 1) or (line[ci + 1] == " ")
            variants = cache.get(ch, [])
            if variants:
                g = variants[int(lrng.integers(0, len(variants)))]
                gh, gw = g.shape[:2]
                sc = cap_h / max(8.0, float(gh))
                nw, nh = max(6, int(gw * sc)), max(8, int(gh * sc))
                if nw > 4 * target_h or nh > 2.4 * target_h:
                    sc2 = min(4 * target_h / max(1, gw), 2.4 * target_h / max(1, gh))
                    nw, nh = max(6, int(gw * sc2)), max(8, int(gh * sc2))
                pil = Image.fromarray(g).resize((nw, nh), Image.LANCZOS)
            else:
                # font fallback keeps the WORD readable even for unenrolled chars
                pil = _font_fallback_cell(ch, target_h, lrng)
                nw, nh = pil.size
            rot = float(lrng.normal(0, 1.5))
            if abs(rot) > 0.4:
                try:
                    pil = pil.convert("L").rotate(
                        rot, resample=Image.BICUBIC, expand=True, fillcolor=255)
                except TypeError:
                    pil = pil.convert("L").rotate(
                        rot, resample=Image.BICUBIC, expand=True)
                nw, nh = pil.size
            wob = math.sin((cx / 110.0) + li * 1.7) * (sag * 0.4) + lrng.normal(0, 1.0)
            press = float(lrng.uniform(0.85, 1.05))
            arr = np.array(pil.convert("L")).astype(np.float32)
            ink = (arr < 200)
            tint = np.ones((arr.shape[0], arr.shape[1], 3), dtype=np.float32) * 253
            shade = (arr / 255.0)[..., None]
            tint = tint * (0.25 + 0.75 * shade)
            tint[..., 0] = np.clip(tint[..., 0] * 0.55 * press, 0, 255)
            tint[..., 1] = np.clip(tint[..., 1] * 0.60 * press, 0, 255)
            tint[..., 2] = np.clip(tint[..., 2] * 0.95 * press, 0, 255)
            joining = (not word_start) and lrng.random() < min(
                0.80, float(feats.get("ligature_pct", 25.0)) / 100.0 * 2.8)
            if joining:
                cx -= nw * 0.30
            paste_top = int(yb + wob - nh * 0.62)
            cell = Image.fromarray(np.clip(tint, 0, 255).astype(np.uint8))
            mask = Image.fromarray((ink * 255).astype(np.uint8))
            img.paste(cell, (int(cx), paste_top), mask)
            if joining and prev_exit is not None:
                # long cursive sweep: reach back into the previous glyph and
                # throw forward into this one, arched like a real pen join
                ex0, ey0 = prev_exit
                ex1 = int(cx + 12)
                ey1 = int(paste_top + nh * 0.55 + lrng.normal(0, 2.0))
                ImageDraw.Draw(img).line(
                    [(ex0 - 8, ey0), ((ex0 + ex1) // 2, (ey0 + ey1) // 2 - 6),
                     (ex1 + 12, ey1)],
                    fill=(30, 35, 80), width=4, joint="curve")
            if word_end and lrng.random() < 0.55:
                fx0 = int(cx + nw * 0.85)
                fy0 = int(paste_top + nh * 0.55)
                flen = int(lrng.uniform(9, 18))
                rise = int(lrng.uniform(2, 7))
                ImageDraw.Draw(img).line(
                    [(fx0, fy0), (fx0 + flen // 2, fy0 - rise // 2),
                     (fx0 + flen, fy0 - rise)],
                    fill=(30, 35, 80), width=3, joint="curve")
            prev_exit = (int(cx + nw - 2), int(paste_top + nh * 0.55))
            # joined pairs ride tight (fused), unjoined keep air (print-like)
            adv_f = 0.80 if joining else 0.90
            cx += max(nw * 0.55, nw * adv_f + lrng.normal(1.0, 1.2))
    arr = np.array(img).astype(np.float32)
    arr = np.clip(arr + rng.normal(0, 1.6, arr.shape[:2])[..., None], 0, 255)
    return Image.fromarray(arr.astype(np.uint8))


def eval_style_error(img: Image.Image, style: Dict) -> Dict:
    """Feature error between generated image and the .style profile.
    Thickness is compared as thickness/glyph-height RATIO (DPI-proof):
    raw px can never match across scan-vs-render DPIs, which is exactly
    what drove the old code to erode text into skeletons."""
    from features import analyze_pages
    feats = style.get("features", {})
    gen = analyze_pages([np.array(img.convert("L"))])
    out = {}
    # slant is unreliable on short samples when the hand is near-vertical
    # (|target| < 2deg): estimator noise dwarfs signal, so report it as
    # diagnostic only and keep it out of the MSE.
    skip_slant = abs(float(feats.get("slant_deg", 0.0))) < 2.0
    # DPI-proof thickness: compare stroke/glyph-height ratios, not raw px.
    t_h = float(feats.get("glyph_h_median", 0.0))
    g_h = float(gen.glyph_h_median or 0.0)
    use_ratio = t_h > 4 and g_h > 4
    if use_ratio:
        t_ratio = float(feats.get("thickness_px", 0.0)) / t_h
        g_ratio = float(gen.thickness_px) / g_h
        denom = max(1e-3, abs(t_ratio))
        out["thickness_ratio"] = {"target": t_ratio, "got": g_ratio,
            "abs_err": abs(g_ratio - t_ratio),
            "rel_err_pct": 100.0 * abs(g_ratio - t_ratio) / denom,
            "note": f"DPI-normalized ({feats.get('thickness_px',0):.2f}px/{t_h:.1f}px vs "
                    f"{gen.thickness_px:.2f}px/{g_h:.1f}px)"}
    for key, gkey in (("slant_deg", "slant_deg"), ("thickness_px", "thickness_px"),
                      ("ligature_pct", "ligature_pct")):
        if use_ratio and key == "thickness_px":
            continue  # ratio row above replaces the raw-px row
        target = float(feats.get(key, 0.0))
        got = float(getattr(gen, gkey))
        denom = max(1.0, abs(target))
        out[key] = {"target": target, "got": got,
                    "abs_err": abs(got - target),
                    "rel_err_pct": 100.0 * abs(got - target) / denom}
    scored = [v for k, v in out.items() if not (skip_slant and k == "slant_deg")]
    mse = float(np.mean([(v["abs_err"]) ** 2 for v in scored]))
    mean_rel = float(np.mean([v["rel_err_pct"] for v in scored]))
    out["feature_mse"] = mse
    out["mean_rel_err_pct"] = mean_rel
    if skip_slant:
        out["slant_note"] = "slant excluded from MSE (near-vertical target, estimator noise)"
    return out


def export_outputs(img: Image.Image, out_dir: str, stem: str = "Handwriting",
                    formats: List[str] = ("PNG",)) -> Dict[str, str]:
    os.makedirs(out_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    paths = {}
    if "PNG" in formats:
        p = os.path.join(out_dir, f"{stem}-{ts}.png")
        img.save(p, dpi=(300, 300))
        paths["PNG"] = p
    if "PDF" in formats:
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.utils import ImageReader
        except ImportError:
            # fallback: PIL pdf
            p = os.path.join(out_dir, f"{stem}-{ts}.pdf")
            img.convert("RGB").save(p, "PDF", resolution=300.0)
            paths["PDF"] = p
        else:
            p = os.path.join(out_dir, f"{stem}-{ts}.pdf")
            w, h = img.size
            # 300dpi -> points (72/inch)
            c = canvas.Canvas(p, pagesize=(w * 72 / 300, h * 72 / 300))
            c.drawImage(ImageReader(img), 0, 0,
                        width=w * 72 / 300, height=h * 72 / 300)
            c.showPage()
            c.save()
            paths["PDF"] = p
    if "SVG" in formats:
        p = os.path.join(out_dir, f"{stem}-{ts}.svg")
        # vector-lite: embed PNG as base64 in SVG (true stroke-vector comes with generator v2)
        import base64, io
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode()
        w, h = img.size
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">'
               f'<image width="{w}" height="{h}" href="data:image/png;base64,{b64}"/>'
               f'<!-- HandWriteAI v0.1: raster-embedded SVG. Stroke-vector export lands with generator v2 -->'
               f'</svg>')
        with open(p, "w", encoding="utf-8") as f:
            f.write(svg)
        paths["SVG"] = p
    return paths
