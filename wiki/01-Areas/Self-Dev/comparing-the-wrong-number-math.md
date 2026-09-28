---
date: 2026-09-28
description: "Formal companion to 'Comparing the Wrong Number' — opportunity cost as a Lagrange shadow price, the study production function, diminishing marginal returns, Cobb-Douglas + Euler's theorem, and which study metric survives. The exam-relevant half."
tags: [self-dev, opportunity-cost, marginal-returns, production-function, cobb-douglas, eulers-theorem, lagrange-multipliers, shadow-price, microeconomics, engineering-math, bridge-page]
type: [youtube-distillation-math]
source_url: "https://www.youtube.com/watch?v=SliceDfqcH8"
source_channel: "avishi mishra"
last_updated: "2026-09-28"
confidence: high
relations:
  relates_to: "[[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]]"
  relates_to: "[[01-Areas/Engineering/engineering-math/module-3-homogeneous-functions|Eng-Math Module 3: Homogeneous Functions]]"
  relates_to: "[[01-Areas/Engineering/engineering-math/module-2-partial-differentiation|Eng-Math Module 2: Partial Differentiation]]"
---

## For future agent
The mathematical half of [[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]] (video `SliceDfqcH8`). Split out because it is a different job: the parent page is a self-dev argument, this one is a **cross-domain bridge** — the "diminishing returns" a productivity note treats as intuition is a derivable exam result in [[01-Areas/Engineering/engineering-math/module-3-homogeneous-functions|Eng-Math Module 3]] (Cobb-Douglas, marginal products, Euler's theorem) and [[01-Areas/Engineering/engineering-math/module-2-partial-differentiation|Module 2]] (Lagrange multiplier = shadow price). Staleness caveat: none — but the **maths is a vault extension**; the speaker gestures at "production function" and "diminishing marginal returns" without any formalisation, so nothing here is his claim beyond the quoted definitions. Notation note: $h$ = hours, $k$ = base knowledge/sleep/stress, $S$ = study output, $c$ = opportunity cost of an hour. Use for: "prove diminishing returns", "what's the shadow price of time", "Cobb-Douglas in plain English", "which study metric is valid".

# Comparing the Wrong Number — The Mathematics

Parent: [[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]] · Source: [youtube.com/watch?v=SliceDfqcH8](https://www.youtube.com/watch?v=SliceDfqcH8)

**Why this page exists.** A self-dev note that says "hour 7 is worth less than hour 1" and an engineering-math module that derives $\partial^2 S/\partial h^2 < 0$ are the *same fact*. The video names the economics but not the derivation. This page closes that gap so the claim can be cited in an exam answer, and so the productivity argument stops looking like a vibe.

| Symbol | Meaning |
|---|---|
| $h$ | hours of study (the **input** people track) |
| $k$ | base knowledge, sleep, stress (the **input** people forget) |
| $S(h,k)$ | study output — units covered, problems solved (**output**) |
| $MP_h$ | marginal product of an hour, $\partial S/\partial h$ |
| $c$ | opportunity cost of one hour, i.e. the **price tag** |

---

## 1. Opportunity cost is a shadow price

Opportunity cost (the parent page §1) is, formally, the value of the best forgone alternative. In optimisation language it is a **shadow price** — the Lagrange multiplier on the binding resource, which here is *time*.

Allocate a fixed time budget $T_{\text{total}}$ across actions $\{a\}$ to maximise utility:

$$\max_{\{a\}} \; U(a) \qquad \text{s.t.} \quad T_a + \sum_i T_{A_i} = T_{\text{total}}$$

Lagrangian (see [[01-Areas/Engineering/engineering-math/module-2-partial-differentiation|Module 2 § Lagrange multipliers]]):

$$\mathcal{L} = U(a) - \lambda\Big(T_a + \sum_i T_{A_i} - T_{\text{total}}\Big)$$

Then

$$\lambda = \frac{\partial U}{\partial T} \;=\; c$$

**$\lambda$ *is* the opportunity cost of an hour.** The first-order conditions say the optimum is where every action's marginal utility per hour is equal:

$$\frac{\partial U}{\partial T_a} = \frac{\partial U}{\partial T_{A_1}} = \frac{\partial U}{\partial T_{A_2}} = \lambda$$

### What that licenses you to say

At an interior optimum **one hour should not be worth more in the agency than in the library.** When it *is* — and for a student running a business it always is — that is not an error to be apologised for; it is a **revealed preference**, and $\lambda$ is the number you are allowed to look at.

This is also why the video's "purchase, not injustice" line is an accounting identity rather than a motivational trick: if you voluntarily buy the expensive alternative, the forgone output is a *cost*, and a cost is a budget question, which has an answer. An injustice does not.

---

## 2. The study production function

Model output as a production function in hours and base knowledge:

$$S(h, k) = f(h, k)$$

Marginal product of an hour:

$$MP_h = \frac{\partial S}{\partial h}$$

**Diminishing marginal returns** — the marginal product falls as you add more of the same input with everything else held fixed:

$$\frac{\partial^2 S}{\partial h^2} < 0 \quad\Longrightarrow\quad \frac{\partial MP_h}{\partial h} < 0 \quad\Longrightarrow\quad MP_h(1) > MP_h(7)$$

So the seventh hour is a strictly worse product than the first. Two consequences:

**(a) The comparison is on the wrong statistic.** Comparing someone's seven hours to your four compares the **total**, not the **return**:

$$\underbrace{h_A - h_B = 3}_{\text{what people compare}} \;\qquad\neq\qquad; \underbrace{\big[S_A - S_B\big] \;\text{vs}\; \big[c_A - c_B\big]}_{\text{what actually differs}}$$

**(b) The curve is personal, because $MP_h$ depends on $k$.** Sleep, stress and prior knowledge all shift the whole curve. A 6-hour night does not merely make you tired; it **re-prices the marginal hour**. This is the formal content of "that marginal curve is personal — it bends at a different point for each and every person."

---

## 3. Cobb-Douglas — where diminishing returns is *derived*, not assumed

A textbook study function is Cobb-Douglas:

$$S(h, k) = A\, h^{\beta} k^{\alpha}, \qquad 0 < \alpha, \beta < 1$$

**Step 1 — marginal products.**

$$MP_h = A\beta\, h^{\beta-1} k^{\alpha}, \qquad MP_k = A\alpha\, h^{\beta} k^{\alpha-1}$$

**Step 2 — diminishing returns falls out of the exponents.** Since $\beta - 1 < 0$ and $\alpha - 1 < 0$:

$$\frac{\partial MP_h}{\partial h} = A\beta(\beta-1)h^{\beta-2}k^{\alpha} < 0 \qquad\checkmark$$

Diminishing returns is **not an extra assumption** — it is implied by the functional form. This is the single cleanest way to answer "why does it flatten out?"

**Step 3 — returns to scale = degree of homogeneity.** $S$ is homogeneous of degree $\alpha + \beta$, so scaling both inputs by $t$ scales output by $t^{\alpha+\beta}$:

| $\alpha + \beta$ | Returns to scale | Meaning |
|---|---|---|
| $< 1$ | decreasing | doubling inputs less than doubles output |
| $= 1$ | constant (CRS) | doubling inputs exactly doubles output |
| $> 1$ | increasing | doubling inputs more than doubles output |

**Step 4 — Euler's theorem.** For a homogeneous function of degree $n$:

$$h \cdot \frac{\partial S}{\partial h} + k \cdot \frac{\partial S}{\partial k} = n \cdot S$$

Substituting $n = \alpha + \beta$ and the marginal products from Step 1:

$$h \cdot A\beta h^{\beta-1}k^{\alpha} + k \cdot A\alpha h^{\beta}k^{\alpha-1} = A h^{\beta}k^{\alpha}(\alpha + \beta) = (\alpha + \beta)\, S \qquad\checkmark$$

> **Exam pointers.** Full statement, proof of Euler's theorem, higher-order and converse forms, and the worked economics example: [[01-Areas/Engineering/engineering-math/module-3-homogeneous-functions|Eng-Math Module 3 — Homogeneous Functions]] (§2.2, Example 2). One-page version: [[01-Areas/Engineering/engineering-math/formula-sheet-am|formula sheet]]. The partial-derivative machinery ($MP$, $\partial^2/\partial h^2$, chain rule): [[01-Areas/Engineering/engineering-math/module-2-partial-differentiation|Module 2]].

---

## 4. Trap: you are not even on the same production function

The video compares "7 hours vs 4 hours" as if it were one comparable variable. Strictly, that comparison is undefined, and the reason matters more than the video's version of it.

Two people comparing study hours differ in **both** $k$ (prior knowledge, sleep, stress) **and** $f$ itself — one of them has an agency, the other does not. So:

$$S_A = f_A(h_A, k_A) \qquad S_B = f_B(h_B, k_B), \qquad f_A \neq f_B$$

Comparing $h_A$ to $h_B$ is therefore not comparing the same quantity twice. The two honest comparisons available are:

- **at your own margin:** $MP_h\big|_{h, k}$ vs $c_{\text{alt}}$ — the only comparison that is actually about a decision;
- **across people, on outputs only:** $S_A$ vs $S_B$ measured on a common scale (syllabus units), never $h_A$ vs $h_B$.

This strengthens the video's own point past what it argues: it is not only that you are comparing the wrong statistic, it is that the two sides of the comparison are not the same function.

---

## 5. Which study metric survives

The parent page's claim in one table. "Vanity metric" = an input that is cheap to inflate and carries no information about output.

| Candidate metric | Input / output | Comparable across people? | Verdict |
|---|---|---|---|
| Hours studied | **input** | No — depends on $MP_h$ at *that* hour | Vanity metric |
| Sessions started | **input** | No — same problem, worse signal | Vanity metric |
| Focus minutes / streak days | **input** | No | Vanity metric |
| Syllabus units covered | **output** | **Yes** — absolute, countable, syllabus-anchored | **Use this** |
| Problems solved / chapters done | **output** | Yes | **Use this** |
| CGPA | output, **lagged + confounded** | Weakly — credits, subject mix, marking scheme, and $k$ all differ | Context only |
| Followers / reach | **input-ish proxy** | No | Vanity metric |
| $MP_h$ on the last hour | **marginal** | Theoretically the best, practically unobserved | Aspirational |

**Why "units covered" wins — three independent reasons:**

1. **It is an output, not an input.** $S$ is what you actually produced; $h$ is what you fed in. This is the APO definition of productivity ($Productivity = Output/Input$) doing real work — see [[01-Areas/Self-Dev/productivity/overview|Productivity Overview]].
2. **It survives the diminishing-returns objection.** Because it measures $S$ rather than $h$, it is not distorted by the flattening curve.
3. **It supplies the objective standard that is missing.** It is anchored to a fixed, external syllabus, so it closes the gap that Festinger's theory says causes comparison in the first place.

**Defining "one unit" is the load-bearing step.** It must be absolute and countable *before* tracking starts — one lecture plus its notes, one chapter, one problem set. If the unit is defined by feeling, it is an input metric wearing an output metric's clothes, and the whole apparatus silently fails.

---

## 6. The $c = 0$ case

One boundary condition the framework must respect: an alternative is only worth pricing if it produces something.

$$c_{\text{alt}} = 0 \iff \text{the alternative produces no output}$$

Scrolling is the canonical $c = 0$ alternative. So "study vs. scroll" is not a hard trade at all, and any guilt framework built on it is measuring fiction. The asymmetry that matters:

| Alternative | $c_{\text{alt}}$ | Implication |
|---|---|---|
| Client deliverable / shipped build | **high, real** | A lower CGPA is a *purchase*. Defensible, and priceable. |
| Reels / doomscroll | **$0$** | Not a purchase at all — a leak. Cut the hour; don't reframe it. |

This is the formal content of "the math is a mirror, not a defence." A high real $c$ is a reason to feel fine about the trade; a $c = 0$ alternative is a reason to *cut* the hour, not a reason to keep it.

---

## Related

- [[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]] — the parent page: opportunity cost, Festinger, the units-not-hours argument, source registry, quote bank.
- [[01-Areas/Self-Dev/comparing-the-wrong-number-practice|Practice & Failure Modes]] — the 9 failure modes and the weekly drill these derivations exist to support.
- [[01-Areas/Engineering/engineering-math/module-3-homogeneous-functions|Eng-Math Module 3: Homogeneous Functions]] — Euler's theorem, Cobb-Douglas, marginal products, returns to scale.
- [[01-Areas/Engineering/engineering-math/module-2-partial-differentiation|Eng-Math Module 2: Partial Differentiation]] — marginal products, Lagrangian, constrained optimisation, shadow price.
- [[01-Areas/Engineering/engineering-math/formula-sheet-am|Engineering-Math Formula Sheet]] — the one-page version.
- [[01-Areas/Self-Dev/productivity/overview|Productivity Overview]] — $Productivity = Output/Input$, Pillar 7 (Completion & Review).
- [[01-Areas/Self-Dev/digital-wellness|Digital Wellness]] — why scrolling is the canonical $c = 0$ alternative.
- [[01-Areas/Self-Dev/how-to-study-hard|How To Study Hard]] — "compare only to your past self"; this page is the derivation of why peer comparison is invalid.
