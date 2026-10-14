---
module: "handwrite-ai"
topic: "HandwriteAI Profile 1 — original hand, 19-letter library"
tags: [handwrite-ai, handwriting, renderer, glyphs, profile-1]
last_updated: "2026-10-15"
confidence: high
description: "Profile 1 of HandwriteAI (the original user_001 hand, active profile): 19 letters / 1137 glyphs exact-letter library, font+labeled+buckets render paths, full history and known issues. Measured 2026-10-15."
---

## For future agent

Profile 1 is the **original** HandwriteAI profile (user_001 hand, renamed 2026-10-10) and the current `active` one in `profiles.json`. It renders by pasting real ink crops for the 19 enrolled letters; everything else (c h j k q x z, digits, most punctuation) falls back to a drawn font cell with a warning. **Functional, not actively developed** — Profile 2 is the current workhorse (see [[handwrite-ai-profile2]]). When resuming Profile 1 work: enroll the missing letters via `enroll.py`, then re-run `_verify.py` gates before/after.

---

## Library state (measured 2026-10-15)

- `styles/profile_001.labeled/` — manifest version `0.2-labeled`: **19 chars / 1137 glyphs / 1137 metrics**.
- **Present:** `a b d e f g i l m n o p r s t u v w y`. **Missing (font fallback):** `c h j k q x z` + all digits + `. , ! ? ; : ' " ( ) -`.
- Top pools: e 355, i 253, n 66, a 65, r 58, d 58, o 55, b 45, p 42, s 25, m 26, l 24, v 20, f 7, w 12, u 15, t 7, g 2, y 2. q stats: min .05 / median .36 / max 1.0 (pick weights q⁴).
- `styles/profile_001.glyphs/` — 3580 source harvest crops (re-clusterable).
- `styles/profile_001.clusters/` — k=64 clusters; **26 labeled**: v i i y u p i a r n e y w d b l g m e o o e e t f r s (contact sheets `cluster_NNN.png` + `_all`/`_idx` variants).
- Style features (`styles/profile_001.style`): `thickness_px=1.91`, `glyph_h_median=26`, `glyph_w_median=21`, `ligature_pct=24.7`, `slant_deg=0.0` (high conf), `n_lines=156`, `n_components=3995`, `baseline_sag_px=334`.

## Render paths (`convert.py --mode`)

| Mode | Renderer | Behavior |
|---|---|---|
| `font` | `render_text_image` | Correct letters, font skeleton + slant/shear. Fast, uniform. |
| `labeled` | `render_labeled` (inference.py ~686) | **Exact letters**: pastes enrolled crops, q⁴-weighted pick per occurrence. Missing chars → drawn font cell + warning. |
| `buckets` | `render_with_glyphs` (inference.py ~407) | Nearest-bucket retrieval: real ink but **wrong letters possible**. Kept for comparison; `auto` never picks it. |
| `auto` | — | `labeled` if enrolled else `font`. |

## History (git log + PLAN.md)
- **7d3bf72** — initial build: font+glyph+labeled renderers, enrollment, cluster labeling.
- **52c98b3** — post-paste welds in font path; auto-never-picks-buckets; cluster labeling tab 6 (Gradio).
- **874a3c0** — y/o/m/g prunes; g ink restoration; y descender variation (split at baseline, scale 0.4–1.0 at render); love-note regression test.
- **79767aa** — g restore, l/b/v prune, t/f/s/r harvest from unlabeled clusters.
- **4a0afa4** — alignment fix pass: bb manifest / i-dot / w-r advance / durability. Cuneiform render quality improved. Profile system v0.3.
- **cda988a** — polish pass: variant demotes (t_006/t_004/p_019/p_030), jitter tightening, `--width` landscape, `load_style` hardening, font-fallback warning.
- **e-pool hygiene (2026-10-12)** — closure metric showed 18.2% of e-picks were open (c-like) variants; 93/355 crops capped to q≤0.10 (→0.05% pick-weight). Manifest-only, backup `manifest.json.bak-e-prune`, reversible.

## Known issues
- **"systems" reads "sysrems"** — t-e weld artifact; residual, low priority.
- **"Organ" g reads ç-ish** — g pool has 2 variants; needs paper enrollment.
- Missing letters/digits/punctuation → font fallback (expected until enrolled).
- **Buckets path has the legacy sc-gated erosion** (inference.py ~558–569: fixed 3×3 erode when scale>2.2 / cross-erode when >1.35) — same bug class as Profile 2's; unaddressed (buckets is not recommended for output anyway).
- **Pools are NOT width-normalized** — only Profile 2's library went through `_p2_normalize_ink.py`; Profile 1's cluster-vs-sheet weight difference is unmeasured/untreated.

## Verification
- `_verify.py` gates: lovenote, prose, gate 7/11/23/42 — last full pass 2026-10-13 (Profile 2 era; gates cover the shared layout engine).
- Smoke render 2026-10-15: `--profile 001 --mode labeled` pangram renders enrolled letters in real ink, fallback for `chjkqxz` as designed.

## File map
| Path | Role |
|---|---|
| `HandwriteAI/inference.py` | all three renderers; `load_labeled` ~604; buckets erosion ~558 |
| `HandwriteAI/enroll.py` | `enroll.py sheet` / `enroll.py build photo.jpg` — enrollment |
| `HandwriteAI/cluster.py` | cluster labeling (tab 6); contact sheets |
| `HandwriteAI/styles/profile_001.labeled/` | live library (19 chars / 1137 glyphs) |
| `HandwriteAI/styles/profile_001.glyphs/` | 3580 source crops |
| `HandwriteAI/styles/profile_001.clusters/` | 64 clusters, 26 labeled |
| `HandwriteAI/styles/profile_001.style` | writer features |
| `HandwriteAI/convert.py` | CLI; `--mode font/labeled/buckets/auto` |
