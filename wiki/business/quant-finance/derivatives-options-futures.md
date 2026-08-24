---
module: "quant-finance"
topic: "Derivatives, Options & Futures"
tags: [quant, finance, derivatives, options, futures, binomial, put-call-parity]
last_updated: "2026-08-09"
---

# Derivatives: Options, Futures & the Binomial Model

> **Sources:** [[raw-sources/quant-finance-basics]], [[raw-sources/btech roadmap]] (Yr3 Options/derivatives assignment), [[raw-sources/ModernMarvels20100406RonnieSircar.pdf]] (binomial tree exposition), [[raw-sources/quantstart-self-study-plan]].

---

## 1. Definitions & Payoffs

A **derivative** is a financial instrument whose value depends on an underlying asset $S_t$ (equity, bond index, FX rate, commodity, credit default).

### 1.1 Forwards & Futures

**Forward:** an OTC agreement to exchange an asset for a pre-agreed price $K$ at time $T$. Payoff at expiry to the long side:

$$
V_T = S_T - K
$$

**Future:** the exchange-traded, daily-margined version — standardized contract, cleared through a CCP.

### 1.2 Options

**European call / put** pay at expiry $T$:

$$
C_T = \max(S_T - K, 0), \qquad P_T = \max(K - S_T, 0)
$$

**American options** may be exercised at any time up to $T$ — their early-exercise value is $\ge$ European value (for puts on dividend-paying or non-dividend stocks the early-exercise premium is positive).

### 1.3 Payoff diagrams (lower bound logic)

- Call: loss capped at premium paid; gain unlimited in $S_T$.
- Put: gain capped at $K$ minus premium; loss capped at premium.
- Long underlying: linear, no floor.
- Short anything: mirror image (risk unlimited).

### 1.4 No-arbitrage bounds

For European options on a non-dividend-paying stock:

$$
\max( S_0 - K e^{-rT},\ 0) \le C \le S_0
$$

**Put–call parity** (the fundamental arbitrage relation):

$$
\boxed{\;
C - P = S_0 - K e^{-rT}
\;}
$$

*Proof:* portfolio A = call + K zero-coupon bond maturing at $T$; portfolio B = put + stock. Both pay $\max(S_T, K)$ at $T$; no-arbitrage forces equal present values.

---

## 2. The Binomial Model (Cox–Ross–Rubinstein)

Time is discrete, $N$ steps of size $\Delta t = T/N$. At each node the price moves up by factor $u > 1$ or down by $d = 1/u < 1$:

```
        S0·u
      ↗
  S0      ↘
      ↙
        S0·d
```

**Risk-neutral probability** (the trick — price as if investors are risk neutral):

The stock price process must satisfy $\mathbb E^{\mathbb Q}[S_{t+1}] = S_t e^{r\Delta t}$, so

$$
p = \frac{e^{r\Delta t} - d}{u - d}, \qquad u = e^{\sigma\sqrt{\Delta t}},\ d = e^{-\sigma\sqrt{\Delta t}} = 1/u.
$$

**Step-by-step pricing of an option:**
1. Build the tree of terminal prices $S_T^{(j)} = S_0 u^j d^{N-j}$, $j = 0,\dots,N$.
2. Backward induction using discounted risk-neutral expectation:

$$
V_{i}^{(j)} = e^{-r\Delta t}\Big[ p\, V_{i+1}^{(j+1)} + (1-p)\, V_{i+1}^{(j)} \Big]
$$

3. Terminal values: $V_N^{(j)} = \max(S_T^{(j)} - K, 0)$ (call) etc.

**Purpose:** the binomial tree is the *proof that Black–Scholes stock-price process is the continuous limit of a random walk.* As $N \to \infty$, $u, d \to$ lognormal diffusion, and the tree price converges to the Black–Scholes price (demonstrated in [[stochastic-calculus-black-scholes]] §8.1, Python).

---

## 3. Pricing / Expectation View

**One-period risk-neutral price of a European option:**

$$
V_0 = e^{-r\Delta t}\, \mathbb E^{\mathbb Q}\big[ V_1 \big]
= e^{-r\Delta t}\big( p\, V_1^u + (1-p)\, V_1^d \big).
$$

In $N$-periods, $V_0 = e^{-rT} \,\mathbb E^{\mathbb Q}[\text{payoff}]$ — the martingale property of discounted prices. So the *two equivalent pillars* are:

$$
\underbrace{\text{cash-flow replication}}_{\text{state-contingent}} \;=\; \underbrace{\text{risk-neutral expectation}}_{\text{probability space}}
$$

The **fundamental theorem of asset pricing** states these coincide for a complete (no-arbitrage) market.

---

## 4. Cox–Ross–Rubinstein convergenence: A worked taste

Take $S_0=100$, $K=105$, $T=0.5$y ($6$m), $r=5\%$, $\sigma=25\%$ (the Sircar lecture's numbers).

- $N$ steps → price via code snippet in [[stochastic-calculus-black-scholes]]:
  - $N=2$: (manual tree) ≈ $C \approx 6.05$
  - $N=50$: ≈ $C \approx 6.14$
  - $N=1000$: ≈ $C \approx 6.16$
  - BS exact: $C = S_0 N(d_1) - K e^{-rT}N(d_2) \approx 6.18$

The drift term disappears; only $r$ and $\sigma$ matter. **This is risk-neutrality in action.** (Numbers approximate — verify in code.)

---

## 5. Options Greeks recap (→ [[stochastic-calculus-black-scholes]])

| Greek | Meaning | Formula (BS call) |
|---|---|---|
| Δ | delta | $N(d_1)$ |
| Γ | gamma | $N'(d_1)/(S_0\sigma\sqrt T)$ |
| Θ | theta (time decay) | $-\frac{S_0 N'(d_1)\sigma}{2\sqrt T} - rKe^{-rT}N(d_2)$ |
| 𝒱 | vega | $S_0 N'(d_1)\sqrt T$ |
| ρ | rho | $KTe^{-rT}N(d_2)$ |

Portfolio risk is a combination of these; **delta hedging** removes Δ exposure so the portfolio P&L is driven by (realized − implied) vol, gamma, theta.

---

## 6. From Discrete to Continuous (taste of the derivation)

In the limit $\Delta t \to 0$, the binomial recursion $V_i = e^{-r\Delta t}\{p V_{i+1}^u + (1-p)V_{i+1}^d\}$ converges to the Black–Scholes PDE; see [[stochastic-calculus-black-scholes]] §5 for the full delta-hedging derivation. Sanity checks:

- Replication portfolio: $\Pi = V - \Delta S_{}$, choose $\Delta = V_S$ → kills $dW_t$.
- No-arbitrage forces $d\Pi = r\Pi dt$, flatly producing

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac12\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV
$$

---

## 7. Architecture Diagram — derivatives lifecycle

```
    ┌──────────────┐      ┌───────────────┐
    │  Trade intent │ ────►│  Pricing       │ → fair value, Greeks, risk
    │  (call $105)  │      │  (tree / BS)   │
    └──────────────┘      └───────┬───────┘
                                 │ price/copy of terms
   ┌─────────────────────────────┴───────────────────┐
   ▼                                     ▼
┌─────────────┐                ┌─────────────┐
│ EXCHANGE /  │                │  CCP        │  (for futures/options)
│ CLEARING    │◄ daily margin► │  NETTING    │
└─────────────┘                └─────────────┘
   │ settlement / collateral
   ▼
┌─────────────┐    ┌────────────────┐
│  Risk        │   │ Trading system  │
│  VaR, limits │   │ (microstructure,│
└─────────────┘   └────────────────┘
```

---

## 8. Reading & Exercises

- Hull ch. "Mechanics of options markets", "Binomial trees", "Properties of stock options" (put–call parity, bounds).
- Sircar lecture: build a 2-step CRR tree by hand for the $K=105$, $T=0.5$, $S_0=100$ example and verify convergence.
- **Assignment (from btech roadmap):** implement CRR binomial pricer in Python AND C++, compare against closed-form BS, plot error vs $N$ on log–log scale (should be $O(1/N)$).

- Related: [[stochastic-calculus-black-scholes]] · [[quantitative-finance-foundations]] · [[market-microstructure]]