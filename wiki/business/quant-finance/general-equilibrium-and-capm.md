---
module: "quant-finance"
topic: "CAPM, General Equilibrium & the Market Model"
tags: [quant, finance, captal-asset-pricing, capm, equilibrium, beta, fama-french]
last_updated: "2026-08-09"
---

# CAPM, General Equilibrium & the Market Model

> **Sources:** [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] (Fabozzi–Focardi–Kolm, ch. 2 "General Equilibrium Theories"), [[raw-sources/btech roadmap]].

---

## 1. From Markowitz to CAPM

Markowitz (1952) gave investors an optimization problem. Sharpe (1964), Lintner (1965) & Mossin (1966) asked: *if everyone solves it, what are asset prices?* The answer is the **Capital Asset Pricing Model**.

**Key idea:** general equilibrium between utility-maximizing (mean-variance) investors and rational asset pricing pins down a single risk-return relation.

---

## 2. Assumptions (the clean textbook set)

1. Investors are **mean-variance optimizers** (quadratic utility / normally distributed returns).
2. **Homogeneous expectations** — everyone sees the same $\mu, \Sigma$.
3. **Single-period** horizon; all wealth invested.
4. **Risk-free asset** exists; can lend/borrow at $r_f$.
5. Frictionless markets: no taxes, no transaction costs, no short-sale constraints.

Under these, everyone holds the two-fund portfolio:
- risk-free asset, plus
- the **tangency/market portfolio** $M$ (see [[markowitz-portfolio-theory]]).

Equilibrium: aggregate demand = supply ⇒ the tangency portfolio must be the **value-weighted market portfolio**. This is the two-fund separation theorem in equilibrium.

---

## 3. The Security Market Line (derivation)

Portfolio of asset $i$ and market $M$ with weight $w$ in $i$:

$$
\mu_w = w\mu_i + (1-w)\mu_M, \qquad
\sigma_w^2 = w^2\sigma_i^2 + (1-w)^2\sigma_M^2 + 2w(1-w)\sigma_{iM}.
$$

At the market point $w=0$, the efficient frontier's slope $= \frac{\mu_M - r_f}{\sigma_M}$ (CML). A useful decomposition: the **Sharpe ratio** curve for the combined portfolio touches the CML tangentially at $w=0$ only if

$$
\frac{\partial \mu_w/\partial w}{\partial \sigma_w/\partial w}\,\Big|_{w=0} = \frac{\mu_M - r_f}{\sigma_M}.
$$

Evaluate at $w=0$:

$$
\left.\frac{\partial \mu_w}{\partial w}\right|_{0} = \mu_i - \mu_M, \qquad
\left.\frac{\partial \sigma_w}{\partial w}\right|_{0} = \frac{\sigma_{iM} - \sigma_M^2}{\sigma_M}.
$$

Equating slopes ⇒

$$
\mu_i - \mu_M = \frac{\sigma_{iM} - \sigma_M^2}{\sigma_M} \cdot \frac{\mu_M - r_f}{\sigma_M}
= (\beta_i - 1)(\mu_M - r_f)
$$

$$
\boxed{\;
\mu_i = r_f + \beta_i\big(\mu_M - r_f\big), \qquad
\beta_i = \frac{\operatorname{Cov}(R_i, R_M)}{\operatorname{Var}(R_M)} = \frac{\sigma_{iM}}{\sigma_M^2}
\;}
$$

**Security Market Line (SML)**: expected excess return is linear in $\beta$. Compare with the CML (which is linear in $\sigma_p$ for *efficient* portfolios alone). The capital-market line only concerns efficient portfolios; the SML prices *every* asset.

---

## 4. Systematic vs Idiosyncratic Risk

Decompose return:

$$
R_i = r_f + \beta_i(R_M - r_f) + \varepsilon_i, \qquad \mathbb E[\varepsilon_i]=0,\ \operatorname{Cov}(\varepsilon_i, R_M)=0.
$$

Then

$$
\sigma_i^2 = \beta_i^2 \sigma_M^2 + \sigma_{\varepsilon}^2.
$$

- $\beta_i^2\sigma_M^2$ = **systematic** risk — common to all stocks, priced.
- $\sigma_\varepsilon^2$ = **idiosyncratic** risk — diversifiable away, *not* priced.

Diversification (law of large numbers on the idiosyncratic component) drives $\sigma_\varepsilon^2 \to 0$ in a portfolio of many $i$. Only systematic risk earns a premium — the essence of CAPM.

---

## 5. Fama–French / Multi-Factor Extensions

The CAPM fails empirically (many anomalies: size, value, momentum). **Fama–French** added factors:

$$
R_i - r_f = \alpha_i + \beta_i(R_M - r_f) + s_i\, \text{SMB} + h_i\, \text{HML} + \varepsilon_i
$$

where SMB = small-minus-big (size), HML = high-minus-low book-to-market (value). Later: **Carhart** adds UMD (momentum); **FF5** adds RMW (profitability) and CMA (investment).

**Interpretation:** excess returns unexplained by beta = $\alpha$ — seek assets with positive $\alpha$ after controlling for risk factors. Factor models also materially solve covariance estimation (see [[portfolio-optimization-practice]]).

Mirror this in **forecasting** literature ([[predictive-return-models]]): multi-factor predictive regressions use the same machinery.

---

## 6. Critique & Modern View (monograph ch. 2 material)

- The book (Fabozzi–Focardi–Kolm ch. 2) stresses that **general equilibrium** theories require strong utility/rationality assumptions that are falsifiable and frequently *not* met (behavioral deviations, non-normal returns).
- Intertemporal CAPM (Merton 1973 — ICAPM), consumption-CAPM (Breeden, Lucas), and arbitrage pricing theory (Ross 1976 — **APT**) relax mean-variance in different directions; APT derives a factor pricing relation with **no equilibrium story**:

$$
\mu_i = r_f + \sum_{k} \beta_{ik}\,\lambda_k
$$

where the $\lambda_k$ are factor **risk premia**.
- The monograph: "evidence on the CAPM is mixed; the empirical asset-pricing literature now routinely relies on multi-factor models."

---

## 7. Estimation Practice

For realized data:

$$
\hat\beta_i = \frac{\widehat{\operatorname{Cov}}(R_i, R_M)}{\widehat{\operatorname{Var}}(R_M)} =
\frac{\sum_t (R_{it}-\bar R_i)(R_{Mt}-\bar R_M)}{\sum_t (R_{Mt}-\bar R_M)^2}
$$

which is exactly the OLS slope in the regression $R_i - r_f = \alpha_i + \beta_i(R_M - r_f) + \varepsilon_i$. Standard errors: use Newey–West (HAC) to handle autocorrelation/heteroskedasticity in returns. (See [[model-estimation]].)

---

## 8. Code Gallery

### 8.1 Python — OLS beta + Fama–French-style factor regression

```python
"""Estimate CAPM beta and a 3-factor regression with statsmodels."""
from __future__ import annotations
import numpy as np
import pandas as pd
import statsmodels.api as sm


def pare_returns(df: pd.DataFrame, cols) -> pd.DataFrame:
    return df

def capm_beta(stock: pd.Series, mkt: pd.Series, rf: pd.Series) -> float:
    """stock/mkt/rf as already-overlapping returns (in decimals)."""
    ex_stock = stock - rf
    ex_mkt = mkt - rf
    X = sm.add_constant(ex_mkt)
    model = sm.OLS(ex_stock, X).fit()
    beta = model.params.iloc[1]
    return float(beta)


def factor_model_regression(returns, factors) -> pd.DataFrame:
    """returns: DataFrame (index=dates) of portfolio returns;
       factors: DataFrame of [MKT-RF, SMB, HML]."""
    y = returns
    X = sm.add_constant(factors)
    result = sm.OLS(y, X).fit()
    params = {k: v for k, v in result.params.items()}
    params["alpha_ann_pos"] = float(result.params["const"]) * 252
    params["r2"] = float(result.rsquared)
    return pd.Series(params)


if __name__ == "__main__":
    np.random.seed(42)
    n = 504
    mkt = pd.Series(np.random.normal(0.0005, 0.01, n))
    rf = pd.Series(0.0002, index=range(n))
    # construct a stock with true beta 1.2
    stock = pd.Series(rf + 1.2 * (mkt - rf) + np.random.normal(0, 0.005, n))
    print("Estimated beta:", round(capm_beta(stock, mkt, rf), 4), "(true 1.20)")
```

### 8.2 C++20 — beta estimation (with rolling window)

```cpp
// beta.hpp
#pragma once
#include <concepts>
#include <numeric>
#include <vector>

namespace qf {

// betas for a single asset vs market using pre-computed mean-return vectors
template <std::floating_point T>
T covariance_sum(const std::vector<T>& a, const std::vector<T>& b) {
    return std::inner_product(a.begin(), a.end(), b.begin(), T{0});
}

template <std::floating_point T>
T mean(const std::vector<T>& v) { return std::accumulate(v.begin(), v.end(), T{0}) / v.size(); }

template <std::floating_point T>
T ols_beta(const std::vector<T>& asset_ret, const std::vector<T>& mkt_ret, T rf) {
    const auto n = asset_ret.size();
    std::vector<T> ea(n), em(n);
    for (size_t i = 0; i < n; ++i) { ea[i] = asset_ret[i] - rf; em[i] = mkt_ret[i] - rf; }
    const T me = mean(ea), mm = mean(em);
    T num = 0, denm = 0;
    for (size_t i = 0; i < n; ++i) { num += (ea[i]-me)*(em[i]-mm); denm += (em[i]-mm)*(em[i]-mm); }
    return num / denm;
}
}  // namespace qf
```

---

## 9. Architecture Diagram — asset-pricing workflow

```
    returns data  ──►  factor returns  ──►  estimate betas (OLS / GMM)
         │                                        │
         ▼                                        ▼
   risk model (Σ = βΣ_M β' + Ψ)     regressions on candidate factors
         │                                        │
         └──────────►  asset pricing test : is α ≈ 0?
                                      │
                              SML slope, pricing errors
```

---

## 10. Related

- [[markowitz-portfolio-theory]] (the optimization the CAPM is built on)
- [[portfolio-optimization-practice]] (factor-based Σ estimation)
- [[forecasting-and-market-efficiency]] (market efficiency vs predictability)
- [[quantitative-finance-foundations]]