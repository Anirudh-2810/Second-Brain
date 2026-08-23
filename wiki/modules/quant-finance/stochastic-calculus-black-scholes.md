---
module: "quant-finance"
topic: "Stochastic Calculus & the Black–Scholes Model"
tags: [quant, finance, stochastic, black-scholes, ito, derivation, concept]
last_updated: "2026-08-09"
---

# Stochastic Calculus & the Black–Scholes Model

> **Sources:** [[raw-sources/quant-finance-basics]], [[raw-sources/btech roadmap]] (Yr3 Stochastic Calculus block),
> [[raw-sources/ModernMarvels20100406RonnieSircar.pdf]] (Princeton ORFE lecture), [[raw-sources/quantstart-self-study-plan]] (Hull, Joshi, Baxter–Rennie reading plan).

Continuous-time finance: modelling asset prices as random processes, deriving portfolios that hedge away risk, and producing a closed-form option price.

---

## 1. Nomenclature and Goals

| Quantity | Symbol | Meaning |
|---|---|---|
| Time | $t \in [0, T]$ | Continuous time up to expiry $T$ |
| Underlying spot | $S_t$ | Asset price at time $t$ |
| Drift (physical) | $\mu$ | Expected rate of return under the *real* ("physical", $\mathbb P$) measure |
| Volatility | $\sigma$ | Constant instantaneous volatility |
| Brownian motion | $W_t$ | Standard $\mathbb P$- or $\mathbb Q$-Brownian motion |
| Risk-free rate | $r$ | Continuously compounded money-market rate |
| Derivative price | $V(S_t, t)$ | Price of a contingent claim |
| Delta | $\Delta = V_S$ | Sensitivity of $V$ to $S$ |

**Why continuous time matters.** The one-period binomial model (see [[derivatives-options-futures]]) leads naturally to a continuous limit as the number of steps $N \to \infty$, $\Delta t \to 0$. The resulting object is a **stochastic differential equation (SDE)**, and the machinery to operate on SDEs is stochastic (Itô) calculus.

---

## 2. Standard Brownian Motion

A standard Brownian motion $W = \{W_t\}_{t \ge 0}$ is a continuous-time stochastic process satisfying:

1. $W_0 = 0$ a.s.
2. Independent increments: for $0 \le s < t$, $W_t - W_s$ is independent of $\mathcal F_s$ (the past).
3. Gaussian increments: $W_t - W_s \sim \mathcal N(0,\, t - s)$.
4. Continuous paths: $t \mapsto W_t$ is a.s. continuous.

### 2.1 Quadratic variation — the single fact that changes calculus

Define the quadratic variation over a partition $0 = t_0 < t_1 < \dots < t_n = T$:

$$
\langle W \rangle_T \;=\; \lim_{n\to\infty} \sum_{k=1}^{n} \big(\Delta W_{k}\big)^2, \qquad \Delta W_k = W_{t_k} - W_{t_{k-1}}.
$$

For Brownian motion this limit is **not zero**, it is deterministic:

$$\boxed{\; \langle W \rangle_T = T \;\text{ a.s.}}$$

**Proof sketch (step-by-step).** Write $\Delta W_k \sim \mathcal N(0, \Delta t_k)$ with $\Delta t_k = t_k - t_{k-1}$. Then $\mathbb{E}[(\Delta W_k)^2] = \Delta t_k$ and $\operatorname{Var}[(\Delta W_k)^2] = 2(\Delta t_k)^2$. Hence

$$
\mathbb E\Big[\sum_{k=1}^n (\Delta W_k)^2\Big] = \sum_{k=1}^n \Delta t_k = T,
\qquad
\operatorname{Var}\Big[\sum_{k=1}^n (\Delta W_k)^2\Big] = \sum_{k=1}^n 2(\Delta t_k)^2 \to 0
$$

as the mesh goes to zero. Convergence in $L^2$ (and therefore in probability) of the sum to $T$ follows. Heuristically this is written as

$$
(dW_t)^2 = dt.
$$

In **ordinary calculus** $\mathrm{d}x^2 = 0$; this is why stochastic calculus needs its own chain rule. Symbiotically, the cross-term and higher-order terms vanish as $n \to \infty$:

$$
(dW_t)(dt) = 0, \qquad (dt)^2 = 0, \qquad (dW_t)^k = 0 \quad (k \ge 3).
$$

### 2.2 Itô process

A process of the form

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

is an **Itô process**: a drift term scaling $dt$, plus a diffusion term scaling $dW_t$.

---

## 3. Itô's Lemma — statement and full derivation

> **Statement.** Let $X_t$ be an Itô process $dX_t = \mu\,dt + \sigma\,dW_t$ and let $f = f(t, x)$ be twice continuously differentiable in $x$ and once in $t$. Then $f(t, X_t)$ is again an Itô process and

$$
\boxed{\;
df \;=\; \Big( f_t + \mu f_x + \tfrac12 \sigma^2 f_{xx} \Big) \, dt \;+\; \sigma f_x \, dW_t
\;}
$$

sub-scripted derivatives evaluated at $(t, X_t)$.

### 3.1 Step-by-step proof

**Step 1 — Taylor expand.** Take a two-variable Taylor expansion of $f$ around $(t, x)$ with increments $\Delta t$, $\Delta X$:

$$
\Delta f \;=\; f_t\,\Delta t + f_x\,\Delta X + \tfrac12 f_{tt}(\Delta t)^2 + f_{tx}\,\Delta t\,\Delta X + \tfrac12 f_{xx}(\Delta X)^2 + \cdots
$$

**Step 2 — substitute the increment of $X$.** Over a small interval, $\Delta X \approx \mu\,\Delta t + \sigma\,\Delta W$. Using the quadratic-variation identities from §2.1:

- $(\Delta t)^2 \to 0$
- $\Delta t\,\Delta X \approx \mu (\Delta t)^2 + \sigma \Delta t\,\Delta W \to 0$
- **$(\Delta X)^2 \approx \mu^2(\Delta t)^2 + 2\mu\sigma\,\Delta t\,\Delta W + \sigma^2(\Delta W)^2 \to \sigma^2\,dt$**  (the surviving term)

**Step 3 — keep only the leading-order terms.** All terms of order higher than $dt$ vanish. The only "surprise" is $(\Delta W)^2 \to dt$, which drags the second-derivative term into the $dt$ part:

$$
\Delta f \;\approx\; f_t\,\Delta t + f_x\big(\mu\,\Delta t + \sigma\,\Delta W\big) + \tfrac12 f_{xx}\,\sigma^2\,\Delta t
$$

**Step 4 — read off the SDE.** Collecting $dt$ and $dW$:

$$
df = \Big(\underbrace{f_t + \mu f_x}_{\text{drift from } t \text{ and } X} + \underbrace{\tfrac12\sigma^2 f_{xx}}_{\text{Itô correction term}}\Big)\,dt + \sigma f_x\,dW_t.
$$

The term $\tfrac12\sigma^2 f_{xx}$ is entirely due to Brownian motion having nonzero quadratic variation. **This is the entire content of Itô's lemma.** ∎

### 3.2 Why you cannot just "take the derivative"

For a deterministic function $g(t)$, $dg = g_t dt$ — the chain rule. For a stochastic process the second-order term survives, so naive differentiation is wrong by a factor that matters enormously (e.g., it is why the drift of $\ln S_t$ is $\mu - \tfrac12\sigma^2$, not $\mu$).

---

## 4. Geometric Brownian Motion (GBM)

Under Black–Scholes, the underlying follows **geometric Brownian motion**:

$$
\boxed{\;
dS_t = \mu S_t\, dt + \sigma S_t\, dW_t
\;}
$$

### 4.1 Explicit solution via Itô on $\ln S_t$

Apply Itô with $f(S) = \ln S$: $f_S = 1/S$, $f_{SS} = -1/S^2$, $f_t = 0$. Then

$$
d\ln S_t = \Big( \mu S \cdot \tfrac1S + \tfrac12 \sigma^2 S^2 \cdot (-\tfrac1{S^2}) \Big)dt + \sigma S \cdot \tfrac1S\,dW_t
= \big( \mu - \tfrac12 \sigma^2\big)dt + \sigma \, dW_t.
$$

Integrate from $0 \to t$:

$$
\ln S_t = \ln S_0 + \big(\mu - \tfrac12\sigma^2\big)t + \sigma W_t
$$

$$
\boxed{\;
S_t = S_0 \exp\Big\{ \big(\mu - \tfrac12\sigma^2\big)t + \sigma W_t \Big\}
\;}
$$

**Key distributional fact.** $S_T$ is **log-normal**: $\ln S_T \sim \mathcal N\big(\ln S_0 + (\mu - \tfrac12\sigma^2)T,\; \sigma^2 T\big)$, so

$$
\mathbb E[S_T] = S_0 e^{\mu T}, \qquad
\operatorname{Var}[S_T] = S_0^2 e^{2\mu T}\big( e^{\sigma^2 T} - 1\big).
$$

### 4.2 Drunken-sailor intuition (Sircar)

Samuelson's GBM is a random-walk ("drunken sailor") model for the stock price, promoted to become the backbone of the Black–Scholes formula. It is *multiplicative*: proportional shocks $\sigma\,dW_t$ compound, so prices stay positive (unlike Bachelier 1900's *additive* arithmetic Brownian motion, which allows negative prices).

---

## 5. The Black–Scholes PDE — full derivation via Delta-hedging

**Setup.** Let $V(S, t)$ be the value of a derivative on $S$. Build a self-financing portfolio with **one derivative and $\Delta$ units of the underlying** (written as "long 1 derivative, short $\Delta$ shares"):

$$
\Pi_t = V(S_t, t) - \Delta_t S_t.
$$

We hold $\Delta$ constant over the infinitesimal interval $dt$.

### 5.1 Apply Itô to $V(S_t, t)$

With $f = V$, $X = S$, $\mu$, $\sigma$ from the GBM SDE:

$$
dV = \Big( V_t + \mu S V_S + \tfrac12\sigma^2 S^2 V_{SS} \Big)dt + \sigma S V_S\, dW_t.
$$

The portfolio change is

$$
d\Pi = dV - \Delta\, dS
       = \Big( V_t + \mu S V_S + \tfrac12\sigma^2 S^2 V_{SS} \Big)dt + \sigma S V_S\, dW_t
        - \Delta\big( \mu S dt + \sigma S dW_t\big).
$$

### 5.2 Kill the randomness — choose $\Delta = V_S$

Group the $dW_t$ terms: coefficient is $\sigma S (V_S - \Delta)$. Choosing

$$
\boxed{\;\Delta = V_S \;}
$$

makes the portfolio **locally riskless**: purely drift. This is **delta-hedging**; the elimination of the $dW_t$ exposure is the replication argument.

With $\Delta = V_S$:

$$
d\Pi = \Big( V_t + \tfrac12 \sigma^2 S^2 V_{SS} \Big) dt.
$$

### 5.3 No-arbitrage: a riskless portfolio must earn $r$

A portfolio with zero instantaneous risk must earn the risk-free rate, else arbitrage exists:

$$
d\Pi = r\,\Pi\, dt = r\big(V - V_S S\big)dt.
$$

### 5.4 Equate and rearrange

$$
V_t + \tfrac12\sigma^2 S^2 V_{SS} = rV - rS V_S
$$

$$
\boxed{\;
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S}
+ \tfrac12\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \;=\; rV
\;}
$$

### 5.5 Remarks

- The **drift $\mu$ has disappeared.** This is the essence of risk-neutral pricing: the real-world expected return is replaced by $r$ because the delta hedge removes it. This is why the Black–Scholes price does not depend on $\mu$.
- The equation is **backwards parabolic** in time (solve from terminal condition $V_T = \text{payoff}$ back to $t=0$).
- Under the **risk-neutral measure $\mathbb Q$**, $S_t$ satisfies the GBM with $\mu \to r$:  $dS_t = rS_t dt + \sigma S_t\, dW_t^{\mathbb Q}$.

---

## 6. Solving the PDE — the Black–Scholes closed form

### 6.1 Terminal / boundary conditions for a European call

- Terminal payoff: $V(S, T) = \max(S - K, 0)$ where $K$ is the strike.
- $S = 0$: $V(0, t) = 0$.
- $S \to \infty$: $V(S,t) \to S - K e^{-r(T-t)}$.

### 6.2 Reduction to the heat equation

**Step 1** — change time variable $\tau = T - t$ (forward time): $V_t = -V_\tau$,

$$
-V_\tau + rS V_S + \tfrac12\sigma^2 S^2 V_{SS} = rV.
$$

**Step 2** — change variable $S = K e^{x}$, i.e. $x = \ln(S/K)$; $S \frac{\partial}{\partial S} = \frac{\partial}{\partial x}$, $S^2\frac{\partial^2}{\partial S^2} = \frac{\partial^2}{\partial x^2} - \frac{\partial}{\partial x}$:

$$
-V_\tau + \big(r - \tfrac12\sigma^2\big)V_x + \tfrac12\sigma^2 V_{xx} = rV.
$$

**Step 3** — eliminate the $rV$ term and the $V_x$ drift with an exponential ansatz

$$
V = e^{\alpha x + \beta \tau}\, u(x, \tau).
$$

Substituting and collecting terms gives $\alpha = -\frac12 - \frac{r}{\sigma^2}$, $\beta = -\frac{r}{2} - \frac{\sigma^2}{8} - \frac{r^2}{2\sigma^2}$. With

$$
w(\xi, \tau) = u\Big(\xi + \big(r-\tfrac12\sigma^2\big)\tau,\ \tau\Big),
$$

you obtain the plain **heat equation**

$$
\boxed{\;
\frac{\partial w}{\partial \tau} = \tfrac12\sigma^2 \frac{\partial^2 w}{\partial \xi^2}
\;}
$$

with initial data $w(\xi, 0) = \max(K(e^\xi - 1), 0)$.

**Step 4** — solve the heat equation with the Gaussian kernel

$$
w(\xi,\tau) = \frac{1}{\sigma\sqrt{2\pi\tau}}\int_{-\infty}^{\infty} w(y,0)\,
\exp\Big\{- \frac{(\xi - y)^2}{2\sigma^2\tau}\Big\}\,dy
$$

**Step 5** — undo changes of variables: standard completion-of-square integration of the payoff yields the **Black–Scholes formula**.

### 6.3 The Black–Scholes formula (European call)

$$
\boxed{\;
C = S_0\, N(d_1) - K e^{-rT}\, N(d_2)
\;}
$$

$$
d_1 = \frac{\ln(S_0/K) + (r + \tfrac12\sigma^2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}.
$$

where $N(\cdot)$ is the standard normal CDF. By put–call parity

$$
P = C - S_0 + K e^{-rT}
$$

giving the European put

$$
\boxed{\;
P = K e^{-rT}\, N(-d_2) - S_0\, N(-d_1)
\;}
$$

### 6.4 Greeks

| Greek | Definition | Closed form |
|---|---|---|
| Delta (call) | $\Delta = \partial C / \partial S$ | $N(d_1)$ |
| Delta (put) |  | $N(d_1) - 1$ |
| Gamma | $\Gamma = \partial^2 C / \partial S^2$ | $\frac{N'(d_1)}{S_0\sigma\sqrt{T}}$ |
| Theta (call, per year) | $\Theta = \partial C / \partial t$ | $-\frac{S_0 N'(d_1)\sigma}{2\sqrt{T}} - rKe^{-rT}N(d_2)$ |
| Vega | $\mathcal V = \partial C / \partial \sigma$ | $S_0 N'(d_1)\sqrt{T}$ |
| Rho (call) | $= \partial C / \partial r$ | $K T e^{-rT}N(d_2)$ |

---

## 7. Risk-neutral / martingale pricing viewpoint

By the **fundamental theorems of asset pricing** (Harrison–Kreps–Pliska; see [[forecasting-and-market-efficiency]]), absence of arbitrage $\iff$ existence of a risk-neutral measure $\mathbb Q$ under which discounted prices are martingales. The derivative price is

$$
V_t = e^{-r(T-t)}\,\mathbb E^{\mathbb Q}\big[\, \text{payoff}(S_T) \,\big].
$$

Under $\mathbb Q$, $S_T = S_0 \exp\{ (r - \tfrac12\sigma^2)T + \sigma w \}$ with $w\sim\mathcal N(0,T)$; evaluating the expectation reproduces §6.3.

---

## 8. Code Gallery

### 8.1 Python — Black–Scholes pricer with Greeks and Monte-Carlo check

```python
"""Black-Scholes European option pricer (exact + Monte Carlo validation)."""
from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass
from scipy.stats import norm

N = norm.cdf
n = norm.pdf


@dataclass(frozen=True)
class OptionParams:
    S0: float          # spot
    K: float           # strike
    T: float           # years to expiry
    r: float           # risk-free rate (continuous)
    sigma: float       # volatility
    q: float = 0.0     # continuous dividend yield


def _d12(p: OptionParams) -> tuple[float, float]:
    sigma_sqrt_t = p.sigma * math.sqrt(p.T)
    d1 = (math.log(p.S0 / p.K) + (p.r - p.q + 0.5 * p.sigma**2) * p.T) / sigma_sqrt_t
    d2 = d1 - sigma_sqrt_t
    return d1, d2


def bs_price(p: OptionParams, option_type: str = "call") -> float:
    d1, d2 = _d12(p)
    fwd = p.S0 * math.exp(-p.q * p.T)
    df = math.exp(-p.r * p.T)
    if option_type == "call":
        return fwd * N(d1) - p.K * df * N(d2)
    return p.K * df * N(-d2) - fwd * N(-d1)


def bs_greeks(p: OptionParams, option_type: str = "call") -> dict[str, float]:
    d1, d2 = _d12(p)
    df, sqrt_t = math.exp(-p.r * p.T), math.sqrt(p.T)
    delta = (N(d1) - 1) if option_type == "put" else N(d1)
    theta = (
        -p.S0 * n(d1) * p.sigma / (2 * sqrt_t)
        - p.r * p.K * df * N(d2)
    )
    if option_type == "put":
        theta += p.r * p.K * df - p.r * p.S0  # adjustment for cash-flow term
    return {
        "delta": delta,
        "gamma": n(d1) / (p.S0 * p.sigma * sqrt_t),
        "theta_per_year": theta,
        "vega": p.S0 * n(d1) * sqrt_t,          # price change per +1 vol unit
        "rho": (p.r > 0) * p.K * p.T * df * (N(d2) if option_type == "call" else -N(-d2)),
    }


def binomial_tree_price(p: OptionParams, steps: int,
                        option_type: str = "call", american: bool = False) -> float:
    """Cox-Ross-Rubinstein binomial tree; converges to Black-Scholes as steps->inf."""
    dt = p.T / steps
    u = math.exp(p.sigma * math.sqrt(dt))
    d = 1.0 / u
    p_up = (math.exp((p.r - p.q) * dt) - d) / (u - d)      # risk-neutral prob
    discount = math.exp(-p.r * dt)

    # terminal payoffs
    values = np.empty(steps + 1)
    for j in range(steps + 1):
        S = p.S0 * (u ** j) * (d ** (steps - j))
        values[j] = max(S - p.K, 0) if option_type == "call" else max(p.K - S, 0)

    # backward induction
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            values[j] = discount * (p_up * values[j + 1] + (1 - p_up) * values[j])
            if american:
                S = p.S0 * (u ** j) * (d ** (i - j))
                values[j] = max(values[j], max(S - p.K, 0) if option_type == "call" else max(p.K - S, 0))
    return float(values[0])


def monte_carlo_price(p: OptionParams, n_paths: int = 200_000, seed: int = 0) -> float:
    rng = np.random.default_rng(seed)
    z = rng.standard_normal((n_paths,))
    s_t = p.S0 * np.exp((p.r - p.q - 0.5 * p.sigma**2) * p.T + p.sigma * np.sqrt(p.T) * z)
    payoff = np.maximum(s_t - p.K, 0.0)
    return float(np.exp(-p.r * p.T) * payoff.mean())


if __name__ == "__main__":
    p = OptionParams(S0=100.0, K=105.0, T=0.5, r=0.05, sigma=0.25)
    call = bs_price(p, "call")
    mc = monte_carlo_price(p)
    bin_ = binomial_tree_price(p, 1000)
    print(f"BS Call = {call:.4f} | Binomial(1000) = {bin_:.4f} | MC = {mc:.4f}")
    print("Greeks:", bs_greeks(p, "call"))
```

### 8.2 C++20 — Black–Scholes formula (constexpr-friendly, header-only)

```cpp
// black_scholes.hpp  (C++20)
#pragma once
#include <cmath>
#include <concepts>
#include <numbers>
#include <string_view>

namespace qf {

template <std::floating_point T>
struct EuropeanOption {
    T spot, strike, time_to_expiry, rate, vol, dividend_yield = 0;
};

namespace detail {
// Standard-normal CDF (Abramowitz & Stegun 26.2.17), |err| < 7.5e-8.
template <std::floating_point T>
constexpr T normal_cdf(T x) {
    constexpr T a1{0.254829592}, a2{-0.284496736}, a3{1.421413741},
                 a4{-1.453152027}, a5{1.061405429}, p{0.3275911};
    T sign = x < T{0} ? T{-1} : T{1};
    x = std::abs(x) / std::sqrt(T{2});
    T t = T{1} / (T{1} + p * x);
    T y = T{1} - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * std::exp(-x * x);
    return T{0.5} * (T{1} + sign * y);
}

template <std::floating_point T>
constexpr T normal_pdf(T x) {
    return std::exp(-x * x / T{2}) / std::sqrt(T{2} * std::numbers::pi_v<T>);
}
}  // namespace detail

template <std::floating_point T>
struct BlackScholes {
    EuropeanOption<T> o{};

    struct Result { T price, d1, d2; };

    constexpr Result price(std::string_view kind = "call") const noexcept {
        const T sqrt_t = std::sqrt(o.time_to_expiry);
        const T sigma_sqrt_t = o.vol * sqrt_t;
        const T d1 = (std::log(o.spot / o.strike) +
                      (o.rate - o.dividend_yield + T{0.5} * o.vol * o.vol)
                          * o.time_to_expiry) / sigma_sqrt_t;
        const T d2 = d1 - sigma_sqrt_t;
        const T fwd = o.spot * std::exp(-o.dividend_yield * o.time_to_expiry);
        const T df  = std::exp(-o.rate * o.time_to_expiry);
        T v{};
        if (kind == "call")
            v = fwd * detail::normal_cdf(d1) - o.strike * df * detail::normal_cdf(d2);
        else
            v = o.strike * df * detail::normal_cdf(-d2) - fwd * detail::normal_cdf(-d1);
        return {v, d1, d2};
    }
};

}  // namespace qf
```

```cpp
// main.cpp — usage
#include "black_scholes.hpp"
#include <iostream>

int main() {
    using T = double;
    const qf::BlackScholes<T> bs{{100.0, 105.0, 0.5, 0.05, 0.25}};
    const auto [call_price, d1, d2] = bs.price("call");
    std::cout << "C = " << call_price << "\t( d1 = " << d1 << ", d2 = " << d2 << " )\n";
    return 0;
}
```

---

## 9. Architecture diagram — delta-hedged replication

```
                 ┌───────────────────────────────────────────────┐
                 │  Asset Price Process (GBM under ℚ)             │
                 │  dS_t = r S_t dt + σ S_t dW_t                 │
                 └───────────────────┬───────────────────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
 ┌───────────────┐          ┌─────────────────┐          ┌───────────────────┐
 │ Derivative V  │  Itô     │  Portfolio      │   n-arb │  PDE              │
 │ dV = (... )dt │ ───────► │  Π = V - Δ S    │ ──────► │ V_t+rSV_S+½σ²S²V_SS │
 │    + σS V_S dW│          │                 │         │ = rV              │
 └───────────────┘          └─────────────────┘         └───────────────────┘
        ▲                            │  Δ = V_S                        │
        │                   (dW term cancelled)                        │ solve
        │                            ▼                                 ▼
 Risk-neutral │      ┌─────────────────────────────┐        ┌───────────────────┐
 valuation     │      │ Closed form (call):         │        │ MC / Binomial /   │
 V = e^{-rT} E^Q│     │ C = S N(d₁) - K e^{-rT}N(d₂)│        │ FDM numerics      │
        └──────┘      └─────────────────────────────┘        └───────────────────┘
```

---

## 10. Reading path & limitations

- **Texts ([[learning-roadmap-and-study-plan]]):** Hull ch. "Wiener processes & Itô's lemma", Black–Scholes–Merton model; Joshi ch. 1–7 (esp. risk neutrality ch. 6); Baxter & Rennie ch. 3; Shreve *Stochastic Calculus for Finance II* for measure-theoretic depth.
- **Assumptions that break:** constant $\sigma$ (real markets show volatility smile/frown — extensions: local vol, SABR, Heston), frictionless trading, continuous hedging, log-normality of returns. Models are calibrated, not gospel; see [[model-selection-and-model-risk]].
- **Related nodes:** [[quantitative-finance-foundations]] · [[derivatives-options-futures]] · [[markowitz-portfolio-theory]] · [[risk-management-value-at-risk]]