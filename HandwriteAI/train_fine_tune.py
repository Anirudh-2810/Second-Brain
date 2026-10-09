"""
HandwriteAI - training pipeline.
Phase 1: pre-train encoder (IAM stub - plug in real IAM loader when dataset present)
Phase 2: fine-tune on user pages -> styles/user_XXX.style (JSON: z + features)
Phase 3: synthetic loop (optional refinement)

Usage:
  python train_fine_tune.py --samples page1.png page2.pdf --out styles/user_001.style --epochs 2
  python train_fine_tune.py --pretrain --iam-root data/iam --epochs 3 --out models/encoder_iam.pth
"""
from __future__ import annotations
import os, json, argparse, random
import numpy as np
from PIL import Image

from features import load_sample_images, analyze_pages, extract_lines, normalize_height, binarize

try:
    import torch
    import torch.nn as nn
    from models import StyleEncoder, StrokeGenerator, save_checkpoint
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False


def compute_style_vector_torch(encoder, line_images, style_dim=128):
    """Mean-pool encoder outputs over line crops -> z (128,)."""
    import torch
    encoder.eval()
    vecs = []
    with torch.no_grad():
        for ln in line_images[:64]:
            arr = normalize_height(ln if isinstance(ln, np.ndarray) else np.array(ln))
            # to tensor 1x1xHxW, scale 0..1, ink=1
            t = torch.from_numpy((255 - arr).astype(np.float32) / 255.0).unsqueeze(0).unsqueeze(0)
            # pad/crop width to 256 for batching
            _, _, h, w = t.shape
            if w < 256:
                pad = torch.zeros(1, 1, h, 256 - w)
                t = torch.cat([t, pad], dim=-1)
            else:
                t = t[:, :, :, :256]
            vecs.append(encoder(t).squeeze(0))
    if not vecs:
        return np.zeros(style_dim, dtype=np.float32)
    z = torch.stack(vecs).mean(dim=0)
    return z.cpu().numpy()


def compute_style_vector_fallback(images) -> np.ndarray:
    """Deterministic pseudo-z from image stats when torch unavailable (keeps pipeline working)."""
    rng = np.random.default_rng(42)
    feats = analyze_pages(images)
    seed = np.array([feats.slant_deg, feats.thickness_px, feats.ligature_pct,
                     feats.baseline_sag_px, feats.n_lines], dtype=float)
    # hash stats into a stable 128-dim vector
    base = rng.standard_normal(128).astype(np.float32) * 0.1
    base[0] = feats.slant_deg / 20.0
    base[1] = feats.thickness_px / 5.0
    base[2] = feats.ligature_pct / 100.0
    base[3] = feats.baseline_sag_px / 20.0
    return base


def save_style_profile(out_path: str, z: np.ndarray, feats, meta: dict):
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    payload = {
        "version": "0.1",
        "style_dim": int(len(z)),
        "z": [float(x) for x in z],
        "features": feats.to_dict(),
        "meta": meta,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    return out_path


def load_style_profile(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def finetune_on_user(samples, out_path, epochs=2, lr=1e-4, style_dim=128, device="cpu"):
    images = load_sample_images(samples)
    if not images:
        raise ValueError("No sample images loaded. Provide 2-4 pages (png/jpg/pdf).")
    feats = analyze_pages(images)

    if HAS_TORCH:
        from models import StyleEncoder
        enc = StyleEncoder(style_dim)
        # try load IAM priors if present
        for cand in ("models/encoder_iam.pth", "HandwriteAI/models/encoder_iam.pth"):
            if os.path.exists(cand):
                try:
                    sd = torch.load(cand, map_location="cpu")
                    if isinstance(sd, dict) and "encoder" in sd:
                        sd = sd["encoder"]
                    enc.load_state_dict(sd, strict=False)
                    print(f"Loaded IAM priors from {cand}")
                    break
                except Exception as e:
                    print(f"Could not load {cand}: {e}")
        enc.to(device)
        # Collect line crops as pseudo-batch, reconstruction-style fine-tune:
        # objective = keep z stable + small weight decay (avoids collapse on tiny data).
        # Real stroke-level loss plugs in here once transcribed IAM-style strokes exist.
        lines = []
        for im in images:
            lines.extend(extract_lines(im))
        opt = torch.optim.Adam(enc.parameters(), lr=lr)
        enc.train()
        for ep in range(epochs):
            tot, n = 0.0, 0
            idx = list(range(len(lines)))
            random.shuffle(idx)
            for i in idx[:64]:
                ln = lines[i]
                arr = normalize_height(ln if isinstance(ln, np.ndarray) else np.array(ln))
                t = torch.from_numpy((255 - arr).astype(np.float32) / 255.0).unsqueeze(0).unsqueeze(0).to(device)
                _, _, h, w = t.shape
                if w < 256:
                    pad = torch.zeros(1, 1, h, 256 - w, device=device)
                    t = torch.cat([t, pad], dim=-1)
                else:
                    t = t[:, :, :, :256]
                z = enc(t)
                loss = (z ** 2).mean() * 1e-3  # gentle regularizer; keeps encoder alive on tiny data
                opt.zero_grad()
                loss.backward()
                opt.step()
                tot += float(loss.item())
                n += 1
            print(f"epoch {ep+1}/{epochs} reg_loss={tot/max(1,n):.6f}")
        z = compute_style_vector_torch(enc, lines, style_dim)
        # save encoder snapshot beside style
        ckpt = os.path.join(os.path.dirname(out_path) or ".", "encoder_finetuned.pth")
        try:
            save_checkpoint(ckpt, enc)
            print(f"Saved fine-tuned encoder -> {ckpt}")
        except Exception as e:
            print(f"Checkpoint save skipped: {e}")
    else:
        print("torch not available - using statistical style vector (MVP mode).")
        z = compute_style_vector_fallback(images)

    meta = {"n_samples": len(samples), "epochs": epochs, "lr": lr,
            "device": device, "torch": HAS_TORCH}
    save_style_profile(out_path, z, feats, meta)
    print(f"Saved style profile -> {out_path}")
    print(f"  slant={feats.slant_deg:.1f}deg thickness={feats.thickness_px:.2f}px "
          f"ligatures={feats.ligature_pct:.1f}% lines={feats.n_lines}")
    # accuracy path: harvest real glyph crops alongside the style vector
    try:
        from glyphs import build_library
        lib_dir = os.path.splitext(out_path)[0] + ".glyphs"
        manifest = build_library(samples, lib_dir)
        print(f"Glyph library: {manifest['n_glyphs']} glyphs "
              f"(narrow={manifest['buckets'].get('narrow',0)} "
              f"xheight={manifest['buckets'].get('xheight',0)} "
              f"wide={manifest['buckets'].get('wide',0)} "
              f"tall={manifest['buckets'].get('tall',0)}) -> {lib_dir}")
        if manifest["n_glyphs"] < 200:
            print("WARNING: <200 glyphs — add more sample pages for 0.5-1% accuracy. "
                  "2-4 dense pages ≈ 800-2500 glyphs is the target.")
    except Exception as e:
        print(f"Glyph harvest skipped: {e}")
    return out_path


def pretrain_stub(iam_root, out_path, epochs=3):
    if not HAS_TORCH:
        raise RuntimeError("torch required for pre-training")
    from models import StyleEncoder
    print(f"IAM pre-train stub: root={iam_root} epochs={epochs}")
    print("Plug real IAM line loader here (forms/ + xml). Saving init weights as priors.")
    enc = StyleEncoder(128)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    save_checkpoint(out_path, enc, extra={"iam_root": iam_root, "epochs": epochs})
    print(f"Saved -> {out_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", nargs="*", default=[], help="user page images/pdfs")
    ap.add_argument("--out", default="styles/user_001.style")
    ap.add_argument("--epochs", type=int, default=2)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--pretrain", action="store_true")
    ap.add_argument("--iam-root", default="data/iam")
    ap.add_argument("--device", default="cpu")
    args = ap.parse_args()
    if args.pretrain:
        pretrain_stub(args.iam_root, "models/encoder_iam.pth", args.epochs)
    else:
        if not args.samples:
            ap.error("--samples page1.png page2.pdf ... (2-4 pages) required")
        finetune_on_user(args.samples, args.out, args.epochs, args.lr, device=args.device)


if __name__ == "__main__":
    main()
