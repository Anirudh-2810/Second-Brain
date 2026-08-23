---
module: "quant-finance"
topic: "Risk Management: VaR, CVaR, Stress Testing, Credit & Copulas"
tags: [quant, finance, risk, var, cvar, monte-carlo, credit, copula, stress]
last_updated: "2026-08-09"
---

# Risk Management: VaR, CVaR, Stress Testing & Credit

> **Sources:** [[raw-sources/The_Applications_of_Quantitative_Finance_in_the_Ma.pdf]] (risk & ESG applications), [[raw-sources/ModernMarvels20100406RonnieSircar.pdf]] (credit derivatives, copulas), [[raw-sources/quant-finance-basics]], [[raw-sources/btech roadmap]] (VaR assignment).

---

## 1. What "risk" means here

Risk = uncertainty in future value, embedded in the **loss distribution** of the portfolio. Tail measures are the industry standard because variance ignores the danger context of losses.

---

## 2. Value-at-Risk (VaR)

For portfolio loss $L = V_{\text{today}} - V_{\text{horizon}}$ and confidence $\alpha$ (typ. 95%, 99%):

$$
\operatorname{VaR}_\alpha = \inf\{ \ell : P(L \le \ell) \ge \alpha \}
$$

i.e. the $\alpha$-quantile of the loss distribution. With normal returns, volatility $\sigma V$:

$$
\operatorname{VaR}_{0.99} = 2.33\,\sigma\,V
$$

**Three standard estimation approaches:**

| Method | Idea | Pros | Cons |
|---|---|---|---|
| **Historical** | empirical quantile of historical losses | simple, no distribution | needs fat sample; ignores regime |
| **Parametric / Delta-Normal** | assume normal returns → quantile of $\mathcal N(\mu,\sigma)$ | fast | normality wrong in tails |
| **Monte Carlo** | simulate price paths, mark-to-market, take tail | flexible | slow, model risk |

**Coherent risk measures (Artzner):** monotonicity, subadditivity, homogeneity, translation invariance. **VaR is NOT subadditive** — CVaR (expected shortfall) is coherent:

$$
\operatorname{CVaR}_\alpha = \mathbb E[ L \,|\, L > \operatorname{VaR}_\alpha]
$$

which is the coherent, more conservative version; now the standard (Basel FRTB).

---

## 3. Component & Marginal risk

- **Marginal VaR** of asset $i$: change in portfolio VaR from +1 unit exposure.
- For a delta (linear) portfolio with normal returns, **component VaR** sums to portfolio VaR:

$$
\operatorname{CVaR}_i^{\rm c} = (\Delta w_i) \cdot \frac{\partial \operatorname{VaR}}{\partial w_i}, \quad \sum_i = \operatorname{VaR}_p
$$

These drive risk budgeting (allocate risk budget to assets with best return-per-risk).

---

## 4. Stress Testing & Extreme Events

VaR/CVaR describe the *middle* of the tail; they mis-price rare crises. **Stress tests:** evaluate P&L under prescribed shocks (2008 × repeat, rate shock ±300bp, vol × 3, illiquidity of credit). **Scenario analysis** differs from simulation: scenarios are designed, not sampled.

**Non-normal reality (the applications paper's point):** quant models usually underestimate extreme events (`rare events`: financial crisis, COVID, flash crashes). Stress testing + fat-tailed distributions (Student-$t$, GARCH tail clustering) compensate.

---

## 5. Credit Risk & Copulas

### 5.1 Credit derivatives

- **Credit Default Swap (CDS):** protection buyer pays periodic premium; seller pays par on default event — insurance against default. CDS spread ≈ probability of default × loss-given-default.
- **CDO (Collateralized Debt Obligation):** pools bonds/loans into tranches (senior→subordinated); default losses hit subordinated first (first-loss). Pricing needs **joint default distribution** of the whole pool.

### 5.2 Copulas (the joint-default machinery, from Sircar)

A **copula** $C$ joins marginal CDFs into a joint CDF:

$$
F(x_1, \dots, x_n) = C\big( F_1(x_1), \dots, F_n(x_n) \big)
$$

*Sklar's theorem:* every joint distribution has a copula; if margins are continuous it's unique. Diagonally independent vs comonotonic extremes matter for tails:

- **Gaussian copula** (Li 2000): market convention for CDOs — famously mis-specified tail dependence (both tails weak) for credit, contributing to 2007–2008 CDO losses.
- **t-copula:** adds *lower-tail dependence* (better for credit defaults clustering).
- **Archimedean / Clayton copulas:** custom assessment of tail dependence.

**Modelling the pool:** each obligor's default time $\tau_i$ linked by copula; loss = $\sum$ losses given default. The 2008 lesson from Sircar's lecture: *model & data risk* — distributional assumptions, not just calibration, carry catastrophe risk.

---

## 6. Monte Carlo Risk Engine

```
  ┌───────────────┐   ┌───────────────────────────┐   ┌──────────────────┐
  │ Market data,  │──►│ Simulate risk factors      │──►│ Mark portfolio   │
  │ vol surface,  │   │ paths (GBM, Heston, multi- │   │ to (t, path)     │
  │ correlations  │   │ factor, copula-jointed)    │   │ P&L per path     │
  └───────────────┘   └───────────────────────────┘   └────────┬─────────┘
                                                               ▼
                                        ┌──────────────────────────────┐
                                        │  Loss histogram → VaR, CVaR, │
                                        │  tail plots, stress add-ons   │
                                        └──────────────────────────────┘
```

---

## 7. Code Gallery

### 7.1 Python — historical & parametric VaR / CVaR + MC VaR

```python
"""VaR / CVaR toolkit (all approaches)."""
from __future__ import annotations
import numpy as np
from scipy import stats


def historic_var_cvar(losses: np.ndarray, alpha: float = 0.95) -> tuple[float, float]:
    q = np.quantile(losses, alpha)
    return float(q), float(losses[losses > q].mean())


def parametric_var(vol: float, capital: float, mu: float, alpha: float, days: int = 1) -> float:
    z = stats.norm.ppf(alpha)
    return float((z * vol * np.sqrt(days) + mu * days) * capital)


def monte_carlo_var(S0: float, mu: float, sigma: float, T: float, paths: int,
                    alpha: float = 0.95, seed: int = 0) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(paths)
    # GBM terminal prices under physical measure
    ST = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*np.sqrt(T)*z)
    losses = S0 - ST
    return historic_var_cvar(losses, alpha)


def gaussian_vs_t_tail_compare(p: float = 0.995, df: int = 4):
    """VaR for normal vs t distribution at same vol -> tail gap."""
    qn, qt = stats.norm.ppf(p), stats.t.ppf(p, df) * np.sqrt((df-2)/df)
    return qn, qt


if __name__ == "__main__":
    np.random.seed(3)
    losses = np.random.normal(0, 0.02, 10_000) * 1e6
    print("Hist VaR95, CVaR95:", historic_var_cvar(losses))
    print("MC VaR / CVaR:", monte_carlo_var(100, 0.08, 0.25, 1/252, 100_000))
    qn, qt = gaussian_vs_t_tail_compare()
    print(f"Tail 99.5%: Normal {qn:.2f} vs t(4) {qt:.2f} (gap = {(qt-qn)/qn*100:.0f}%)")
```

### 7.2 C++20 — Gaussian & t-copula joint defaults (toy engine)

```cpp
// risk.hpp (C++20 + Eigen, C++11 rand borrowed for portability)
#pragma once
#include <Eigen/Dense>
#include <random>
#include <concepts>
#include <cmath>

namespace qf {

template <typename T> requires std::floating_point<T>
inline T norm_cdf(T x) { const auto t = T{1}/ (T{1} + T{0.3275911}*std::abs(x)); const auto y = ...
   /* use qf::normal_cdf from black_scholes.hpp */ }

// sample default times using Gaussian copula with correlation matrix R
template <std::floating_point T>
std::vector<T> sample_gaussian_copula(std::size_t n_obligors,
                                      const Eigen::MatrixX<T>& corr,
                                      const std::vector<T>& lam,   // hazard
                                      std::mt19937& rng) {
    Eigen::MatrixX<T> L = corr.llt().matrixL();
    std::normal_distribution<T> nd(0, 1);
    std::uniform_real_distribution<T> ud(0, 1);
    Eigen::VectorX<T> z(n_obligors);
    for (auto& a : z) a = nd(rng);
    z = L * z;
    std::vector<T> tau(n_obligors);
    auto exp_cdf = [](T h, T t){ return T{1} - std::exp(-h*t); };   // default time CDF
    for (int i = 0; i < (int)z.size(); ++i) {
        const T u = norm_cdf(z[i]);
        tau[i] = -std::log(1 - u) / lam[i];                          // inverse-CDF sampling
    }
    return tau;
}
} // namespace qf
```

---

## 8. Stress-testing workflow diagram

```
  portfolio positions ─┐
  factor loads       ─┤
                      ▼
       ┌────────────────────────────────┐
       │ scenario: 2008 ×, rates ±300bp,│
       │ vol ×3, credit spread widen   │
       └───────────────┬────────────────┘
                       ▼
         mark-to-model under scenario
                       ▼
            P&L deficit → limits breach
            → risk budget reallocation ([[markowitz-portfolio-theory]])
```

---

## 9. Reading & notes

- **Basel/FRTB:** CVaR at 97.5% is the market risk standard.
- **Applications paper takeaways:** quant + ESG integration (ESG screens reduce tail risks in some settings), rare-event limitation, reliability of historical data — leads to layering stress tests over VaR.
- **2007–2008 CDO lesson (Sircar):** wrong copula/tail assumption + rating dependence devastated senior tranches; always test the *assumption*, not just calibration.

---

## 10. Related

- [[portfolio-optimization-practice]] · [[model-selection-and-model-risk]] · [[stochastic-calculus-black-scholes]] · [[model-estimation]] · [[applications-of-quantitative-finance]]