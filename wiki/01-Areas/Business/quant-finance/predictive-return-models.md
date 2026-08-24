---
module: "quant-finance"
topic: "Predictive Models of Return & Cointegration"
tags: [quant, finance, predictive, regression, cointegration, var, pairs]
last_updated: "2026-08-09"
---

# Predictive Models of Return & Cointegration

> **Sources:** [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] — Fabozzi–Focardi–Kolm *Trends in Quantitative Finance* ch. 8 ("Predictive Models of Return"); [[raw-sources/btech roadmap]] (pairs trading assignment); [[raw-sources/quantstart-self-study-plan]].

---

## 1. The Setup

Model next-period expected return as a function of conditioning information $X_{t-1}$:

$$
\mathbb E[r_t \,|\, \mathcal F_{t-1}] = f(X_{t-1}).
$$

Linear workhorse: **predictive regression**

$$
r_t = \alpha + X_{t-1}^\top \beta + \varepsilon_t
$$

or AR-style mean-modeling for a single variable. The statistical subtleties (Stambaugh bias when regressors are persistent; spurious regression with near unit roots) are exactly the monograph ch. 8 concerns.

---

## 2. Spurious regression & cointegration

**Spurious regression:** two independent random walks regressed on each other → meaningless $t$-stats, huge $R^2$, pure nonsense.

**Fix — cointegration (Engle–Granger).** Variables are cointegrated if a linear combination is stationary $I(0)$ despite each being $I(1)$:

$$
y_t = \alpha + \beta x_t + z_t, \qquad z_t \sim I(0).
$$

**Error-correction form (Engle–Granger 2-step):**

1. Estimate $\hat z_t = y_t - \hat\alpha - \hat\beta x_t$
2. Fit the **error-correction model**:

$$
\Delta y_t = \gamma \underbrace{\hat z_{t-1}}_{\text{ECM}} + \sum \text{lagged differences} + \varepsilon_t
$$

with $\gamma < 0$ measuring the speed of reversion to the long-run relation.

---

## 3. Pairs trading (the classic exploit)

Pick two cointegrated assets (e.g. two oil majors, ETF pairs). Mean-reverting spread:

$$
s_t = \ln P_A - \beta \ln P_B - \mu
$$

**Strategy:** when $s_t$ is far from $\mu$ (by $k\sigma$), short the rich leg and long the poor leg; close when $s_t$ reverts to $\mu$; stop-loss if it doesn't — betting on cointegration persistence. Quantities sizes use $\beta$ for a market-neutral book.

---

## 4. Vector Autoregression & VAR/VECM

- **VAR(p):** $y_t = c + \sum_{i=1}^p A_i y_{t-i} + \varepsilon_t$ — models the joint dynamics of several $I(0)$ series.
- **VECM (cointegrated VAR):** adds the error-correction term for $I(1)$ series.
- **Granger causality** & impulse-response analysis flow from the VAR/VECM fit (see [[model-estimation]] for fitting details).

Modern alternative: **forecast via factor models** (dynamic factor — observable + latent) and **ML** — see [[model-selection-and-model-risk]] and [[transformers-attention-detail]].

---

## 5. Why predictive models fail (monograph ch. 8 emphasis)

- **Non-stationarity / structural breaks** — parameter instability.
- **Small signal-to-noise** — predictive $R^2$ often < 1%.
- **Estimation from overlapping samples** inflates significance.
- **Transaction costs & capacity** dwarf the predicted edge.
- **Data snooping** — see [[model-selection-and-model-risk]] for the remedy.

**Meta-lesson:** your model's edge must be validated *out-of-sample with cost*, not in-sample with high $R^2$.

---

## 6. Code Gallery

### 6.1 Python — cointegration test + pairs signal

```python
"""Engle–Granger style pairs logic."""
from __future__ import annotations
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller


def cointegration_test(a: np.ndarray, b: np.ndarray, max_pval: float = 0.05) -> bool:
    lg = sm.OLS(a, sm.add_constant(b)).fit()
    resid = lg.resid
    p = adfuller(resid, autolag="AIC")[1]
    return p <= max_pval


def zscore_spread(a: np.ndarray, b: np.ndarray, beta: float | None = None, μ: float = 1.0) -> np.ndarray:
    if beta is None:
        beta = sm.OLS(a, sm.add_constant(b)).fit().params[1]
    beta = float(beta)
    spread = np.log(a) - beta * np.log(b)
    # subtract rolling mean to get "z"
    window = 30
    s = pd.Series(spread)
    z = (s - s.rolling(window).mean()) / s.rolling(window).std()
    return z.values


def signal(z: np.ndarray, entry: float = 2.0, exit_: float = 0.5) -> np.ndarray:
    """-1 short spread / +1 long spread."""
    out = np.zeros(len(z)); pos = 0
    for i, zz in enumerate(z):
        if np.isnan(zz): continue
        if pos == 0 and zz > entry:   pos, out[i] = -1, -1      # short the rich leg
        elif pos == 0 and zz < -entry: pos, out[i] = 1, 1       # long the rich leg
        elif pos == -1 and zz < exit_: pos = 0
        elif pos == 1 and zz > -exit_: pos = 0
    return out
```

### 6.2 C++20 — rolling z-score signal

```cpp
// pairs.hpp
#pragma once
#include <concepts>
#include <vector>
#include <numeric>
#include <cmath>

namespace qf {

template <std::floating_point T>
void rolling_mean_std(const std::vector<T>& x, int w,
                      std::vector<T>& mean, std::vector<T>& sd) {
    const int n = static_cast<int>(x.size());
    mean.assign(n, 0); sd.assign(n, 0);
    std::vector<T> cum(n + 1, 0), cum2(n + 1, 0);
    for (int i = 0; i < n; ++i) { cum[i+1] = cum[i] + x[i]; cum2[i+1] = cum2[i] + x[i]*x[i]; }
    for (int i = w - 1; i < n; ++i) {
        const T s = cum[i+1] - cum[i+1-w], s2 = cum2[i+1] - cum2[i+1-w];
        mean[i] = s / w;
        const T var = std::max(T{0}, (s2 - s*s/w) / (w - 1));
        sd[i] = std::sqrt(var);
    }
}

template <std::floating_point T>
std::vector<int> crossover_signal(const std::vector<T>& z, T entry = 2, T exit = 0.5) {
    std::vector<int> sig(z.size(), 0); int pos = 0;
    for (int i = 0; i < (int)z.size(); ++i) {
        if (!std::isfinite(z[i])) continue;
        if (pos == 0 && z[i] > entry) { pos = -1; sig[i] = -1; }
        else if (pos == 0 && z[i] < -entry) { pos = +1; sig[i] = +1; }
        else if (pos == -1 && z[i] < exit) { pos = 0; }
        else if (pos == +1 && z[i] > -exit) { pos = 0; }
    }
    return sig;
}
} // namespace qf
```

---

## 7. Architecture diagram

```
  price A ─────────┐
                   ├──► cointegration check (ADF on residual) ──no─► discard
  price B ─────────┘                       │ yes
                                           ▼
                              β (long-run hedge ratio)
                                           ▼
                     z(t) = (s − rolling mean)/rolling sd
                                           ▼
                         entry/exit rule on z (entry=2, exit=0.5)
                                           ▼
                    market-neutral legs, sized by 1 unit / β
                                           ▼
                           → [[event-driven-backtesting]] P&L
```

---

## 8. Related

- [[model-estimation]] · [[forecasting-and-market-efficiency]] · [[model-selection-and-model-risk]] · [[portfolio-optimization-practice]] · [[quantitative-finance-foundations]]