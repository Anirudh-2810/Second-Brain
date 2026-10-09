"""
HandwriteAI - PyTorch models: StyleEncoder (CNN) + StrokeGenerator (Transformer+LSTM).
CPU-only inference. Imports torch lazily so UI works without torch installed.
"""
from __future__ import annotations
from typing import Optional

try:
    import torch
    import torch.nn as nn
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False
    torch = None  # type: ignore
    nn = None  # type: ignore


if HAS_TORCH:
    class StyleEncoder(nn.Module):
        """CNN: glyph image (1xHxW) -> 128-dim style vector z."""
        def __init__(self, style_dim: int = 128):
            super().__init__()
            self.features = nn.Sequential(
                nn.Conv2d(1, 32, kernel_size=3, padding=1),
                nn.BatchNorm2d(32),
                nn.ReLU(inplace=True),
                nn.Conv2d(32, 64, kernel_size=3, padding=1),
                nn.BatchNorm2d(64),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(2),
                nn.Conv2d(64, 128, kernel_size=3, padding=1),
                nn.BatchNorm2d(128),
                nn.ReLU(inplace=True),
                nn.AdaptiveAvgPool2d((1, 1)),
            )
            self.fc = nn.Sequential(
                nn.Flatten(),
                nn.Linear(128, 512),
                nn.ReLU(inplace=True),
                nn.Dropout(0.2),
                nn.Linear(512, style_dim),
            )
            self.style_dim = style_dim

        def forward(self, x):
            return self.fc(self.features(x))

    class StrokeGenerator(nn.Module):
        """
        Autoregressive stroke generator.
        text_tokens: (B, T) long, z: (B, style_dim).
        Output per step: (dx, dy, pen_up_logit, pressure, end_logit) -> (B, T, 5).
        """
        def __init__(self, style_dim: int = 128, vocab: int = 128,
                     d_model: int = 256, nhead: int = 8, nlayers: int = 4):
            super().__init__()
            self.style_dim = style_dim
            self.char_emb = nn.Embedding(vocab, d_model)
            enc_layer = nn.TransformerEncoderLayer(
                d_model=d_model, nhead=nhead, dim_feedforward=512,
                dropout=0.1, batch_first=True)
            self.transformer = nn.TransformerEncoder(enc_layer, num_layers=nlayers)
            self.lstm = nn.LSTM(input_size=d_model + style_dim, hidden_size=256,
                                num_layers=2, batch_first=True, dropout=0.1)
            self.out = nn.Sequential(
                nn.Linear(256, 256), nn.ReLU(inplace=True),
                nn.Linear(256, 5),
            )

        def forward(self, text_tokens, z):
            # text_tokens: (B,T), z: (B,D)
            e = self.char_emb(text_tokens)          # (B,T,d)
            h = self.transformer(e)                 # (B,T,d)
            zexp = z.unsqueeze(1).expand(-1, h.size(1), -1)
            lstm_in = torch.cat([h, zexp], dim=-1)
            o, _ = self.lstm(lstm_in)
            return self.out(o)                      # (B,T,5)

    def build_models(style_dim: int = 128):
        return StyleEncoder(style_dim), StrokeGenerator(style_dim)

    def save_checkpoint(path: str, encoder, generator=None, extra: Optional[dict] = None):
        payload = {"encoder": encoder.state_dict()}
        if generator is not None:
            payload["generator"] = generator.state_dict()
        if extra:
            payload["extra"] = extra
        torch.save(payload, path)

    def load_encoder(path: str, style_dim: int = 128):
        enc = StyleEncoder(style_dim)
        sd = torch.load(path, map_location="cpu")
        if isinstance(sd, dict) and "encoder" in sd:
            sd = sd["encoder"]
        enc.load_state_dict(sd)
        enc.eval()
        return enc
else:
    class StyleEncoder:  # type: ignore
        def __init__(self, *a, **k):
            raise RuntimeError("torch not installed: pip install torch torchvision")
    class StrokeGenerator:  # type: ignore
        def __init__(self, *a, **k):
            raise RuntimeError("torch not installed: pip install torch torchvision")
    def build_models(*a, **k):
        raise RuntimeError("torch not installed")
    def save_checkpoint(*a, **k):
        raise RuntimeError("torch not installed")
    def load_encoder(*a, **k):
        raise RuntimeError("torch not installed")
