---
module: "quant-finance"
topic: "Applications of Quantitative Finance (incl. ESG) & Limitations"
tags: [quant, finance, applications, esg, monte-carlo, var, rare-events]
last_updated: "2026-08-09"
---

# Applications of Quantitative Finance (incl. ESG) & Limitations

> **Sources:** [[raw-sources/The_Applications_of_Quantitative_Finance_in_the_Ma.pdf]] — Z. He, Pace University; plus [[raw-sources/quant-finance-basics]], [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]].

Q-finance is not just pricing — it's an applied risk/return engineering discipline used across investment management, banking, insurance and increasingly **sustainability**.

---

## 1. Application map

| Domain | Technique | Module |
|---|---|---|
| Asset allocation | mean-variance, factor, robust | [[markowitz-portfolio-theory]], [[portfolio-optimization-practice]] |
| Pricing | closed forms, trees, MC, PDE | [[stochastic-calculus-black-scholes]] |
| Market risk | VaR/CVaR/ES, stress | [[risk-management-value-at-risk]] |
| Credit | CDS/CDO, copulas | [[risk-management-value-at-risk]] |
| Execution/trading | impact models, algos, HFT | [[market-microstructure]] |
| Alpha | ML, cointegration, forecasting | [[predictive-return-models]], [[model-selection-and-model-risk]] |
| ESG investing | scoring + portfolio constraints + tail-risk analysis | this module's focus |

---

## 2. ESG in a quantitative framework

**ESG taxonomy:** Environmental (carbon, water), Social (labour, community), Governance (board, risk controls). Investors integrate ESG as:

1. **Screening/negative screens** — exclude controversial sectors (simplest; implemented as weight constraints in the optimizer).
2. **ESG tilt / integration** — score each asset, tilt weights toward high-scorers while keeping risk budget.
3. **Thematic** — build portfolios concentrated on green/climate themes.

**Implementation in the machinery:**

$$
\min_{w} \tfrac12 w^\top\Sigma w - \lambda\big(w^\top\mu\big)
\quad \text{s.t.} \quad 1^\top w = 1,\; w^\top s \ge s_{\min},\; w\ge 0
$$

where $s$ = ESG scores vector, $s_{\min}$ = minimum portfolio ESG score. A leverage point in the applications paper: ESG tilt **does not necessarily sacrifice return**, and it can **decrease tail/volatility risk** in some settings — but the statistical evidence is mixed and horizon-dependent.

---

## 3. The applications paper's key structural lessons

- Monte Carlo + VaR is the standard quant toolkit for capital & tail assessment.
- **Rare events are the Achilles' heel** — models trained on normal data systematically underestimate the probability & size of crises (fat tails, jumps, correlation breakdowns under stress).
- Historical statistical relations are **non-stationary**; correlations spike to ~1 in crashes.
- Therefore: quant methods + judgment (stress tests, scenario overlays, ESG risk qualitative overlay).

---

## 4. Where quantitative models definitively added value

- **Diversification** (Markowitz) — provably lowers variance.
- **Derivatives pricing & hedging** — replication worked; the free risk-sharing is real.
- **Risk measurement standardization** — VaR/ES allow transparent risk budgeting & capital allocation.
- **Execution efficiency** — impact-aware algos.

---

## 5. Limitations (be honest about them)

| Limitation | Consequence |
|---|---|
| Model risk & misspecification | wrong hedge, wrong price |
| Rare/huge events | tails mis-priced |
| Non-stationarity | parameters drift |
| Data snooping | spurious edges |
| Liquidity/capacity | model works in backtest; can't scale |
| Behavioral deviation | people don't act like $\mathcal N(\mu,\Sigma)$ |

**The professional posture (echoed across sources):** models are *diagnostics and decision-support*, not crystal balls. Use them for *relative* comparison, calibrate with experience, and layer scenario awareness.

---

## 6. Worked mini-example — ESG-constrained risk allocation

```python
"""ESG-constrained minimum-variance (simplified) via scipy."""
from __future__ import annotations
import numpy as np
from scipy.optimize import minimize


def esg_min_var(mu: np.ndarray, cov: np.ndarray, esg: np.ndarray,
                esg_min: float, max_w: float = 0.2) -> np.ndarray:
    n = len(mu)
    def obj(w): return w @ cov @ w
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1},
            {"type": "ineq", "fun": lambda w: w @ esg - esg_min},
            {"type": "ineq", "fun": lambda w: max_w - w}]
    w0 = np.ones(n) / n
    res = minimize(obj, w0, bounds=[(0, 1)] * n, constraints=cons, method="SLSQP")
    return res.x


if __name__ == "__main__":
    np.random.seed(7)
    n = 6
    cov = np.eye(n) * 0.04 + np.full((n, n), 0.005)
    esg = np.array([90, 40, 70, 30, 80, 55])
    w = esg_min_var(np.full(n, 0.08), cov, esg, 60)
    print("weights:", np.round(w, 3), "esg_score:", round(float(w @ esg), 1))
```

---

## 7. Related

- [[quantitative-finance-foundations]] · [[risk-management-value-at-risk]] · [[portfolio-optimization-practice]] · [[model-selection-and-model-risk]] · [[forecasting-and-market-efficiency]]