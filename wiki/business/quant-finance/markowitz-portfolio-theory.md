---
module: "quant-finance"
topic: "Markowitz Portfolio Theory & the Efficient Frontier"
tags: [quant, finance, portfolio, markowitz, frontier, mean-variance, derivation]
last_updated: "2026-08-09"
---

# Markowitz Portfolio Theory & the Efficient Frontier

> **Sources:** [[raw-sources/quant-finance-basics]], [[raw-sources/btech roadmap]] (Yr3 Portfolio Optimization block — Markowitz, CAPM),
> [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] (Fabozzi–Focardi–Kolm monograph, ch. 2–3 MPT & extensions).

Harry Markowitz (1952, *Portfolio Selection*, J. Finance) framed investing as a **trade-off between mean return and variance of return** — the birth of quantitative asset allocation ("diversification is a free lunch").

---

## 1. Setting

- $n$ risky assets, returns $R \in \mathbb R^n$, mean vector $\mu = \mathbb E[R]$.
- Covariance matrix $\Sigma = \mathbb E[(R - \mu)(R - \mu)^\top] \in \mathbb R^{n\times n}$, assumed symmetric positive definite ($\Sigma \succ 0$: no redundant assets, all variances finite).
- Portfolio weight vector $w \in \mathbb R^n$, $\sum_i w_i = 1$ (written $\mathbf 1^\top w = 1$), $w_i$ = fraction of wealth in asset $i$.
- **Portfolio return:** $R_p = w^\top R$.
- **Portfolio mean:** $\mu_p = w^\top \mu$.
- **Portfolio variance:** $\sigma_p^2 = w^\top \Sigma w$. (Check: $\operatorname{Var}(w^\top R) = w^\top \Sigma w$ by bilinearity of covariance.)

### 1.1 Why variance is the risk measure

Two assets with identical mean but imperfectly correlated returns combine into a portfolio with **strictly lower variance than either alone**:

$$
\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho\sigma_1\sigma_2,
$$

which is minimized along the curve $w_1 + w_2 = 1$ at the diversifying weight.

---

## 2. The Constrained Optimization Problem

**Markowitz MVP (convex quadratic program):**

$$
\min_{w} \; \tfrac12\, w^\top \Sigma w
\qquad \text{s.t.} \quad
\mathbf 1^\top w = 1, \qquad \mu^\top w = \mu_p.
$$

(The $\tfrac12$ is convenience for differentiation.) Choosing a target return $\mu_p$ and minimizing variance traces out the **minimum-variance frontier**.

---

## 3. Full Derivation via Lagrange Multipliers

### Step 1 — Lagrangian

Introduce multipliers $\lambda$, $\gamma$ for the budget and return constraints:

$$
\mathcal L(w, \lambda, \gamma)
= \tfrac12 w^\top \Sigma w - \lambda\big( \mathbf 1^\top w - 1 \big) - \gamma\big( \mu^\top w - \mu_p \big).
$$

### Step 2 — First-order conditions

Using $\frac{\partial}{\partial w} (w^\top A w) = 2Aw$ (for symmetric $A$):

$$
\nabla_w \mathcal L = \Sigma w - \lambda \mathbf 1 - \gamma \mu = 0
$$

$$
\boxed{\;\Sigma w = \lambda \mathbf 1 + \gamma \mu\;}
\quad\Longrightarrow\quad
\boxed{\;w = \Sigma^{-1}\big( \lambda \mathbf 1 + \gamma \mu \big)\;}
$$

plus the two constraint equations $\mathbf 1^\top w = 1$ and $\mu^\top w = \mu_p$.

### Step 3 — Substitute into constraints

Pre-multiply $w$ by $\mathbf 1^\top$ and $\mu^\top$:

$$
1 = \mathbf 1^\top w = \lambda\, (\mathbf 1^\top \Sigma^{-1}\mathbf 1) + \gamma\, (\mathbf 1^\top \Sigma^{-1}\mu)
$$

$$
\mu_p = \mu^\top w = \lambda\, (\mu^\top \Sigma^{-1}\mathbf 1) + \gamma\, (\mu^\top \Sigma^{-1}\mu).
$$

Define the **frontier scalars**

$$
\boxed{
\begin{aligned}
A &= \mathbf 1^\top \Sigma^{-1} \mathbf 1 & \text{(scalar)} \\
B &= \mathbf 1^\top \Sigma^{-1} \mu = \mu^\top \Sigma^{-1}\mathbf 1 & \text{(symmetric, scalar)} \\
C &= \mu^\top \Sigma^{-1} \mu & \text{(scalar)} \\
D &= AC - B^2 > 0 & \text{(≠ 0 by Cauchy–Schwarz, since } \mu \not\propto \mathbf 1\text{)}
\end{aligned}}
$$

### Step 4 — Solve the 2×2 linear system

$$
\begin{bmatrix} A & B \\ B & C \end{bmatrix}
\begin{bmatrix} \lambda \\ \gamma \end{bmatrix}
=
\begin{bmatrix} 1 \\ \mu_p \end{bmatrix}
\quad\Longrightarrow\quad
\lambda = \frac{C - B\mu_p}{D}, \qquad \gamma = \frac{A\mu_p - B}{D}.
$$

### Step 5 — Optimal portfolio as an affine function of $\mu_p$

Substitute back:

$$
\boxed{\;
w^*(\mu_p) = \underbrace{\frac{C\, \Sigma^{-1}\mathbf 1 - B\, \Sigma^{-1}\mu}{D}}_{\text{GMV portfolio } w_g}
\;+\; \mu_p\, \underbrace{\frac{A\, \Sigma^{-1}\mu - B\, \Sigma^{-1}\mathbf 1}{D}}_{w_d}
\;=\; w_g + \mu_p\, w_d.
\;}
$$

The efficient frontier is therefore a **one-parameter family**:

$$
\mu_p(w^*) = \mu^\top w^* = \frac{B}{A} + \frac{\sqrt{D (AC - B^2)}}{A}\,\sigma_p
$$

after expressing $C$ in terms of $\sigma_p$ — i.e. **frontier in mean–variance space is a parabola**; in mean–standard-deviation space it is a **hyperbola**.

### Step 6 — Variance equation (frontier parabola)

$$
\sigma_p^2 = w^\top \Sigma w = \frac{1}{D}\big( A\mu_p^2 - 2B\mu_p + C \big)
\quad\Longleftrightarrow\quad
\frac{\sigma_p^2}{1/D} - \frac{(\mu_p - B/A)^2}{(D/A^2)} = \frac{C}{D} - \frac{B^2}{D A} \quad (A\mu_p^2 - 2B\mu_p+C > 0).
$$

The **minimum-variance point** ($\partial \sigma_p^2/\partial \mu_p = 0$):

$$
\boxed{\;
\mu_{gmv} = \frac{B}{A}, \qquad \sigma_{gmv}^2 = \frac{1}{A}, \qquad w_{gmv} = \frac{\Sigma^{-1}\mathbf 1}{\mathbf 1^\top \Sigma^{-1}\mathbf 1}.
\;}
$$

Only the branch with $\mu_p \ge B/A$ is the **efficient frontier** (upper half) — lower half is dominated.

---

## 4. Two-Fund (Two-Theorem) Separation

**Scalar-fund / mutal-fund theorem (Tobin 1958):** any point on the efficient frontier is a convex combination of two frontier funds

$$
w^* = \theta\, w^{(\text{fund 1})} + (1 - \theta)\, w^{(\text{fund 2})}.
$$

In particular the **two-fund theorem** (for the risky-only world) states every frontier portfolio is a combination of the global minimum-variance portfolio and any other frontier portfolio. Adding a **risk-free asset** $r_f$ (return $\mu_f = r_f$, zero variance) yields the **Capital Market Line**: the tangency line from $(0, r_f)$ to the frontier, touching at the **tangency portfolio** $w_T$:

$$
w_T = \frac{\Sigma^{-1}(\mu - r_f \mathbf 1)}
           {\mathbf 1^\top \Sigma^{-1}(\mu - r_f \mathbf 1)}.
$$

The CML equation:

$$
\mu_p = r_f + \frac{\mu_T - r_f}{\sigma_T}\,\sigma_p
$$

Sharpe ratio (reward-to-variability) maximized:

$$
\mathrm{Sharpe}(w) = \frac{w^\top\mu - r_f}{\sqrt{w^\top \Sigma w}}, \qquad
\boxed{\; w^* = \dfrac{\Sigma^{-1}(\mu - r_f\mathbf 1)}{\mathbf 1^\top \Sigma^{-1}(\mu - r_f\mathbf 1)} \;}
$$

---

## 5. Capital Asset Pricing Model (relation)

The CAPM (see [[general-equilibrium-and-capm]]) emerges by assuming all investors hold the tangency portfolio = **market portfolio** $\mathcal M$. Then

$$
\mathbb E[R_i] = r_f + \beta_i\,\big(\mathbb E[R_\mathcal M] - r_f\big), \qquad
\beta_i = \frac{\operatorname{Cov}(R_i, R_\mathcal M)}{\operatorname{Var}(R_\mathcal M)} = \frac{\sigma_{i\mathcal M}}{\sigma_\mathcal M^2}.
$$

The Security Market Line says the only risk priced is **systematic** (market) risk; idiosyncratic risk is diversifiable and unpriced.

---

## 6. Practical critiques (Fabozzi-era & modern)

- **Estimation error is the killer:** $\Sigma^{-1}$ is extremely sensitive to noise in estimated $\Sigma$ when $n$ is large (curse of dimensionality; $n(n{+}1)/2$ covariance entries need estimation). Row/column shrinkage, factor models, robust optimization, random-matrix denoising — see [[portfolio-optimization-practice]].
- **Mean is even harder to estimate than variance:** championed and non-estimable for many assets. Investors concentrate on variance/vol targets.
- **Non-normality:** fat tails, skew (see [[risk-management-value-at-risk]]).
- **Transaction costs & turnover** — see [[market-microstructure]].
- **Constraint-driven optimizers:** usually add long-only, turnover, sector caps, tracking-error bounds.

---

## 7. Code Gallery

### 7.1 Python — mean-variance efficient frontier + tangency portfolio

```python
"""Markowitz: analytic frontier (uses the A/B/C/D scalars), tangency + GMV."""
from __future__ import annotations
import numpy as np


def efficient_frontier_weights(mu: np.ndarray, sigma: np.ndarray, mu_p: float) -> np.ndarray:
    """Weights of the min-variance portfolio for target return mu_p.
       Closed form: w = (C*Σ⁻¹1 - B*Σ⁻¹μ)/D + mu_p*(A*Σ⁻¹μ - B*Σ⁻¹1)/D
    """
    inv = np.linalg.inv(sigma)                       # Σ⁻¹
    ones = np.ones_like(mu)
    A = float(ones @ inv @ ones)
    B = float(ones @ inv @ mu)
    C = float(mu @ inv @ mu)
    D = A * C - B * B
    w_g = (C * inv @ ones - B * inv @ mu) / D
    w_d = (A * inv @ mu - B * inv @ ones) / D
    return w_g + mu_p * w_d


def tangency_weights(mu: np.ndarray, sigma: np.ndarray, rf: float) -> np.ndarray:
    excess = mu - rf
    inv = np.linalg.inv(sigma)
    w = inv @ excess
    return w / w.sum()                               # normalize to weights summing to 1


def portfolio_stats(w: np.ndarray, mu: np.ndarray, sigma: np.ndarray) -> tuple[float, float]:
    mu_p = float(w @ mu)
    sd_p = float(np.sqrt(w @ sigma @ w))
    return mu_p, sd_p


if __name__ == "__main__":
    # 3-asset toy example
    mu = np.array([0.10, 0.12, 0.08])
    sigma = np.array([
        [0.04, 0.006, 0.002],
        [0.006, 0.09, 0.008],
        [0.002, 0.008, 0.022],
    ])
    for target in (0.09, 0.10, 0.11):
        w = efficient_frontier_weights(mu, sigma, target)
        print(f"mu_p={target} -> w={np.round(w,4)}, stats={portfolio_stats(w, mu, sigma)}")
    w_t = tangency_weights(mu, sigma, rf=0.03)
    print("Tangency w:", np.round(w_t, 4), "sharpe:", portfolio_stats(w_t, mu, sigma))
```

### 7.2 C++20 — tangency portfolio & frontier scalars

```cpp
// markowitz.hpp (C++20) — small dense linear algebra using Eigen
#pragma once
#include <Eigen/Dense>
#include <concepts>
#include <tuple>

namespace qf {

template <typename Mat, typename Vec>
requires std::floating_point<typename Mat::Scalar>
struct Markowitz {
    Vec mu;     // expected returns (n,)
    Mat sigma;  // covariance (n x n), symmetric positive definite
    typename Mat::Scalar rf;

    // A=1'Σ⁻¹1, B=1'Σ⁻¹μ, C=μ'Σ⁻¹μ, D=AC-B²
    auto scalars() const {
        const Mat inv = sigma.inverse();
        const auto ones = Vec::Ones(mu.size());
        const auto sA = ones.dot(inv * ones);
        const auto sB = ones.dot(inv * mu);
        const auto sC = mu.dot(inv * mu);
        const auto sD = sA * sC - sB * sB;
        return std::tuple{sA, sB, sC, sD, inv};
    }

    Vec tangency() const {
        const Vec excess = mu.array() - rf;
        return (sigma.inverse() * excess) / (excess.transpose() * sigma.inverse() * excess).value();
    }

    Vec global_min_variance() const {
        const auto [A, B, C, D, inv] = scalars();
        return (inv * Vec::Ones(mu.size())) / (Vec::Ones(mu.size()).transpose() * inv * Vec::Ones(mu.size())).value();
    }
};

}  // namespace qf
```

```cpp
// main.cpp
#include "markowitz.hpp"
#include <Eigen/Dense>
#include <iostream>

int main() {
    using Scalar = double;
    Eigen::Matrix<Scalar, 3, 1> mu;
    mu << 0.10, 0.12, 0.08;
    Eigen::Matrix<Scalar, 3, 3> sigma;
    sigma << 0.04, 0.006, 0.002,
             0.006, 0.090, 0.008,
             0.002, 0.008, 0.022;
    const qf::Markowitz<decltype(sigma), decltype(mu)> m{mu, sigma, 0.03};
    const auto w_t                  = m.tangency();
    const auto w_g                  = m.global_min_variance();
    std::cout << "Tangency w:     " << w_t.transpose() << "\n";
    std::cout << "Min-variance w: " << w_g.transpose() << "\n";
    return 0;
}
```

---

## 8. Architecture diagram — the allocation pipeline

```
        µ estimates ─┐                      ┌─ Σ estimates (sample / factor / shrinkage)
        Σ estimates ─┤                      │
                     ▼                      ▼
            ┌──────────────────────────────────────┐
            │        Objective & Constraints       │
            │  min ½w'Σw   s.t. 1'w=1, µ'w=µ_target │
            │  (use A=1'Σ⁻¹1, B, C, D closed form)  │
            └───────────────┬──────────────────────┘
                            │  w*
                            ▼
            ┌──────────────────────────────────────┐
            │   Portfolio analytics                 │
            │   µ_p = w'µ   σ²_p = w'Σw             │
            │   Sharpe, tracking error, turnover     │
            └───────────────┬──────────────────────┘
                            │
            ┌───────────────┴──────────────────┐
            ▼                                  ▼
   Risk model checks                  Execution layer (see market-microstructure)
   (VaR, CVaR, stress)               → rebalance schedule, TC model
```

---

## 9. Reading path

- Markowitz (1952) classic paper; DeMiguel, Garlappi & Uppal (2009) "Optimal Versus Naive Diversification".
- Fabozzi–Focardi–Kolm ch. 2–3: market equilibrium and the extended mean-variance framework.
- Hull ch. (portfolio theory) and Shreve for the risk-neutral implications.
- Related: [[general-equilibrium-and-capm]] · [[portfolio-optimization-practice]] · [[quantitative-finance-foundations]]