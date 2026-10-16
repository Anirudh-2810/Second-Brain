---
module: "handwrite-ai"
topic: "HandwriteAI Profile 2 — exact-letter handwriting renderer (WIP)"
tags: [handwrite-ai, handwriting, renderer, glyphs, profile-2, wip]
last_updated: "2026-10-17"
confidence: high
description: "Profile 2 of HandwriteAI (E:\Brain\Second-Brain\HandwriteAI): exact-letter renderer pasting the user's real ink crops. Session log 2026-10-14→17: pool rebuild, ink normalization, FULL pool replace from the owner's new photo sheet, component-based re-harvest fixing floating/detached descenders, then fixed landscape 3500x1800 pages with pagination. STATUS: working — descenders seated, landscape output, verified render 2026-10-17."
---

## For future agent

Profile 2 renders text by pasting the user's real handwritten glyph crops. **Since 2026-10-15 the pool is sheet-only: 1 variant per char (74 crops, 71 chars), harvested from the owner's photo `C:\Users\Asus\Pictures\Screenshots\Screenshot 2026-10-15 150355.png`** (370x621, blue ink, A-Z a-z 0-9 + % , \ - = + ×). Full-replace decision by owner (was sheet+clusters). Missing chars: `.` and `/` (font fallback; `/` was on the OLD 2026-10-13 sheet, not the new one). All library data is gitignored (regenerable); the scripts that build it are untracked in the repo. When resuming: read this page top-to-bottom, check `wiki/log.md` for the 2026-10-15 entry, then re-render the verification texts before changing anything.

---

## What Profile 2 is

- `HandwriteAI` — local handwriting renderer (PIL + numpy + cv2, no ML inference needed for this mode).
- `--mode labeled` → `render_labeled()` in `inference.py`: each character pastes one enrolled variant of THAT character; missing chars fall back to a drawn font cell.
- Library: `styles/profile_002.labeled/` (manifest.json + 74 crop PNGs, version `0.2-labeled`, sheet-only since the 2026-10-15 full replace). Loader `load_labeled()` (inference.py ~604) reads manifest `chars` + per-file `metrics {bb, q}`; pick weights = `q^4` (moot with 1 variant/char).
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

### 5. V2 sheet enrollment — FULL POOL REPLACE (2026-10-15, done)
Owner fed a new photo sheet with **everything**: caps A-Z (3 rows), lowers a-z (3 rows), digits 1-9+10, symbols `% , \ - = + ×` (comma-separated), and asked for it to be "the letter preset". Pipeline retargeted and re-run end to end:
- **`_p2_sheet_reharvest2.py`** (new): SRC = `Screenshot 2026-10-15 150355.png`; thr `dark<140` (photo — the old 110 was screenshot-tuned); `LEFT=0` (no UI chrome). 8 bands probed exactly: R1 (14,51) ABCDEFGHI, R2 (52,116) JKLMNOPQR — R1/R2 boundary is clean at row 51/52 (J/R top bars start at 52, A's true bottom is 51) — R3 (127,168), R4 (188,257) abcdefgh (g tail to 256), R5 (258,301) ijklmnop, R6 (300,357) qrstuvwxyz (starts below j hook), R7 (365,422) `12345678910` (**`10` segments into `1`+`0`** — 11 cells), R10 (536,569) punct: 11 cells, symbol/comma pairs split at `GAP_PUNCT=2` (7 merges them). Rows `11,12,…,17,` and `18,19,20` SKIPPED (redundant multi-digit groups). Result: **69 chars / 74 crops, all 8 band counts exact, zero mismatches.**
- **Contact-sheet QA** (visual): all crops clean — i/j dots attached in-cell, g/y/q tails whole, no band bleed. `strip_edge_junk` unchanged.
- **`_p2_manifest_rebuild.py --replace`**: new flag drops ALL `cNN_*`/`enr_*` refs (683 dropped), pools = sheet crops only, all metrics recomputed (`baseline_frac` descender logic unchanged). Backup `manifest.json.bak-rebuild2`. Result: 71 chars / 74 glyphs, 0 cluster chars. **`/` is now missing** (was on the old sheet, not the new one) → font fallback, same as `.`.
- **`_p2_normalize_ink.py`**: the new sheet is natively uniform — 73/74 crops measured 1.91±0.23 BEFORE normalizing (med=p10=p90=1.91); only 1 crop changed. The old bimodal-pool problem (1.91 vs 2.74/3.82) is gone by construction (one pen, one photo). Fresh backup `.bak-normalize`; old one renamed `.bak-normalize-v1`.
- **`THICK_SCALE` unchanged (0.75 → 4.30px)** — verified on new pools, no retune needed.

## Verification (2026-10-15)
- Render: `python convert.py --profile 002 --mode labeled --seed 7 --text "..."` (outputs/v2_*.png).
- **V2 renders (post-replace):** pangram, full caps, digits `0123456789 2026 10 11 12`, punct `100% off, tax = net + fee × 2.`, descender words (`jump gypsy queen yoga project pages`), 6-line passage — **all legible, stroke weight uniform page-wide** (the "very uneven" complaint is fixed). `.` renders as font fallback (warning confirms, expected). i dots attached; g/y/q tails whole.
- V1 renders (pre-replace): line-level stroke med 4.65px, std 0.32, range [3.82, 4.65].
- Glyph-component stats remain noisy (i-dots, welds, junctions dominate) — trust line-level stats + eyes.

### 6. Component-based re-harvest — floating/detached descenders (2026-10-16, done)
**Symptom:** in the 2026-10-15 V2 renders, `y h j` floated above the baseline and `g/y` tails detached as stray strokes below the line (owner report). Root causes, both in harvest, not inference:
- **Fixed y-bands clip overlapping rows.** The three lowercase rows (a-h / i-p / q-z) are ONE connected ink block on the photo (sheet rows 186–357); so are the caps rows. A fixed band cuts letters whose ascender/descender crosses the nominal gap: p's bowl top (rows 246–262) was clipped by the `ijklmnop` band top (258); j's body/hook (rows 283–316) clipped by the band bottom (301). Expanding the band by a margin then grabbed the *neighbouring* row's letter at the same x (j vs r), so that fix was abandoned.
- **Wrong `bb` from the old descender heuristic** (`baseline_frac` = largest wide row-run), plus the `_shrink_descender` y-tail scale in inference.

**Fix — the harvester (`_p2_sheet_reharvest2.py`) is now COMPONENT-BASED:**
1. `cv2.connectedComponentsWithStats` (8-conn) on the whole sheet.
2. `column_cells` still segments each band into letter columns (unchanged); each cell only says *which* component is the letter.
3. `pick_comp` = component with the most ink in the cell columns × band rows → then take that component's **FULL** vertical extent (no clipping).
4. `gather` adds nearby small comps in the same columns (i/j dots, E/F bars) with a module-level `DOT_ABOVE/DOT_BELOW` window.
5. **`bb` from a per-row least-squares fit** of non-descender ink bottoms (the photo is rotated, slope ≈ −0.09…−0.13 row/px): a descender's baseline = the fitted baseline at its x; non-descenders keep ink-bottom/h. `bb` is written to a new `styles/_p2_stage/staged_meta.json` and consumed by `_p2_manifest_rebuild.py` (no longer recomputed there).
- Descender set widened to `{g,j,p,q,y,f}` (f is a real descender in this hand); `J`,`Q` use the fit too.
- `_p2_normalize_ink.py` **skipped** for V2 (sheet is natively uniform 1.91px; it only damaged p's bowl earlier).
- **`inference.py`:** removed the y tail-shrink (`_shrink_descender` on `y`, `lrng.uniform(0.4,1.0)`) — owner chose "writer-authentic" (keep the full tail); the `t` safety-net shrink stays.
- Result: **69 chars / 74 crops**, all 8 band counts exact; only the overlapping-row crops changed (L/M etc. byte-identical). Every crop audited: tight top & bottom; multi-component crops are only `% 5 E F i j` (all legitimate dots/bars).
- Verified renders 2026-10-16: `outputs/v3_pangram`, `v3_descenders`, `v3_passage`, `v3_punct`, `v3_caps` — all legible, **descenders seated on the baseline, tails attached**.

## Still to do
1. **Aesthetic tuning** — `THICK_SCALE` is the knob; owner judges by eye.
2. **Caps-line joins** — `ABCDEFGHIJKLMNOPQRSTUVWXYZ` runs slightly blobby at welds (pre-existing joining behavior, not a thickness bug).
3. **More variants per letter** — NOW the top polish item: pool is 1 variant/char, so repeated letters paste identically. If the owner wants natural variation, enroll a SECOND sheet (or harvest variants from notes pages) and merge — same pipeline, `--replace` becomes default merge.
4. **Profile 1 parity** — `render_with_glyphs` (buckets path) still has the legacy sc-gated erosion; same bug class, out of scope so far.
5. **Commit** — `_p2_*.py` scripts + `styles/_p2_stage/` (incl. `staged_meta.json`). `.labeled/` + `outputs/` gitignored by design. V2 enrollment (`dca41ee`) + backups (`bb7c11d`) committed; the 2026-10-16 descender fix is the pending commit.

Resolved (2026-10-15): pool-replace item done (full replace, owner's call); degenerate-cluster-crops item moot (clusters dropped).

## Page geometry — landscape 3500×1800 + pagination (2026-10-17)

Owner request: the old output was a tall vertical strip (`width=1600`, height = `line_h*lines + 140`). Now every renderer produces **fixed landscape pages of 3500×1800** and paginates when the text is taller than one page.

- **Signature:** `render_text_image` / `render_with_glyphs` / `render_labeled` take `width=3500`, new `page_h=1800` (kills the auto-grow), and **return `List[Image.Image]`** (one per page; a single page is still a 1-element list). `page_h=None` restores the old single auto-height strip.
- **Pagination:** `lines_per_page = (page_h - 140) // line_h`. For `line_h = target_h*2.8 = 157` (labeled + buckets at `target_h=56`) that is **10 lines/page**; the font renderer (`line_h = font_size*2.1 = 121`) fits **13 lines/page**. The draw loop is **byte-identical** to before — only the canvas is swapped at page boundaries (`li % lines_per_page == 0`), so glyph ink, jitter, welds, word gaps, and per-line seeds are unchanged (owner constraint: "do not change how the words look").
- **Export:** `export_outputs` now returns `{format: [paths]}`. PNG/SVG emit one file per page (`…-p1.png`, `-p2`… when multi-page; the un-suffixed name when single). PDF is always **one multi-page file** (reportlab `showPage()` per page; PIL `save_all`+`append_images` fallback).
- **CLI:** `python convert.py … --width 3500 --page-h 1800` (both defaults now). `--page-h 0` = old single strip. Prints `pages: N at 3500x1800`.
- **Gradio:** Generate previews page 1 and reports "N page(s) 3500x1800"; Download exports all pages.
- **Verified 2026-10-17:** labeled short → 1 page; long 6-para → 3 pages × 3500×1800; `page_h=None` → 3500×3728 strip; font → 3500×1800; buckets → 2 pages; export → 3 PNGs + 1 three-page PDF (pypdf). CLI + Gradio handlers end-to-end OK.
- **Manual verification:** rendered look unverified by agent — eyeball the output PNGs.

## File map
| Path | Role |
|---|---|
| `HandwriteAI/inference.py` | `render_labeled`, `_match_thickness`, `THICK_SCALE` (~26), `load_labeled`; all three renderers take `width=3500, page_h=1800` and return `List[Image]` (landscape pagination) |
| `HandwriteAI/_p2_sheet_reharvest.py` | V1 band re-harvest (2026-10-13 screenshot), ord-safe names, left-expansion, `strip_edge_junk` |
| `HandwriteAI/_p2_sheet_reharvest2.py` | V2 harvest (2026-10-15 photo sheet) — **component-based (2026-10-16)**: cv2 CCs, full-extent crops, per-row baseline-fit `bb` → `staged_meta.json` |
| `HandwriteAI/_p2_manifest_rebuild.py` | merge clusters+sheet OR `--replace` (sheet-only), drop enr, metrics (reads `bb` from `staged_meta.json`), `.bak-rebuild` / `.bak-rebuild2` |
| `HandwriteAI/_p2_normalize_ink.py` | binarize + width-normalize library to 1.91px native (**skipped for V2** — sheet already uniform) |
| `HandwriteAI/styles/profile_002.labeled/` | live library (71 chars / 74 glyphs, sheet-only); backups `.bak-rebuild2`, `.bak-normalize`, `.bak-normalize-v1` |
| `HandwriteAI/styles/_p2_stage/` | staged V2 raw sheet crops + `staged.json` + `staged_meta.json` (per-crop `top`, `cx`, `band`, `bb`) |
| `HandwriteAI/styles/profile_002.style` | writer features (thickness_px=1.91 — the target source) |
| `HandwriteAI/convert.py` | CLI: `--profile 002 --mode labeled --seed 7 --text "..."` (+ `--width 3500 --page-h 1800` landscape defaults, `--page-h 0` = strip) |

**Pipeline order (rebuild from scratch):** `_p2_sheet_reharvest2.py` → `_p2_manifest_rebuild.py --replace` → render. (`_p2_normalize_ink.py` is skipped for the V2 sheet — it is natively uniform.)
