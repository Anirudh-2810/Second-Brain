"""
HandwriteAI - convert text notes -> your handwriting.
Modes (best first):
  labeled: exact-letter renderer from YOUR enrollment sheet (correct letters,
           your ink). Needs a .labeled library: see enroll.py.
  glyphs:  legacy shape-bucket retrieval (real ink, WRONG letters possible).
           Kept for comparison; not recommended for readable output.
  font:    handwriting-font renderer (correct letters, font skeleton).

  auto = labeled if enrolled else font.

Usage:
  python convert.py --style styles/user_001.style --input notes.txt --format PNG
  python convert.py --style styles/user_001.style --text "hello" --mode font --seed 21
  python convert.py --style styles/user_001.style --input notes.md --format PDF --eval
  # enrollment:
  python enroll.py sheet
  python enroll.py build mysheet.jpg --out styles/mine.labeled
  python convert.py --style styles/user_001.style --glyphs styles/mine.labeled --input notes.txt
"""
from __future__ import annotations
import os, argparse
BASE = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, BASE)
from inference import load_style, render_text_image, export_outputs


def _has_manifest(d: str) -> bool:
    return bool(d) and os.path.exists(os.path.join(d, "manifest.json"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", default=os.path.join(BASE, "styles", "user_001.style"))
    ap.add_argument("--input", default="", help=".txt/.md file to convert")
    ap.add_argument("--text", default="", help="raw text (if --input omitted)")
    ap.add_argument("--format", default="PNG", choices=["PNG", "PDF", "SVG"])
    ap.add_argument("--mode", default="auto",
                    choices=["auto", "labeled", "glyphs", "font"],
                    help="auto = labeled if enrolled else buckets ink if harvested "
                         "else font (user chose look-first)")
    ap.add_argument("--glyphs", default="",
                    help="path to .labeled library (default: <style>.labeled, then <style>.glyphs)")
    ap.add_argument("--out-dir", default=os.path.join(BASE, "outputs"))
    ap.add_argument("--stem", default="Handwriting")
    ap.add_argument("--slant-adj", type=float, default=0.0)
    ap.add_argument("--strength", type=float, default=1.0)
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
    style = load_style(args.style)
    feats = style.get("features", {})
    print(f"style: slant={feats.get('slant_deg',0):.1f}deg "
          f"thick={feats.get('thickness_px',0):.2f}px "
          f"lig={feats.get('ligature_pct',0):.1f}%")

    stem = os.path.splitext(args.style)[0]
    labeled_dir = args.glyphs or (stem + ".labeled")
    buckets_dir = stem + ".glyphs"
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
                             seed=args.seed, style_strength=args.strength)
        print(f"mode: labeled (your letters, {labeled_dir})")
    elif use_buckets:
        from inference import render_with_glyphs
        img = render_with_glyphs(text, style, buckets_dir, lined=args.lined,
                                 seed=args.seed, style_strength=args.strength)
        print(f"mode: glyphs/buckets (real ink, possibly wrong letters, {buckets_dir})")
    else:
        img = render_text_image(text, style, slant_adj=args.slant_adj,
                                style_strength=args.strength, lined=args.lined,
                                seed=args.seed)
        print("mode: font (correct letters, font skeleton)")
    paths = export_outputs(img, args.out_dir, stem=args.stem, formats=[args.format])
    print(f"saved: {paths[args.format]} ({img.size[0]}x{img.size[1]})")
    if args.eval:
        from inference import eval_style_error
        err = eval_style_error(img, style)
        print(f"feature_mse={err['feature_mse']:.4f} "
              f"mean_rel_err={err['mean_rel_err_pct']:.1f}%")
        for k in ("slant_deg", "thickness_ratio", "thickness_px", "ligature_pct"):
            if k not in err:
                continue
            v = err[k]
            extra = f" [{v['note']}]" if "note" in v else ""
            print(f"  {k}: target={v['target']:.4f} got={v['got']:.4f} "
                  f"err={v['rel_err_pct']:.1f}%{extra}")
        if "slant_note" in err:
            print(f"  note: {err['slant_note']}")


if __name__ == "__main__":
    main()
