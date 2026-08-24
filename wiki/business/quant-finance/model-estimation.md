---
module: "quant-finance"
topic: "Model Estimation: OLS, MLE, Shrinkage, PCA & Filtering"
tags: [quant, finance, estimation, mle, ols, pca, kalman, shrinkage]
last_updated: "2026-08-09"
---

# Model Estimation

> **Sources:** [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] — Fabozzi–Focardi–Kolm *Trends in Quantitative Finance* ch. 9 ("Model Estimation"), ch. 8 (predictive models), plus standard econometrics.

All finance models (beta, factor, return-prediction, risk) reduce to **estimate parameters from noisy data**. This module covers the core estimators and their pitfalls.

---

## 1. The Problem

Given observations $\{(y_t, x_t)\}_{t=1}^T$ and a statistical model, choose parameter vector $\theta$ to best explain the data, while being robust to noise and to **model misspecification**.

---

## 2. Ordinary Least Squares

For linear model $y = X\beta + \varepsilon$:

Compute (for full-rank $X$):

$$
\hat\beta = (X^\top X)^{-1} X^\top y
$$

**Step-by-step:** minimize $\|y - X\beta\|^2$: set $\frac{\partial}{\partial\beta}\|y-X\beta\|^2 = -2X^\top(y-X\beta) = 0$ ⇒ $X^\top y = X^\top X \beta$ ⇒ the normal equations.

Properties: $\hat\beta$ unbiased, Gauss–Markov optimal (BLUE) under spherical errors, asymptotically normal.

**In finance, plain OLS is rarely safe because errors are correlated & heteroskedastic.** → use:
- **Newey–West HAC** standard errors (autocorrelation + heteroskedasticity)
- **GLS / WLS**
- **Instrumental variables** when regressors are endogenous

---

## 3. Maximum Likelihood

Given density $f_\theta(y_t|x_t)$, the likelihood $L(\theta) = \prod_t f_\theta(y_t|x_t)$; the MLE

$$
\hat\theta_{\rm MLE} = \arg\max_\theta \ln L(\theta)
$$

MLE is consistent, asymptotically efficient, invariant; standard errors from Fisher information:

$$
\operatorname{Var}(\hat\theta) \approx \mathcal I^{-1}, \qquad \mathcal I = -\mathbb E_f\Big[\frac{\partial^2\ln L}{\partial\theta\partial\theta^\top}\Big].
$$

**Key finance uses:**
- GARCH volatility estimation: $r_t = \sigma_t z_t$, $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta\sigma_{t-1}^2$.
- Heston model / stochastic volatility calibration (fit to observed market option prices).
- Factor model residuals → correlated-normal likelihood.

---

## 4. Generalized Method of Moments (GMM)

Moment condition $\mathbb E[g(y_t, \theta)] = 0$; minimize the quadratic form of sample moments:

$$
\hat\theta = \arg\min_\theta \; \bar g(\theta)^\top W\, \bar g(\theta)
$$

with optimal weight $W = \operatorname{Var}^{-1}(\bar g)$. Used for Euler-equation asset-pricing and dynamic models where full likelihood is hard.

---

## 5. Shrinkage (James–Stein / Ledoit–Wolf)

See [[portfolio-optimization-practice]] §2–3. The key recipe for covariance:

$$
\hat\Sigma = \alpha T + (1-\alpha) S
$$

with optimal $\alpha \approx \frac{\sum_{ij}\operatorname{Var}(s_{ij}) - \operatorname{Cov}(s_{ij}, t_{ij})}{\sum_{ij} (s_{ij}-t_{ij})^2}$ (Ledoit–Wolf closed form). Handles $T< n$ gracefully.

---

## 6. Principal Component Analysis (via SVD)

Given $X \in \mathbb R^{T\times n}$ (centered returns), compute

$$
X = U \Sigma V^\top
$$

Column vectors of $V$ are loadings; top-$k$ singular vectors capture the dominant cross-sectional factors. Used to:
- Build **statistical factor models** ($R \approx F B^\top + \varepsilon$).
- **Denoise** covariance (keep top PCs, set the rest—shots through Marcenko–Pastur threshold—to zero/regularized).
- Dimensionality reduction for ML features.

**Estimated factor selection via eigenvalue gap / Marcenko–Pastur.**

---

## 7. State-space / Kalman Filter

For time-varying parameters:

$$
\begin{aligned}
x_{t+1} &= A x_t + w_t & \text{(state eq)} \\
y_t &= C x_t + v_t & \text{(observation eq)}
\end{aligned}
$$

Kalman filter computes posterior $\hat x_{t|t} = \mathbb E[x_t | y_{1:t}]$ recursively (predict → update).

**Finance use:** estimation of **time-varying beta**, regime-switching spot/vol, the "price ≠ fundamental" dynamic signal, and in pairs trading (see [[predictive-return-models]]).

---

## 8. Practical Estimation Checklist (monograph key insights)

1. **Estimate covariance through a factor model or clustering**, not raw sample when $n$ large.
2. **Use shrinkage** to combat noise in both $\mu$ and $\Sigma$.
3. **Correct SEs for HAC** before making inference claims (otherwise spurious t-stats).
4. **Check stability** of parameters across sub-samples/windows (rolling estimation).
5. **Beware of data snooping/in-sample tuning** — see [[model-selection-and-model-risk]].
6. **Prefer predictive validation** (walk-forward) to in-sample $R^2$.

---

## 9. Code Gallery

### 9.1 Python — OLS with Newey-West, MLE for GARCH(1,1)

```python
"""Estimation toolkit: OLS + HAC SEs, GARCH MLE, PCA factors."""
from __future__ import annotations
import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize


def ols_hac(y, X):
    Xd = sm.add_constant(X)
    model = sm.OLS(y, Xd).fit(cov_type="HAC", cov_kwds={"maxlags": 10})
    return model.params, model.bse, model.rsquared


def garch_ml(log_ret: np.ndarray) -> dict:
    """Fit GARCH(1,1) r_t = σ_t z_t by Gaussian MLE."""
    def negll(params):
        omega, alpha, beta = params
        sigma2 = np.empty_like(log_ret); sigma2[0] = np.var(log_ret)
        for t in range(1, len(log_ret)):
            sigma2[t] = omega + alpha * log_ret[t-1]**2 + beta * sigma2[t-1]
        # guard: sigma2 must be positive
        if np.any(sigma2 <= 0): return 1e9
        return 0.5 * np.sum(np.log(sigma2) + log_ret**2 / sigma2)
    res = minimize(negll, x0=[1e-6, 0.1, 0.85], bounds=[(1e-8, None)]*3, method="L-BFGS-B")
    return {"omega": res.x[0], "alpha": res.x[1], "beta": res.x[2], "ll": -res.fun}


def pca_factors(returns: np.ndarray, k: int, T_burn: int):
    """Statistical factors via SVD; returns loadings and factor scores."""
    X = returns[T_burn:] - returns[T_burn:].mean(axis=0)
    _, s, vh = np.linalg.svd(X, full_matrices=False)
    loadings = vh[:k].T                       # (n, k)
    scores = X @ loadings                     # (T', k)
    return scores, loadings, np.cumsum(s**2)/np.sum(s**2)   # cum. var. share
```

### 9.2 C++20 — OLS via QR decomposition (Eigen) + Newey–West SE sketch

```cpp
// ols.hpp (C++20 + Eigen)
#pragma once
#include <Eigen/Dense>
#include <concepts>

namespace qf {

template <typename Mat> requires std::floating_point<typename Mat::Scalar>
struct OLS {
    Mat X;           // (T, p) regressors (already includes intercept if desired)

    auto fit(const Eigen::VectorXd& y, int hac_lags = 10) {
        const auto qr = X.colPivHouseholderQr();
        const Eigen::VectorXd beta = qr.solve(y);                 // more stable than (X'X)⁻¹X'y
        const Eigen::VectorXd resid = y - X * beta;
        const auto T = X.rows(), p = X.cols();
        // White/HAC covariance: Σ = (X'X)⁻¹ X' Ω X (X'X)⁻¹ ; Ω from residuals
        // For simplicity we show White only:
        // (full Newey-West adds lagged inner products budgeted as an exercise)
        Eigen::MatrixXd xw = X.array().colwise() * resid.array().square();
        Eigen::MatrixXd sigma = (X.transpose()*X).inverse() *
                                (X.transpose()*xw) * (X.transpose()*X).inverse();
        return beta, sigma;
    }
};
} // namespace qf
```

---

## 10. Architecture diagram

```
  returns / factors                     candidates
      │  ┌──────────────────────────────────────┐
      ▼  ▼                                      ▼
  ┌───────────────┐   ┌───────────────────┐ ┌──────────────┐
  │  Covariance:  │   │  Conditional mean: │ │  Vol / risk: │
  │  sample /     │   │  OLS, VAR, ML,      │ │  GARCH, PCA, │
  │  factor /     │   │  random forest     │ │  Kalman      │
  │  shrinkage    │   └─────────┬──────────┘ └──────┬───────┘
  └───────┬───────┘             │                  │
          ▼                     ▼                  ▼
  ┌──────────────────────────────────────────────────┐
  │         diagnostic: SEs (HAC), stability,        │
  │         walk-forward validation, overfit check   │
  └──────────────────────────────────────────────────┘
```

---

## 11. Related

- [[portfolio-optimization-practice]] — shrinkage in portfolio setting
- [[predictive-return-models]] — estimation in predictive setting
- [[model-selection-and-model-risk]] — the DGP caveat
- [[risk-management-value-at-risk]]