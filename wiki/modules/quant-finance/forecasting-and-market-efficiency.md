---
module: "quant-finance"
topic: "Forecasting Financial Markets & Market Efficiency"
tags: [quant, finance, forecasting, efficiency, random-walk, martingale, emh]
last_updated: "2026-08-09"
---

# Forecasting Financial Markets & Market Efficiency

> **Sources:** [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] — Fabozzi–Focardi–Kolm *Trends in Quantitative Finance* ch. 1, 4, 5 (Forecasting, Tactical Asset Management, Long-Term Forecastability) and ch. 2.

---

## 1. The central tension

**Efficient Market Hypothesis (EMH) / random walk:** current prices reflect all available information, so returns are unpredictable — no free lunch.

**Forecasting literature:** pervasive evidence of *partial* predictability for horizons, factor and anomaly premia, momentum, fundamentals-growth convergence. The truth is **degrees of efficiency**, not an either/or.

### Fama's three forms
1. **Weak:** prices reflect historical prices only. (Deviations: momentum/mean-reversion, technical rules in some data.)
2. **Semistrong:** prices reflect all public info.
3. **Strong:** prices reflect all private info too (essentially unrealized).

### Martingale view
Under the risk-neutral measure, discounted price process is a **martingale**:

$$
\mathbb E^{\mathbb Q}[ e^{-r(t-s)} S_t \,|\, \mathcal F_s] = S_s
$$

so "unpredictable" means "a martingale under the correct measure — **not** necessarily unpredictable *under* $\mathbb P$".

---

## 2. The mathematics of predictability

A return is predictable if $\mathbb E[\varepsilon_t\,|\, \mathcal F_{t-1}] \neq 0$ in

$$
r_t = \mu_{t-1} + \varepsilon_t
$$

**Testing:** autocorrelation, variance-ratio tests, unit-root tests (ADF), Ljung–Box, out-of-sample $R^2$ ridge/ML comparisons.

**Well-documented predictable components:**
- Momentum (Horizon 3–12 mo); reversal at longer horizons.
- Value/earnings-yield spreads.
- **Cointegration** between related assets (pairs) — see [[predictive-return-models]].
- Volatility clustering → vol forecasting with GARCH/factors — see [[model-estimation]].
- Regime shifts (business cycle, vol state).

---

## 3. Long-term forecastability (monograph ch. 5)

Siegel-style long-horizon results: equities' mean-reversion creates *longer-horizon predictability* (dividend yield predictive regressions with $R^2$ that rises with horizon). The monograph emphasizes **mean-reversion at long horizons vs momentum at short** — the sign of autocorrelation can flip with horizon, both being "predictable".

---

## 4. Forecasting in tactical asset allocation (ch. 4)

- **Tactical asset allocation (TAA)** uses short-horizon forecasts to time between asset classes; strategic AA is long-run static.
- Models: predictive regressions on (dividend yield, term spread, default spread, momentum), switching models, Bayesian shrinkage of forecasts.
- Discipline: forecasts enter an optimizer with **shrinkage toward benchmark** and **position limits** (avoid overconfident extremes) — bridging to [[portfolio-optimization-practice]] and [[model-selection-and-model-risk]].

---

## 5. Beware: statistical traps

- **Data snooping:** abusing the same data to select and then test ⇒ spurious predictive factors. (See [[model-selection-and-model-risk]].)
- **Survivorship bias:** dropped dead assets inflate backtested performance.
- **Look-ahead bias:** using information not yet available at trade time.
- **Multiple testing:** thousands of backtests → the best one often pure luck (Bonferroni/FDR, White's reality check, Hansen's SPA).
- **Non-stationarity:** parameters/champions drift; rolling re-estimation and structural-break tests required.

---

## 6. The forecasting pipeline

```
        inputs                       models                        validation
  past returns        ┌───────────────────────────────┐   ┌────────────────────────┐
  yields/spreads ────►│ ARIMA / VAR / vector error    │──►│ in-sample fit          │
  volumes, vol        │ correction / ML (RF, NN,      │   │ OOS walk-forward       │
  macro, sentiment    │ transformers) → predictive μ   │   │ transaction-cost eq.   │
                      └───────────────────────────────┘   └────────────────────────┘
```

---

## 7. Code snippet — variance ratio test (speed diagnostic)

```python
"""Variance-ratio test for random-walk (Lo–MacKinlay)."""
from __future__ import annotations
import numpy as np


def variance_ratio(px: np.ndarray, q: int = 2) -> float:
    r = np.diff(np.log(px))
    n, mu, var = len(r), r.mean(), ((r - r.mean()) ** 2).sum() / (len(r) - 1)
    # VR(q) = Var(sum of q returns)/(q*Var(1-return))
    rq = np.convolve(px, np.convolve([1.0], [1.0], mode='full'), mode='valid')
    # simpler: sum of q consecutive returns
    z = np.convolve(r, np.ones(q), mode="valid")      # q-period returns
    varq = ((z - q * mu) ** 2).sum() / (len(z) - 1)
    return varq / (q * var)


if __name__ == "__main__":
    np.random.seed(1)
    rw = np.exp(np.cumsum(np.random.normal(0, 0.01, 1000)))
    ar = np.exp(np.cumsum(0.5 * np.random.normal(0, .01, 1000) + 0.5 * np.random.normal(0, .01, 1000)**2))  # toy
    print("VR(rw)=", round(variance_ratio(rw), 3), " VR(ar)=", round(variance_ratio(ar), 3))
```

---

## 8. Architecture diagram

```
  ┌──────────────┬─────────────────┬─────────────────┐
  ▼              ▼                 ▼                 ▼
 macro data     prices/vols      fundamentals      sentiment
     └──────────┴───────┬─────────┴─────────┘
                        ▼
               feature engineering
               ┌────────────────────┐        ┌────────────────────┐
               │ econometric: ARIMA, │        │ ML: RF/Boost/Transformer│
               └──────────┬─────────┘        └──────────┬─────────┘
                          │   μ̂_t (predictive mean)      │
                          └───────────────┬─────────────┘
                                          ▼
                           forecast combination / shrinkage
                                          ▼
                     allocation → [[portfolio-optimization-practice]]
```

---

## 9. Takeaways

1. Markets are **mostly efficient** but **partly predictable** — the balance depends on horizon, asset class and data mining discipline.
2. Predictability, even real, is small; **it must clear transaction costs** to be exploitable.
3. **Data-mining discipline is the real edge** (see [[model-selection-and-model-risk]]).

---

## 10. Related

- [[predictive-return-models]] · [[model-selection-and-model-risk]] · [[model-estimation]] · [[general-equilibrium-and-capm]] · [[quantitative-finance-foundations]]