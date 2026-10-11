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
  _*.py              # lab tools: _isheet/_resheet/_fullsheet/_pool_sheet/
                     # _suspect/_prune*/_harvest*/_restore_g/_verify/_proof
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
   Currently 26/64 labeled; the rest skipped as junk/mixed. Unlabeled
   clusters are NOT wasted — full indexed sheets (`_fullsheet.py <cid>`)
   + eyeball harvest (`_harvest_tfsr.py` pattern) recovered t/f/s/r
   from c11/c29/c44/c47 this session.

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

## Current library state (2026-10-11, after t/f/s/r harvest)
- 1141 glyphs / 19 letters: e355 i253 n66 a65 d58 r58 b45 o55 p42 s25 m26
  l24 v20 f15 w12 u15 t3 g2 y2.
- Missing (font-fallback at render): c h j k q x z + digits + punctuation.
  t/f/s/r harvested this session from unlabeled clusters (c11/c29/c44/c47)
  but pools are thin — t=3, s=25, f=15, r=58 (r fattened from 14).
- g restored from c45 (2 clean closed-bowl variants; lined ones pruned).
- q stats: min .05 / median .36 / max 1.0.

## Known issues (as of 2026-10-11 t/f/s/r harvest)
- FIXED earlier this pass: y->J (body_bottom_frac largest-area rule +
  descender shrink), o->a / l+o->b (pool prune + round-bowel join pull
  0.10 + advance >=0.98), w->u / u->n (w#4/w#5/u#8 dropped).
- Word-final t reads f in some picks ("most"->"mosft", "rate"->"rafe"):
  the user's t and f share crossbar + bottom-hook; at word end (no join)
  the hook curls down and reads as f's descender. Inherent hand ambiguity,
  not a pool bug — only 3 clean t variants exist. Paper enrollment of
  clearer t's is the fix.
- s->j on thin top-hook variants (rare after prune); s pool mixed
  printed-3style + cursive-loop styles.
- Residual (known, low priority): "organ"->argan (o+r join), "away"->auay
  (w pool thin at 12), e-pool a-picks in isolated words, flicks at 55%
  and wild in-word joins are accepted style.

## Next steps (ordered)
1. Paper enrollment decision (USER): covers the 7 missing letters (c h j k
   q x z) + digits + punctuation + true dotted i/j + clearer t/f variants
   to fatten thin pools — `data/enrollment-sheet.pdf`.
2. Optional: second e-pool pass (355 variants, occasional a-like).
3. Optional: harvest more unlabeled clusters for digits (c31 has 8/3/2/6/5)
   and remaining letters if any clean pools exist.
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
