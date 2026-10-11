# HandwriteAI - build map (v0.2)

For personal note digitization only. Offline, CPU-only, no data leaves device.

## Layout
```
HandwriteAI/
  requirements.txt
  features.py        # deskew/binarize/lines/slant(+confidence)/thickness/baseline
  models.py          # StyleEncoder CNN + StrokeGenerator Transformer+LSTM
  train_fine_tune.py # Phase1 IAM stub / Phase2 fine-tune / Phase3 synthetic loop
  inference.py       # font + buckets + LABELED renderers, PNG/PDF/SVG export
  enroll.py          # alphabet-sheet enrollment -> .labeled library (paper path)
  cluster.py         # shape clustering + label apply -> .labeled (no-paper path)
  glyphs.py          # unlabeled harvest + sanitize + body_bottom_frac + line_h_ref
  convert.py         # CLI: --mode auto (=labeled if present else font)
  gradio_ui.py       # 6-tab flow (tab 6 = cluster labeling), localhost:7860
  _*.py              # lab tools: _isheet/_resheet/_suspect/_prune*/_verify/_proof
  models/            # encoder_iam.pth, encoder_finetuned.pth
  styles/            # user_001.style + user_001.labeled/ + user_001.clusters/
  outputs/           # generated files (gitignored)
  data/              # enrollment-sheet.pdf (print me)
  Test_input/        # user's own sample scans (gitignored)
```

## Render modes (best first)
- labeled: YOUR letters from enrollment sheet OR cluster labeling. Correct +
  real ink. `auto` picks this whenever present.
- font: correct letters, font skeleton + human texture. Always readable.
- glyphs/buckets: legacy shape lookalikes (real ink, wrong letters). Explicit
  opt-in only; `auto` never selects it (gibberish incident).

## Correctness paths (pick one — both write .labeled libraries)
A. Paper: `python enroll.py sheet` -> print/fill/photo ->
   `python enroll.py build photo.jpg --out styles/mine.labeled`
B. No paper: UI tab 6 builds shape clusters from uploads -> label each ->
   Finish writes `styles/user_001.labeled/` (64 clusters, numpy KMeans).
   Currently 22/64 labeled; the rest skipped as junk/mixed.

## Labeling rules + QA (learned the hard way)
- Queue runs biggest-first (coverage per minute); per-cluster shape stats
  flag suspect sheets (aspect > 1.2 or width-cv > 0.45: probably joined,
  consider Skip).
- One letter only if ALL samples agree. Skip joined-pair junk — a two-letter
  crop renders as a scrawl. Never blind-Confirm guesses under ~0.55.
- Finish always builds but PRINTS the missing-letter fallback list.
- Contact sheets show first 12 only — for any cluster > 12, regenerate a
  full indexed sheet (`_resheet.py <cid>` / `_isheet.py <cid>`) before
  trusting the label. `_suspect.py` flags structural junk (fragments /
  multi-letter crops / aspect outliers) for visual confirmation.
- Prune by removing member indices from `clusters.json` (files stay in the
  source lib), then re-run `apply_labels`. NEVER prune by letter-wide index
  mixups — `_fix_e_prune.py` records the byte-match recovery pattern.
- Writers store per-crop metrics (`metrics: {file: {bb, q}}`); readers fall
  back to 0.62 (bb) / 1.0 (q) without them.

## Render engine v0.2 (current behavior)
- ONE global ink-height factor (font-cell median ink / lib median ink), NOT
  per-canvas ref_h (that undershot ink ~2x).
- Baseline body-bottom seating (`body_bottom_frac`), descenders drop below
  naturally. Mixed-padding crops stop seesawing.
- Welds/flicks anchor at INK edges on the baseline. Canvas-edge anchors drew
  phantom crossbars (e read H, l read r). Welds only when `_seam_meet`
  confirms mid-zone ink faces ink across the seam.
- Font-fallback cells crop to ink bbox (+3px) so advance matches real ink
  (killed `respo nse`, `t imef rame` holes). Capital-I gets hand-style
  crossbars (bare bar reads as l).
- Line-wrap sums real per-char advances (not a flat px/char constant).
- Labeled pick is quality-weighted (~q^4, q from aspect/fill/sharpness) +
  aspect-outlier retry (uniform picks hit bad-tail crops in LONG text:
  `got`->`fot`, `name`->`rame`).
- Double letters (mm/tt/nn/ll) never weld +5% advance; unjoined adjacent ink
  bboxes pushed apart (joined pairs keep designed overlap).
- i-dot synthesis: enrollment detached the writer's dots (is read ls, I'd
  read lid) — dash-dot drawn above i bodies unless the crop has its own dot.
- Upscale thickness-match erosion (small crops fatten ~2x); rotation capped
  off for tiny crops (dots/punctuation read as noise).
- Slant carries evidence: `slant_confidence` high/med/low + `slant_n`
  (adaptive Hough retry before moments fallback); weighted median across
  pages; low-confidence excluded from MSE with reason.
- Thickness scored as DPI-proof ratio (stroke/glyph-height), raw px is a
  diagnostic only. Glyph libs store per-page `line_h_ref` (derived, not
  hard-coded 60) + `ref_h`.

## Current library state (2026-10-11, after y/o/w/u identity pass)
- 1095 glyphs / 15 letters: e355 i253 n66 a65 b60 o56 d58 l46 p42 m26 v25
  u15 r14 w12 y2.
- Missing (font-fallback at render): c f g h j k q s t x z + digits +
  punctuation. g was pruned wholesale overnight (all read 9-like/d-like);
  good variants extracted from cluster_045_all.png but NOT yet restored.
- y is down to 2 variants (c7); the γ-style c30 pool (34) was dropped whole.
- q stats: min .05 / median .36 / max 1.0.

## Known issues (as of 2026-10-11 identity pass)
- FIXED y->J: root cause was `body_bottom_frac` anchoring y at the tail
  TIP (the tail's end-hook is wide enough to pass the old threshold),
  seating the cup at cap-height. New rule = largest-area ink run (an
  i-dot is a smaller run than the stem and must not steal the anchor).
  Two y crops re-anchored (bb 0.96->~0.33) + render-time descender
  shrink (scale below-baseline rows 0.4-1.0 per placement).
- FIXED o->a and l+o->b: three causes stacked - (1) pool carried
  right-stem/θ/C-hook o's (dropped 87->56, incl. two high-q a-like
  crops the q^4 weighting kept re-picking); (2) the 30% join PULL put
  the next letter's stem ON the bowl edge ('come'->'came') or a bowl
  INTO a tall stem ('look'->'bok'); (3) joined ADVANCE let the next
  stem start inside the bowl's width ('on'->'an'). Now: either side
  round (oadgcq) => 0.10 pull + >=0.98 advance, weld line alone bridges.
- FIXED w->u / u->n: w#4 (u+detached stroke), w#5 (shallow middle
  peak), u#8 (arched top = n) dropped. "wanna" reads.
- Residual (known, low priority): 'come'/'on' borderline a-read at
  tiny sizes in some seeds (pool still has a couple of top-tick o's);
  e-pool a-picks in isolated words ('have'->'hava'); thin pools
  r14/w12/y2/u15 vary per pick; flicks at 55% and wild in-word joins
  are accepted style.

## Next steps (ordered)
1. g ink restoration: re-add the variants extracted from the c45 sheet
   (clean bowl+descender g's).
2. Paper enrollment decision (USER): covers the 11 missing letters +
   digits + punctuation + true dotted i/j + fresh y/w/r variants to
   fatten the thin pools — `data/enrollment-sheet.pdf`.
3. Optional: second e-pool pass (355 variants, occasional a-like).
4. Re-run `_verify.py` (love-note + prose + 4-seed gates) after each pass.

## Quickstart (10-15 min to first generation)
```
cd HandwriteAI
pip install -r requirements.txt
python gradio_ui.py
# 1. Upload 2-4 pages -> Extract Features
# 2. Fine-tune (2 epochs, CPU)
# 3. Type text -> Generate -> Download PNG/PDF/SVG
```

CLI fine-tune without UI:
```
python train_fine_tune.py --samples page1.png page2.pdf --out styles/user_001.style --epochs 2
```

## Notes
- SVG v0.1 embeds raster (true stroke-vector lands with generator v2).
- IAM pre-training: `python train_fine_tune.py --pretrain --iam-root data/iam --epochs 3`
- Success targets: feature MSE < 0.05, spacing corr > 0.85, <5s/100 chars CPU.
- Kill stale UI server before re-testing (old process serves old code).

## Ethics (must-read)
Legitimate: personal notes, stationery, accessibility, practice, creativity.
Prohibited: reproducing others' coursework, bypassing handwritten requirements,
deceptive docs, unlicensed font commercialization, academic dishonesty.
