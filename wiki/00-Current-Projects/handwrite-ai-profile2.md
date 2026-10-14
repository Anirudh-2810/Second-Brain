---
module: "handwrite-ai"
topic: "HandwriteAI Profile 2 — exact-letter handwriting renderer (WIP)"
tags: [handwrite-ai, handwriting, renderer, glyphs, profile-2, wip]
last_updated: "2026-10-15"
confidence: high
description: "Profile 2 of HandwriteAI (E:\Brain\Second-Brain\HandwriteAI): exact-letter renderer pasting the user's real ink crops. Full session log 2026-10-14→15: glyph pool rebuild, 4-crop fixes, ink-uniformity normalization. STATUS: working, aesthetics still being tuned — owner paused for exams."
---

## For future agent

Profile 2 renders text by pasting the user's real handwritten glyph crops (one crop per letter occurrence, quality-weighted random pick). Source: alphabet screenshot `C:\Users\Asus\Pictures\Screenshots\Screenshot 2026-10-13 134208.png`. **Status: functional but NOT finished** — owner paused work for exams; remaining polish items in "Still to do". All library data is gitignored (regenerable); the scripts that build it are untracked in the repo. When resuming: read this page top-to-bottom, check `wiki/log.md` for the 2026-10-15 entry, then re-render the verification texts before changing anything.

---

## What Profile 2 is

- `HandwriteAI` — local handwriting renderer (PIL + numpy + cv2, no ML inference needed for this mode).
- `--mode labeled` → `render_labeled()` in `inference.py`: each character pastes one enrolled variant of THAT character; missing chars fall back to a drawn font cell.
- Library: `styles/profile_002.labeled/` (manifest.json + 756 crop PNGs, version `0.2-labeled`). Loader `load_labeled()` (inference.py ~604) reads manifest `chars` + per-file `metrics {bb, q}`; pick weights = `q^4`.
- Writer's measured features (`styles/profile_002.style`): `thickness_px=1.91`, `glyph_h_median=16`, `ligature_pct=11.1`, `slant_deg=0`.

## Session log — 2026-10-14 → 2026-10-15

### 1. Glyph pool rebuild (root-cause fix for "garbage letters")
The original screenshot harvester mis-assigned rows (uppercase shapes in lowercase pools) and Windows' case-insensitive FS made `sheet_a_0.png` == `sheet_A_0.png` (uppercase band overwrote every lowercase crop). Fixes, all in `_p2_sheet_reharvest.py` + `_p2_manifest_rebuild.py`:
- **Ord-based filenames** `sheet_<ord(ch)>_<k>.png` — case-safe on Windows.
- **Tight non-overlapping bands** (dark<110 over x[40:], gap tol 3) — loose bands let cells bleed ink from the row below, corrupting `body_bottom_frac`.
- **Char-aware `baseline_frac(ch, arr)`** — non-descenders use ink-bottom/h (≈1.0 on tight crops); only `gjpqy` use the run/area logic. The old `body_bottom_frac` mis-picked thin-stroke letters (J/C/F/I/S floated).
- **Always recompute sheet metrics** in the rebuild (stale-metrics reuse bug).
- Merge policy: KEEP `cNN_*` cluster crops (11 chars: c d e l n o r t u y +), DROP all `enr_*` (unreliable), ADD 73 verified sheet crops.
- Result: **69 chars / 756 glyphs / missing only `.`** (period not on sheet → font fallback, expected). Backup: `manifest.json.bak-rebuild`.

### 2. Four bad crops fixed (verified via ASCII art)
- `8`: pen speck (y365) + ruled-line bar (y389) inside crop → `strip_edge_junk()` drops detached edge runs (h≤1, or h≤2 & width≥60%) then retrims.
- `W`: 1px stray dot at y340 → same stripper.
- `9`: loop clipped at LEFT=40 (ink at x37–39) → left-boundary expansion in `column_cells` (grow x0 ≤6px while adjacent column has ink in y-range, never crossing previous cell).
- `+` (punct cell 0): left arm clipped at x37–39 → same expansion.
- Re-run: band counts exact `[10,10,6,10,10,6,8,3]` + 10 punct; 68 staged chars / 73 crops.

### 3. Ink uniformity (the "some words thick, some thin" fix)
**Diagnosis:** two crop pools with ~2× different stroke weight — 73 binary sheet crops (native 1.91px = writer's true pen) vs 683 soft-grayscale cluster crops (native 2.74/3.82px, bimodal). At render scale (`_k=3.0`, clamped) that's 3.8px vs 7.4px strokes; the legacy sc-gated erosion (fixed 3×3 kernel at sc>1.35/2.2) subtracted absolute ~2px from everything → sheet glyphs collapsed to hairlines while cluster glyphs stayed fat. Cluster crops dominate picks 97–99% for the 11 shared chars (q^4 weights × count).

**Fix, two layers:**
- **`_p2_normalize_ink.py`** (new one-shot): binarize every library crop at <200 (uniform upscale behavior), then width-normalize to 1.91px native via supersampled erode/dilate. 512/756 crops changed; result 1.91±0.23. Backup: `styles/profile_002.labeled.bak-normalize`. **Run AFTER `_p2_manifest_rebuild.py`** (rebuild copies raw stage crops back into the library).
- **`inference.py` `_match_thickness(mask_arr, target_px)`**: pools are uniform now, so one measured correction per paste — `cur = 2*median(dt)`, then erode/dilate by `k = round(|cur−target|×2)` rings of 0.25px on a 4× supersampled mask (sub-pixel needs supersampling). Weld/flick draw widths keyed to the same target.

**Failed approaches (do NOT retry blindly):**
- Plain dt-threshold erode/dilate: cv2's approximate DT (maskSize=3) bottoms out at ~0.95, so any radius <1px is a **no-op** — 450 crops stuck.
- Whole-step 3×3 morphology: median-dt barely moves on blobby interiors; 388 crops unchanged.
- p90-of-dt measurement: overcorrected (268 crops eroded too thin) — p90 and median disagree by ~1px systematically on these shapes.
- Multi-pass dt-threshold loops: median-dt is an *interior* statistic — eroding a fat blob's boundary barely moves it.

### 4. Thickness target tuning
- Target = `thick_px × effective_scale × THICK_SCALE` (inference.py, `render_labeled`).
- `THICK_SCALE = 1.0` → 5.73px strokes: too heavy, welds/blobby variants read as blobs, apertures close up.
- **`THICK_SCALE = 0.75` → 4.30px: current setting** (welds 6→4px). Owner approved look 2026-10-15.
- Tuning: 0.65 → 3.7px, 0.85 → 4.9px. One constant.

## Verification (2026-10-15)
- Render: `python convert.py --profile 002 --mode labeled --seed 7 --text "..."` (outputs/Profile_2-*.png).
- Passage render: line-level stroke med 4.65px, std 0.32, range [3.82, 4.65] — uniform.
- Regression (pangram + caps + digits + punct + descenders gjpqy): all legible, no shattering.
- Glyph-component stats remain noisy (i-dots, welds, junctions dominate) — trust line-level stats + eyes.

## Still to do (owner paused for exams)
0. **NEXT SESSION (owner feeding a full A–Z + 0–9 + symbols sheet):** strip it and use as the enrollment template — current texts render "very uneven", pools get replaced. Order: harvest (bands + ord-names + left-expansion + strip_edge_junk, adapted to the new layout) → rebuild manifest (backup first) → **`_p2_normalize_ink.py` (mandatory — this is what fixes unevenness)** → re-render passage + regression, measure, re-tune `THICK_SCALE`. **Open decision:** replace pools fully (recommended — cleanest fix) vs merge (keep old clusters as variants only for chars the sheet lacks).
1. **Aesthetic tuning** — `THICK_SCALE` is the knob; owner judges by eye.
2. **Degenerate cluster crops** — a few blobby `e`/`o` variants (native 3.82 bucket) still read heavy at joins; consider pruning or re-harvesting those specific letters.
3. **Caps-line joins** — `ABCDEFGHIJKLMNOPQRSTUVWXYZ` runs slightly blobby at welds (pre-existing joining behavior, not a thickness bug).
4. **More variants per letter** — pools are thin for some letters; more variants = more natural variation (see [[00-Current-Projects/INDEX]] update discipline).
5. **Profile 1 parity** — `render_with_glyphs` (buckets path) still has the legacy sc-gated erosion; same bug class, out of scope so far.
6. **Commit** — `_p2_*.py` scripts + `styles/_p2_stage/` are untracked; `.labeled/` + `outputs/` gitignored by design. Nothing committed yet.

## File map
| Path | Role |
|---|---|
| `HandwriteAI/inference.py` | `render_labeled` (~686), `_match_thickness` (~686), `THICK_SCALE` (~21), `load_labeled` (~604) |
| `HandwriteAI/_p2_sheet_reharvest.py` | band re-harvest, ord-safe names, left-expansion, `strip_edge_junk` |
| `HandwriteAI/_p2_manifest_rebuild.py` | merge clusters+sheet, drop enr, metrics, `.bak-rebuild` |
| `HandwriteAI/_p2_normalize_ink.py` | binarize + width-normalize library to 1.91px native |
| `HandwriteAI/styles/profile_002.labeled/` | live library (69 chars / 756 glyphs); backups `.bak-rebuild`, `.bak-normalize` |
| `HandwriteAI/styles/_p2_stage/` | staged raw sheet crops + `staged.json` |
| `HandwriteAI/styles/profile_002.style` | writer features (thickness_px=1.91 — the target source) |
| `HandwriteAI/convert.py` | CLI: `--profile 002 --mode labeled --seed 7 --text "..."` |

**Pipeline order (rebuild from scratch):** `_p2_sheet_reharvest.py` → `_p2_manifest_rebuild.py` → `_p2_normalize_ink.py` → render.
