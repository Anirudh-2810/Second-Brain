---
module: "quant-finance"
topic: "Foundations of Quantitative Finance"
tags: [quant, finance, foundations, overview]
last_updated: "2026-08-09"
---

# Foundations of Quantitative Finance

> **Sources:** [[raw-sources/quant-finance-basics]], [[raw-sources/cmu-mscf-how-to-become-a-quant]], [[raw-sources/cqf-quant-roles-industry]], [[raw-sources/quantstart-self-study-plan]], [[raw-sources/btech roadmap]].

This module is the entry hub. It defines the discipline, the money flows, the players, and the mathematical core — every other module hangs off it.

---

## 1. What is Quantitative Finance?

Quantitative finance applies **mathematics, statistics, programming, and financial theory** to price securities, manage risk, and design trading strategies.

**The two pyramids:**
- **Math/Stat core:** probability → stochastic calculus → option pricing & risk.
- **Engineering core:** data structures → C++/Python → matching engines, simulators, backtesters.

**The central problem** is that models are *wrong* (violating most textbook assumptions), so q-finance is an engineering discipline of **approximating, hedging, hedging the hedging, and stress-testing**.

---

## 2. Key Concepts (one-line precis)

| Concept | One-liner |
|---|---|
| Discounting | $PV = FV \cdot e^{-rT}$ — money has a time price |
| Present value of cashflows | $P = \sum_t c_t e^{-rt}$ |
| Risk-free rate | Yield of govt./money-market; the "cost" against which all risk is priced |
| Derivative | Security whose payoff is a function of another ("underlying") asset |
| Hedging | Trades that offset risk (e.g. delta hedge, futures hedge) |
| Arbitrage | Riskless profit; absence of arbitrage drives pricing |
| No-arbitrage principle | Two portfolios with identical payoffs must have identical prices |
| Risk-neutral pricing | $V_t = e^{-r(T-t)}\mathbb E^{\mathbb Q}[\text{payoff}]$ |
| Diversification | Combining imperfectly correlated assets lowers variance |
| Volatility | $\sigma$; the square root of variance of return |

**Fundamental Theorem of Asset Pricing (informal):** No arbitrage ⇔ a risk-neutral/probability measure $\mathbb Q$ under which discounted asset prices are martingales exists. (See [[forecasting-and-market-efficiency]].)

---

## 3. The Money Flows & Players

```
                ┌──────────────────────────────────────────────┐
                │              CENTRAL BANK /  GOVT             │
                │         (sets rates, PRINTS money)            │
                └───────────────┬──────────────────────────────┘
                                │ money flows / rates
   ┌───────────────────────────┴───────────────────────────────┐
   ▼                                                           ▼
┌─────────────┐   borrows/lends   ┌────────────────┐  securities  ┌───────────┐
│  BANKS      │  ◄──────────────► │   EXCHANGES    │ ───────────► │ INVESTORS │
│  (traders,  │                   │  LSE, NYSE,    │              │ (retail,  │
│   market mk)│   OTC derivatives │  CME, ICE      │              │  funds)   │
└─────────────┘  ◄──────────────► └────────────────┘              └───────────┘
        │                  ▲
        └── CDS, IRS, FX ──┘   ← derivatives dealers/traders
```

- **Sell-side:** Investment banks/market-makers who manufacture & trade products (a buy-side client buys the product) — dealers make money on spread + inventory risk.
- **Buy-side:** Asset managers, pension funds, hedge funds — they *consume* the products; they want good expected returns at controlled risk.
- **Market infrastructure:** exchanges (LSE, NYSE, CME, ICE), clearing houses, settlement, market-data feeds.
- **Regulators:** FCA, SEC, PRA; discourage insider trading, ensure market integrity.

---

## 4. Products Landscape

```
                         SECURITIES
        ┌────────────────────┼──────────────────────┐
        ▼                    ▼                      ▼
     EQUITIES             FIXED INCOME           FX / COMMODITIES
   shares, ETFs        bonds, notes, MTNs     FOREX, futures, options
        │                    │                      │
     DERIVATIVES ◄──────────┴──────────────────────┘
   ________________|________________________________
   │               │               │               │
 FORWARDS        FUTURES        OPTIONS          SWAPS
 (private)      (exchange)   (call/put, exotic)  (IRS, CDS)
```

- **Forwards** — private agreements, settled at expiry; no money up-front.
- **Futures** — standardized forwards on an exchange with daily margin; daily settlement.
- **Options** — right *not obligation*; convex payoff → limited loss unlimited upside (call); premium paid up-front. (Full treatment: [[derivatives-options-futures]], [[stochastic-calculus-black-scholes]].)
- **Swaps** — exchange cashflow streams: interest-rate swaps (fixed↔floating), credit default swaps (protection on default), total-return swaps.

---

## 5. The Mathematical Core (what the quants actually use)

### Probability & Statistics
- Discrete & continuous distributions; moments, conditional expectation.
- **Law of large numbers, CLT** — the basis of Monte Carlo.
- Time series: ARMA/VAR, cointegration (see [[predictive-return-models]]).

### Linear Algebra & Optimization
- Vectors/matrices, eigen-decomposition, quadratic programming ($\min \tfrac12 w^\top \Sigma w$).
- Used for portfolios ([[markowitz-portfolio-theory]]), factor models, regime detection.

### Stochastic Calculus
- Brownian motion, Itô's lemma, SDEs, martingales, risk-neutral measure
  → produces Black–Scholes ([[stochastic-calculus-black-scholes]]).

### Numerical Methods
- Binomial tree, Monte Carlo, finite differences, PDE solvers — see §8 architecture.

### Information Theory / ML (modern)
- Feature engineering from market data, neural nets for alpha/regime switches, transformers, RL for execution/PPO (see [[reinforcement-learning-ppo]], [[transformers-attention-detail]]).

---

## 6. What Skills Industry Wants (from [[quant-careers-and-industry]])

| Domain | Core skills |
|---|---|
| Quantitative Research | Probability/statistics, stochastic calculus, econometrics, Python/R |
| Quant Development | C++/C#, low-latency, data structures, pricing & risk engines |
| Risk Management | VaR/ES, stress testing, factor models, scenario analysis |
| Strategy/ Execution | Market microstructure, optimal execution, market making |
| Data Science | Data engineering, ML, backtesting discipline |

The CMU MSCF view: "highly technical, selective; quant strategies beat non-quant; **winning on logic, speed and statistical edge**."

---

## 7. Architecture Diagram — an end-to-end quant stack

```
   ┌─────────────┐ ┌──────────────┐ ┌──────────────┐
   │ MARKET DATA │ │ FUNDAMENTALS │ │ ALTERNATIVE  │
   │ L1/L2 ticks │ │ (fundament,   │ │ DATA (ESG,   │
   │ order books │ │  earnings)    │ │  satellites) │
   └──────┬──────┘ └──────┬───────┘ └──────┬───────┘
          ▼               ▼                ▼
   ┌───────────────────────────────────────────────┐
   │ DATA LAKE / RESEARCH DB  (numpy/pandas, parquet)│
   └───────────────────────┬───────────────────────┘
                           ▼
   ┌───────────────────────────────────────────────┐
   │ RESEARCH     signal gen → models → backtesting│
   │              (see predictive-return-models,    │
   │               portfolio-optimization-practice) │
   └───────────────────────┬───────────────────────┘
                           ▼ weights / orders
   ┌───────────────────────────────────────────────┐
   │ EXECUTION   (see market-microstructure)       │
   │ smart order routing, algos, matching engine    │
   └───────────────────────┬───────────────────────┘
                           ▼ fills / P&L
   ┌───────────────────────────────────────────────┐
   │ RISK & MIDDLE OFFICE   VaR, limits, compliance │
   └───────────────────────────────────────────────┘
```

---

## 8. The Self-Study Path (compressed, from quantstart)

> Detailed plan: [[learning-roadmap-and-study-plan]].

1. **Foundations (2–3 mo):** micro-maths (calc, linear algebra, probability), read Hull.
2. **Core theory (2–3 mo):** binomial pricing, Black–Scholes, Greeks, VaR.
3. **Programming:** Python first, then C++ for performance; build pricers + a backtester.
4. **Markets & products:** bonds, futures, options, swaps; microstructure.
5. **Math depth:** stochastic calculus, martingales, measure theory (as needed).
6. **Modeling:** time series, ML, factor models; **dedicated backtesting** (see [[event-driven-backtesting]]).

**Recommended texts:** Hull *Options, Futures & Other Derivatives*; Joshi *C++ Design Patterns and Derivatives Pricing*; Baxter & Rennie *Financial Calculus*; Rodríguez & Duffy for PDEs.

---

## 9. Related Modules

- [[stochastic-calculus-black-scholes]] — the core calculus and flagship result
- [[derivatives-options-futures]] — product mechanics & binomial pricing
- [[markowitz-portfolio-theory]] — diversification and allocation
- [[risk-management-value-at-risk]] — measuring risk
- [[quant-toolkit-and-skills]] — the toolchain
- [[quant-careers-and-industry]] · [[learning-roadmap-and-study-plan]]