# HandwriteAI - build map (v0.1 MVP)

For personal note digitization only. Offline, CPU-only, no data leaves device.

## Layout
```
HandwriteAI/
  requirements.txt
  features.py        # deskew/binarize/lines/slant/thickness/baseline/ligatures
  models.py          # StyleEncoder CNN + StrokeGenerator Transformer+LSTM
  train_fine_tune.py # Phase1 IAM stub / Phase2 fine-tune / Phase3 synthetic loop
  inference.py       # font + buckets + LABELED renderers, PNG/PDF/SVG export
  enroll.py          # alphabet-sheet enrollment -> .labeled library (paper path)
  cluster.py         # shape clustering + cluster labeling -> .labeled (no-paper path)
  glyphs.py          # unlabeled harvest + sanitize (slab guards)
  convert.py         # CLI: --mode auto (=labeled if present else font)
  gradio_ui.py       # 6-tab flow (tab 6 = cluster labeling), localhost:7860
  models/            # encoder_iam.pth, encoder_finetuned.pth
  styles/            # user_001.style + user_001.labeled/ + user_001.clusters/
  outputs/           # generated files
  data/              # enrollment-sheet.pdf (print me)
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
B. No paper: UI tab 6 builds shape clusters from uploads -> label each ~10 min
   -> Finish writes `styles/user_001.labeled/` (64 clusters, numpy KMeans,
   intra-NCC 0.49 vs inter 0.19).

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
- MVP renderer produces legible slant/thickness/baseline-styled output immediately;
  the LSTM stroke generator refines glyphs once trained weights exist.
- SVG v0.1 embeds raster (true stroke-vector lands with generator v2).
- IAM pre-training: `python train_fine_tune.py --pretrain --iam-root data/iam --epochs 3`
- Success targets: feature MSE < 0.05, spacing corr > 0.85, <5s/100 chars CPU.

## Ethics (must-read)
Legitimate: personal notes, stationery, accessibility, practice, creativity.
Prohibited: reproducing others' coursework, bypassing handwritten requirements,
deceptive docs, unlicensed font commercialization, academic dishonesty.
