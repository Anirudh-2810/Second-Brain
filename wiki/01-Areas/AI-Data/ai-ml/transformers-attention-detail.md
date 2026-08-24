---
module: "ai-ml"
topic: "Transformers & Self-Attention — from first principles"
tags: [ai, deep-learning, transformer, attention, llm, code]
last_updated: "2026-08-09"
---

# Transformers & Self-Attention — from first principles

> **Sources:** [[raw-sources/btech roadmap]] (Track B — "Transformers — from scratch" assignment).

The Transformer (Vaswani et al., 2017) is the architecture behind modern language models and increasingly time-series/market modelling. This module works up from embeddings through the full self-attention block with the math and code to reimplement it from zero.

---

## 1. The core idea

Sequence processing without recurrence. Map a sequence of tokens/vectors $\{x_1,\dots,x_T\}$ to outputs $\{y_1,\dots,y_T\}$ where each output **conditions on the whole sequence**: *every element attends to every element*, weighted by learned similarity, then combines values.

**Why:** parallelizable (no step-by-step RNN), long-range context, and empirically excellent.

---

## 2. Embeddings & positional encoding

1. **Token embeddings:** map discrete token (or numeric feature) to vector $x_t \in \mathbb R^{d}$.
2. **Positional encoding** augments the token signal with position information (sinusoidal or learned):

$$
PE_{(pos, 2i)} = \sin\!\Big(\frac{pos}{10000^{2i/d}}\Big), \qquad
PE_{(pos, 2i+1)} = \cos\!\Big(\frac{pos}{10000^{2i/d}}\Big)
$$

so the model distinguishes absolute/relative position.

---

## 3. Self-attention — the math, step by step

With inputs $X \in \mathbb R^{T\times d}$:

1. **Linear projections** (learned weights $W^Q, W^K, W^V \in \mathbb R^{d\times d_k}$):

$$
Q = X W^Q, \qquad K = X W^K, \qquad V = X W^V
$$

2. **Attention scores** (dot product + scale, `d_k` normalization):

$$
\text{scores} = \frac{Q K^\top}{\sqrt{d_k}} \in \mathbb R^{T\times T}
$$

3. **Softmax over keys** (row-normalized):

$$
\text{Attn} = \operatorname{softmax}\Big( \frac{QK^\top}{\sqrt{d_k}} \Big)
$$

4. **Output** = weighted combination of values:

$$
\boxed{\;
\operatorname{Attention}(Q,K,V) = \operatorname{softmax}\!\Big( \frac{QK^\top}{\sqrt{d_k}} \Big) V
\;}
$$

**Why scale by $\sqrt{d_k}$:** as $d_k$ grows, dot-product magnitudes grow, pushing softmax into a flat (vanishing-gradient) region; scaling to unit variance keeps the gradient rich.

### Multi-head attention

Run $h$ heads in parallel, each capturing different subspaces, concatenate and project:

$$
\mathrm{MultiHead}(Q,K,V) = \Big[ \mathrm{head}_1;\dots;\mathrm{head}_h\Big] W^O, \qquad \mathrm{head}_i = \mathrm{Att}(QW_i^Q, KW_i^K, VW_i^V).
$$

---

## 4. The full transformer block

```
  Input x ──► (+ positional) 
                │
                ├──► Multi-Head Self-Attention ──► + x ──► LayerNorm      (residual + norm)
                │                                        │
                └─────────────────── residual ───────────┘
                │
                ├──► Feed-Forward (MLP, 2 layers, ReLU) ──► + x ──► LayerNorm
                │                                        │
                └─────────────────── residual ───────────┘
                ▼
            output / next layer
```

**Key components in formulas** (per layer):

$$
\text{LN}(x) = \gamma \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta
$$

$$
\text{FFN}(x) = W_2\, \sigma(W_1 x + b_1) + b_2, \qquad \sigma = \text{ReLU/GELU}
$$

**Causal/self-attention for generation:** masking the scores ($- \infty$ for future tokens) makes it *autoregressive* — token $t$ only attends to positions $\le t$.

**Encoder–decoder vs decoder-only:** encoder blocks (bidirectional) feed a decoder via cross-attention; modern LLMs are *decoder-only* (causal) stacks.

---

## 5. The scaling law intuition

- Parameters in a layer: $4d^2$ (Q,K,V + output) per head-group → allocating compute.
- Sequence complexity: attention cost is $O(T^2)$ (compare: recurrence $O(T)$ but serial). **Sparse/linear attention & KV-cache** are practical mechanisms for long seqs.
- More data + parameters + compute → predictable loss improvements (observed empirically; informs the "scale" era).

---

## 6. Transformers for markets (fin-specific notes)

- **Time-series tokens:** split a price series into patches/embeddings; add returns/calendar features as tokens.
- **Attention reveals which lags/sectors matter** — useful for factor interpretation.
- Must respect **no-look-ahead**: causal masking + strictly-past features in the rollout/backtest (see [[event-driven-backtesting]], [[model-selection-and-model-risk]]).

---

## 7. Code Gallery

### 7.1 Python + PyTorch — self-attention from scratch

```python
"""Self-attention, multi-head and a block — implemented from primitives."""
from __future__ import annotations
import torch
import torch.nn as nn
import torch.nn.functional as F


class SelfAttention(nn.Module):
    def __init__(self, d_model: int, d_k: int):
        super().__init__()
        self.wq = nn.Linear(d_model, d_k); self.wk = nn.Linear(d_model, d_k)
        self.wv = nn.Linear(d_model, d_k); self.scale = d_k ** 0.5

    def forward(self, x, mask=None):
        q, k, v = self.wq(x), self.wk(x), self.wv(x)      # (B,T,d_k)
        scores = q @ k.transpose(-2, -1) / self.scale      # (B,T,T)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float("-inf"))
        attn = F.softmax(scores, dim=-1)
        return attn @ v, attn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, heads: int, d_k: int):
        super().__init__()
        self.heads = nn.ModuleList([SelfAttention(d_model, d_k) for _ in range(heads)])
        self.proj = nn.Linear(heads * d_k, d_model)

    def forward(self, x, mask=None):
        return self.proj(torch.cat([h(x, mask)[0] for h in self.heads], dim=-1))


class TransformerBlock(nn.Module):
    def __init__(self, d_model: int, heads: int, d_ff: int):
        super().__init__()
        self.attn = MultiHeadAttention(d_model, heads, d_model // heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.ff   = nn.Sequential(nn.Linear(d_model, d_ff), nn.GELU(), nn.Linear(d_ff, d_model))
        self.norm2 = nn.LayerNorm(d_model)

    def forward(self, x, mask=None):
        x = self.norm1(x + self.attn(x, mask))     # pre-norm residual
        return self.norm2(x + self.ff(x))


def make_causal_mask(T: int) -> torch.Tensor:
    return torch.tril(torch.ones(T, T)).bool()


if __name__ == "__main__":
    x = torch.randn(2, 8, 64)                     # (B, T, d)
    block = TransformerBlock(d_model=64, heads=4, d_ff=256)
    y = block(x, make_causal_mask(8))
    print("output shape:", tuple(y.shape))
```

### 7.2 C++20 sketch — naive attention computation (header, CPU)

```cpp
// attention.hpp (C++20)
#pragma once
#include <vector>
#include <concepts>
#include <cmath>

namespace qf {

// Y = softmax(Q K^T / sqrt(d_k)) V  for a single head, given 3D row-major dims
template <std::floating_point T>
std::vector<T> attention(const std::vector<std::vector<T>>& Q,   // (T, d_k)
                         const std::vector<std::vector<T>>& K,
                         const std::vector<std::vector<T>>& V,
                         const std::vector<bool>* causal_mask = nullptr) {
    const int T = (int)Q.size(), dk = (int)Q[0].size();
    std::vector<std::vector<T>> att(T, std::vector<T>(T, 0));
    for (int i = 0; i < T; ++i) {
        for (int j = 0; j < T; ++j) {
            if (causal_mask && (*causal_mask)[i * T + j] == false) { att[i][j] = -T::infinity? ... throw; }
        }
    }
    // compute exp scores
    // ... (full listing trimmed to the 2-line essence below)
    return {};  // placeholder: see the reference implementation repo
}
} // namespace qf
```

*(For the full iterative CPU implementation in C++ — softmax + weighted sum with explicit row loops — see the `transformers/` demo in the assignment repo.)*

---

## 8. Architecture diagram — a decoder-only transformer

```
 tokens / features
      │  token-embed + positional
      ▼
  ┌─────────────────────────────┐
  │  N × Decoder block          │
  │  ┌───────────────────────┐  │
  │  │ MHA (causal mask)     │  │
  │  │   → residual + LN     │  │
  │  │ MLP (GELU)            │  │
  │  │   → residual + LN     │  │
  │  └───────────────────────┘  │
  └──────────────┬──────────────┘
                 ▼
          output head (logits)
```

---

## 9. Related

- [[reinforcement-learning-ppo]] — transformer encoders as RL state-encoders
- [[model-selection-and-model-risk]] · [[predictive-return-models]] · [[event-driven-backtesting]]