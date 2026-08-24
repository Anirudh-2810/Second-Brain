---
module: "engineering-math"
topic: "Module 4: Linear Differential Equations — First-order to Cauchy-Euler"
tags: [differential-equations, linear-de, variation-of-parameters, cauchy-euler, constant-coefficients, complementary-function, particular-integral]
last_updated: "2026-08-18"
prerequisites: ["Single Variable Calculus", "Integration Techniques"]
---

# Module 4: Linear Differential Equations

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

---

### 1.1 Classification of Differential Equations

#### Master Classification Table

| Classification Criteria | Type | Definition | Example |
|------------------------|------|------------|---------|
| **By Kind** | Ordinary (ODE) | Involves derivatives with respect to **one** independent variable | `dy/dx + y = 0` |
| | Partial (PDE) | Involves partial derivatives with respect to **two or more** independent variables | `∂u/∂t = α²∂²u/∂x²` |
| **By Linearity** | Linear | Dependent variable `y` and its derivatives appear to the **first power** only; no products `y·y'` or nonlinear functions `sin(y)` | `y'' + 3y' + 2y = eˣ` |
| | Nonlinear | Any violation of the linearity conditions | `y'' + y² = 0` |
| **By Homogeneity** | Homogeneous | Every term contains `y` or a derivative of `y`; RHS = 0 | `y'' - 4y' + 4y = 0` |
| | Non-homogeneous | Contains terms that are functions of `x` alone (RHS ≠ 0) | `y'' - 4y' + 4y = e²ˣ` |
| **By Order** | First-order | Highest derivative is `dy/dx` | `dy/dx + 2y = x` |
| | Second-order | Highest derivative is `d²y/dx²` | `y'' + y = sin(x)` |
| | n-th order | Highest derivative is `dⁿy/dxⁿ` | `y⁽ⁿ⁾ + a₁y⁽ⁿ⁻¹⁾ + ... = f(x)` |
| **By Degree** | Degree 1 | Highest derivative appears to the first power | `(y'')² + y = 0` → degree 2 |
| | Degree 2 | Highest derivative appears squared | `(y'')² = x` |
| **By Coefficients** | Constant coefficients | All coefficients `aᵢ` are constants | `y'' + 5y' + 6y = 0` |
| | Variable coefficients | At least one coefficient is a function of `x` | `xy'' + y' + y = 0` |

#### Standard Forms Reference

| Form | Equation | Notes |
|------|----------|-------|
| **First-order linear** | `dy/dx + P(x)y = Q(x)` | Standard form for integrating factor method |
| **Second-order linear** | `a₂y'' + a₁y' + a₀y = f(x)` | `a₂ ≠ 0` |
| **Cauchy-Euler** | `aₙxⁿy⁽ⁿ⁾ + aₙ₋₁xⁿ⁻¹y⁽ⁿ⁻¹⁾ + ... + a₁xy' + a₀y = f(x)` | Variable coefficients with specific structure |
| **Exact** | `M(x,y)dx + N(x,y)dy = 0` where `∂M/∂y = ∂N/∂x` | Special integrable form |

---

### 1.2 First-Order Linear Differential Equation — Solution Flowchart

**Standard Form:** `dy/dx + P(x)y = Q(x)`

```
┌─────────────────────────────────────────────┐
│         START: dy/dx + P(x)y = Q(x)        │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│  STEP 1: Identify P(x) and Q(x)            │
│  Compare with standard form                 │
│  P(x) = coefficient of y                    │
│  Q(x) = RHS (function of x alone)          │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│  STEP 2: Compute Integrating Factor (I.F.)  │
│                                             │
│         I.F. = e^{∫P(x) dx}                │
│                                             │
│  Important: ∫P(x)dx without constant of    │
│  integration — any antiderivative works      │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│  STEP 3: Multiply both sides by I.F.        │
│                                             │
│  e^{∫Pdx}·(dy/dx) + e^{∫Pdx}·P(x)·y      │
│              = e^{∫Pdx}·Q(x)               │
│                                             │
│  LHS becomes: d/dx[ y · e^{∫Pdx} ]         │
│  This is the KEY insight                    │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│  STEP 4: Recognize product rule on LHS      │
│                                             │
│  d/dx[ y · I.F. ] = Q(x) · I.F.            │
│                                             │
│  This follows from:                         │
│  d/dx[y·e^{∫Pdx}] = y'·e^{∫Pdx}          │
│                    + y·e^{∫Pdx}·P(x)       │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│  STEP 5: Integrate both sides w.r.t. x     │
│                                             │
│  y · I.F. = ∫ Q(x) · I.F. dx + C          │
│                                             │
│  C = arbitrary constant of integration      │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│  STEP 6: Solve for y                        │
│                                             │
│        y = (1/I.F.) [ ∫ Q·I.F. dx + C ]   │
│                                             │
│  or equivalently:                           │
│  y = e^{-∫Pdx} [ ∫ Q·e^{∫Pdx} dx + C ]   │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│           COMPLETE SOLUTION                 │
│  y = y_c + y_p                             │
│  y_c = C·e^{-∫Pdx}  (complementary)       │
│  y_p = e^{-∫Pdx}·∫Q·e^{∫Pdx} dx (PI)    │
└─────────────────────────────────────────────┘
```

**Quick Reference — Common Integrating Factors:**

| P(x) | ∫P(x)dx | I.F. = e^{∫Pdx} |
|-------|---------|------------------|
| 1/x | ln x | x |
| -1/x | -ln x | 1/x |
| 2/x | 2 ln x | x² |
| n/x | n ln x | xⁿ |
| 1 | x | eˣ |
| -1 | -x | e⁻ˣ |
| 2x | x² | eˣ² |
| -2x | -x² | e⁻ˣ² |
| tan x | -ln(cos x) | sec x |
| cot x | ln(sin x) | sin x |
| sec x | ln|sec x + tan x| | sec x + tan x |

---

### 1.3 Higher-Order LDE with Constant Coefficients — Solution Flowchart

**Standard Form:** `aₙy⁽ⁿ⁾ + aₙ₋₁y⁽ⁿ⁻¹⁾ + ... + a₁y' + a₀y = f(x)`

For this module we focus primarily on `n = 2`: `a₂y'' + a₁y' + a₀y = f(x)`

```
┌──────────────────────────────────────────────────┐
│   START: a₂y'' + a₁y' + a₀y = f(x),  a₂ ≠ 0   │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 1: Write Auxiliary (Characteristic) Eq.    │
│                                                  │
│  Set f(x) = 0 (homogeneous version):             │
│                                                  │
│  a₂r² + a₁r + a₀ = 0                            │
│                                                  │
│  (or aₙrⁿ + aₙ₋₁rⁿ⁻¹ + ... + a₁r + a₀ = 0)   │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 2: Solve auxiliary equation for roots      │
│                                                  │
│  For quadratic: r = [-a₁ ± √(a₁²-4a₂a₀)]/2a₂  │
│                                                  │
│  Discriminant Δ = a₁² - 4a₂a₀                   │
└───────┬──────────────┬───────────────┬───────────┘
        │              │               │
        ▼              ▼               ▼
┌──────────────┐ ┌─────────────┐ ┌──────────────────┐
│  Δ > 0       │ │  Δ = 0      │ │  Δ < 0           │
│  Two REAL    │ │  One REPEATED│ │  COMPLEX roots   │
│  DISTINCT    │ │  real root   │ │  α ± iβ          │
│  roots       │ │  r₁ = r₂ = r│ │                  │
│  r₁, r₂     │ │             │ │  α = -a₁/(2a₂)   │
└──────┬───────┘ └──────┬──────┘ │  β = √|Δ|/(2a₂) │
       │                │        └────────┬──────────┘
       ▼                ▼                 ▼
┌──────────────────────────────────────────────────┐
│  STEP 3: Write Complementary Function (CF)       │
│                                                  │
│  CASE A (Distinct real roots r₁ ≠ r₂):          │
│    y_c = C₁e^{r₁x} + C₂e^{r₂x}                │
│                                                  │
│  CASE B (Repeated real root r₁ = r₂ = r):       │
│    y_c = (C₁ + C₂x)e^{rx}                      │
│                                                  │
│  CASE C (Complex roots α ± iβ):                 │
│    y_c = e^{αx}(C₁cos βx + C₂sin βx)          │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 4: Find Particular Integral (PI)           │
│                                                  │
│  Method depends on the form of f(x):            │
│                                                  │
│  Use operator D = d/dx, so:                      │
│  PI = (1/f(D)) · f(x)                           │
│                                                  │
│  Select PI form from Table 1.4                   │
│  Apply appropriate rule or expansion             │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 5: Apply boundary/initial conditions       │
│                                                  │
│  Use given ICs: y(x₀) = y₀, y'(x₀) = y₀'      │
│  Substitute into general solution                │
│  Solve system of equations for C₁, C₂           │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  COMPLETE GENERAL SOLUTION                       │
│                                                  │
│  y(x) = y_c(x) + y_p(x)                        │
│  y(x) = Complementary Function + Particular     │
│         Integral                                │
└──────────────────────────────────────────────────┘
```

---

### 1.4 Particular Integral — Selection & Rules Table

**Operator Notation:** `D = d/dx`, `D² = d²/dx²`, etc.
**Characteristic Polynomial:** `f(D) = aₙDⁿ + aₙ₋₁Dⁿ⁻¹ + ... + a₁D + a₀`

#### PI Selection Master Table

| f(x) Type | PI Form | Condition | Notes |
|-----------|---------|-----------|-------|
| `eᵃˣ` | `(1/f(a))eᵃˣ` | `f(a) ≠ 0` | Direct substitution of `D → a` |
| `eᵃˣ` (when `f(a) = 0`) | `x·(1/f'(a))eᵃˣ` | `f(a) = 0, f'(a) ≠ 0` | Multiply by `x` once |
| `eᵃˣ` (when `f(a) = f'(a) = 0`) | `x²·(1/f''(a))eᵃˣ` | `f(a) = f'(a) = 0, f''(a) ≠ 0` | Multiply by `x` twice |
| `sin(ax)` | `(1/f(-a²))sin(ax)` | Replace `D² → -a²` | Only even powers survive |
| `cos(ax)` | `(1/f(-a²))cos(ax)` | Replace `D² → -a²` | Only even powers survive |
| `sin(ax)` (resonance) | Apply `x` rule | `f(-a²) = 0` | Similar to exponential case |
| `xᵐ` (polynomial) | Binomial expansion of `(1/f(D))` | Expand for descending powers | Apply term by term |
| `eᵃˣ·V(x)` | `eᵃˣ·(1/f(D+a))V(x)` | Shift rule | Replace `D → D+a` |
| `x·eᵃˣ` | `x·(1/f(a))eᵃˣ` | If `f(a) ≠ 0` | Direct with x multiplier |
| `x·eᵃˣ` (resonance) | Use `(1/f(D))` expansion | If `f(a) = 0` | Expand and apply rules |
| `eᵃˣ·sin(bx)` | `eᵃˣ·(1/f(D+a))sin(bx)` | Shift then apply sin rule | Combine rules |
| `eᵃˣ·cos(bx)` | `eᵃˣ·(1/f(D+a))cos(bx)` | Shift then apply cos rule | Combine rules |

#### PI Rules for Polynomial f(x) = xᵐ

| Method | Formula | When to Use |
|--------|---------|-------------|
| **Negative Binomial** | `(1/(1+x))ⁿ = 1 - nx + n(n+1)/2!·x² - ...` | When `f(D) = (D-a)ⁿ` |
| **Direct Division** | Divide `xᵐ` by `f(D)` term by term | When `f(D)` has no constant term |
| **Complete Expansion** | Expand `1/f(D)` as power series in `D`, apply to `xᵐ` | General method |
| **Derivative Rule** | `(1/D)xᵐ = xᵐ⁺¹/(m+1)` | When `D` is a factor |
| **Repeated D** | `(1/D²)xᵐ = xᵐ⁺²/[(m+1)(m+2)]` | Extension of derivative rule |

#### "Multiply by x" Rule — Complete Decision Tree

```
f(x) = eᵃˣ  and  f(a) = 0  ?

    YES → f'(a) = 0 ?
                YES → f''(a) = 0 ?
                            YES → PI = x³·(1/f'''(a))eᵃˣ
                            NO  → PI = x²·(1/f''(a))eᵃˣ
                NO  → PI = x·(1/f'(a))eᵃˣ

    NO  → PI = (1/f(a))eᵃˣ

For sin(ax) or cos(ax):
    Replace D² → -a² in f(D). If result = 0, then
    differentiate the result and multiply by x, repeat until non-zero.
```

#### Operator Identities — Essential Reference

| Identity | Statement | Proof Sketch |
|----------|-----------|--------------|
| **Linearity** | `(1/f(D))[αu + βv] = α(1/f(D))u + β(1/f(D))v` | Superposition of operator |
| **Exponential shift** | `(1/f(D))[eᵃˣu] = eᵃˣ·(1/f(D+a))u` | Substitute `D → D+a` |
| **Inverse of D** | `(1/D)u = ∫u dx` | Integration is inverse of differentiation |
| **Inverse of (D-a)** | `(1/(D-a))u = eᵃˣ∫e⁻ᵃˣu dx` | Integrating factor technique |
| **Removal of root** | If `f(a) = 0`, factor `(D-a)` out | Write `f(D) = (D-a)g(D)` |
| **Partial fractions** | `1/[(D-a)(D-b)] = (1/(a-b))[(1/(D-a)) - (1/(D-b))]` | Partial fraction decomposition |

---

### 1.5 Variation of Parameters — Solution Flowchart

**Applicable to:** `y'' + P(x)y' + Q(x)y = f(x)` (or any second-order linear non-homogeneous)

```
┌──────────────────────────────────────────────────┐
│  START: Given y'' + P(x)y' + Q(x)y = f(x)       │
│  (or a₂y'' + a₁y' + a₀y = g(x))                │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 1: Solve homogeneous equation              │
│                                                  │
│  y'' + P(x)y' + Q(x)y = 0                       │
│  Find two linearly independent solutions:        │
│  y₁(x) and y₂(x)                                │
│                                                  │
│  CF = C₁y₁ + C₂y₂                               │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 2: Replace constants with functions        │
│                                                  │
│  Replace C₁ → u₁(x), C₂ → u₂(x)               │
│  Assume: y_p = u₁(x)·y₁(x) + u₂(x)·y₂(x)     │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 3: Impose constraint (first equation)      │
│                                                  │
│  u₁'·y₁ + u₂'·y₂ = 0                           │
│                                                  │
│  This simplifies the second derivative term      │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 4: Compute Wronskian                       │
│                                                  │
│         | y₁    y₂  |                           │
│  W =    |            | = y₁y₂' - y₂y₁'          │
│         | y₁'   y₂'  |                           │
│                                                  │
│  CRITICAL: W ≠ 0 for linear independence         │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 5: Set up system (second equation)         │
│                                                  │
│  Substitute y_p into original equation:          │
│  u₁'·y₁' + u₂'·y₂' = f(x)   [if monic form]   │
│                                                  │
│  Or: u₁'·y₁' + u₂'·y₂' = g(x)/a₂  [general]   │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 6: Solve for u₁' and u₂' using Cramer's   │
│                                                  │
│          | 0     y₂ |                           │
│  u₁' = -|          | / W = -y₂·f(x)/W          │
│          | f(x)  y₂'|                            │
│                                                  │
│          | y₁    0  |                           │
│  u₂' =  |          | / W = y₁·f(x)/W           │
│          | y₁'  f(x)|                            │
│                                                  │
│  General formulas:                               │
│  u₁' = -y₂·g(x) / (a₂·W)                       │
│  u₂' =  y₁·g(x) / (a₂·W)                       │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 7: Integrate to find u₁ and u₂             │
│                                                  │
│  u₁ = ∫ [-y₂·g(x)/(a₂·W)] dx                   │
│  u₂ = ∫ [ y₁·g(x)/(a₂·W)] dx                   │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 8: Construct particular integral           │
│                                                  │
│  y_p = u₁·y₁ + u₂·y₂                           │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  COMPLETE GENERAL SOLUTION                       │
│                                                  │
│  y = y_c + y_p                                  │
│  y = C₁y₁ + C₂y₂ + u₁y₁ + u₂y₂                │
└──────────────────────────────────────────────────┘
```

**Variation of Parameters vs. Undetermined Coefficients:**

| Feature | Variation of Parameters | Undetermined Coefficients |
|---------|------------------------|--------------------------|
| Applicable when | Any continuous `f(x)` | `f(x)` from limited set: `eᵃˣ, sin, cos, polynomials, products` |
| Requires | Finding CF first | Finding CF + guessing PI form |
| Computational effort | Often involves integrals | Usually algebraic (solving linear system) |
| Generality | Completely general | Restricted to specific `f(x)` types |
| Memory load | Must remember formulas | Must remember PI forms and rules |

---

### 1.6 Cauchy-Euler Equation — Solution Flowchart

**Standard Form (2nd order):** `x²y'' + axy' + by = 0` (homogeneous)
**Non-homogeneous:** `x²y'' + axy' + by = f(x)`

```
┌──────────────────────────────────────────────────┐
│  START: x²y'' + axy' + by = 0                   │
│  (Cauchy-Euler homogeneous equation)             │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 1: Assume trial solution                   │
│                                                  │
│  Try y = xᵐ                                     │
│                                                  │
│  Compute derivatives:                            │
│  y' = mxᵐ⁻¹                                     │
│  y'' = m(m-1)xᵐ⁻²                               │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 2: Substitute into equation                │
│                                                  │
│  x²·m(m-1)xᵐ⁻² + ax·mxᵐ⁻¹ + bxᵐ = 0         │
│                                                  │
│  Simplify: [m(m-1) + am + b]xᵐ = 0             │
│                                                  │
│  Since xᵐ ≠ 0 (for x > 0):                     │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 3: Write characteristic equation           │
│                                                  │
│  m(m-1) + am + b = 0                            │
│                                                  │
│  m² + (a-1)m + b = 0                            │
│                                                  │
│  (Quadratic in m)                                │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 4: Solve for m                             │
│                                                  │
│  m = [-(a-1) ± √((a-1)²-4b)] / 2               │
│                                                  │
│  Discriminant Δ = (a-1)² - 4b                   │
└───────┬──────────────┬───────────────┬───────────┘
        │              │               │
        ▼              ▼               ▼
┌──────────────┐ ┌─────────────┐ ┌──────────────────┐
│  Δ > 0       │ │  Δ = 0      │ │  Δ < 0           │
│  Two REAL    │ │  REPEATED   │ │  COMPLEX roots   │
│  DISTINCT    │ │  real root   │ │  α ± iβ          │
│  roots       │ │  m₁ = m₂ = m│ │                  │
│  m₁, m₂     │ │             │ │  α = (1-a)/2     │
└──────┬───────┘ └──────┬──────┘ │  β = √|Δ|/2     │
       │                │        └────────┬──────────┘
       ▼                ▼                 ▼
┌──────────────────────────────────────────────────┐
│  STEP 5: Write Complementary Function            │
│                                                  │
│  CASE A (m₁ ≠ m₂, real):                        │
│    y_c = C₁xᵐ¹ + C₂xᵐ²                        │
│                                                  │
│  CASE B (m₁ = m₂ = m, repeated):                │
│    y_c = (C₁ + C₂ln x)xᵐ                       │
│                                                  │
│  CASE C (m = α ± iβ, complex):                  │
│    y_c = xᵅ[C₁cos(β ln x) + C₂sin(β ln x)]   │
│                                                  │
│  NOTE: xᵅ = e^(α ln x)                         │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  STEP 6: For non-homogeneous case                │
│                                                  │
│  OPTION 1: Substitute x = eᵗ (transform to      │
│  constant coefficient equation in t)             │
│                                                  │
│  Then solve using methods from §1.3-1.4          │
│                                                  │
│  OPTION 2: Use Variation of Parameters           │
│  directly on the Cauchy-Euler form               │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  COMPLETE SOLUTION                               │
│  y(x) = y_c(x) + y_p(x)                        │
└──────────────────────────────────────────────────┘
```

**Alternative Method — Substitution x = eᵗ (t = ln x):**

```
┌──────────────────────────────────────────────────┐
│  SUBSTITUTION METHOD FOR CAUCHY-EULER             │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  Let x = eᵗ  (so t = ln x, x > 0)              │
│                                                  │
│  Then: dy/dx = (1/x)·dy/dt                      │
│        d²y/dx² = (1/x²)·(d²y/dt² - dy/dt)     │
│                                                  │
│  Operator form:                                  │
│  xD = Dₜ  (where Dₜ = d/dt)                    │
│  x²D² = Dₜ(Dₜ - 1)                             │
│  xⁿDⁿ = Dₜ(Dₜ-1)(Dₜ-2)...(Dₜ-n+1)           │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  The Cauchy-Euler equation transforms to:        │
│                                                  │
│  aₙ·Dₜ(Dₜ-1)(Dₜ-2)...(Dₜ-n+1)y               │
│  + aₙ₋₁·Dₜ(Dₜ-1)...(Dₜ-n+2)y                  │
│  + ... + a₁·Dₜy + a₀·y = f(eᵗ)                │
│                                                  │
│  This is a LINEAR DE with CONSTANT COEFFICIENTS  │
│  in the variable t!                              │
└────────────────────────┬─────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────┐
│  Solve using standard constant-coefficient      │
│  methods, then substitute back x = eᵗ           │
│  (i.e., t = ln x)                               │
└──────────────────────────────────────────────────┘
```

**General n-th Order Cauchy-Euler Operator Transformations:**

| Expression | Transforms to (in t) |
|------------|---------------------|
| `xy'` | `Dₜy` |
| `x²y''` | `Dₜ(Dₜ - 1)y` |
| `x³y'''` | `Dₜ(Dₜ - 1)(Dₜ - 2)y` |
| `xⁿy⁽ⁿ⁾` | `Dₜ(Dₜ - 1)...(Dₜ - n + 1)y` |

---

## 2. MATHEMATICAL FORMULATION & CORE THEOREMS

---

### 2.1 First-Order Linear Differential Equation

#### Standard Form and Complete Derivation

**Standard form:**
```
dy/dx + P(x)y = Q(x)
```

where `P(x)` and `Q(x)` are continuous functions on some interval `I`.

#### Complete Derivation Using Integrating Factor

**Step 1:** The integrating factor approach seeks a function `μ(x)` such that multiplying the entire equation by `μ(x)` makes the LHS an exact derivative.

Multiply by `μ(x)`:
```
μ(x)·(dy/dx) + μ(x)·P(x)·y = μ(x)·Q(x)
```

**Step 2:** We want the LHS to equal `d/dx[μ(x)·y]`. Expanding this:
```
d/dx[μ·y] = μ·(dy/dx) + y·(dμ/dx)
```

Comparing with our multiplied equation, we need:
```
dμ/dx = μ·P(x)
```

**Step 3:** This is a separable ODE for `μ`:
```
dμ/μ = P(x)dx
∫dμ/μ = ∫P(x)dx
ln|μ| = ∫P(x)dx
μ = e^{∫P(x)dx}
```

**Step 4:** Multiply original equation by `μ = e^{∫Pdx}`:
```
e^{∫Pdx}·(dy/dx) + e^{∫Pdx}·P(x)·y = e^{∫Pdx}·Q(x)
```

**Step 5:** Recognize LHS as product rule:
```
d/dx[y·e^{∫Pdx}] = Q(x)·e^{∫Pdx}
```

**Step 6:** Integrate both sides:
```
y·e^{∫Pdx} = ∫Q(x)·e^{∫Pdx} dx + C
```

**Step 7:** Solve for `y`:
```
y = e^{-∫Pdx} [∫Q(x)·e^{∫Pdx} dx + C]
```

This can be written as:
```
y = C·e^{-∫Pdx} + e^{-∫Pdx}·∫Q(x)·e^{∫Pdx} dx
    ─────────────    ──────────────────────────────
    Complementary        Particular Integral
    Function (y_c)              (y_p)
```

#### Existence and Uniqueness Theorem (First-Order)

**Theorem:** If `P(x)` and `Q(x)` are continuous on an open interval `I` containing `x₀`, then the initial value problem:
```
dy/dx + P(x)y = Q(x),    y(x₀) = y₀
```
has a unique solution defined on the entire interval `I`.

**Key points:**
- Continuity of `P` and `Q` is sufficient (not necessary)
- Solution exists on the entire interval where continuity holds
- The solution is unique — no two different solutions can pass through the same point
- This is a **global** existence theorem (no local restriction)

#### Symbol Reference Table — First-Order LDE

| Symbol | Meaning | Domain |
|--------|---------|--------|
| `y` | Dependent variable (unknown function) | Real-valued function of x |
| `x` | Independent variable | Real number in interval I |
| `P(x)` | Coefficient of y (known function) | Continuous on I |
| `Q(x)` | Forcing function / RHS (known function) | Continuous on I |
| `μ(x)` or I.F. | Integrating factor | `μ(x) = e^{∫Pdx}` |
| `C` | Arbitrary constant of integration | Any real number |
| `y_c` | Complementary function (homogeneous solution) | `C·e^{-∫Pdx}` |
| `y_p` | Particular integral (particular solution) | `e^{-∫Pdx}·∫Q·e^{∫Pdx}dx` |

---

### 2.2 Higher-Order Linear Differential Equations

#### General Form

The general `n`-th order linear differential equation:
```
aₙ(x)y⁽ⁿ⁾ + aₙ₋₁(x)y⁽ⁿ⁻¹⁾ + ... + a₁(x)y' + a₀(x)y = g(x)
```

**Monic form** (divide by `aₙ(x)`):
```
y⁽ⁿ⁾ + pₙ₋₁(x)y⁽ⁿ⁻¹⁾ + ... + p₁(x)y' + p₀(x)y = f(x)
```

where `pᵢ(x) = aᵢ(x)/aₙ(x)` and `f(x) = g(x)/aₙ(x)`.

For **constant coefficients**: `aᵢ` are all constants, giving:
```
aₙy⁽ⁿ⁾ + aₙ₋₁y⁽ⁿ⁻¹⁾ + ... + a₁y' + a₀y = f(x)
```

#### Existence and Uniqueness Theorem (Higher-Order)

**Theorem:** If `p₀(x), p₁(x), ..., pₙ₋₁(x)` and `f(x)` are continuous on an open interval `I` containing `x₀`, then the initial value problem:
```
y⁽ⁿ⁾ + pₙ₋₁(x)y⁽ⁿ⁻¹⁾ + ... + p₁y' + p₀y = f(x)
y(x₀) = y₀, y'(x₀) = y₀', ..., y⁽ⁿ⁻¹⁾(x₀) = y₀⁽ⁿ⁻¹⁾
```
has a unique solution defined on the entire interval `I`.

**Number of initial conditions required:** `n` (one for each derivative from 0 to n-1).

#### Superposition Principle

**Theorem (Homogeneous):** If `y₁` and `y₂` are solutions of the homogeneous equation:
```
aₙy⁽ⁿ⁾ + ... + a₁y' + a₀y = 0
```
then `C₁y₁ + C₂y₂` is also a solution for any constants `C₁, C₂`.

**Theorem (Non-homogeneous):** If `yₚ₁` is a particular solution of:
```
L[y] = f₁(x)
```
and `yₚ₂` is a particular solution of:
```
L[y] = f₂(x)
```
then `yₚ₁ + yₚ₂` is a particular solution of:
```
L[y] = f₁(x) + f₂(x)
```

**Corollary:** The general solution of `L[y] = f(x)` is `y = y_c + yₚ` where `y_c` is the general solution of `L[y] = 0` and `yₚ` is any particular solution of `L[y] = f(x)`.

#### Linear Independence and Wronskian

**Definition:** Functions `y₁, y₂, ..., yₙ` are **linearly independent** on interval `I` if:
```
c₁y₁ + c₂y₂ + ... + cₙyₙ = 0  for all x in I
```
implies `c₁ = c₂ = ... = cₙ = 0`.

**Wronskian** (for two functions):
```
W(y₁, y₂) = | y₁   y₂  |  = y₁y₂' - y₂y₁'
             | y₁'  y₂'  |
```

**Wronskian** (for `n` functions):
```
W(y₁,...,yₙ) = | y₁      y₂      ...  yₙ     |
               | y₁'     y₂'     ...  yₙ'    |
               | ...      ...     ...  ...    |
               | y₁⁽ⁿ⁻¹⁾ y₂⁽ⁿ⁻¹⁾ ... yₙ⁽ⁿ⁻¹⁾|
```

**Key theorems:**
1. If `W(y₁,...,yₙ)(x₀) ≠ 0` for some `x₀` in `I`, then `y₁,...,yₙ` are linearly independent on `I`.
2. If `y₁,...,yₙ` are solutions of an `n`-th order homogeneous linear ODE, then they are linearly independent if and only if `W ≠ 0` (for all `x` in `I`).
3. If `W = 0` at even a single point, then `W = 0` for all `x` in `I` (for solutions of the same ODE).

#### Fundamental Set of Solutions

**Definition:** If `y₁, y₂, ..., yₙ` are `n` linearly independent solutions of the homogeneous equation on interval `I`, they form a **fundamental set of solutions**, and:
```
y_c = C₁y₁ + C₂y₂ + ... + Cₙyₙ
```
is the **general solution** of the homogeneous equation.

---

### 2.3 Complementary Function — Complete Analysis

The complementary function (CF) is the general solution of the homogeneous equation:
```
aₙy⁽ⁿ⁾ + aₙ₋₁y⁽ⁿ⁻¹⁾ + ... + a₁y' + a₀y = 0
```

For second-order (`n = 2`): `a₂r² + a₁r + a₀ = 0`

#### CASE A: Real Distinct Roots (`r₁ ≠ r₂`, both real)

**Auxiliary equation has discriminant** `Δ > 0`

**Roots:**
```
r₁ = (-a₁ + √Δ) / (2a₂)
r₂ = (-a₁ - √Δ) / (2a₂)
```

**Complementary function:**
```
y_c = C₁e^{r₁x} + C₂e^{r₂x}
```

**Derivation:** Each root `r` of the auxiliary equation makes `e^{rx}` a solution. By superposition, `C₁e^{r₁x} + C₂e^{r₂x}` is also a solution. Linear independence follows from the Wronskian:
```
W = |e^{r₁x}  e^{r₂x} | = (r₂-r₁)e^{(r₁+r₂)x} ≠ 0  (since r₁ ≠ r₂)
    |r₁e^{r₁x} r₂e^{r₂x}|
```

#### CASE B: Real Repeated Roots (`r₁ = r₂ = r`)

**Auxiliary equation has discriminant** `Δ = 0`

**Root:** `r = -a₁/(2a₂)`

**Complementary function:**
```
y_c = (C₁ + C₂x)e^{rx}
```

**Derivation:** When `Δ = 0`, we get only one root, giving only one solution `y₁ = e^{rx}`. To find a second linearly independent solution, use **reduction of order** or the **method of annihilation**.

**Reduction of order approach:** Assume `y₂ = v(x)e^{rx}`. Substitute into the homogeneous equation:
```
Let y = v·e^{rx}
y' = v'e^{rx} + rv·e^{rx}
y'' = v''e^{rx} + 2rv'e^{rx} + r²v·e^{rx}
```

Substituting and using the fact that `e^{rx}` is a solution:
```
a₂·v''e^{rx} + (2a₂r + a₁)v'e^{rx} = 0
```

Since `2a₂r + a₁ = 0` (from the repeated root condition), we get:
```
a₂·v''e^{rx} = 0
```

Thus `v'' = 0`, giving `v = C₁ + C₂x`. The simplest non-trivial second solution is `v = x`, so `y₂ = xe^{rx}`.

**Wronskian check:**
```
W = |e^{rx}   xe^{rx}  | = e^{2rx} ≠ 0
    |re^{rx} (1+rx)e^{rx}|
```

#### CASE C: Complex Conjugate Roots (`r = α ± iβ`)

**Auxiliary equation has discriminant** `Δ < 0`

**Roots:**
```
α = -a₁/(2a₂)     (real part)
β = √|Δ|/(2a₂)    (imaginary part, β > 0)
```

**Complementary function:**
```
y_c = e^{αx}(C₁cos βx + C₂sin βx)
```

**Derivation:** The complex solutions are `e^{(α+iβ)x}` and `e^{(α-iβ)x}`. Using Euler's formula:
```
e^{(α+iβ)x} = e^{αx}(cos βx + i·sin βx)
e^{(α-iβ)x} = e^{αx}(cos βx - i·sin βx)
```

By superposition (allowing complex constants), the real and imaginary parts are also solutions:
```
y₁ = Re[e^{(α+iβ)x}] = e^{αx}cos βx
y₂ = Im[e^{(α+iβ)x}] = e^{αx}sin βx
```

**Wronskian check:**
```
W = |e^{αx}cos βx   e^{αx}sin βx  |
    |αe^{αx}cos βx - βe^{αx}sin βx  αe^{αx}sin βx + βe^{αx}cos βx|
    = β·e^{2αx} ≠ 0  (since β ≠ 0)
```

#### Summary Table — All Cases for Second-Order

| Case | Condition | Auxiliary Eq. | Roots | CF |
|------|-----------|---------------|-------|-----|
| Distinct real | `a₁² > 4a₂a₀` | `a₂r² + a₁r + a₀ = 0` | `r₁, r₂ ∈ ℝ, r₁ ≠ r₂` | `C₁e^{r₁x} + C₂e^{r₂x}` |
| Repeated real | `a₁² = 4a₂a₀` | `a₂r² + a₁r + a₀ = 0` | `r₁ = r₂ = r ∈ ℝ` | `(C₁ + C₂x)e^{rx}` |
| Complex conjugate | `a₁² < 4a₂a₀` | `a₂r² + a₁r + a₀ = 0` | `α ± iβ` | `e^{αx}(C₁cos βx + C₂sin βx)` |

---

### 2.4 Particular Integral Methods

#### Method of Undetermined Coefficients

For `f(D)y = f(x)` where `f(x)` belongs to a special class:

**Step 1:** Assume a PI form based on `f(x)` (see Table 1.4)
**Step 2:** Substitute into the equation
**Step 3:** Equate coefficients of like terms
**Step 4:** Solve for the undetermined coefficients
**Step 5:** Write the PI

#### Method of Inverse Operators

The particular integral can be written as:
```
yₚ = (1/f(D)) · f(x)
```

where `f(D) = aₙDⁿ + ... + a₁D + a₀`.

**Essential Operator Rules:**

| Rule | Formula | Example |
|------|---------|---------|
| **Rule 1** | `(1/D)·xⁿ = xⁿ⁺¹/(n+1)` | `(1/D)·x² = x³/3` |
| **Rule 2** | `(1/D)·eᵃˣ = (1/a)·eᵃˣ` | `(1/D)·e³ˣ = e³ˣ/3` |
| **Rule 3** | `(1/D)·sin(ax) = -(1/a)·cos(ax)` | `(1/D)·sin 2x = -cos 2x/2` |
| **Rule 4** | `(1/D)·cos(ax) = (1/a)·sin(ax)` | `(1/D)·cos 3x = sin 3x/3` |
| **Rule 5** | `(1/(D-a))·eᵃˣ = x·eᵃˣ` (resonance) | `(1/(D-2))·e²ˣ = xe²ˣ` |
| **Rule 6** | `(1/f(D))·eᵃˣ = (1/f(a))·eᵃˣ` if `f(a)≠0` | `(1/(D²+1))·e³ˣ = e³ˣ/10` |
| **Rule 7** | `(1/f(D²))·sin(ax) = (1/f(-a²))·sin(ax)` | `(1/(D²+4))·sin x = sin x/3` |
| **Rule 8** | `(1/f(D²))·cos(ax) = (1/f(-a²))·cos(ax)` | `(1/(D²+4))·cos x = cos x/3` |
| **Rule 9** | `eᵃˣ·(1/f(D))·V = eᵃˣ·(1/f(D+a))·V` | Shift rule |
| **Rule 10** | `(1/Dⁿ)·xᵐ = xᵐ⁺ⁿ/[(m+1)(m+2)...(m+n)]` | Extension of Rule 1 |

#### Special Cases — Removal of Factors

When `f(a) = 0` for `eᵃˣ`:

**Case 1:** `(D-a)` is a factor of `f(D)` but `(D-a)²` is not:
```
(1/f(D))·eᵃˣ = (1/[(D-a)·g(D)])·eᵃˣ
              = (1/g(D))·(1/(D-a))·eᵃˣ
              = (1/g(D))·x·eᵃˣ
              = x·(1/g(a))·eᵃˣ   [if g(a) ≠ 0]
```

**Case 2:** `(D-a)²` is a factor of `f(D)`:
```
(1/f(D))·eᵃˣ = x²·(1/f''(a))·eᵃˣ
```

**General rule:** If `(D-a)ᵏ` divides `f(D)` but `(D-a)ᵏ⁺¹` does not:
```
(1/f(D))·eᵃˣ = xᵏ·(1/[f⁽ᵏ⁾(a)/k!])·eᵃˣ
```

#### Complete Derivation: Inverse Operator (D-a)⁻¹

**Theorem:**
```
(1/(D-a))·u(x) = eᵃˣ · ∫e⁻ᵃˣ · u(x) dx
```

**Proof:**
We need to solve `(D-a)y = u(x)`, i.e., `y' - ay = u`.

This is a first-order linear ODE with integrating factor `e⁻ᵃˣ`:
```
d/dx[y·e⁻ᵃˣ] = u·e⁻ᵃˣ
y·e⁻ᵃˣ = ∫u·e⁻ᵃˣ dx
y = eᵃˣ·∫e⁻ᵃˣ·u dx
```

---

### 2.5 Variation of Parameters — Complete Derivation

#### Problem Setup

Given the second-order linear ODE:
```
y'' + P(x)y' + Q(x)y = f(x)        ... (*)
```

**Monic form** (leading coefficient = 1).

#### Step 1: Complementary Function

Solve the homogeneous equation:
```
y'' + P(x)y' + Q(x)y = 0
```

Let `y₁(x)` and `y₂(x)` be two linearly independent solutions. The CF is:
```
y_c = C₁y₁ + C₂y₂
```

#### Step 2: Assumption of Variation of Parameters

Replace constants with functions:
```
y_p = u₁(x)·y₁(x) + u₂(x)·y₂(x)
```

where `u₁(x)` and `u₂(x)` are unknown functions to be determined.

#### Step 3: Compute Derivatives

```
y_p' = u₁'y₁ + u₁y₁' + u₂'y₂ + u₂y₂'
```

**Impose the constraint** (to simplify):
```
u₁'y₁ + u₂'y₂ = 0              ... (I)
```

This reduces the first derivative to:
```
y_p' = u₁y₁' + u₂y₂'
```

**Second derivative:**
```
y_p'' = u₁'y₁' + u₁y₁'' + u₂'y₂' + u₂y₂''
```

#### Step 4: Substitute into original equation (*)

```
[u₁'y₁' + u₁y₁'' + u₂'y₂' + u₂y₂''] + P(x)[u₁y₁' + u₂y₂'] + Q(x)[u₁y₁ + u₂y₂] = f(x)
```

Rearranging:
```
u₁[y₁'' + P(x)y₁' + Q(x)y₁] + u₂[y₂'' + P(x)y₂' + Q(x)y₂] + u₁'y₁' + u₂'y₂' = f(x)
```

Since `y₁` and `y₂` satisfy the homogeneous equation:
```
y₁'' + P(x)y₁' + Q(x)y₁ = 0
y₂'' + P(x)y₂' + Q(x)y₂ = 0
```

This simplifies to:
```
u₁'y₁' + u₂'y₂' = f(x)          ... (II)
```

#### Step 5: System of Equations

We now have:
```
(I):   u₁'y₁ + u₂'y₂ = 0
(II):  u₁'y₁' + u₂'y₂' = f(x)
```

#### Step 6: Solve Using Cramer's Rule

The system matrix:
```
| y₁    y₂  | |u₁'|   |  0   |
|            | |   | = |      |
| y₁'   y₂' | |u₂'|   | f(x) |
```

Determinant = `W(y₁, y₂) = y₁y₂' - y₂y₁'` (Wronskian)

**For u₁':**
```
        | 0     y₂  |
u₁' =  |           | / W = (0·y₂' - y₂·f(x)) / W = -y₂·f(x)/W
        | f(x)  y₂' |
```

**For u₂':**
```
        | y₁    0  |
u₂' =  |          | / W = (y₁·f(x) - 0·y₁') / W = y₁·f(x)/W
        | y₁'  f(x)|
```

**Final formulas:**
```
u₁' = -y₂·f(x) / W(y₁, y₂)
u₂' =  y₁·f(x) / W(y₁, y₂)
```

#### Step 7: Integrate

```
u₁ = ∫[-y₂·f(x)/W] dx
u₂ = ∫[ y₁·f(x)/W] dx
```

#### Step 8: Particular Integral

```
y_p = u₁·y₁ + u₂·y₂
    = y₁·∫[-y₂·f(x)/W] dx + y₂·∫[y₁·f(x)/W] dx
```

#### Step 9: General Solution

```
y = C₁y₁ + C₂y₂ + y_p
```

#### Important Note on Non-Monic Form

For `a₂y'' + a₁y' + a₀y = g(x)`, the formulas become:
```
u₁' = -y₂·g(x) / (a₂·W)
u₂' =  y₁·g(x) / (a₂·W)
```

---

### 2.6 Cauchy-Euler Equations — Complete Analysis

#### Definition

A Cauchy-Euler equation of order `n` has the form:
```
aₙxⁿy⁽ⁿ⁾ + aₙ₋₁xⁿ⁻¹y⁽ⁿ⁻¹⁾ + ... + a₂x²y'' + a₁xy' + a₀y = f(x)
```

**Key feature:** The power of `x` matches the order of the derivative.

#### Second-Order Cauchy-Euler: Complete Analysis

**Standard form:** `x²y'' + axy' + by = 0`

#### Method 1: Direct Substitution y = xᵐ

**Step 1:** Assume `y = xᵐ` (for `x > 0`)
```
y' = mxᵐ⁻¹
y'' = m(m-1)xᵐ⁻²
```

**Step 2:** Substitute:
```
x²·m(m-1)xᵐ⁻² + a·x·mxᵐ⁻¹ + b·xᵐ = 0
m(m-1)xᵐ + amxᵐ + bxᵐ = 0
[m(m-1) + am + b]xᵐ = 0
```

**Step 3:** Since `xᵐ ≠ 0`:
```
m² + (a-1)m + b = 0     (characteristic equation)
```

**Step 4:** Solve for `m`:
```
m = [-(a-1) ± √((a-1)² - 4b)] / 2
```

**Step 5:** Three cases:

**Case A: Real distinct roots** `m₁ ≠ m₂`
```
y_c = C₁xᵐ¹ + C₂xᵐ²
```

**Case B: Repeated root** `m₁ = m₂ = m`
```
y_c = (C₁ + C₂ln x)xᵐ
```

**Case C: Complex roots** `m = α ± iβ`
```
y_c = xᵅ[C₁cos(β ln x) + C₂sin(β ln x)]
```

where `α = (1-a)/2` and `β = √|Δ|/2` with `Δ = (a-1)² - 4b`.

#### Method 2: Substitution x = eᵗ (Transformation to Constant Coefficients)

**The substitution:** Let `x = eᵗ`, so `t = ln x` (for `x > 0`).

**Chain rule transformations:**
```
dy/dx = (dy/dt)·(dt/dx) = (1/x)·(dy/dt)
```

For second derivative:
```
d²y/dx² = d/dx[(1/x)·dy/dt]
         = -(1/x²)·dy/dt + (1/x)·d²y/dt²·(1/x)
         = (1/x²)·(d²y/dt² - dy/dt)
```

**Operator form:**
Let `D = d/dx` and `Dₜ = d/dt`. Then:
```
xD = Dₜ
x²D² = Dₜ(Dₜ - 1)
```

**Verification:**
```
xy' = x·(dy/dx) = Dₜy = dy/dt          ✓
x²y'' = x²·(d²y/dx²) = d²y/dt² - dy/dt = Dₜ(Dₜ-1)y    ✓
```

**Transforming the Cauchy-Euler equation:**
```
x²y'' + axy' + by = 0
[Dₜ(Dₜ-1) + aDₜ + b]y = 0
[Dₜ² + (a-1)Dₜ + b]y = 0
```

This is a **second-order linear ODE with constant coefficients** in the variable `t`!

#### General n-th Order Transformation

For `xⁿDⁿ`:
```
xⁿDⁿ = Dₜ(Dₜ-1)(Dₜ-2)...(Dₜ-n+1)
```

**Verification for small n:**
```
n=1: xD = Dₜ                                ✓
n=2: x²D² = Dₜ(Dₜ-1) = Dₜ² - Dₜ            ✓
n=3: x³D³ = Dₜ(Dₜ-1)(Dₜ-2) = Dₜ³ - 3Dₜ² + 2Dₜ   ✓
```

#### Non-Homogeneous Cauchy-Euler

For `x²y'' + axy' + by = f(x)`:

**After substitution** `x = eᵗ`:
```
[Dₜ² + (a-1)Dₜ + b]y = f(eᵗ) = F(t)
```

Solve this constant-coefficient equation in `t`, then substitute back `t = ln x`.

**Example:** If `f(x) = xᵏ`, then after substitution `f(eᵗ) = eᵏᵗ`.

**Operator tables for Cauchy-Euler (after substitution):**

| Original (x) | Transformed (t) |
|--------------|-----------------|
| `xy'` | `Dₜy` |
| `x²y''` | `Dₜ²y - Dₜy` |
| `x³y'''` | `Dₜ³y - 3Dₜ²y + 2Dₜy` |
| `x⁴y⁽⁴⁾` | `Dₜ⁴y - 6Dₜ³y + 11Dₜ²y - 6Dₜy` |

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: First-Order LDE with Integrating Factor

**Solve:**
```
dy/dx + 2y = e⁻ˣ
```

#### Complete Solution

**Step 1: Identify P(x) and Q(x)**

Comparing with standard form `dy/dx + P(x)y = Q(x)`:
```
P(x) = 2
Q(x) = e⁻ˣ
```

**Step 2: Compute Integrating Factor**

```
I.F. = e^{∫P(x)dx} = e^{∫2dx} = e^{2x}
```

**Step 3: Multiply both sides by I.F.**

```
e^{2x}·(dy/dx) + e^{2x}·2y = e^{2x}·e⁻ˣ
```

LHS = `d/dx[y·e^{2x}]` (by product rule, verified)
RHS = `e^{2x}·e⁻ˣ = e^{2x-x} = eˣ`

**Step 4: Write as exact derivative**

```
d/dx[y·e^{2x}] = eˣ
```

**Step 5: Integrate both sides**

```
y·e^{2x} = ∫eˣ dx = eˣ + C
```

**Step 6: Solve for y**

```
y = e^{-2x}(eˣ + C)
y = eˣ·e^{-2x} + C·e^{-2x}
y = e⁻ˣ + Ce⁻²ˣ
```

**Verification:**
```
y = e⁻ˣ + Ce⁻²ˣ
y' = -e⁻ˣ - 2Ce⁻²ˣ

LHS: y' + 2y = (-e⁻ˣ - 2Ce⁻²ˣ) + 2(e⁻ˣ + Ce⁻²ˣ)
             = -e⁻ˣ - 2Ce⁻²ˣ + 2e⁻ˣ + 2Ce⁻²ˣ
             = e⁻ˣ
RHS: e⁻ˣ  ✓
```

**Final Answer:** **y = e⁻ˣ + Ce⁻²ˣ**

---

### Problem 2: Higher-Order LDE with Constant Coefficients

**Solve:**
```
y'' - 5y' + 6y = e²ˣ
```

#### Complete Solution

**Step 1: Write auxiliary equation**

For homogeneous part: `y'' - 5y' + 6y = 0`
```
r² - 5r + 6 = 0
```

**Step 2: Solve auxiliary equation**

```
r² - 5r + 6 = 0
(r - 2)(r - 3) = 0
r₁ = 2,  r₂ = 3
```

**Step 3: Write complementary function**

```
y_c = C₁e^{2x} + C₂e^{3x}
```

**Step 4: Find particular integral**

We need `PI = (1/(D² - 5D + 6))·e²ˣ`

Using the exponential rule: `(1/f(D))·eᵃˣ = (1/f(a))·eᵃˣ` if `f(a) ≠ 0`

Here `a = 2`, so:
```
f(2) = (2)² - 5(2) + 6 = 4 - 10 + 6 = 0
```

**Problem:** `f(2) = 0`, so we need the **multiply-by-x rule**.

**Step 5: Apply multiply-by-x rule**

When `f(a) = 0`, use:
```
(1/f(D))·eᵃˣ = x·(1/f'(D))·eᵃˣ evaluated at D = a
```

First, find `f'(D)`:
```
f(D) = D² - 5D + 6
f'(D) = 2D - 5
f'(2) = 2(2) - 5 = 4 - 5 = -1 ≠ 0
```

Therefore:
```
PI = x·(1/(-1))·e²ˣ = -x·e²ˣ
```

**Verification:**
```
y_p = -xe²ˣ
y_p' = -e²ˣ - 2xe²ˣ
y_p'' = -2e²ˣ - 2e²ˣ - 4xe²ˣ = -4e²ˣ - 4xe²ˣ

LHS: y_p'' - 5y_p' + 6y_p
    = (-4e²ˣ - 4xe²ˣ) - 5(-e²ˣ - 2xe²ˣ) + 6(-xe²ˣ)
    = -4e²ˣ - 4xe²ˣ + 5e²ˣ + 10xe²ˣ - 6xe²ˣ
    = (-4+5)e²ˣ + (-4+10-6)xe²ˣ
    = e²ˣ + 0
    = e²ˣ  ✓
```

**Step 6: General solution**

```
y = y_c + y_p
y = C₁e^{2x} + C₂e^{3x} - xe^{2x}
```

**Final Answer:** **y = C₁e^{2x} + C₂e^{3x} - xe^{2x}**

---

### Problem 3: Resonance Case — Multiply by x Rule

**Solve:**
```
y'' + 4y = sin(2x)
```

#### Complete Solution

**Step 1: Write auxiliary equation**

For homogeneous part: `y'' + 4y = 0`
```
r² + 4 = 0
r² = -4
r = ±2i
```

**Step 2: Write complementary function**

Complex roots: `α = 0, β = 2`
```
y_c = C₁cos(2x) + C₂sin(2x)
```

**Step 3: Find particular integral**

We need `PI = (1/(D² + 4))·sin(2x)`

Using the sine rule: replace `D² → -a²` where `a = 2`:
```
D² → -(2)² = -4

PI = (1/(-4 + 4))·sin(2x) = (1/0)·sin(2x)
```

**Problem:** Division by zero! This is the **resonance case**.

**Step 4: Apply resonance rule**

When `f(-a²) = 0` for `sin(ax)`, we use:
```
(1/f(D²))·sin(ax) = x·(1/f'(D²))·sin(ax)
```

where `f'(D²)` is the derivative of `f(D²)` with respect to `D²`.

Here `f(D²) = D² + 4`, so:
```
f'(D²) = 1 (derivative of D² + 4 with respect to D²)
```

Wait — this doesn't work directly. Let's use the correct approach.

**Correct approach for resonance with sin:**

Write `sin(2x) = Im[e^{i2x}]` (imaginary part of complex exponential).

Now solve: `PI = (1/(D² + 4))·e^{i2x}`

Here `a = 2i` (complex), and:
```
f(2i) = (2i)² + 4 = -4 + 4 = 0
```

So we need the multiply-by-x rule:
```
PI = x·(1/f'(D))·e^{i2x} at D = 2i
f'(D) = 2D
f'(2i) = 4i

PI = x·(1/(4i))·e^{i2x}
   = (x/(4i))·e^{i2x}
   = (x/(4i))·(cos 2x + i sin 2x)
   = (x/4)·(-i cos 2x + sin 2x)    [since 1/i = -i]
   = (x/4)·sin 2x - i·(x/4)·cos 2x
```

Taking the imaginary part:
```
PI = (x/4)·cos 2x
```

**Verification:**
```
y_p = (x/4)cos 2x
y_p' = (1/4)cos 2x - (x/2)sin 2x
y_p'' = -(1/2)sin 2x - (1/2)sin 2x - x cos 2x
      = -sin 2x - x cos 2x

LHS: y_p'' + 4y_p
    = (-sin 2x - x cos 2x) + 4·(x/4)cos 2x
    = -sin 2x - x cos 2x + x cos 2x
    = -sin 2x

Hmm, this gives -sin(2x), not sin(2x). Let me recalculate.

Actually, let me redo this more carefully.

y_p = (x/4)cos 2x
y_p' = (1/4)cos 2x + (x/4)(-2 sin 2x)
     = (1/4)cos 2x - (x/2)sin 2x

y_p'' = (1/4)(-2 sin 2x) - (1/2)sin 2x - (x/2)(2 cos 2x)
      = -(1/2)sin 2x - (1/2)sin 2x - x cos 2x
      = -sin 2x - x cos 2x

LHS: y_p'' + 4y_p = (-sin 2x - x cos 2x) + 4·(x/4)cos 2x
                  = -sin 2x - x cos 2x + x cos 2x
                  = -sin 2x

We need LHS = sin 2x, so we need to negate:

y_p = -(x/4)cos 2x

Let me verify:
y_p = -(x/4)cos 2x
y_p' = -(1/4)cos 2x + (x/2)sin 2x
y_p'' = (1/2)sin 2x + (1/2)sin 2x + x cos 2x
      = sin 2x + x cos 2x

LHS: y_p'' + 4y_p = (sin 2x + x cos 2x) + 4·(-(x/4)cos 2x)
                  = sin 2x + x cos 2x - x cos 2x
                  = sin 2x ✓
```

**Step 5: General solution**

```
y = y_c + y_p
y = C₁cos(2x) + C₂sin(2x) - (x/4)cos(2x)
```

**Final Answer:** **y = C₁cos(2x) + C₂sin(2x) - (x/4)cos(2x)**

---

### Problem 4: Variation of Parameters

**Solve:**
```
y'' - 2y' + y = eˣ/x²
```

#### Complete Solution

**Step 1: Write auxiliary equation**

For homogeneous part: `y'' - 2y' + y = 0`
```
r² - 2r + 1 = 0
(r - 1)² = 0
r = 1 (repeated)
```

**Step 2: Write complementary function**

```
y_c = (C₁ + C₂x)eˣ = C₁eˣ + C₂xeˣ
```

So `y₁ = eˣ` and `y₂ = xeˣ`.

**Step 3: Compute Wronskian**

```
W(y₁, y₂) = | eˣ    xeˣ   |
             | eˣ   (1+x)eˣ|

W = eˣ·(1+x)eˣ - xeˣ·eˣ
  = (1+x)e²ˣ - xe²ˣ
  = e²ˣ + xe²ˣ - xe²ˣ
  = e²ˣ
```

**Step 4: Set up Variation of Parameters**

Here `f(x) = eˣ/x²` and the equation is in monic form (coefficient of `y''` is 1).

**Formulas:**
```
u₁' = -y₂·f(x) / W
u₂' =  y₁·f(x) / W
```

**For u₁':**
```
u₁' = -(xeˣ)·(eˣ/x²) / e²ˣ
    = -(xeˣ·eˣ/x²) / e²ˣ
    = -(e²ˣ/x) / e²ˣ
    = -1/x
```

**For u₂':**
```
u₂' = (eˣ)·(eˣ/x²) / e²ˣ
    = (e²ˣ/x²) / e²ˣ
    = 1/x²
```

**Step 5: Integrate to find u₁ and u₂**

```
u₁ = ∫(-1/x) dx = -ln|x|

u₂ = ∫(1/x²) dx = ∫x⁻² dx = -1/x
```

**Step 6: Construct particular integral**

```
y_p = u₁·y₁ + u₂·y₂
    = (-ln|x|)·eˣ + (-1/x)·xeˣ
    = -eˣ·ln|x| - eˣ
    = -eˣ(ln|x| + 1)
```

**Step 7: General solution**

```
y = y_c + y_p
y = C₁eˣ + C₂xeˣ - eˣ(ln|x| + 1)
y = C₁eˣ + C₂xeˣ - eˣ·ln|x| - eˣ
```

Simplifying (absorbing the `-eˣ` into `C₁eˣ`):
```
y = C₁eˣ + C₂xeˣ - eˣ·ln|x|
```

where `C₁` is now an arbitrary constant (different from before).

**Verification:**
```
y = C₁eˣ + C₂xeˣ - eˣln x

y' = C₁eˣ + C₂(eˣ + xeˣ) - (eˣln x + eˣ/x)
   = C₁eˣ + C₂eˣ(1+x) - eˣln x - eˣ/x

y'' = C₁eˣ + C₂(eˣ(1+x) + eˣ) - (eˣln x + eˣ/x + eˣ/x - eˣ/x²)
    = C₁eˣ + C₂eˣ(2+x) - eˣln x - 2eˣ/x + eˣ/x²

LHS: y'' - 2y' + y
    = [C₁eˣ + C₂eˣ(2+x) - eˣln x - 2eˣ/x + eˣ/x²]
    - 2[C₁eˣ + C₂eˣ(1+x) - eˣln x - eˣ/x]
    + [C₁eˣ + C₂xeˣ - eˣln x]

Collecting C₁eˣ terms: (1-2+1) = 0
Collecting C₂eˣ terms: (2+x) - 2(1+x) + x = 2+x-2-2x+x = 0
Collecting eˣln x terms: -1+2-1 = 0
Collecting eˣ/x terms: -2+2 = 0
Collecting eˣ/x² terms: 1

LHS = eˣ/x² ✓
```

**Final Answer:** **y = C₁eˣ + C₂xeˣ - eˣ·ln|x|**

---

### Problem 5: Cauchy-Euler Equation

**Solve:**
```
x²y'' - 2xy' + 2y = x³
```

#### Complete Solution

**Step 1: Solve homogeneous equation**

For `x²y'' - 2xy' + 2y = 0`:

**Method: Assume y = xᵐ**

```
y = xᵐ
y' = mxᵐ⁻¹
y'' = m(m-1)xᵐ⁻²
```

Substitute:
```
x²·m(m-1)xᵐ⁻² - 2x·mxᵐ⁻¹ + 2xᵐ = 0
m(m-1)xᵐ - 2mxᵐ + 2xᵐ = 0
[m(m-1) - 2m + 2]xᵐ = 0
[m² - m - 2m + 2]xᵐ = 0
[m² - 3m + 2]xᵐ = 0
```

Since `xᵐ ≠ 0`:
```
m² - 3m + 2 = 0
(m - 1)(m - 2) = 0
m₁ = 1, m₂ = 2
```

**Step 2: Complementary function**

Real distinct roots `m₁ = 1, m₂ = 2`:
```
y_c = C₁x + C₂x²
```

**Step 3: Find particular integral**

The non-homogeneous term is `f(x) = x³`.

**Method: Undetermined Coefficients (after substitution x = eᵗ)**

Let `x = eᵗ`, so `t = ln x`.

Using the operator transformation:
```
x²D² = Dₜ(Dₜ - 1)
xD = Dₜ
```

The equation becomes:
```
[Dₜ(Dₜ-1) - 2Dₜ + 2]y = (eᵗ)³ = e³ᵗ
[Dₜ² - Dₜ - 2Dₜ + 2]y = e³ᵗ
[Dₜ² - 3Dₜ + 2]y = e³ᵗ
```

This is a constant-coefficient equation in `t`.

**Try PI = Ae³ᵗ:**
```
f(Dₜ) = Dₜ² - 3Dₜ + 2
f(3) = 9 - 9 + 2 = 2 ≠ 0
```

So:
```
PI = (1/2)·e³ᵗ = (1/2)x³
```

**Step 4: Transform back to x**

```
y_p = (1/2)x³
```

**Step 5: Verify**

```
y_p = (1/2)x³
y_p' = (3/2)x²
y_p'' = 3x

LHS: x²y_p'' - 2xy_p' + 2y_p
    = x²·3x - 2x·(3/2)x² + 2·(1/2)x³
    = 3x³ - 3x³ + x³
    = x³ ✓
```

**Step 6: General solution**

```
y = y_c + y_p
y = C₁x + C₂x² + (1/2)x³
```

**Final Answer:** **y = C₁x + C₂x² + (1/2)x³**

---

## 4. ENGINEERING APPLICATIONS MAP

---

### Application Domains Table

| Differential Equation Type | Engineering Application | Physical System | Key Parameters |
|---------------------------|------------------------|-----------------|----------------|
| **First-order LDE** `dy/dx + Py = Q` | RC Circuit charging/discharging | Capacitor voltage `V_c(t)` | R (resistance), C (capacitance) |
| | Newton's Law of Cooling | Temperature `T(t)` of cooling body | k (cooling constant), T_ambient |
| | Radioactive Decay | Mass `m(t)` of radioactive substance | λ (decay constant) |
| | First-order chemical kinetics | Concentration `C(t)` of reactant | k (rate constant) |
| | RL Circuit | Current `I(t)` in inductor | R (resistance), L (inductance) |
| | Logistic Population Growth | Population `P(t)` | r (growth rate), K (carrying capacity) |
| | Mixing Problems | Concentration `C(t)` in tank | Flow rate, tank volume |
| **Second-order constant coeff** `ay'' + by' + cy = f(x)` | RLC Circuit (series/parallel) | Charge `q(t)` or current `I(t)` | R, L, C values |
| | Spring-Mass-Damper System | Displacement `x(t)` | m (mass), c (damping), k (spring constant) |
| | Structural Vibration | Beam/column deflection | Material properties, geometry |
| | Seismic Response | Building sway during earthquake | Natural frequency, damping ratio |
| | Automobile Suspension | Shock absorber response | Spring constant, damping coefficient |
| | Electrical Oscillator | Voltage/current oscillation | L, C values |
| **Complex roots** (`underdamped case`) | RLC Circuit (underdamped) | Oscillatory charge/current | ω₀ (natural freq), ζ (damping ratio) |
| | Damped Harmonic Oscillator | Decaying oscillations | m, c, k |
| | AC Circuit Analysis | Impedance, phase angle | ω (frequency), R, L, C |
| | Vibration with Light Damping | Structural dynamics | Damping ratio ζ < 1 |
| **Cauchy-Euler** `x²y'' + axy' + by = f(x)` | Euler-Bernoulli Beam Theory | Beam deflection `w(x)` | Young's modulus, moment of inertia |
| | Variable Cross-Section Problems | Stress distribution in tapered beams | Cross-sectional area function |
| | Radial Heat Conduction | Temperature `T(r)` in cylindrical/spherical coordinates | Thermal conductivity, geometry |
| | Thick-Walled Pressure Vessel | Radial stress `σᵣ(r)` | Internal/external pressure, radii |
| | Steady-State Temperature Distribution | Temperature in annular regions | Boundary temperatures |
| **Variation of Parameters** `y'' + Py' + Qy = f(x)` | Forced Vibration Analysis | Response to arbitrary forcing | Forcing function `f(t)` |
| | Non-homogeneous Thermal Problems | Temperature with heat source | Source distribution `Q(x)` |
| | Beam Deflection Under Arbitrary Load | Deflection `y(x)` | Load distribution `w(x)` |
| | Electrical Networks with Time-Varying Sources | Current/voltage response | Source function `V(t)` or `I(t)` |
| | Control Systems | System response to arbitrary input | Transfer function |

### Detailed Application Examples

#### 1. RC Circuit — First-Order LDE

**Physical setup:** A capacitor `C` charges through a resistor `R` with a DC voltage source `V₀`.

**Governing equation:**
```
RC(dV_c/dt) + V_c = V₀
```

**Standard form:**
```
dV_c/dt + (1/RC)V_c = V₀/RC
```

**Identify:** `P = 1/RC`, `Q = V₀/RC`

**Integrating factor:** `I.F. = e^{t/(RC)}`

**Solution:**
```
V_c(t) = V₀(1 - e^{-t/(RC)})
```

**Time constant:** `τ = RC` — time to reach ~63.2% of final value

**Applications:** Timing circuits, filter design, sample-and-hold circuits, camera flashes

#### 2. Spring-Mass-Damper — Second-Order Constant Coefficient

**Physical setup:** Mass `m` on spring with constant `k`, damper with coefficient `c`, external force `F(t)`.

**Governing equation:**
```
m·x'' + c·x' + k·x = F(t)
```

**Standard form:**
```
x'' + 2ζω₀x' + ω₀²x = F(t)/m
```

where `ω₀ = √(k/m)` (natural frequency) and `ζ = c/(2√(mk))` (damping ratio).

**Solution behavior depends on ζ:**

| Damping Ratio | Root Type | Behavior |
|---------------|-----------|----------|
| `ζ > 1` (overdamped) | Real distinct | Exponential decay, no oscillation |
| `ζ = 1` (critically damped) | Real repeated | Fastest return to equilibrium |
| `0 < ζ < 1` (underdamped) | Complex conjugate | Decaying oscillations |
| `ζ = 0` (undamped) | Pure imaginary | Sustained oscillations |

#### 3. RLC Circuit — Second-Order Constant Coefficient

**Physical setup:** Series RLC circuit with voltage source `V(t)`.

**Governing equation (for charge q):**
```
L·q'' + R·q' + (1/C)·q = V(t)
```

**Or for current I = dq/dt:**
```
L·I'' + R·I' + (1/C)·I = V'(t)
```

**Natural frequency:** `ω₀ = 1/√(LC)`

**Damping:** `ζ = R/(2)·√(C/L)`

**Applications:** Radio tuning, bandpass filters, oscillators, impedance matching

#### 4. Euler-Bernoulli Beam — Cauchy-Euler Type

**Physical setup:** Beam with flexural rigidity `EI` under distributed load `w(x)`.

**Governing equation:**
```
EI·(d⁴w/dx⁴) = w(x)
```

For variable cross-section (varying `I`), this becomes a variable-coefficient equation. When `I(x) = I₀xⁿ` (power-law variation), the equation has Cauchy-Euler-like structure.

**Simplified case (point load):**
```
EI·(d²w/dx²) = M(x)
```

where `M(x)` is the bending moment. For circular cross-sections and radial problems, Cauchy-Euler equations naturally arise.

#### 5. Forced Vibration — Variation of Parameters

**When to use:** The external force `F(t)` is not a simple exponential, sine, or polynomial — e.g., impulsive loads, earthquake records, arbitrary periodic forces.

**Equation:**
```
m·x'' + c·x' + k·x = F(t)
```

**After finding CF** (homogeneous solution), use variation of parameters to find PI for arbitrary `F(t)`.

**Advantage:** Handles ANY continuous forcing function, not just the special forms required by undetermined coefficients.

### Application Parameter Quick Reference

| System | Parameter | Physical Meaning | Typical Units |
|--------|-----------|------------------|---------------|
| RC Circuit | τ = RC | Time constant | seconds |
| RLC Circuit | ω₀ = 1/√(LC) | Natural frequency | rad/s |
| RLC Circuit | ζ = R/(2)·√(C/L) | Damping ratio | dimensionless |
| RLC Circuit | Q = ω₀L/R | Quality factor | dimensionless |
| Spring-Mass | ω₀ = √(k/m) | Natural frequency | rad/s |
| Spring-Mass | ζ = c/(2√(mk)) | Damping ratio | dimensionless |
| Beam | EI | Flexural rigidity | N·m² |
| Thermal | α = k/(ρcₚ) | Thermal diffusivity | m²/s |

---

## APPENDIX: QUICK REFERENCE FORMULAS

---

### Master Formula Sheet

**First-order LDE:** `dy/dx + P(x)y = Q(x)`
```
I.F. = e^{∫Pdx}
y = e^{-∫Pdx}[∫Q·e^{∫Pdx}dx + C]
```

**Second-order homogeneous:** `ay'' + by' + cy = 0`

| Discriminant | Roots | Solution |
|-------------|-------|----------|
| `b²-4ac > 0` | `r₁, r₂` real | `C₁e^{r₁x} + C₂e^{r₂x}` |
| `b²-4ac = 0` | `r` repeated | `(C₁+C₂x)e^{rx}` |
| `b²-4ac < 0` | `α±iβ` | `e^{αx}(C₁cos βx + C₂sin βx)` |

**Cauchy-Euler:** `x²y'' + axy' + by = 0`

| Discriminant | Roots | Solution |
|-------------|-------|----------|
| `(a-1)²-4b > 0` | `m₁, m₂` real | `C₁x^{m₁} + C₂x^{m₂}` |
| `(a-1)²-4b = 0` | `m` repeated | `(C₁+C₂ln x)x^{m}` |
| `(a-1)²-4b < 0` | `α±iβ` | `x^{α}(C₁cos(βln x)+C₂sin(βln x))` |

**Variation of Parameters:**
```
u₁' = -y₂·f(x)/W
u₂' =  y₁·f(x)/W
W = y₁y₂' - y₂y₁'
y_p = u₁y₁ + u₂y₂
```

**PI Operator Rules:**
```
(1/f(D))eᵃˣ = (1/f(a))eᵃˣ  [if f(a)≠0]
(1/f(D))eᵃˣ = x(1/f'(a))eᵃˣ  [if f(a)=0, f'(a)≠0]
(1/f(D²))sin ax = (1/f(-a²))sin ax
(1/f(D²))cos ax = (1/f(-a²))cos ax
eᵃˣ(1/f(D))V = eᵃˣ(1/f(D+a))V
```

---

## CROSS-REFERENCES

- [[engineering-math/module-1-matrices|Module 1: Matrices]] — Systems of linear ODEs (ẋ = Ax) are solved by matrix diagonalization: eigenvalues give the characteristic roots, and eigenvectors form the transformation matrix P. The Cayley-Hamilton theorem enables computation of e^{At} without full diagonalization.
- [[engineering-math/module-3-homogeneous-functions|Module 3: Homogeneous Functions]] — The substitution y = vx for homogeneous ODEs (dy/dx = F(y/x)) relies on the property that a degree-0 homogeneous function depends only on the ratio y/x, reducing the ODE to separable form.
- [[engineering-math/module-5-complex-numbers|Module 5: Complex Numbers]] — Complex roots α ± iβ of the characteristic equation produce oscillatory solutions e^{αx}(C₁cos βx + C₂sin βx) via Euler's formula. De Moivre's theorem underlies the derivation of trigonometric identities used in PI computation.
- [[engineering-math/module-2-partial-differentiation|Module 2: Partial Differentiation]] — The variation of parameters method and exact differential conditions use partial derivatives; the Jacobian appears when transforming variables in higher-order systems.

*Module 4 of 5 — [[engineering-math/module-3-homogeneous-functions|← Module 3]] | [[engineering-math/module-5-complex-numbers|Module 5 →]]*

*End of Module 4: Linear Differential Equations*
