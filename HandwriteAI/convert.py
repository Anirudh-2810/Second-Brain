"""
HandwriteAI - convert text notes -> your handwriting.
Modes (best first):
  labeled: exact-letter renderer from YOUR enrollment sheet (correct letters,
           your ink). Needs a .labeled library: see enroll.py.
  glyphs:  legacy shape-bucket retrieval (real ink, WRONG letters possible).
           Kept for comparison; not recommended for readable output.
  font:    handwriting-font renderer (correct letters, font skeleton).

  auto = labeled if enrolled else font.

Profiles: each saved handwriting is a named profile (styles/profiles.json).
The active profile is used when neither --profile nor --style is given.

Usage:
  python convert.py --input notes.txt --format PNG
  python convert.py --profile "Profile 1" --input notes.md --format PNG,PDF
  python convert.py --profile 001 --text "hello" --mode font --seed 21
  python convert.py --style styles/profile_001.style --input notes.txt   # power override
  # enrollment:
  python enroll.py sheet
  python enroll.py build mysheet.jpg --profile mine
  python convert.py --profile mine --input notes.txt
"""
from __future__ import annotations
import os, argparse, re
BASE = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, BASE)
from inference import load_style, render_text_image, export_outputs
import profiles as profmod


def _has_manifest(d: str) -> bool:
    return bool(d) and os.path.exists(os.path.join(d, "manifest.json"))


def _safe_stem(name: str) -> str:
    return re.sub(r"[^\w\-]+", "_", name.strip()).strip("_") or "Handwriting"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="",
                    help="profile id / display name / number (default: active profile)")
    ap.add_argument("--style", default="",
                    help="explicit .style path (power override; skips profile lookup)")
    ap.add_argument("--input", default="", help=".txt/.md file to convert")
    ap.add_argument("--text", default="", help="raw text (if --input omitted)")
    ap.add_argument("--format", default="PNG",
                    help="PNG, PDF and/or SVG, comma-separated (e.g. PNG,PDF)")
    ap.add_argument("--mode", default="auto",
                    choices=["auto", "labeled", "glyphs", "font"],
                    help="auto = labeled if enrolled else buckets ink if harvested "
                         "else font (user chose look-first)")
    ap.add_argument("--glyphs", default="",
                    help="path to .labeled library (default: <style>.labeled, then <style>.glyphs)")
    ap.add_argument("--out-dir", default=os.path.join(BASE, "outputs"))
    ap.add_argument("--stem", default="",
                    help="output filename stem (default: profile display name)")
    ap.add_argument("--slant-adj", type=float, default=0.0)
    ap.add_argument("--strength", type=float, default=1.0)
    ap.add_argument("--width", type=int, default=1600,
                    help="page width in px; height auto-grows with wrapped "
                         "lines (1600 = portrait, 3080 = landscape)")
    ap.add_argument("--seed", type=int, default=7, help="ink/layout seed: change for a fresh take")
    ap.add_argument("--lined", action="store_true", default=False)
    ap.add_argument("--no-lined", dest="lined", action="store_false")
    ap.add_argument("--eval", action="store_true", help="report feature error vs style profile")
    args = ap.parse_args()

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        ap.error("provide --input notes.txt or --text \"...\"")

    formats = [fmt.strip().upper() for fmt in args.format.split(",") if fmt.strip()]
    bad = [fmt for fmt in formats if fmt not in ("PNG", "PDF", "SVG")]
    if bad or not formats:
        ap.error("bad --format %r (use PNG, PDF and/or SVG, comma-separated)" % args.format)

    if args.style:
        style_path = args.style
        stem_base = os.path.splitext(style_path)[0]
        display = os.path.basename(stem_base)
        info = None
    else:
        try:
            info = profmod.resolve(args.profile)
        except KeyError as e:
            ap.error(str(e))
        style_path = info["style"]
        stem_base = os.path.splitext(style_path)[0]
        display = info["display_name"]
        print("profile: %s (%s)" % (info["id"], display))

    style = load_style(style_path)
    feats = style.get("features", {})
    # DPI-proof headline: stroke/height ratio is the real thickness metric;
    # raw px depends on scan DPI and is diagnostic only (D2).
    gh_ref = float(feats.get("glyph_h_median", 0.0) or 0.0)
    thick_head = ("ratio=%.3f" % (float(feats.get("thickness_px", 0.0)) / gh_ref)
                  if gh_ref > 4 else "px=%.2f" % float(feats.get("thickness_px", 0.0)))
    print(f"style: slant={feats.get('slant_deg',0):.1f}deg "
          f"({feats.get('slant_confidence') or 'n/a-old-profile'}) "
          f"thick[{thick_head}] "
          f"lig={feats.get('ligature_pct',0):.1f}%")

    labeled_dir = args.glyphs or (stem_base + ".labeled")
    buckets_dir = stem_base + ".glyphs"
    # POLICY (user override 2026-10-10): look-first. auto = labeled if
    # enrolled (correct + ink), else buckets ink if harvested (the beloved
    # wild look; letters are lookalikes), else font (correct, tame).
    use_labeled = args.mode in ("labeled", "auto") and _has_manifest(labeled_dir)
    use_buckets = (not use_labeled and args.mode in ("glyphs", "auto")
                   and _has_manifest(buckets_dir))
    if args.mode == "labeled" and not use_labeled:
        print(f"WARNING: labeled library not found at {labeled_dir}. Enroll first: "
              f"python enroll.py sheet, fill it, then "
              f"python enroll.py build photo.jpg --out {labeled_dir}")
    if use_labeled:
        from inference import render_labeled
        img = render_labeled(text, style, labeled_dir, lined=args.lined,
                             width=args.width,
                             seed=args.seed, style_strength=args.strength)
        print(f"mode: labeled (your letters, {labeled_dir})")
    elif use_buckets:
        from inference import render_with_glyphs
        img = render_with_glyphs(text, style, buckets_dir, lined=args.lined,
                                 width=args.width,
                                 seed=args.seed, style_strength=args.strength)
        print(f"mode: glyphs/buckets (real ink, possibly wrong letters, {buckets_dir})")
    else:
        img = render_text_image(text, style, slant_adj=args.slant_adj,
                                style_strength=args.strength, lined=args.lined,
                                width=args.width, seed=args.seed)
        print("mode: font (correct letters, font skeleton)")
    out_stem = args.stem or _safe_stem(display)
    paths = export_outputs(img, args.out_dir, stem=out_stem, formats=formats)
    for fmt in formats:
        print(f"saved {fmt}: {paths[fmt]}")
    print(f"size: {img.size[0]}x{img.size[1]}")
    if args.eval:
        from inference import eval_style_error
        err = eval_style_error(img, style)
        print(f"feature_mse={err['feature_mse']:.4f} "
              f"mean_rel_err={err['mean_rel_err_pct']:.1f}%")
        # ratio row first: it is the scored metric; raw px is DPI-invalid.
        for k in ("thickness_ratio", "slant_deg", "thickness_px", "ligature_pct"):
            if k not in err:
                continue
            v = err[k]
            extra = f" [{v['note']}]" if "note" in v else ""
            tag = " (diagnostic, not scored)" if (k == "thickness_px" and "thickness_ratio" in err) else ""
            print(f"  {k}: target={v['target']:.4f} got={v['got']:.4f} "
                  f"err={v['rel_err_pct']:.1f}%{extra}{tag}")
        if "slant_note" in err:
            print(f"  note: {err['slant_note']}")


if __name__ == "__main__":
    main()
