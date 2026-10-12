# HandwriteAI - build map (v0.3)

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
  profiles.py        # named-profile registry: list/resolve/create/rename (B2)
  convert.py         # CLI: --profile / --style / --mode auto / --format PNG,PDF
  gradio_ui.py       # 6-tab flow (tab 5 = Profiles & Settings, tab 6 = label)
  _*.py              # lab tools: _isheet/_resheet/_fullsheet/_pool_sheet/
                     # _suspect/_prune*/_harvest*/_restore_g/_verify/_proof
  models/            # encoder_iam.pth, encoder_finetuned.pth (shared)
  styles/
    profiles.json        # active profile + display-name registry
    profile_001.style    # Profile 1 (original user_001 hand, renamed 2026-10-10)
    profile_001.labeled/ # render library (1137 glyphs / 19 letters)
    profile_001.glyphs/  # source harvest (re-clusterable)
    profile_001.clusters/# cluster-labeling state
  outputs/           # generated files (gitignored)
  data/              # enrollment-sheet.pdf (print me)
  Test_input/        # user's own sample scans (gitignored)
```

## Profiles (multi-hand support, B2, 2026-10-10)
- Each saved handwriting = one profile: `styles/profiles.json` + a family of
  `<id>.style` / `<id>.labeled/` / `<id>.glyphs` / `<id>.clusters`.
- `profiles.py` resolves by id (`profile_001`), display name (`Profile 1`),
  bare number (`001`/`1`), or empty string (active profile). Missing registry
  self-heals by registering any unregistered `styles/*.style`.
- CLI: `--profile "Profile 1"` on convert/enroll/cluster/train_fine_tune;
  `--style path` still works as a power override.
- UI Tab 5: dropdown to switch active profile, create new (fresh or copy),
  rename, export/import full-profile bundle (.zip), delete active.
- Tab 3: multi-format CheckboxGroup (PNG/PDF/SVG any combo); Tab 4 Download
  saves every picked format.
- Tab 1 fine-tune and Tab 6 cluster-labeling write to the ACTIVE profile.
- One-shot `_prune_*`/`_g_*`/`_spy_smoke*` scripts still hard-code
  `user_001` paths (dead, not worth migrating). Live lab scripts
  (`_verify`, `_ggate`, `_pool_sheet`, `_spy_cuneiform`, `_recover_c11`,
  `_harvest_t_backfill`) resolve via `profiles.resolve("")`.

## Render modes (best first)
- labeled: YOUR letters from enrollment sheet OR cluster labeling. Correct +
  real ink. `auto` picks this whenever present.
- font: correct letters, font skeleton + human texture. Always readable.
- glyphs/buckets: legacy shape lookalikes (real ink, wrong letters). Explicit
  opt-in only; `auto` never selects it (gibberish incident).

## Correctness paths (pick one — both write .labeled libraries)
A. Paper: `python enroll.py sheet` -> print/fill/photo ->
   `python enroll.py build photo.jpg --profile "Profile 1"`
B. No paper: UI tab 6 builds shape clusters from uploads -> label each ->
   Finish writes `styles/profile_001.labeled/` (64 clusters, numpy KMeans).
   Currently 26/64 labeled; the rest skipped as junk/mixed. Unlabeled
   clusters are NOT wasted — full indexed sheets (`_fullsheet.py <cid>`)
   + eyeball harvest (`_harvest_tfsr.py` pattern) recovered t/f/s/r
   from c11/c29/c44/c47; c11 orphans recovered this pass via `_recover_c11.py`
   (pipeline-calibrated md5 match against `full_11.png`, 31/31 calibration).

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
- F5 (2026-10-12): arch-stroke runs `[mnu]+` never weld + 0.95 advance —
  vertical downstrokes + sweeps fused into an unreadable picket fence
  (`condimentum`: m vs nn vs un vs nu). Spacing carries identity.
- F6 (2026-10-12): no weld sweep + light 0.10 pull when either side is `r`;
  the sweep routed through r's loop zone and flattened it (`ver` read n).
  r-pool audited same pass (58 crops, no degenerate, no prune needed).
- F7 (2026-10-12): line rhythm 2.5 -> 2.8 x target_h (font path 1.9 -> 2.1);
  p/y descenders cut across next-line ascenders (`Pulvinar` stacks).
  Costs ~12% page height. Air over tail surgery.
- e-pool hygiene (2026-10-12): closure metric (mid-right band fill) showed
  18.2% of e-picks came from open (c-like) variants; 93/355 crops capped
  to q<=0.10 (-> 0.05% pick-weight). Files kept, manifest-only change,
  backup `manifest.json.bak-e-prune`. Reversible.
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

## Current library state (2026-10-11, after Phase A quality pass)
- 1137 glyphs / 19 letters: e355 i253 n66 a65 d58 r58 b45 o55 p42 s25 m26
  l24 v20 f7 w12 u15 t7 g2 y2.
- Missing (font-fallback at render): c h j k q x z + digits + punctuation.
  t=7 (3 original + 4 harvested via `_harvest_t_backfill.py` from orphans
  #0/#10/#12/#29 of c11; source PNGs cleaned in place — ruling rows erased,
  stray comma blob removed from #10); f=7 (15 pruned down to f001/f002/f003/
  f004/f007/f013/f014 after `_spy_cuneiform.py` pick-spy — the q=1.00
  joined-crop f_012 was the "Cuneiform" culprit; f003 (high crossbar) is
  the dominant pick now).
- q stats: min .05 / median .36 / max 1.0.

## Known issues (as of 2026-10-11 Phase A)
- FIXED this pass: t->f misread. Root cause: `body_bottom_frac` threshold
  (`0.35 × max_row_width`) is inflated by t's wide crossbar; the narrow stem
  falls below threshold and bb anchors at the crossbar top instead of the
  stem bottom, so the whole stem+flick hangs below the writing line and reads
  as f. Verified t-only; f's bb were all correct. Fix: corrected t bb in BOTH
  manifests (original 3 crops re-measured; 4 new crops carry their measured
  bb); added a t-only descender-shrink safety net at `inference.py:811`
  (factor 0.45-0.75 when descender >8 rows). "Cuneiform", "from", "after",
  "fragmented" all read correctly now.
- Residual (known, low priority): "systems" reads "sysrems" (t-e weld
  artifact); "Organ" g reads ç-ish (g=2 limitation, needs paper enrollment);
  hyphens/digits/c-h-j-k-q-x-z are font fallback; wild in-word joins are
  accepted style.

## Profile 2 (2026-10-12, in progress)
- Same-hand DocScanner post-lab pages (arrays/loops/decision-making, 9 pp).
  Excluded: 08-Oct clipboard answer-sheet (different hand, user decision).
- `profile_002` created fresh; `profile_002.glyphs/` = 3038 crops
  (line_h_ref=276, xheight-heavy); `profile_002.clusters/` = 64 clusters
  from 2716 crops. 9 clusters pre-flagged as joined/mixed junk (c45/c7/
  c41/c47/c11/c61/c3/c35/c28) — Skip candidates at labeling.
- LABELED 2026-10-12 by agent (user delegated): 64 clusters reviewed
  via contact + full indexed sheets; 14 labeled (o/n/u/t/e/c/l/d/y/r/+/l/d),
  50 skipped (mixed/joined/junk), 71 members pruned across 10 clusters.
  Result: `profile_002.labeled/` = 683 glyphs / 11 letters. Missing (font
  fallback): a b f g h i j k m p q s v w x z + digits + punctuation.
- e-pool verified clean at build (closure min 0.208, no cap needed).
- Style measured from 9 pages (slant 0.0 high-conf, ligature 11.1%);
  fresh-style backup `profile_002.style.bak-fresh`.
- Ruling cleanup (ruled-notebook source): derule (213 bottom-row crops),
  derule3 (64 thin detached blocks), decc (299 detached CCs in 222 crops).
  Backups `.bak-ruling*` / `.bak-decc`. Remaining ticks are connected
  pen flicks — left alone deliberately.
- Engine fix same pass: labeled-wrap iteration `sorted()` — set order used
  to re-wrap fallback-heavy text differently on every run.

## Next steps (ordered)
1. Paper enrollment decision (USER): covers the 7 missing letters (c h j k
   q x z) + digits + punctuation + true dotted i/j + clearer g variants —
   `data/enrollment-sheet.pdf`. Profiles make this easy: create "Profile 2",
   enroll a different hand without disturbing Profile 1.
2. Optional: second e-pool pass (355 variants, occasional a-like).
3. Optional: harvest more unlabeled clusters for digits (c31 has 8/3/2/6/5)
   and remaining letters if any clean pools exist.
4. Re-run `_verify.py` (love-note + prose + 4-seed gates) after each pass.
5. Gradio UI smoke test: open `python gradio_ui.py`, confirm Tab 5 profile
   dropdown/create/rename/export/import/delete work (manual — agent cannot
   see rendered Obsidian or a running Gradio app).

## Quickstart (10-15 min to first generation)
```
cd HandwriteAI
pip install -r requirements.txt
python gradio_ui.py
# 1. Upload 2-4 pages -> Extract Features
# 2. Fine-tune (2 epochs, CPU)
# 3. Type text -> Generate -> Download PNG/PDF/SVG
```

CLI:
```
python convert.py --profile "Profile 1" --input notes.txt --format PNG,PDF
python train_fine_tune.py --samples page1.png page2.pdf --profile "Profile 1" --epochs 2
python enroll.py build photo.jpg --profile "Profile 1"
python cluster.py build --profile "Profile 1" --k 64
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
