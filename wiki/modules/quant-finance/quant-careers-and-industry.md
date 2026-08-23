---
module: "quant-finance"
topic: "Quant Careers, Roles & the Industry"
tags: [quant, finance, career, roles, sell-side, buy-side, hft]
last_updated: "2026-08-09"
---

# Quant Careers, Roles & the Industry

> **Sources:** [[raw-sources/cmu-mscf-how-to-become-a-quant]], [[raw-sources/cqf-quant-roles-industry]], [[raw-sources/quantstart-self-study-plan]].

---

## 1. Map of roles

```
                    QUANTITATIVE FINANCE CAREERS
        ┌──────────────┬───────────────┬──────────────┬────────────┐
        ▼              ▼               ▼              ▼            ▼
  QUANT RESEARCH  QUANT DEVELOPER  RISK / VAL        STRATEGY /   DATA SCI/
  (front office)  (dev/front)      (validation,      EXECUTION    ML
                                   market risk,      (quant trader  (alpha signals,
                                   FRTB)             / execution)   alternative data)
        │              │               │              │            │
        ▼              ▼               ▼              ▼            ▼
   model pricing   C++/Python engine,  independent     market-making  feature
   risk analysis   low-latency, tools  challenge       optimal exec   engineering,
   alpha research  for quants         the desk        microstruct.   pair with
   (stat, ML)                         models                            backtests
```

### Buy-side vs Sell-side

| Aspect | Sell-side | Buy-side |
|---|---|---|
| Clients | external (buy-side) | themselves / LPs |
| Business | market making, product struct, flow | alpha generation, allocation |
| Philosophy | turnover, spread capture, liquidity provision | medium-long term, factor/asset selection |
| Latency | often HFT-sensitive | rarely |
| Titles | quant strat, structurer, exotic trader | portfolio manager, researcher, modeler |

**Hedge funds/asset managers (buy-side)** pursue *edge over long horizons*; **banks (sell-side)** run desks serving clients and managing inventory. Hybrid roles (quant trader) mix research + execution.

---

## 2. Core resumés

Typical quant-research skills combo (CMU MSCF / CQF flavor):

- **Mathematics:** probability, statistics, stochastic calculus, econometrics, numerical methods.
- **Finance:** derivatives pricing, fixed income, risk, portfolio theory.
- **Programming:** Python (research), C++ (production), git, SQL.
- **Domain:** market microstructure, ML/RL for execution.

### Typical interview prep areas
- Brainteasers + probability puzzles.
- Options & Black–Scholes derivations (see [[stochastic-calculus-black-scholes]]).
- Statistical reasoning & data-questions (regression, hypothesis testing).
- **Coding on a whiteboard / live IDE:** arrays, trees, DP, string parsing.

---

## 3. Career paths worth knowing

- **Quant Dev** route: strong C++/C#, system design → pricing engines, model libraries, low-latency platforms. Less maths, deep engineering.
- **Quant Researcher** route: heavier stats/ML; knowledge of markets to build predictive models.
- **Quant Trader / Execution:** combination; microstructure-heavy.
- **Model Validation & Market Risk:** consume & challenge desk models (a natural early-career choice that teaches the whole book).
- **Strats (sell-side):** hybrid researcher-developer embedded with trading desks.

---

## 4. Skills matrix (what to build in your lab)

| Role | Must-have | Nice-to-have |
|---|---|---|
| Researcher | stats, Python, markets | C++ |
| Developer | C++, low-latency, design | Python |
| Trader | microstructure, speed | algos |
| Risk | VaR/CVaR, model review | C++ |
| Data/ML | feature eng., NLP | RL, DP |

---

## 5. The industry rhythm (monograph survey — 21 large asset managers)

From *Trends in Quantitative Finance* (2005 industry survey): managers rank **risk management & asset allocation** among top quant investment priorities; they blend factor/optimization methods; **estimation error & model risk** concern institutional adoption of advanced portfolio optimization. Translation: firms want **robust**, implementable analytics — reliability is the product.

---

## 6. Portfolio career advice

1. Build a **quant portfolio** — a repo with pricers, backtester, and a couple of reproducible strategy studies (see [[quant-toolkit-and-skills]], [[event-driven-backtesting]]).
2. **Document everything** — producing polished notes is a signal.
3. Understand a product end-to-end: model → engine → risk → trade.
4. Stay current: the field oscillates between math- and data-driven; ML/alpha + RL execution is the 2020s lever.

---

## 7. Related

- [[learning-roadmap-and-study-plan]] · [[quantitative-finance-foundations]] · [[quant-toolkit-and-skills]] · [[applications-of-quantitative-finance]] · [[forecasting-and-market-efficiency]]