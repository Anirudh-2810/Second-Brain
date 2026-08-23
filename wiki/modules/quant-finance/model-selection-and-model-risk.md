---
module: "quant-finance"
topic: "Machine Learning, Model Selection & Model Risk"
tags: [quant, finance, ml, overfitting, model-selection, data-snooping, model-risk]
last_updated: "2026-08-09"
---

# Machine Learning, Model Selection & Model Risk

> **Sources:** [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] — Fabozzi–Focardi–Kolm *Trends in Quantitative Finance* ch. 6 ("Machine Learning") and ch. 7 ("Model Selection, Data Snooping, Overfitting, and Model Risk"); [[raw-sources/btech roadmap]].

---

## 1. Machine Learning in Finance

ML models map features $X$ → target $y$ (return, volatility spike, regime, optimal execution action) via flexible function approximations: decision trees/random forests, gradient boosting, neural nets (including transformers — see [[transformers-attention-detail]] and [[reinforcement-learning-ppo]]).

**Why now:** cheap compute; high-dimensional alternative data (satellite, ESG, search, news); non-linear signal detection; backtest automation.

**Uses:**
- Predictive means ([[predictive-return-models]])
- Covariance / regime detection / vol forecasting
- Fill prediction, optimal execution, market making ([[market-microstructure]])
- Fraud, credit scoring, synthetic-data augmentation

---

## 2. Overfitting vs Underfitting — the math

For a hypothesis function $f \in \mathcal H$, decomposition with a squared loss:

$$
\mathbb E\big[(y - \hat f(x))^2\big] = \underbrace{\sigma^2}_{\text{irreducible}} + \underbrace{\mathrm{Bias}^2(\hat f)}_{\text{underfit}} + \underbrace{\operatorname{Var}(\hat f)}_{\text{overfit}}
$$

- High model complexity ⇒ low bias, high variance (overfit).
- Low complexity ⇒ high bias (underfit).
- **Best model balances the two** — found via validation, not training error (training error always decreases with complexity).

**Curse of dimensionality:** sample needed grows exponentially in feature count; more features ⇒ more noise fit. In finance signals are small (~<1% $R^2$) so variance dominates.

---

## 3. Data Snooping (the crime)

Using the **same data** to build *and* test a rule bakes in luck. In optimization this is **selection bias**:

- **700+ backtests** → the best one is likely luck (Bonferroni rule: $\alpha_{corrected} = \alpha/m$).
- **Multiple testing corrections:** Bonferroni, Holm, Benjamini–Hochberg (FDR), White's Reality Check, Hansen's SPA (variance/block bootstrap of performance gap).
- **Instrument proliferation:** trying many predictors until one is "significant".

**Survivorship bias & look-ahead bias** (see [[forecasting-and-market-efficiency]]) are data-snooping siblings.

---

## 4. Model Risk

The model used is wrong in ways that matter (assumptions violated, unseen regime, parameter drift, numerical failure). Sources:
- Misspecified structure (linear vs nonlinear).
- Wrong calibration window.
- Non-stationarity (parameters move).
- Extreme events absent from training data (fat tails — see [[risk-management-value-at-risk]]).

**Mitigation:** validation protocol (walk-forward), model ensemble, model-risk governance (documentation, challenger models, limits on allowed leverage), stress-testing.

---

## 5. Proper Validation Protocol (the discipline)

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Split: train / validation / test  (chronological!)           │
│ 2. Train on t ≤ T0; tune on (T0, T1]; TEST ONCE on (T1, Tmax)   │
│ 3. Walk-forward: re-train each period, trade from next period   │
│ 4. Compare with cost: report net, turnover, capacity            │
│ 5. Multiple-testing audit: count all tried models                │
└─────────────────────────────────────────────────────────────────┘
```

- **Sacred rule:** the *test* segment is touched exactly once.
- Use **purged k-fold** (López de Prado) to avoid leakage between overlapping labels and embargo gaps.

---

## 6. Regularization (fighting overfit directly)

**Ridge:** $\min_\beta \|y - X\beta\|^2 + \lambda\|\beta\|^2$ — shrinks toward zero → effective shrinkage as in Ledoit–Wolf.

**Lasso:** $\min_\beta \|y - X\beta\|^2 + \lambda\|\beta\|_1$ — drives selected coefficients to zero (feature selection).

**Elastic net:** mix of both. For trees/NNs: depth/leaf constraints, dropout, early stopping, weight decay.

Regularization trades variance for bias — pushes the balance point right, robust to noisy predictors.

---

## 7. Code Gallery

### 7.1 Python — purged walk-forward with ML

```python
"""Disciplined walk-forward: lightGBM-esque gradient boosting on returns."""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error


def walk_forward_oos(X: np.ndarray, y: np.ndarray,
                     train_frac: float = 0.6, roll: int = 250):
    n = len(y); split = int(n * train_frac)
    preds, actuals = [], []
    start = split
    while start + roll <= n:
        tr = slice(start - roll, start)
        model = HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05,
                                              max_iter=300).fit(X[tr], y[tr])
        for i in range(start, min(start + roll, n)):
            preds.append(model.predict(X[i:i+1])[0]); actuals.append(y[i])
        start += roll
    preds, actuals = np.array(preds), np.array(actuals)
    return {"mse": mean_squared_error(actuals, preds),
            "oos_r2": 1 - mean_squared_error(actuals, preds)/np.var(actuals),
            "n": len(preds)}
```

### 7.2 C++20 — ridge regression closed-form (via SVD) + lasso coordinate descent sketch

```cpp
// ridge.hpp (C++20 + Eigen)
#pragma once
#include <Eigen/Dense>
#include <concepts>

namespace qf {

template <typename Mat> requires std::floating_point<typename Mat::Scalar>
struct RidgeRegressor {
    Eigen::MatrixXd w;
    void fit(const Mat& X, const Eigen::VectorXd& y, typename Mat::Scalar l2) {
        const auto n = X.cols();
        const Mat XtX = X.transpose() * X;
        const Eigen::MatrixXd eye = Eigen::MatrixXd::Identity(n, n);
        w = (XtX + l2 * eye).ldlt().solve(X.transpose() * y);   // ridge normal eq
    }
    Eigen::VectorXd predict(const Mat& X) const { return X * w; }
};
} // namespace qf
```

---

## 8. Architecture — research loop

```
  data aquisition → features → models(lin / tree / NN / transformer)
                                   │
                                   ▼
                  walk-forward validation  (purged, embargoed, ONCE on test)
                                   │
              ┌────────────────────┴───────────────────┐
              ▼                                        ▼
        acceptable signal?                    debugging / feature work
              │
              ▼
      cost-aware backtest  → [[portfolio-optimization-practice]] sizing
      → trade in sim → small live allocation (paper) → scale
```

---

## 9. Related

- [[predictive-return-models]] · [[model-estimation]] · [[forecasting-and-market-efficiency]] · [[portfolio-optimization-practice]] · [[transformers-attention-detail]] · [[reinforcement-learning-ppo]] · [[risk-management-value-at-risk]]