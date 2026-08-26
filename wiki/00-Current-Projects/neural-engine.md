---
module: "current-projects"
topic: "Neural Engine — From-Scratch Neural Network Library (NumPy)"
tags: [builds, neural-networks, numpy, from-scratch, adam, rmsprop, dropout, l2-regularization, early-stopping, backpropagation, gradient-descent]
last_updated: "2026-08-26"
confidence: "high"
source: "Desktop/Anirudh/My apps/Neural net 2/neuralnet.py"
description: "Production-grade neural network engine with multiple optimizers (SGD, Adam, AdamW, RMSprop), He/Xavier initialization, dropout, L2 regularization, early stopping, and model serialization. Built from scratch using only NumPy. 497 lines of dense, documented NumPy implementing forward/backward passes, 4 optimizers, and training loop."
---

# Neural Engine — From-Scratch Neural Network Library

> **Source:** `Desktop/Anirudh/My apps/Neural net 2/neuralnet.py` (497 lines)
> **Status:** Complete, production-ready library
> **Dependencies:** `numpy`, `matplotlib` (optional for plotting), `pickle` (serialization)
> **Lines of Code:** 497 (core engine) + 38 (demo)

---

## For future agent
This is a **personal build** — a fully functional neural network library written from scratch in NumPy. It implements modern deep learning primitives (optimizers, regularization, initialization schemes) without PyTorch/TensorFlow. Use as reference for understanding backprop mechanics, optimizer internals, or as a lightweight dependency-free ML engine. Cross-links: [[stock-predictor]] (uses this engine), [[quant-finance/quant-toolkit-and-skills]], [[ai-ml/reinforcement-learning-ppo]].

---

## 1. Architecture Overview

```mermaid
flowchart TD
    subgraph Core[NeuralEngine Core]
        A[__init__] --> B[Layer Registry]
        B --> C[add_layer]
        C --> D[Layer Config Dict]
    end
    
    subgraph Forward[Forward Pass]
        E[forward] --> F[_init_weights]
        F --> G[Layer Loop]
        G --> H[Z = A @ W.T + b]
        H --> I[_activation]
        I --> J[Dropout Mask]
        J --> K[Cache Z, A, Mask]
    end
    
    subgraph Backward[Backward Pass]
        K --> L[backward]
        L --> M[dA = output - y]
        M --> N[Layer Loop Reversed]
        N --> O[dA *= dropout_mask]
        O --> P[dZ = dA * _activation_deriv]
        P --> Q[dW = (dZ.T @ A) / m + L2]
        Q --> R[db = sum(dZ) / m]
        R --> S[_update_weights]
    end
    
    subgraph Optimizers[Optimizer Step]
        S --> T{optimizer}
        T -->|sgd| U[_sgd_update]
        T -->|adam| V[_adam_update]
        T -->|adamw| W[_adamw_update]
        T -->|rmsprop| X[_rmsprop_update]
    end
```

---

## 2. Core Features (Detailed)

| Feature | Implementation Details |
|---------|------------------------|
| **Layer API** | `add_layer(neurons, activation, input_size=None, dropout=None)` — returns `self` for chaining. Stores config dict with: `type='dense'`, `neurons`, `activation`, `input_size`, `dropout`, `W`, `b`, `dW`, `db`, optimizer states (`mW`, `mb`, `vW`, `vb`, `sW`, `sb`) |
| **Activations** | **ReLU:** `max(0, z)` · **LeakyReLU:** `where(z>0, z, 0.01*z)` · **Sigmoid:** `1/(1+exp(-clip(z,-500,500)))` · **Tanh:** `tanh(z)` · **Swish:** `z * sigmoid(z)` · **Linear:** identity. Derivatives implemented in `_activation_deriv` |
| **Initialization** | **He (ReLU/LeakyReLU/Swish):** `scale = sqrt(2/prev_size)` · **Xavier (Sigmoid/Tanh/Linear):** `scale = sqrt(1/prev_size)` · Weights: `randn(neurons, prev_size) * scale` · Biases: `zeros((1, neurons))` |
| **Optimizers** | **SGD:** `W -= lr * dW` · **Adam:** `m = β1*m + (1-β1)*g; v = β2*v + (1-β2)*g²; m̂ = m/(1-β1^t); v̂ = v/(1-β2^t); W -= lr * m̂/(sqrt(v̂)+ε)` · **AdamW:** Adam + `W *= (1 - lr * weight_decay)` · **RMSprop:** `s = β*s + (1-β)*g²; W -= lr * g/(sqrt(s)+ε)` |
| **Regularization** | **L2:** Added to gradient: `dW += λ * W` · **Dropout:** Inverted dropout mask `mask = (rand > rate) / (1-rate)` applied during training only (except output layer) |
| **Training** | Mini-batch GD with shuffling per epoch. Validation split (chronological, not random). Metrics: MSE loss + accuracy (binary: `>0.5`, multiclass: `argmax`). Early stopping on val_loss with patience. |
| **Serialization** | `pickle.dump` of dict: `{layers: [{neurons, activation, dropout, W, b}], optimizer, learning_rate, l2_lambda}`. Load reconstructs architecture then restores weights. |
| **Visualization** | `matplotlib` subplots: Loss (train/val) + Accuracy (train/val) with grid, legends, tight_layout. |
| **Inspection** | `summary()` prints table: Layer | Activation | Neurons | Params. Total params = Σ(W.size + b.size). |

---

## 3. Complete API Reference

### `NeuralEngine.__init__()`
```python
def __init__(
    self,
    learning_rate: float = 0.01,
    optimizer: Literal['sgd', 'adam', 'rmsprop', 'adamw'] = 'adam',
    l2_lambda: float = 0.0,
    dropout_rate: float = 0.0,
    early_stopping_patience: int = 20
):
```
**Optimizer-specific defaults:**
- `adam`: β1=0.9, β2=0.999, ε=1e-8
- `adamw`: β1=0.9, β2=0.999, ε=1e-8, weight_decay=0.01 (hardcoded)
- `rmsprop`: β=0.9, ε=1e-8

### `add_layer()`
```python
def add_layer(
    self,
    neurons: int,
    activation: Literal['relu', 'sigmoid', 'tanh', 'linear', 'leaky_relu', 'swish'] = 'relu',
    input_size: Optional[int] = None,
    dropout: Optional[float] = None
) -> 'NeuralEngine':
```
- `input_size` only needed for first layer (inferred from `X` in `forward`)
- `dropout` overrides instance `dropout_rate` for this layer
- Appends layer dict to `self.layers`, prints confirmation

### `forward()`
```python
def forward(self, X: np.ndarray, training: bool = True) -> np.ndarray:
```
- Sets `self.training_mode = training`
- Calls `_init_weights(X)` if first forward
- Iterates layers: `Z = A @ W.T + b` → `A = activation(Z)` → dropout (if not last layer)
- Caches: `self.cache = {'Z': [], 'A': [X], 'dropout_masks': []}`
- Returns final `A` (predictions)

### `backward()`
```python
def backward(self, X: np.ndarray, y: np.ndarray, output: np.ndarray):
```
- `m = X.shape[0]`
- `dA = output - y` (MSE derivative)
- Reversed layer loop:
  - Apply dropout mask: `dA *= mask`
  - `dZ = dA * activation_deriv(Z, act)`
  - `dW = (dZ.T @ A_prev) / m + λ * W`
  - `db = sum(dZ, axis=0, keepdims=True) / m`
  - Store in layer: `layer['dW']`, `layer['db']`
  - Next `dA = dZ @ W`
- Calls `_update_weights()`

### `fit()`
```python
def fit(
    self,
    X: np.ndarray,
    y: np.ndarray,
    epochs: int = 100,
    batch_size: int = 32,
    val_split: float = 0.2,
    verbose: bool = True,
    plot: bool = True
) -> 'NeuralEngine':
```
**Validation split:** `val_size = int(n * val_split)`; `X_train = X[:-val_size]`, `X_val = X[-val_size:]` (chronological, no shuffle across split)

**Per-epoch:**
1. Shuffle training indices
2. Mini-batch loop: `forward(Xb, training=True)` → `backward(Xb, yb, output)`
3. Compute train metrics on full train set (no dropout)
4. Compute val metrics (if val_split > 0)
5. Early stopping check: `if val_loss < best_val_loss: best = val_loss; patience = 0 else: patience += 1`
6. Print every 10 epochs if verbose
7. Plot if requested

### `predict()`, `evaluate()`, `save()`, `load()`, `summary()`, `plot_training_history()`
Standard implementations as shown in quick start.

---

## 4. Mathematical Details

### Forward Pass (Layer i)
```
Zⁱ = Aⁱ⁻¹ Wⁱᵀ + bⁱ          (A⁰ = X)
Aⁱ = φⁱ(Zⁱ)                  (φ = activation)
Ãⁱ = Aⁱ ⊙ Mⁱ / (1-p)         (Mⁱ ~ Bernoulli(1-p), training only)
```

### Backward Pass (Layer i)
```
δⁱ = (δⁱ⁺¹ Wⁱ⁺¹) ⊙ φ'ⁱ(Zⁱ) ⊙ Mⁱ/(1-p)   (for i < L-1)
δᴸ = (Aᴸ - Y) ⊙ φ'ᴸ(Zᴸ)                  (output layer, MSE loss)

∇Wⁱ = (δⁱ)ᵀ Aⁱ⁻¹ / m + λ Wⁱ
∇bⁱ = Σ δⁱ / m
```

### Optimizer Updates (per parameter θ = W or b)
| Optimizer | State Variables | Update |
|-----------|-----------------|--------|
| **SGD** | — | `θ ← θ - η ∇θ` |
| **Adam** | `m ← β₁ m + (1-β₁)∇θ`, `v ← β₂ v + (1-β₂)∇θ²` | `m̂ = m/(1-β₁ᵗ)`, `v̂ = v/(1-β₂ᵗ)`, `θ ← θ - η m̂/(√v̂+ε)` |
| **AdamW** | Same as Adam | `θ ← θ(1 - η λ_wd)`, then Adam step |
| **RMSprop** | `s ← β s + (1-β)∇θ²` | `θ ← θ - η ∇θ/(√s+ε)` |

---

## 5. Complete Usage Examples

### Binary Classification (XOR)
```python
from neuralnet import NeuralEngine
import numpy as np

engine = NeuralEngine(learning_rate=0.1, optimizer='adam', l2_lambda=0.001)
engine.add_layer(16, 'relu')
engine.add_layer(8, 'relu')
engine.add_layer(1, 'sigmoid')

X = np.array([[0,0], [0,1], [1,0], [1,1]], dtype=np.float32)
y = np.array([[0], [1], [1], [0]], dtype=np.float32)

engine.fit(X, y, epochs=500, batch_size=2, val_split=0.0, verbose=True)
engine.save('xor_model.pkl')

# Evaluate
results = engine.evaluate(X, y)
print(f"Accuracy: {results['accuracy']:.2%}")
for inp, pred, target in zip(X, results['predictions'], y):
    print(f"  {inp} → {pred[0]:.3f} (target: {target[0]})")
```

### Multiclass Classification (Iris-style)
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

data = load_iris()
X, y_raw = data.data, data.target.reshape(-1, 1)
enc = OneHotEncoder(sparse_output=False)
y = enc.fit_transform(y_raw)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

engine = NeuralEngine(learning_rate=0.01, optimizer='adam', l2_lambda=0.001, dropout_rate=0.1)
engine.add_layer(32, 'relu')
engine.add_layer(16, 'relu')
engine.add_layer(3, 'linear')  # Linear for softmax-like output (MSE)

engine.fit(X_train, y_train, epochs=300, batch_size=16, val_split=0.2)

results = engine.evaluate(X_test, y_test)
print(f"Test Accuracy: {results['accuracy']:.2%}")
```

### Regression (Boston Housing-style)
```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = fetch_california_housing()
X, y = data.data, data.target.reshape(-1, 1)

scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

engine = NeuralEngine(learning_rate=0.001, optimizer='adam', l2_lambda=0.01, dropout_rate=0.15)
engine.add_layer(64, 'relu')
engine.add_layer(32, 'relu')
engine.add_layer(1, 'linear')  # Linear output for regression

engine.fit(X_train, y_train, epochs=200, batch_size=32, val_split=0.2)

# Inverse transform for interpretable metrics
preds_scaled = engine.predict(X_test)
preds = scaler_y.inverse_transform(preds_scaled)
actuals = scaler_y.inverse_transform(y_test)
mae = np.mean(np.abs(preds - actuals))
print(f"MAE: ${mae[0]:.2f}k")
```

---

## 6. Internal Architecture Deep Dive

### Layer Dict Structure
```python
layer = {
    'type': 'dense',
    'neurons': 64,
    'activation': 'relu',
    'input_size': 10,           # Set in _init_weights
    'dropout': 0.1,
    'W': np.ndarray(64, 10),    # (neurons, input_size)
    'b': np.ndarray(1, 64),     # (1, neurons)
    'dW': np.ndarray(64, 10),   # Gradient
    'db': np.ndarray(1, 64),
    # Optimizer states:
    'mW': np.zeros_like(W),     # Adam momentum
    'mb': np.zeros_like(b),
    'vW': np.zeros_like(W),     # Adam velocity / RMSprop square
    'vb': np.zeros_like(b),
    'sW': np.zeros_like(W),     # RMSprop only
    'sb': np.zeros_like(b),
}
```

### Cache Structure (Forward Pass)
```python
self.cache = {
    'Z': [Z1, Z2, ..., ZL],           # Pre-activations (L layers)
    'A': [X, A1, A2, ..., AL],        # Activations (L+1 including input)
    'dropout_masks': [M1, M2, ..., M(L-1)]  # Masks for layers 1..L-1
}
```

### Training State
```python
self.loss_history = []           # Train loss per epoch
self.val_loss_history = []       # Val loss per epoch
self.accuracy_history = []       # Train acc per epoch
self.val_accuracy_history = []   # Val acc per epoch
self._t = 0                      # Adam timestep
self.training_mode = True        # Controls dropout
```

---

## 7. Weight Initialization Mathematics

### He Initialization (for ReLU variants)
```
Var(W) = 2 / fan_in
W ~ Normal(0, sqrt(2 / fan_in))
```
Derivation: For ReLU, half the activations are zero. To preserve variance:
`Var(y) = Var(Wx) = n * Var(W) * Var(x) * 0.5` → set `Var(W) = 2/n`

### Xavier Initialization (for Sigmoid/Tanh)
```
Var(W) = 1 / fan_in
W ~ Normal(0, sqrt(1 / fan_in))
```
Derivation: For linear activations, `Var(y) = n * Var(W) * Var(x)` → `Var(W) = 1/n`

### Implementation
```python
if 'relu' in layer['activation']:
    scale = np.sqrt(2.0 / prev_size)   # He
else:
    scale = np.sqrt(1.0 / prev_size)   # Xavier
layer['W'] = np.random.randn(layer['neurons'], prev_size) * scale
```

---

## 8. Dropout Mathematics

### Inverted Dropout (Training)
```
M ~ Bernoulli(1-p)  (element-wise mask)
Ã = A ⊙ M / (1-p)
E[Ã] = E[A] * E[M] / (1-p) = E[A] * (1-p) / (1-p) = E[A]
```
Preserves expected value during training.

### Inference (No Dropout)
```
Ã = A  (no mask, no scaling)
```
Since training already scaled by `1/(1-p)`, inference uses raw activations.

### Gradient Flow
```
∂L/∂A = (∂L/∂Ã) ⊙ M / (1-p)
```
Mask zeros out gradients for dropped units; scaling preserves gradient magnitude.

---

## 9. Cross-References

- [[stock-predictor]] — Uses this engine for S&P 500 direction prediction
- [[quant-finance/quant-toolkit-and-skills]] — From-scratch ML for quant workflows
- [[ai-ml/reinforcement-learning-ppo]] — Policy/value networks could use this engine
- [[mathematics-of-creativity]] — Neural nets as combinatorial creativity engines
- [[wiki/01-Areas/Programming/math-for-programming]] — Linear algebra foundations

---

## 10. Known Limitations / TODOs

| Limitation | Priority | Notes |
|------------|----------|-------|
| No GPU acceleration | High | Pure NumPy CPU; consider CuPy/JAX backend |
| No conv/recurrent layers | Medium | Only dense layers implemented |
| No autodiff graph | Medium | Manual backprop per layer; could add micro-grad |
| No batch normalization | Medium | Would need running mean/var tracking |
| No LR schedulers | Low | Fixed LR; add cosine annealing, step decay |
| No mixed precision | Low | FP32 only |
| No distributed training | Low | Single-process only |

---

## 11. Performance Characteristics

| Operation | Complexity | Notes |
|-----------|------------|-------|
| Forward (batch) | O(batch × Σ nᵢ × nᵢ₊₁) | Matrix multiplications dominate |
| Backward | O(batch × Σ nᵢ × nᵢ₊₁) | ~2x forward (gradient + param update) |
| Memory | O(Σ nᵢ × nᵢ₊₁ + batch × Σ nᵢ) | Weights + activations cache |
| Save/Load | O(Σ nᵢ × nᵢ₊₁) | Pickle serialization |

---

## See Also
- [[Neural net 2/xor_model.pkl]] — Saved XOR demo model
- [[stock-predictor]] — Financial application of this engine
- [[Neural net 2/neuralnet.py]] — Full source (497 lines)