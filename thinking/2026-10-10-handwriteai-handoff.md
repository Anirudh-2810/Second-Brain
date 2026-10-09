# HandwriteAI — handoff for tomorrow (making-sense part)

Date: 2026-10-10 ~01:50 IST. State: GOOD. User happy with look-first buckets
energy. Tomorrow = correctness (true letters) via Tab-6 cluster labeling.

## Where things stand (commit 705381c, pushed to main)
- Default `convert.py` (no flags) -> buckets ink: dense joins (~80% pairs),
  deep tucks, living sizes, real-ink pressure. Ligature 1.9% err, mean 4.3%.
- auto policy: labeled (if enrolled) > buckets (if harvested) > font.
- Guards holding: monster-crop reject (harvest/load/pick), sanitize_library(),
  no erosion/bridge loops anywhere (deleted, not disabled).
- 64 shape clusters pre-built: styles/user_001.clusters/ (3022 crops,
  intra-NCC 0.49 vs inter 0.19). UI Tab 6 ready: build/show/save/skip/back/
  confirm-guess/finish -> styles/user_001.labeled/.
- Enrollment-sheet paper path also ready: data/enrollment-sheet.pdf.
- Proof outputs (gitignored, local only): outputs/LookFirst-*.png (the look),
  outputs/Flow1 was deleted, test libs removed.

## Tomorrow's job: identity (correct letters, keep the energy)
1. User labels 64 clusters in Tab 6 (~10 min) -> Finish writes .labeled/.
2. Render note1.txt with --mode labeled (auto will pick it up). EXPECT:
   joins/energy carry over (render_labeled shares the weld/flick layout).
3. Watch for: (a) sparse buckets for rare letters -> font fallback visible
   as clean skeleton amid wild ink (acceptable; note which chars);
   (b) over-joined seeds pushing words together -> vary --seed, keep best;
   (c) tall-bucket misassignment (1345 tall vs line_h_ref=60 — bucket_of may
   misclassify if user's line height differs; check a few tall crops).
4. If labeling stalls: paper path (enrollment-sheet.pdf) gives 1 variant/char.

## Open technical debts (do NOT touch unless asked)
- Slant estimator noisy on short/near-vertical text (excluded from MSE).
- eval thickness absolute-px rows are DPI-invalid; ratio rows are the real ones
  (activate after re-train populates glyph_h_median — user_001.style has it now).
- Buckets letters are lookalikes by design (user chose look-first 2026-10-10).
- Unrelated working-tree changes (wiki chem/SPM mods, thinking/* scratch,
  temp_ion.txt) are NOT mine — never commit them with HandwriteAI work.

## Quick commands
- UI: python HandwriteAI/gradio_ui.py -> http://127.0.0.1:7860 (Tab 6)
- CLI: python HandwriteAI/convert.py --style HandwriteAI/styles/user_001.style --input HandwriteAI/data/note1.txt --format PNG --eval
- Kill stale UI server before re-testing (old process serves old code).
