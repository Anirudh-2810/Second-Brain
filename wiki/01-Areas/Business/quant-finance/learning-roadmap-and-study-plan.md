---
module: "quant-finance"
topic: "Learning Roadmap & Study Plan"
tags: [quant, finance, study, roadmap, self-study, btech, plan]
last_updated: "2026-08-09"
---

# Learning Roadmap & Study Plan

> **Sources:** [[raw-sources/btech roadmap]] (track A: Quant Finance; track B: Advanced AI/ML), [[raw-sources/quantstart-self-study-plan]], [[raw-sources/cmu-mscf-how-to-become-a-quant]].

This is the orchestration page for the whole KB. Everything else hangs off the phases below.

---

## 1. Big picture (2–3 year intellectual arc)

```
  Y1 FOUNDATION    math/stats/linear-alg + Python + intro finance
  Y2 CORE THEORY   stochastic calc, BS, Greeks, VaR, portfolio
  Y3 MODELS&MACH   econ forecasting, ML, cointegration, factor models
  Y4 SYSTEMS/LIVE  C++20 production: matching engine, backtester, RL exec
        │
        ▼
   internship / capstone-facing portfolio
```

Tracks (from the BTech roadmap):
- **Track A — Quant Finance:** financial theory + stochastic calculus + portfolio + risk.
- **Track B — Advanced AI/ML:** transformers, RL/PPO, DL for markets + systems design.

The two merge at the execution layer (see [[quant-toolkit-and-skills]], [[reinforcement-learning-ppo]]).

---

## 2. Phase-by-phase (from QuantStart 6-month to 2-year plan)

### Phase 1 — Foundations (2–3 months)
- Calculus, linear algebra (eigenvalues, SVD, quadratic forms).
- Probability & statistics (distributions, moments, CLT/LLN).
- Python: `numpy`, `pandas`, visualisation; basic OOP.
- Intro derivatives reading: **Hull**.

### Phase 2 — Core quantitative finance (2–3 months)
- Continuous compounding, no-arbitrage, binomial tree → Black–Scholes ([[derivatives-options-futures]], [[stochastic-calculus-black-scholes]]).
- Greeks + delta-hedging; VaR basics ([[risk-management-value-at-risk]]).
- Portfolio theory + CAPM ([[markowitz-portfolio-theory]], [[general-equilibrium-and-capm]]).

### Phase 3 — Toolchain & systems (2–3 months)
- Build: binomial pricer (Python + C++), Monte Carlo pricer, daily P&L calculator.
- Event-driven backtester ([[event-driven-backtesting]]).
- C++20: Eigen for matrices, constexpr math, `std::jthread`.

### Phase 4 — Markets knowledge
- Bonds an FX; futures/options mechanics; microstructure & execution ([[market-microstructure]]); fixed income math (yield, duration, convexity).

### Phase 5 — Advanced math
- Measure-theoretic basics as needed; stochastic calculus review; martingales; Girsanov (risk-neutral change-of-measure) — flagged optional-deep.

### Phase 6 — Modelling
- Time series: ARIMA, cointegration, VAR; factor models; shrinkage; ML in finance with **walk-forward discipline** ([[predictive-return-models]], [[model-selection-and-model-risk]], [[model-estimation]]).

---

## 3. The BTech roadmap's flagship assignments (map them here)

| Assignment | Module |
|---|---|
| CRR binomial pricer in Python and C++ vs closed-form BS | [[derivatives-options-futures]], [[stochastic-calculus-black-scholes]] |
| Black–Scholes with Greeks visualisation | [[stochastic-calculus-black-scholes]] |
| VaR (parametric/historical/MC) on a portfolio | [[risk-management-value-at-risk]] |
| Pairs trading (cointegration) | [[predictive-return-models]] |
| Markowitz efficient frontier numerics | [[markowitz-portfolio-theory]] |
| Event-driven backtester | [[event-driven-backtesting]] |
| C++20 matching engine | [[matching-engine-cpp]] |
| Multi-factor equity regression | [[general-equilibrium-and-capm]] |
| PPO agent for execution (RL) | [[reinforcement-learning-ppo]] |
| Transformer self-attention demo | [[transformers-attention-detail]] |

---

## 4. Book ladder (practical order)

1. **Hull** — *Options, Futures & Other Derivatives* (ch. 5, 7, 9, 13, 19 core).
2. **Baxter & Rennie** — *Financial Calculus* (probability view, ~200 pp).
3. **Joshi** — *C++ Design Patterns and Derivatives Pricing* (implementation).
4. **Shreve** — *Stochastic Calculus for Finance II* (measure-theoretic, opt.).
5. **Fabozzi–Focardi–Kolm** — *Trends in Quantitative Finance* (survey/metatheory).
6. **López de Prado** — *Advances in Financial Machine Learning* (backtest discipline).

---

## 5. Weekly cadence suggestion

```
  Mon: theory (stochastic/stat) + 1 exercise
  Tue: implement yesterday's theory (Python)
  Wed: markets/data hygiene task
  Thu: C++/systems component
  Fri: review + forward notes into KB
  Sat: build assignment / mini-project
```

Note-take into this KB with [[wiki/index]] discipline; attach every formula, code, and source.

---

## 6. Definition of "done" per phase

- **Phase 2:** price a call via binomial tree, delta-hedge it on paper, reproduce BS closed-form, understand the *derivation*, not just formula.
- **Phase 3:** backtester runs a strategy end-to-end with transaction costs; C++ engine passes a Python-oracle test.
- **Phase 6:** one reproducible, costs-adjusted, OOS-validated strategy notebook committed to repo.

---

## 7. Related

- [[quantitative-finance-foundations]] · [[quant-careers-and-industry]] · [[quant-toolkit-and-skills]] · all `quant-finance/*` and `ai-ml/*` modules