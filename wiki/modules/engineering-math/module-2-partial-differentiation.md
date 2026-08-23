---
module: "engineering-math"
topic: "Module 2: Partial Differentiation — Derivatives, Chain Rule, Maxima/Minima"
tags: [partial-differentiation, multivariable-calculus, chain-rule, jacobian, hessian, maxima-minima]
last_updated: "2026-08-18"
prerequisites: ["Single Variable Calculus", "Basic Algebra"]
---

# Module 2: Partial Differentiation

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

---

### 1.1 Partial Derivative Notation Table

A partial derivative measures how a multivariable function changes when **one** variable varies while all others are held constant. Multiple equivalent notations exist across mathematics, physics, and engineering.

| Symbol | Name | Read As | Order | Variables |
|--------|------|---------|-------|-----------|
| `∂f/∂x` | Partial of f with respect to x | "partial f partial x" | First | f(x, y) |
| `fₓ` | Subscript notation for f_x | "f sub x" | First | f(x, y) |
| `∂f/∂y` | Partial of f with respect to y | "partial f partial y" | First | f(x, y) |
| `fᵧ` | Subscript notation for f_y | "f sub y" | First | f(x, y) |
| `∂²f/∂x²` | Second partial of f w.r.t. x | "partial squared f partial x squared" | Second | f(x, y) |
| `fₓₓ` | Second subscript notation | "f sub x x" | Second | f(x, y) |
| `∂²f/∂y²` | Second partial of f w.r.t. y | "partial squared f partial y squared" | Second | f(x, y) |
| `fᵧᵧ` | Second subscript notation | "f sub y y" | Second | f(x, y) |
| `∂²f/∂x∂y` | Mixed partial: first y, then x | "partial squared f partial x partial y" | Second | f(x, y) |
| `fₓᵧ` | Mixed subscript (right-to-left) | "f sub x y" | Second | f(x, y) |
| `∂²f/∂y∂x` | Mixed partial: first x, then y | "partial squared f partial y partial x" | Second | f(x, y) |
| `fᵧₓ` | Mixed subscript notation | "f sub y x" | Second | f(x, y) |
| `∂ⁿf/∂xⁿ` | nth partial w.r.t. x | "partial n f partial x n" | nth | f(x, y) |
| `∇f` | Gradient vector | "del f" or "grad f" | First | f(x, y, z) |
| `∇²f` | Laplacian of f | "del squared f" or "Laplacian of f" | Second | f(x, y, z) |

**Key convention for mixed partials:** In the Leibniz notation `∂²f/∂x∂y`, differentiation proceeds **right to left**: first differentiate with respect to `y`, then with respect to `x`. In the subscript notation `fₓᵧ`, differentiation proceeds **left to right**: first with respect to `x`, then `y`. Thus `∂²f/∂x∂y = fᵧₓ` and `∂²f/∂y∂x = fₓᵧ`.

---

### 1.2 Higher Order Partial Derivatives

Higher order partial derivatives are obtained by repeated partial differentiation. For a function `f(x, y)` of two variables, there are four possible second-order partial derivatives.

**Second-order partial derivatives:**

| Derivative | Computation |
|------------|-------------|
| `∂²f/∂x² = fₓₓ` | Differentiate `fₓ` with respect to `x` again |
| `∂²f/∂y² = fᵧᵧ` | Differentiate `fᵧ` with respect to `y` again |
| `∂²f/∂x∂y = fᵧₓ` | Differentiate `fᵧ` with respect to `x` |
| `∂²f/∂y∂x = fₓᵧ` | Differentiate `fₓ` with respect to `y` |

**Third-order partial derivatives (2-variable case):**

There are 8 possible third-order partials:

```
fₓₓₓ,  fₓₓᵧ,  fₓᵧₓ,  fᵧₓₓ
fₓᵧᵧ,  fᵧₓᵧ,  fᵧᵧₓ,  fᵧᵧᵧ
```

**General pattern:** For a function of `n` variables, the number of `k`th-order partial derivatives is `nᵏ`.

#### Clairaut's Theorem (Symmetry of Second Derivatives)

**Statement:** If `f(x, y)` is defined on a domain `D ⊂ ℝ²` and both `fₓᵧ` and `fᵧₓ` exist and are **continuous** on `D`, then:

```
fₓᵧ = fᵧₓ      (always, on the domain)
```

equivalently:

```
∂²f     ∂²f
──── = ────
∂x∂y    ∂y∂x
```

**Conditions for equality:**
1. Both mixed partial derivatives must exist on the domain.
2. Both mixed partial derivatives must be **continuous** on the domain.

**Generalization:** For functions of `n` variables, mixed partial derivatives are equal regardless of the order of differentiation, provided all mixed partials of that order are continuous.

**Example where Clairaut's Theorem holds:**

Let `f(x, y) = x²y³ + cos(xy)`.

Compute `fₓᵧ`:
```
fₓ  = 2xy³ - y·sin(xy)
fₓᵧ = 6xy² - sin(xy) - xy·cos(xy)
```

Compute `fᵧₓ`:
```
fᵧ  = 3x²y² - x·sin(xy)
fᵧₓ = 6xy² - sin(xy) - xy·cos(xy)
```

Since both are equal: `fₓᵧ = fᵧₓ = 6xy² - sin(xy) - xy·cos(xy)`. ✓

**Example where Clairaut's Theorem fails:**

Consider the classic counterexample:

```
         ⎧ (x²y²)/(x² + y²)    if (x,y) ≠ (0,0)
f(x,y) = ⎨
         ⎩ 0                     if (x,y) = (0,0)
```

At the origin, one can show:
```
fₓᵧ(0,0) = 1
fᵧₓ(0,0) = 0
```

Thus `fₓᵧ ≠ fᵧₓ` at `(0, 0)`. The mixed partials are **not continuous** at the origin, so the hypotheses of Clairaut's Theorem are violated.

**Another counterexample:**

```
         ⎧ x³y - xy³     if (x,y) ≠ (0,0)
g(x,y) = ⎨
         ⎩ 0              if (x,y) = (0,0)
```

This function satisfies `gₓᵧ(0,0) = -3(0)² = 0` while `gᵧₓ(0,0) = 3(0)² = 0`. However, computing directly:
```
gₓ = 3x²y - y³     →  gₓᵧ = 3x² - 3y²
gᵧ = x³ - 3xy²     →  gᵧₓ = 3x² - 3y²
```

Both mixed partials equal `3x² - 3y²` everywhere, including the origin. This is an example where continuity holds and Clairaut applies trivially.

**Higher order mixed partials:** If all partial derivatives of order ≤ `k` are continuous, then all `k`th-order mixed partials are equal regardless of the order of differentiation.

---

### 1.3 Chain Rule Decision Flowchart

The chain rule is used to compute derivatives of composite functions where an intermediate variable depends on other independent variables. For `z = f(x, y)` where `x = x(s, t)` and `y = y(s, t)`:

```
                  z = f(x, y)
                 /            \
                /              \
          x = x(s,t)       y = y(s,t)
          /       \         /       \
         s         t       s         t
```

**Chain Rule Formulas:**

```
∂z     ∂f   ∂x     ∂f   ∂y
─── = ─── · ─── + ─── · ───
∂s     ∂x   ∂s     ∂y   ∂s

∂z     ∂f   ∂x     ∂f   ∂y
─── = ─── · ─── + ─── · ───
∂t     ∂x   ∂t     ∂y   ∂t
```

**ASCII Flowchart: Chain Rule Computation Process**

```
START
  │
  ▼
┌──────────────────────────────────────┐
│  Identify the composite function     │
│  z = f(x, y) where x = x(s, t),    │
│  y = y(s, t)                        │
└──────────────────┬───────────────────┘
                   │
                   ▼
         ┌─────────────────┐
         │ Draw dependency  │
         │ tree diagram     │
         │                 │
         │    z            │
         │   / \           │
         │  x   y          │
         │ / \ / \         │
         │ s  t s  t       │
         └────────┬────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│  For ∂z/∂s:                          │
│  Follow all paths from z to s:      │
│  Path 1: z → x → s: (∂f/∂x)(∂x/∂s)│
│  Path 2: z → y → s: (∂f/∂y)(∂y/∂s)│
│  Sum all path contributions          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  For ∂z/∂t:                          │
│  Follow all paths from z to t:      │
│  Path 1: z → x → t: (∂f/∂x)(∂x/∂t)│
│  Path 2: z → y → t: (∂f/∂y)(∂y/∂t)│
│  Sum all path contributions          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Compute each individual partial     │
│  derivative explicitly               │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Substitute and simplify             │
└──────────────────┬───────────────────┘
                   │
                   ▼
                DONE
```

**General Rule (n intermediate, m independent variables):**

If `w = f(x₁, x₂, ..., xₙ)` where each `xᵢ = xᵢ(u₁, u₂, ..., uₘ)`:

```
∂w         ∂f   ∂xᵢ
─── = Σ   ─── · ───
∂uⱼ  i=1   ∂xᵢ  ∂uⱼ
```

**Chain Rule Decision Table:**

| Scenario | Formula | # of Terms |
|----------|---------|------------|
| z = f(x), x = g(t) | dz/dt = (df/dx)(dx/dt) | 1 |
| z = f(x,y), x = x(t), y = y(t) | dz/dt = fₓ(dx/dt) + fᵧ(dy/dt) | 2 |
| z = f(x,y), x = x(s,t), y = y(s,t) | ∂z/∂s = fₓ(∂x/∂s) + fᵧ(∂y/∂s) | 2 per formula |
| w = f(x,y,z), x = x(r,s), y = y(r,s), z = z(r,s) | ∂w/∂r = fₓ(∂x/∂r) + fᵧ(∂y/∂r) + f_z(∂z/∂r) | 3 per formula |
| w = f(x₁,...,xₙ), xᵢ = xᵢ(u₁,...,uₘ) | ∂w/∂uⱼ = Σᵢ (∂f/∂xᵢ)(∂xᵢ/∂uⱼ) | n per formula |

---

### 1.4 Total Differential

The total differential captures the **infinitesimal change** in a function due to infinitesimal changes in all its independent variables simultaneously.

**For z = f(x, y):**

```
dz = (∂f/∂x) dx + (∂f/∂y) dy
```

**For w = f(x, y, z):**

```
dw = (∂f/∂x) dx + (∂f/∂y) dy + (∂f/∂z) dz
```

**General n-variable form:**

For `w = f(x₁, x₂, ..., xₙ)`:

```
              n
dw = Σ   (∂f/∂xᵢ) dxᵢ
            i=1
```

**Geometric interpretation:** The total differential `dz` represents the change in `z` along the tangent plane (linear approximation) at point `(x, y)` due to displacements `dx` and `dy`.

**Application — Linear Approximation:**

```
f(x + Δx, y + Δy) ≈ f(x, y) + fₓ(x,y)·Δx + fᵧ(x,y)·Δy
```

**Application — Error Propagation:**

If `z = f(x, y)` and `x` has error `Δx`, `y` has error `Δy`, then the error in `z` is approximately:

```
Δz ≈ |fₓ|·Δx + |fᵧ|·Δy     (maximum absolute error)
```

or in the root-mean-square sense:

```
Δz ≈ √[(fₓ·Δx)² + (fᵧ·Δy)²]
```

#### Exact Differentials

A differential expression `M(x,y) dx + N(x,y) dy` is **exact** if there exists a function `f(x, y)` such that:

```
∂f/∂x = M     and     ∂f/∂y = N
```

**Necessary and sufficient condition for exactness:**

```
∂M/∂y = ∂N/∂x
```

(provided `M` and `N` have continuous first partial derivatives on a simply connected domain.)

**Terminology table:**

| Term | Meaning | Example |
|------|---------|---------|
| Exact differential | `df = (∂f/∂x)dx + (∂f/∂y)dy` for some `f` | `2xy dx + x² dy = d(x²y)` |
| Inexact differential | Not the total differential of any function | `y dx - x dy` |
| Integrating factor | A function μ(x,y) making `μ(M dx + N dy)` exact | `1/x²` for `(y dx - x dy)/x²` |
| Conservative field | A field `F = (M, N)` that is the gradient of some potential | Gravitational field |

**Thermodynamics connection:** In thermodynamics, `dU = δQ - δW` where `U` is an exact differential (state function) but `δQ` and `δW` are inexact (path-dependent). The first law states that their difference is exact.

---

### 1.5 Maxima/Minima Decision Flowchart

**Problem:** Find and classify all critical points of `f(x, y)`.

**ASCII Flowchart: Complete Classification Process**

```
START
  │
  ▼
┌──────────────────────────────────────┐
│  Step 1: Find Critical Points        │
│  Solve simultaneously:              │
│    fₓ(x₀, y₀) = 0                  │
│    fᵧ(x₀, y₀) = 0                  │
│  This gives all critical points      │
│  (x₀, y₀)                          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 2: Compute Second Partial      │
│  Derivatives at each critical point  │
│    fₓₓ, fᵧᵧ, fₓᵧ                   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 3: Compute the Discriminant    │
│  (Jacobian of the Hessian)           │
│                                      │
│  D = fₓₓ · fᵧᵧ - (fₓᵧ)²          │
│                                      │
│  NOTE: D = det(H) where H is the    │
│  Hessian matrix                      │
└──────────────────┬───────────────────┘
                   │
                   ▼
          ┌────────────────┐
          │   D > 0 ?      │
          └────┬───────┬───┘
           YES │       │ NO
               ▼       ▼
    ┌──────────────┐  ┌────────────────┐
    │ D > 0:       │  │ D < 0 ?        │
    │ fₓₓ > 0 ?   │  └──┬─────────┬───┘
    └──┬──────┬───┘  YES │         │ NO (D = 0)
  YES  │  NO  │          ▼         ▼
       ▼      ▼    ┌──────────┐ ┌──────────┐
┌──────────┐ ┌──────────┐ │ SADDLE   │ │INCONCLUSIVE│
│ LOCAL    │ │ LOCAL    │ │ POINT    │ │  Use higher│
│ MINIMUM  │ │ MAXIMUM  │ │          │ │  order     │
│          │ │          │ └──────────┘ │  tests     │
└──────────┘ └──────────┘              └──────────┘
```

**Summary Decision Table:**

| Condition | Classification | Geometric Shape |
|-----------|---------------|-----------------|
| D > 0 and fₓₓ > 0 | **Local minimum** | Paraboloid opening upward |
| D > 0 and fₓₓ < 0 | **Local maximum** | Paraboloid opening downward |
| D < 0 | **Saddle point** | Hyperbolic paraboloid |
| D = 0 | **Inconclusive** | Higher order tests needed |

**Note:** When D > 0, `fₓₓ` and `fᵧᵧ` must have the same sign (since `fₓₓ · fᵧᵧ > D ≥ 0`). So checking `fₓₓ` alone suffices.

**For n-variable functions:** The Hessian matrix `H` generalizes the discriminant:

- If `H` is **positive definite** (all eigenvalues > 0): local minimum
- If `H` is **negative definite** (all eigenvalues < 0): local maximum
- If `H` is **indefinite** (eigenvalues of mixed sign): saddle point
- If `H` is **singular** (eigenvalue = 0): inconclusive

**Sylvester's criterion for positive definiteness:** All leading principal minors of `H` are positive.

**For f(x₁, x₂, ..., xₙ):** D becomes the determinant of the full Hessian matrix.

---

### 1.6 Lagrange Multipliers Flowchart

**Problem:** Optimize `f(x, y)` subject to the constraint `g(x, y) = 0`.

**ASCII Flowchart: Lagrange Multiplier Method**

```
START
  │
  ▼
┌──────────────────────────────────────┐
│  Step 1: Define the Lagrangian       │
│                                      │
│  L(x, y, λ) = f(x, y) - λ·g(x, y) │
│                                      │
│  λ is the Lagrange multiplier        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 2: Set up the system of        │
│  equations (3 equations, 3 unknowns) │
│                                      │
│  ∂L/∂x = fₓ(x,y) - λ·gₓ(x,y) = 0  │
│  ∂L/∂y = fᵧ(x,y) - λ·gᵧ(x,y) = 0  │
│  ∂L/∂λ = -g(x,y) = 0               │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 3: Solve the system            │
│                                      │
│  From first two equations:           │
│    fₓ = λ·gₓ  →  λ = fₓ/gₓ        │
│    fᵧ = λ·gᵧ  →  λ = fᵧ/gᵧ        │
│                                      │
│  Therefore: fₓ/gₓ = fᵧ/gᵧ           │
│  (provided gₓ, gᵧ ≠ 0)             │
│                                      │
│  This eliminates λ and gives         │
│  equations in x, y alone             │
│                                      │
│  Also use g(x,y) = 0                 │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 4: Find candidate points       │
│  (x₀, y₀, λ₀)                       │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 5: Classify candidates         │
│  Evaluate f at each candidate point  │
│  Compare values to determine max/min │
│                                      │
│  (Second derivative test for          │
│   Lagrange multipliers is more        │
│   complex; compare function values   │
│   directly when possible)            │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Step 6: Report extrema              │
│  Maximum value = f(x_max, y_max)     │
│  Minimum value = f(x_min, y_min)     │
└──────────────────┬───────────────────┘
                   │
                   ▼
                DONE
```

**Geometric interpretation:** At the constrained optimum, the gradient of `f` must be parallel to the gradient of `g`:

```
∇f = λ∇g
```

This means the level curve of `f` is tangent to the constraint curve `g = 0` at the optimum.

**Lagrange multipliers with multiple constraints:**

For optimizing `f(x₁, ..., xₙ)` subject to `g₁ = 0, g₂ = 0, ..., gₘ = 0`:

```
∇f = λ₁∇g₁ + λ₂∇g₂ + ... + λₘ∇gₘ
```

This gives `n + m` equations in `n + m` unknowns (`x₁, ..., xₙ, λ₁, ..., λₘ`).

**Method of Substitution vs Lagrange Multipliers:**

| Feature | Substitution | Lagrange Multipliers |
|---------|-------------|---------------------|
| Technique | Solve constraint for one variable, substitute | Form Lagrangian, solve system |
| Ease for simple constraints | Easier | Overkill |
| Ease for complex constraints | Difficult | More systematic |
| Geometric insight | Limited | Clear (∇f ∥ ∇g) |
| Multiple constraints | Very cumbersome | Systematic extension |
| Extends to n dimensions | Poorly | Naturally |

---

## 2. MATHEMATICAL FORMULATION & CORE THEOREMS

---

### 2.1 Partial Derivative Definitions (Limit Form)

**Definition (first-order partial derivative with respect to x):**

```
∂f        f(x + h, y) - f(x, y)
─── = lim ───────────────────────
∂x   h→0          h
```

**Definition (first-order partial derivative with respect to y):**

```
∂f        f(x, y + k) - f(x, y)
─── = lim ───────────────────────
∂y   k→0          k
```

**Key property:** When computing `∂f/∂x`, treat `y` as a constant. When computing `∂f/∂y`, treat `x` as a constant.

**Second-order partial derivative (limit form):**

```
∂²f         fₓ(x + h, y) - fₓ(x, y)
──── = lim ───────────────────────────
∂x²    h→0              h
```

**Mixed partial derivative (limit form):**

```
∂²f         fᵧ(x + h, y) - fᵧ(x, y)
──── = lim ───────────────────────────
∂x∂y   h→0              h
```

**Symbol reference table for Section 2.1:**

| Symbol | Meaning |
|--------|---------|
| `f` | Function of two or more variables |
| `x, y` | Independent variables |
| `h, k` | Small increments (differentials) in x and y respectively |
| `lim` | Limit as h → 0 (or k → 0) |
| `∂` | Partial differential operator (curly d) |

---

### 2.2 Euler's Theorem for Homogeneous Functions

A function `f(x₁, x₂, ..., xₙ)` is **homogeneous of degree k** if for all `t > 0`:

```
f(tx₁, tx₂, ..., txₙ) = tᵏ · f(x₁, x₂, ..., xₙ)
```

**Euler's Theorem (forward):**

If `f` is homogeneous of degree `k`, then:

```
x₁·(∂f/∂x₁) + x₂·(∂f/∂x₂) + ... + xₙ·(∂f/∂xₙ) = k · f(x₁, x₂, ..., xₙ)
```

or compactly:

```
Σ xᵢ · (∂f/∂xᵢ) = k · f
```

**Converse (Euler's Theorem — converse):**

If `Σ xᵢ · (∂f/∂xᵢ) = k · f`, then `f` is homogeneous of degree `k`.

**Proof sketch (forward direction):**

Let `φ(t) = f(tx₁, tx₂, ..., txₙ) = tᵏ · f(x₁, ..., xₙ)`.

Differentiate both sides with respect to `t`:

```
dφ/dt = Σ xᵢ · (∂f/∂xᵢ)(tx₁, ..., txₙ)
```

Also:

```
dφ/dt = k · tᵏ⁻¹ · f(x₁, ..., xₙ)
```

Setting `t = 1`:

```
Σ xᵢ · (∂f/∂xᵢ) = k · f(x₁, ..., xₙ)
```

**Symbol reference table for Section 2.2:**

| Symbol | Meaning |
|--------|---------|
| `k` | Degree of homogeneity |
| `t` | Scaling parameter (positive real) |
| `n` | Number of variables |
| `φ(t)` | Auxiliary function of t alone |
| `Σ` | Summation over i from 1 to n |

**Important special cases:**

| Degree k | Name | Example |
|----------|------|---------|
| k = 0 | Homogeneous of degree 0 | f(x,y) = x/y, f(x,y) = arctan(x/y) |
| k = 1 | Homogeneous of degree 1 (linearly homogeneous) | f(x,y) = √(xy), Cobb-Douglas with α+β=1 |
| k = 2 | Quadratic homogeneous | f(x,y) = x² + xy + y² |

**Example:** Let `f(x, y) = x³ + x²y + xy² + y³`.

Check homogeneity: `f(tx, ty) = t³x³ + t³x²y + t³xy² + t³y³ = t³·f(x, y)`. So `f` is homogeneous of degree 3.

Euler's Theorem: `x·fₓ + y·fᵧ = 3f`.

Verify:
```
fₓ = 3x² + 2xy + y²
fᵧ = x² + 2xy + 3y²

x·fₓ + y·fᵧ = x(3x² + 2xy + y²) + y(x² + 2xy + 3y²)
             = 3x³ + 2x²y + xy² + x²y + 2xy² + 3y³
             = 3x³ + 3x²y + 3xy² + 3y³
             = 3(x³ + x²y + xy² + y³)
             = 3f   ✓
```

---

### 2.3 Chain Rule — Full Derivation and Forms

#### Single-Variable Chain Rule (Recap)

If `z = f(x)` and `x = g(t)`, then:

```
dz     df   dg
─── = ─── · ───
dt     dx   dt
```

#### Two-Variable Chain Rule (Case 1: One independent variable)

If `z = f(x, y)` where `x = x(t)` and `y = y(t)`:

```
dz     ∂f   dx     ∂f   dy
─── = ─── · ─── + ─── · ───
dt     ∂x   dt     ∂y   dt
```

**Derivation:**

```
         f(x(t + Δt), y(t + Δt)) - f(x(t), y(t))
Δz = ─────────────────────────────────────────────
                        Δt

   = [f(x(t + Δt), y(t + Δt)) - f(x(t), y(t + Δt))] / Δt
   + [f(x(t), y(t + Δt)) - f(x(t), y(t))] / Δt

   → (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)    as Δt → 0
```

#### Two-Variable Chain Rule (Case 2: Two independent variables)

If `z = f(x, y)` where `x = x(s, t)` and `y = y(s, t)`:

```
∂z     ∂f   ∂x     ∂f   ∂y
─── = ─── · ─── + ─── · ───
∂s     ∂x   ∂s     ∂y   ∂s

∂z     ∂f   ∂x     ∂f   ∂y
─── = ─── · ─── + ─── · ───
∂t     ∂x   ∂t     ∂y   ∂t
```

**Matrix form:**

```
┌ ∂z/∂s ┐   ┌ ∂x/∂s  ∂y/∂s ┐   ┌ ∂f/∂x ┐
│       │ = │              │ · │       │
└ ∂z/∂t ┘   └ ∂x/∂t  ∂y/∂t ┘   └ ∂f/∂y ┘
```

or:

```
[∇ₜz] = Jᵀ · [∇ₓf]
```

where `J` is the Jacobian matrix of the transformation `(s,t) → (x,y)`.

#### Three-Variable Chain Rule

If `w = f(x, y, z)` where `x = x(u, v)`, `y = y(u, v)`, `z = z(u, v)`:

```
∂w     ∂f   ∂x     ∂f   ∂y     ∂f   ∂z
─── = ─── · ─── + ─── · ─── + ─── · ───
∂u     ∂x   ∂u     ∂y   ∂u     ∂z   ∂u

∂w     ∂f   ∂x     ∂f   ∂y     ∂f   ∂z
─── = ─── · ─── + ─── · ─── + ─── · ───
∂v     ∂x   ∂v     ∂y   ∂v     ∂z   ∂v
```

#### Higher-Order Chain Rules

**Second derivative chain rule (for `z = f(x,y)` with `x = x(t)`, `y = y(t)`):**

```
d²z     d   ⎡ ∂f   dx     ∂f   dy ⎤
──── = ─── ⎢ ─── · ─── + ─── · ─── ⎥
dt²    dt  ⎣ ∂x   dt     ∂y   dt ⎦

     = [∂²f/∂x² · (dx/dt)² + 2·∂²f/∂x∂y · (dx/dt)(dy/dt) + ∂²f/∂y² · (dy/dt)²]
     + [∂f/∂x · d²x/dt² + ∂f/∂y · d²y/dt²]
```

**Symbol reference table for Section 2.3:**

| Symbol | Meaning |
|--------|---------|
| `z, w` | Dependent variable(s) |
| `x, y` | Intermediate variables |
| `s, t, u, v` | Independent variables |
| `∇ₓf` | Gradient of f with respect to intermediate variables |
| `∇ₜz` | Gradient of z with respect to independent variables |
| `J` | Jacobian matrix of the transformation |
| `Δt` | Small change in t |

---

### 2.4 Implicit Function Theorem

**Statement:** If `F(x, y) = 0` and `F(x₀, y₀) = 0`, and `∂F/∂y ≠ 0` at `(x₀, y₀)`, then there exists a function `y = y(x)` defined near `x₀` such that:

```
F(x, y(x)) = 0    for all x near x₀
```

and:

```
dy     -∂F/∂x     -Fₓ
─── = ───────── = ────
dx     ∂F/∂y       Fᵧ
```

**Proof (informal):** Differentiate `F(x, y(x)) = 0` with respect to `x`:

```
∂F/∂x · (dx/dx) + ∂F/∂y · (dy/dx) = 0
Fₓ + Fᵧ · (dy/dx) = 0
dy/dx = -Fₓ / Fᵧ
```

**Implicit differentiation (for `F(x,y) = 0`):**

To find `∂y/∂x`: differentiate `F = 0` w.r.t. `x`, treating `y` as a function of `x`:

```
Fₓ + Fᵧ · (∂y/∂x) = 0  ⟹  ∂y/∂x = -Fₓ/Fᵧ
```

**Second derivative (implicit):**

```
∂²y     ∂     ⎡ -Fₓ ⎤
──── = ─── ⎢ ──── ⎥     (differentiating w.r.t. x, using chain rule)
∂x²    ∂x    ⎣  Fᵧ ⎦

     = -[Fₓₓ + 2Fₓᵧ·(dy/dx) + Fᵧᵧ·(dy/dx)²] / Fᵧ
```

where `Fₓₓ, Fₓᵧ, Fᵧᵧ` are evaluated at the point and `dy/dx = -Fₓ/Fᵧ`.

**For n equations in n+m unknowns:**

If `F₁(x₁,...,xₙ, y₁,...,yₘ) = 0, ..., Fₙ(x₁,...,xₙ, y₁,...,yₘ) = 0` and the Jacobian determinant `det(∂Fᵢ/∂yⱼ) ≠ 0`, then locally the `yⱼ` can be expressed as functions of the `xᵢ`.

**Symbol reference table for Section 2.4:**

| Symbol | Meaning |
|--------|---------|
| `F(x, y)` | Implicit function defining y implicitly |
| `Fₓ, Fᵧ` | Partial derivatives of F |
| `∂F/∂y ≠ 0` | Non-degeneracy condition |
| `Fₓₓ, Fₓᵧ, Fᵧᵧ` | Second partial derivatives of F |

---

### 2.5 Jacobian Matrix and Determinant

The Jacobian matrix captures all first-order partial derivatives of a vector-valued function. It is fundamental in change of variables, optimization, and differential geometry.

**Definition:**

Given `u = f(x, y, z)` and `v = g(x, y, z)`, the Jacobian matrix is:

```
        ┌ ∂u/∂x  ∂u/∂y  ∂u/∂z ┐
J =     │                      │
        └ ∂v/∂x  ∂v/∂y  ∂v/∂z ┘
```

**General definition:**

For `F: ℝⁿ → ℝᵐ` where `F(x₁, ..., xₙ) = (F₁, ..., Fₘ)`:

```
        ┌ ∂F₁/∂x₁  ∂F₁/∂x₂  ···  ∂F₁/∂xₙ ┐
        │ ∂F₂/∂x₁  ∂F₂/∂x₂  ···  ∂F₂/∂xₙ │
J(F) =  │    ·         ·              ·      │
        │    ·         ·              ·      │
        └ ∂Fₘ/∂x₁  ∂Fₘ/∂x₂  ···  ∂Fₘ/∂xₙ ┘

        Jᵢⱼ = ∂Fᵢ/∂xⱼ
```

**The Jacobian determinant (square case):**

When `m = n`, the determinant `det(J)` is called the **Jacobian determinant** (often just "the Jacobian").

For `u = u(x, y)`, `v = v(x, y)`:

```
        │ ∂u/∂x  ∂u/∂y │
J = det │              │ = (∂u/∂x)(∂v/∂y) - (∂u/∂y)(∂v/∂x)
        │ ∂v/∂x  ∂v/∂y │
```

**Notation:** `J = ∂(u, v)/∂(x, y)`.

**Properties of the Jacobian:**

| Property | Statement |
|----------|-----------|
| Chain rule | `J(F∘G) = J(F)·J(G)` (matrix product) |
| Inverse | `J(F⁻¹) = [J(F)]⁻¹` (if invertible) |
| Scaling of area/volume | `dA' = |J| · dA` |
| Coordinate transformation | `∫∫ f(x,y) dx dy = ∫∫ f(x(u,v),y(u,v)) · |J| du dv` |

**Coordinate Transformation Examples:**

**Polar coordinates:** `x = r cos θ`, `y = r sin θ`

```
        │ ∂x/∂r  ∂x/∂θ │   │ cos θ   -r sin θ │
J =     │              │ = │                   │ = r
        │ ∂y/∂r  ∂y/∂θ │   │ sin θ    r cos θ │
```

So `dx dy = |r| dr dθ = r dr dθ` (since `r ≥ 0`).

**Cylindrical coordinates:** `x = r cos θ`, `y = r sin θ`, `z = z`

```
J = det │ cos θ   -r sin θ   0 │
        │ sin θ    r cos θ   0 │ = r
        │  0         0       1 │
```

**Spherical coordinates:** `x = ρ sin φ cos θ`, `y = ρ sin φ sin θ`, `z = ρ cos φ`

```
J = ρ² sin φ
```

So `dx dy dz = ρ² sin φ dρ dφ dθ`.

**Inverse Function Theorem:**

If `F: ℝⁿ → ℝⁿ` is continuously differentiable and `J(F)(a) ≠ 0` at a point `a`, then `F` is locally invertible near `a`, and:

```
J(F⁻¹)(b) = [J(F)(a)]⁻¹    where b = F(a)
```

**Symbol reference table for Section 2.5:**

| Symbol | Meaning |
|--------|---------|
| `J` | Jacobian matrix or determinant |
| `∂(u,v)/∂(x,y)` | Jacobian determinant notation |
| `det` | Determinant |
| `J(F)` | Jacobian matrix of function F |
| `|J|` | Absolute value of Jacobian determinant |
| `ρ, θ, φ` | Spherical coordinates (radius, azimuthal angle, polar angle) |
| `r, θ` | Polar coordinates (radius, angle) |

---

### 2.6 Hessian Matrix

The Hessian matrix of a scalar-valued function is the matrix of all second-order partial derivatives. It encodes the local curvature of the function and is central to second-order optimization.

**Definition:**

For `f: ℝⁿ → ℝ`, the Hessian matrix `H` (or `∇²f`) has entries:

```
Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ
```

**For f(x, y):**

```
        ┌ ∂²f/∂x²    ∂²f/∂x∂y ┐
H(f) =  │                      │
        └ ∂²f/∂y∂x   ∂²f/∂y²  ┘

       = ┌ fₓₓ  fₓᵧ ┐
         │          │
         └ fᵧₓ  fᵧᵧ ┘
```

By Clairaut's Theorem, `H` is symmetric: `fₓᵧ = fᵧₓ` (when continuous).

**For f(x, y, z):**

```
        ┌ fₓₓ  fₓᵧ  fₓz ┐
H(f) =  │ fᵧₓ  fᵧᵧ  fᵧz │
        │ fzₓ  fzᵧ  fzz ┘
```

**Properties of the Hessian:**

| Property | Statement |
|----------|-----------|
| Symmetry | H = Hᵀ (by Clairaut's Theorem) |
| Chain rule | H(f∘g) involves first and second derivatives |
| Invariance | Hessian transforms covariantly under coordinate changes |

**Classification via eigenvalues:**

Let `λ₁, λ₂, ..., λₙ` be the eigenvalues of `H`.

| Eigenvalue Condition | Classification | Geometric Meaning |
|----------------------|----------------|-------------------|
| All `λᵢ > 0` | Positive definite | All principal curvatures positive (bowl shape) |
| All `λᵢ < 0` | Negative definite | All principal curvatures negative (hill shape) |
| Mixed signs | Indefinite | Saddle-type curvatures |
| Some `λᵢ = 0` | Positive/negative semi-definite or singular | Flat directions |
| All `λᵢ ≥ 0` | Positive semi-definite | Non-negative curvature in all directions |
| All `λᵢ ≤ 0` | Negative semi-definite | Non-positive curvature in all directions |

**Classification via leading principal minors:**

Let `Mₖ` denote the `k`th leading principal minor (determinant of the top-left `k × k` submatrix).

| Condition | Classification |
|-----------|----------------|
| `M₁ > 0, M₂ > 0, ..., Mₙ > 0` | Positive definite |
| `(-1)ᵏ Mₖ > 0` for all k | Negative definite |
| Neither of the above | Indefinite or semi-definite |

**For the 2×2 case (f(x,y)):**

```
M₁ = fₓₓ
M₂ = det(H) = fₓₓ · fᵧᵧ - (fₓᵧ)²  =  D (the discriminant)
```

| M₁ | M₂ | Classification |
|----|----|----------------|
| > 0 | > 0 | Positive definite → local minimum |
| < 0 | > 0 | Negative definite → local maximum |
| any | < 0 | Indefinite → saddle point |
| any | = 0 | Inconclusive |

**Second derivative test for f(x, y) using the Hessian:**

At a critical point `(x₀, y₀)` (where `fₓ = fᵧ = 0`):

```
D = fₓₓ(x₀,y₀) · fᵧᵧ(x₀,y₀) - [fₓᵧ(x₀,y₀)]²
```

- `D > 0` and `fₓₓ > 0` → local minimum
- `D > 0` and `fₓₓ < 0` → local maximum
- `D < 0` → saddle point
- `D = 0` → test is inconclusive

**Relationship to curvature:**

For a surface `z = f(x, y)`, the Gaussian curvature `K` and mean curvature `H` are related to the Hessian:

```
K = (fₓₓ · fᵧᵧ - fₓᵧ²) / (1 + fₓ² + fᵧ²)²    =  D / (1 + |∇f|²)²

H = [fₓₓ(1 + fᵧ²) - 2fₓfᵧfₓᵧ + fᵧᵧ(1 + fₓ²)] / [2(1 + fₓ² + fᵧ²)^(3/2)]
```

**Symbol reference table for Section 2.6:**

| Symbol | Meaning |
|--------|---------|
| `H(f)` or `∇²f` | Hessian matrix of f |
| `Hᵢⱼ` | Element (i,j) of the Hessian |
| `λᵢ` | Eigenvalues of H |
| `Mₖ` | kth leading principal minor |
| `D` | Discriminant (= det(H) for 2×2 case) |
| `K` | Gaussian curvature |
| `H` (curvature) | Mean curvature (not to be confused with Hessian) |
| `∇²f` | Laplacian of f (= trace of Hessian) |

---

### 2.7 Constrained Optimization — Full Derivation

#### Method of Lagrange Multipliers (Detailed)

**Problem formulation:**

```
Optimize f(x₁, x₂, ..., xₙ)
Subject to: g₁(x₁, ..., xₙ) = 0, ..., gₘ(x₁, ..., xₙ) = 0
```

where `m < n`.

**Lagrangian:**

```
L(x₁, ..., xₙ, λ₁, ..., λₘ) = f(x₁, ..., xₙ) - Σⱼ λⱼ gⱼ(x₁, ..., xₙ)
```

**First-order necessary conditions:**

```
∂L/∂xᵢ = ∂f/∂xᵢ - Σⱼ λⱼ (∂gⱼ/∂xᵢ) = 0    for i = 1, ..., n
∂L/∂λⱼ = -gⱼ(x₁, ..., xₙ) = 0              for j = 1, ..., m
```

In vector form:

```
∇f = λ₁∇g₁ + λ₂∇g₂ + ... + λₘ∇gₘ
g₁ = 0, g₂ = 0, ..., gₘ = 0
```

This gives `n + m` equations in `n + m` unknowns.

**Geometric interpretation (single constraint):**

At the constrained extremum, `∇f` is perpendicular to the constraint surface `g = 0`, hence parallel to `∇g`.

The level curve of `f` is tangent to the constraint curve `g = 0`.

**Method of substitution vs. Lagrange multipliers comparison:**

| Scenario | Preferred Method |
|----------|-----------------|
| Simple constraint, e.g., x + y = 1 | Substitution |
| Circular constraint, e.g., x² + y² = 1 | Lagrange multipliers |
| Multiple constraints | Lagrange multipliers |
| Complex constraint, e.g., implicit | Lagrange multipliers |
| Need geometric insight | Lagrange multipliers |

#### Second-Order Conditions (Lagrange Multipliers)

For a single constraint `g(x, y) = 0`, form the bordered Hessian:

```
        ┌ 0     gₓ    gᵧ  ┐
H̄ =    │ gₓ   fₓₓ   fₓᵧ │
        │ gᵧ   fᵧₓ   fᵧᵧ ┘
```

**Classification (single constraint, 2 variables):**

| Condition | Classification |
|-----------|----------------|
| `det(H̄) > 0` | Local maximum |
| `det(H̄) < 0` | Local minimum |

**For two constraints `g₁ = 0`, `g₂ = 0` (n = 3 variables), the bordered Hessian is 5×5:**

```
        ┌ 0   0   g₁ₓ  g₁ᵧ  g₁z ┐
        │ 0   0   g₂ₓ  g₂ᵧ  g₂z │
H̄ =    │ g₁ₓ g₂ₓ fₓₓ  fₓᵧ  fₓz │
        │ g₁ᵧ g₂ᵧ fᵧₓ  fᵧᵧ  fᵧz │
        └ g₁z g₂z fzₓ  fzᵧ  fzz ┘
```

The sign of `det(H̄)` alternates for min/max starting from `(-1)ᵐ` where `m` is the number of constraints.

**Symbol reference table for Section 2.7:**

| Symbol | Meaning |
|--------|---------|
| `L` | Lagrangian function |
| `λᵢ` | Lagrange multipliers |
| `∇f` | Gradient of objective function |
| `∇gⱼ` | Gradient of jth constraint |
| `H̄` | Bordered Hessian matrix |
| `m` | Number of constraints |
| `n` | Number of variables |
| `det(H̄)` | Determinant of bordered Hessian |

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: First and Second Order Partial Derivatives

**Problem:** Find all first and second order partial derivatives of:

```
f(x, y) = x³y² + eˣʸ + sin(xy)
```

**Solution:**

**Step 1: First-order partial derivative with respect to x (fₓ)**

Treat `y` as a constant:

```
fₓ = ∂/∂x [x³y² + eˣʸ + sin(xy)]
   = 3x²y² + y·eˣʸ + y·cos(xy)
```

**Step 2: First-order partial derivative with respect to y (fᵧ)**

Treat `x` as a constant:

```
fᵧ = ∂/∂y [x³y² + eˣʸ + sin(xy)]
   = 2x³y + x·eˣʸ + x·cos(xy)
```

**Step 3: Second-order partial derivative fₓₓ**

Differentiate `fₓ` with respect to `x`:

```
fₓₓ = ∂/∂x [3x²y² + y·eˣʸ + y·cos(xy)]
     = 6xy² + y²·eˣʸ - y²·sin(xy)
```

**Step 4: Second-order partial derivative fᵧᵧ**

Differentiate `fᵧ` with respect to `y`:

```
fᵧᵧ = ∂/∂y [2x³y + x·eˣʸ + x·cos(xy)]
     = 2x³ + x²·eˣʸ - x²·sin(xy)
```

**Step 5: Mixed partial derivative fₓᵧ**

Differentiate `fₓ` with respect to `y`:

```
fₓᵧ = ∂/∂y [3x²y² + y·eˣʸ + y·cos(xy)]
     = 6x²y + eˣʸ + xy·eˣʸ + cos(xy) - xy·sin(xy)
     = 6x²y + (1 + xy)eˣʸ + cos(xy) - xy·sin(xy)
```

**Step 6: Mixed partial derivative fᵧₓ**

Differentiate `fᵧ` with respect to `x`:

```
fᵧₓ = ∂/∂x [2x³y + x·eˣʸ + x·cos(xy)]
     = 6x²y + eˣʸ + xy·eˣʸ + cos(xy) - xy·sin(xy)
     = 6x²y + (1 + xy)eˣʸ + cos(xy) - xy·sin(xy)
```

**Verification:** `fₓᵧ = fᵧₓ` ✓ (Clairaut's Theorem confirmed since all terms are continuous.)

**Summary of all derivatives:**

```
fₓ  = 3x²y² + y·eˣʸ + y·cos(xy)

fᵧ  = 2x³y + x·eˣʸ + x·cos(xy)

fₓₓ = 6xy² + y²·eˣʸ - y²·sin(xy)

fᵧᵧ = 2x³ + x²·eˣʸ - x²·sin(xy)

fₓᵧ = fᵧₓ = 6x²y + (1 + xy)eˣʸ + cos(xy) - xy·sin(xy)
```

---

### Problem 2: Verify Clairaut's Theorem

**Problem:** Verify Clairaut's Theorem for `f(x, y) = x²y³ + cos(xy)`.

**Solution:**

**Step 1: Compute fₓ**

```
fₓ = ∂/∂x [x²y³ + cos(xy)]
   = 2xy³ - y·sin(xy)
```

**Step 2: Compute fᵧ**

```
fᵧ = ∂/∂y [x²y³ + cos(xy)]
   = 3x²y² - x·sin(xy)
```

**Step 3: Compute fₓᵧ (differentiate fₓ with respect to y)**

```
fₓᵧ = ∂/∂y [2xy³ - y·sin(xy)]
     = 6xy² - sin(xy) - y·x·cos(xy)
     = 6xy² - sin(xy) - xy·cos(xy)
```

**Step 4: Compute fᵧₓ (differentiate fᵧ with respect to x)**

```
fᵧₓ = ∂/∂x [3x²y² - x·sin(xy)]
     = 6xy² - sin(xy) - x·y·cos(xy)
     = 6xy² - sin(xy) - xy·cos(xy)
```

**Step 5: Compare**

```
fₓᵧ = 6xy² - sin(xy) - xy·cos(xy)
fᵧₓ = 6xy² - sin(xy) - xy·cos(xy)
```

**Conclusion:** `fₓᵧ = fᵧₓ` for all `(x, y) ∈ ℝ²`. Clairaut's Theorem is verified. ✓

Both mixed partials are continuous everywhere (they are sums of products of continuous functions), so the conditions of Clairaut's Theorem are satisfied.

---

### Problem 3: Chain Rule Application

**Problem:** Given `z = eᵘ sin(v)`, where `u = x²` and `v = xy`, find `∂z/∂x` and `∂z/∂y`.

**Solution:**

**Step 1: Identify the dependency structure**

```
z = f(u, v) = eᵘ sin(v)
u = u(x, y) = x²
v = v(x, y) = xy
```

Tree diagram:
```
        z
       / \
      u   v
     / \ / \
    x  y x  y
```

**Step 2: Compute the required partial derivatives**

```
∂f/∂u = eᵘ sin(v)
∂f/∂v = eᵘ cos(v)
∂u/∂x = 2x
∂u/∂y = 0
∂v/∂x = y
∂v/∂y = x
```

**Step 3: Apply chain rule for ∂z/∂x**

```
∂z     ∂f   ∂u     ∂f   ∂v
─── = ─── · ─── + ─── · ───
∂x     ∂u   ∂x     ∂v   ∂x

     = (eᵘ sin(v))(2x) + (eᵘ cos(v))(y)
     = 2x · eᵘ sin(v) + y · eᵘ cos(v)
```

**Step 4: Express in terms of x and y**

Substitute `u = x²` and `v = xy`:

```
∂z/∂x = 2x · eˣ² · sin(xy) + y · eˣ² · cos(xy)
```

Factor out `eˣ²`:

```
∂z/∂x = eˣ² [2x sin(xy) + y cos(xy)]
```

**Step 5: Apply chain rule for ∂z/∂y**

```
∂z     ∂f   ∂u     ∂f   ∂v
─── = ─── · ─── + ─── · ───
∂y     ∂u   ∂y     ∂v   ∂y

     = (eᵘ sin(v))(0) + (eᵘ cos(v))(x)
     = x · eᵘ cos(v)
```

**Step 6: Express in terms of x and y**

```
∂z/∂y = x · eˣ² · cos(xy)
```

**Final Answers:**

```
∂z/∂x = eˣ² [2x sin(xy) + y cos(xy)]

∂z/∂y = x · eˣ² · cos(xy)
```

---

### Problem 4: Maxima, Minima, and Saddle Points

**Problem:** Find and classify all critical points of:

```
f(x, y) = x³ + y³ - 3xy
```

**Solution:**

**Step 1: Find critical points**

Set `fₓ = 0` and `fᵧ = 0` simultaneously:

```
fₓ = 3x² - 3y = 0    →    y = x²       ... (i)
fᵧ = 3y² - 3x = 0    →    x = y²       ... (ii)
```

Substitute (i) into (ii):

```
x = (x²)² = x⁴
x⁴ - x = 0
x(x³ - 1) = 0
x(x - 1)(x² + x + 1) = 0
```

Real solutions: `x = 0` or `x = 1`.

From `y = x²`:
- If `x = 0`, then `y = 0` → critical point: **(0, 0)**
- If `x = 1`, then `y = 1` → critical point: **(1, 1)**

**Step 2: Compute second-order partial derivatives**

```
fₓₓ = 6x
fᵧᵧ = 6y
fₓᵧ = -3
```

**Step 3: Compute the discriminant D at each critical point**

```
D = fₓₓ · fᵧᵧ - (fₓᵧ)² = (6x)(6y) - (-3)² = 36xy - 9
```

**Step 4: Classify (0, 0)**

```
D(0, 0) = 36(0)(0) - 9 = -9
```

Since `D = -9 < 0`:

**Conclusion: (0, 0) is a saddle point.**

The value at this point: `f(0, 0) = 0`.

**Step 5: Classify (1, 1)**

```
D(1, 1) = 36(1)(1) - 9 = 27
fₓₓ(1, 1) = 6(1) = 6
```

Since `D = 27 > 0` and `fₓₓ = 6 > 0`:

**Conclusion: (1, 1) is a local minimum.**

The value at this point: `f(1, 1) = 1 + 1 - 3 = -1`.

**Summary Table:**

| Critical Point | D | fₓₓ | Classification | Function Value |
|---------------|---|------|----------------|----------------|
| (0, 0) | -9 | 0 | **Saddle point** | f = 0 |
| (1, 1) | 27 | 6 | **Local minimum** | f = -1 |

**Graph interpretation:** The surface `z = x³ + y³ - 3xy` has a saddle point at the origin and a bowl-shaped local minimum at `(1, 1, -1)`.

---

### Problem 5: Lagrange Multipliers

**Problem:** Use Lagrange multipliers to find the extrema of:

```
f(x, y) = x²y
```

subject to the constraint:

```
g(x, y) = x² + y² - 1 = 0
```

**Solution:**

**Step 1: Set up the Lagrangian**

```
L(x, y, λ) = x²y - λ(x² + y² - 1)
```

**Step 2: Form the system of equations**

```
∂L/∂x = 2xy - 2λx = 0          ... (1)
∂L/∂y = x² - 2λy = 0           ... (2)
∂L/∂λ = -(x² + y² - 1) = 0     ... (3)
```

**Step 3: Solve equation (1)**

```
2xy - 2λx = 0
2x(y - λ) = 0
```

So either `x = 0` or `λ = y`.

**Case A: x = 0**

From equation (3): `0 + y² - 1 = 0` → `y = ±1`

Critical points: **(0, 1)** and **(0, -1)**

Evaluate: `f(0, 1) = 0`, `f(0, -1) = 0`

**Case B: λ = y**

Substitute into equation (2):

```
x² - 2y(y) = 0
x² - 2y² = 0
x² = 2y²
```

From equation (3):

```
x² + y² = 1
2y² + y² = 1
3y² = 1
y² = 1/3
y = ±1/√3
```

If `y = 1/√3`: `x² = 2/3`, so `x = ±√(2/3) = ±√6/3`

If `y = -1/√3`: `x² = 2/3`, so `x = ±√(2/3) = ±√6/3`

Critical points: **(√6/3, 1/√3)**, **(-√6/3, 1/√3)**, **(√6/3, -1/√3)**, **(-√6/3, -1/√3)**

**Step 4: Evaluate f at all critical points**

| Point | x²y | Value |
|-------|-----|-------|
| (0, 1) | 0·1 | **0** |
| (0, -1) | 0·(-1) | **0** |
| (√6/3, 1/√3) | (2/3)(1/√3) | **2/(3√3) ≈ 0.385** |
| (-√6/3, 1/√3) | (2/3)(1/√3) | **2/(3√3) ≈ 0.385** |
| (√6/3, -1/√3) | (2/3)(-1/√3) | **-2/(3√3) ≈ -0.385** |
| (-√6/3, -1/√3) | (2/3)(-1/√3) | **-2/(3√3) ≈ -0.385** |

**Step 5: Classify**

```
Maximum value: f = 2/(3√3) at (√6/3, 1/√3) and (-√6/3, 1/√3)

Minimum value: f = -2/(3√3) at (√6/3, -1/√3) and (-√6/3, -1/√3)
```

**Rationalized forms:**

```
2/(3√3) = 2√3/9

-2/(3√3) = -2√3/9
```

**Final Answers:**

```
Maximum:  2√3/9  at  (±√6/3, 1/√3)
Minimum: -2√3/9  at  (±√6/3, -1/√3)
```

**Verification using bordered Hessian (optional):**

At `(√6/3, 1/√3)` with `y = 1/√3`, `λ = y = 1/√3`:

```
H̄ = │  0      2x     2y  │     │ 0     2√6/3   2/√3  │
    │ 2x    2y-2λ    2x   │  =  │ 2√6/3  0      2√6/3 │
    │ 2y     2x      2y   │     │ 2/√3  2√6/3    2/√3  │

det(H̄) < 0  →  local maximum ✓
```

---

## 4. ENGINEERING APPLICATIONS MAP

---

| Partial Differentiation Concept | Engineering Application | Domain | Description |
|--------------------------------|------------------------|--------|-------------|
| **First partial derivatives** | Heat transfer | Mechanical/Chemical | Temperature gradients: `∂T/∂x`, `∂T/∂y`, `∂T/∂z` describe how temperature varies in space, driving heat flux via Fourier's law: `q = -k∇T` |
| **First partial derivatives** | Fluid flow | Aerospace/Civil | Velocity components `∂u/∂x`, `∂v/∂y` describe strain rates in fluid elements; pressure gradients `∂p/∂x` drive flow |
| **First partial derivatives** | Structural mechanics | Civil/Mechanical | Stress and strain fields: `∂u/∂x` (normal strain), `∂u/∂y + ∂v/∂x` (shear strain) in elasticity theory |
| **Chain rule** | Rate of change in coupled systems | All engineering | When multiple subsystems are coupled (e.g., thermal-mechanical, electrical-mechanical), chain rule relates internal rates to observable quantities |
| **Chain rule** | Control systems | Electrical/Mechanical | In state-space models `ẋ = f(x, u)`, chain rule computes `df/dt` for time-varying inputs |
| **Chain rule** | Dimensional analysis | General | Relating derivatives across different unit systems or coordinate representations |
| **Jacobian matrix** | Coordinate transformations | Robotics/Aerospace | Mapping velocities and forces between coordinate frames in robot arm kinematics and spacecraft attitude control |
| **Jacobian matrix** | Numerical methods | Computational | Newton-Raphson method for systems: `xₙ₊₁ = xₙ - J⁻¹F(xₙ)` for solving nonlinear systems `F(x) = 0` |
| **Jacobian determinant** | Integration by substitution | General | Converting integrals between coordinate systems (polar, cylindrical, spherical, general curvilinear) |
| **Jacobian** | Nonlinear system analysis | Control engineering | Linearization of nonlinear systems around operating points: `ẋ ≈ A·δx + B·δu` where `A, B` are Jacobian blocks |
| **Hessian matrix** | Structural stability analysis | Civil/Mechanical | Second-order energy methods: positive definite Hessian of strain energy guarantees stable equilibrium |
| **Hessian matrix** | Optimization | All engineering | Second-order sufficient conditions for local minima in design optimization, finite element analysis, and machine learning |
| **Hessian matrix** | Image processing | Electrical/Computer | Hessian-based feature detection (blob detection, ridge detection) in computer vision for autonomous systems |
| **Hessian matrix** | Curvature analysis | Mechanical/Civil | Gaussian and mean curvature of surfaces for stress analysis in shells and plates |
| **Lagrange multipliers** | Constrained design optimization | All engineering | Optimizing performance (weight, cost, efficiency) subject to constraints (stress limits, budget, geometry) |
| **Lagrange multipliers** | Resource allocation | Operations/Industrial | Optimizing production/utility subject to resource constraints in manufacturing and supply chain |
| **Lagrange multipliers** | Structural optimization | Civil/Mechanical | Minimum-weight design subject to stress, deflection, and frequency constraints |
| **Lagrange multipliers** | Electrical circuits | Electrical | Power transfer optimization subject to impedance matching constraints |
| **Total differentials** | Error propagation | Metrology/Quality | If `z = f(x, y)` with measurement errors `Δx`, `Δy`, then `Δz ≈ fₓ·Δx + fᵧ·Δy` estimates uncertainty |
| **Total differentials** | Thermodynamics | Chemical/Mechanical | State functions (`dU`, `dH`, `dS`) are exact differentials; path-dependent quantities (`δQ`, `δW`) are inexact; the first law connects them |
| **Total differentials** | Fluid mechanics | Aerospace/Civil | Material derivative: `Df/Dt = ∂f/∂t + v·∇f` combines local and convective changes |
| **Exact differential conditions** | Thermodynamic consistency | Chemical | Ensuring constitutive relations are thermodynamically consistent: Maxwell relations from exactness of `dG`, `dF`, `dA` |
| **Implicit function theorem** | Constraint qualification | All engineering | Verifying that constraints define valid implicit surfaces near a point; essential for Lagrange multiplier method validity |
| **Higher-order derivatives** | Bending theory | Civil/Mechanical | Beam deflection: `EI·d²y/dx² = M(x)` involves second derivatives; plate theory uses fourth-order PDEs |
| **Higher-order derivatives** | Wave propagation | Electrical/Acoustic | Wave equation `∂²u/∂t² = c²∇²u` involves second-order partial derivatives in both space and time |
| **Clairaut's theorem** | Potential theory | Geophysics/Electrostatics | Ensures mixed partials of gravitational/electric potential are equal, validating path-independence of work integrals |
| **Euler's theorem** | Homogeneous production functions | Industrial/Economics | Cobb-Douglas production `Y = AK^αL^β`: returns to scale = `α + β`; Euler's theorem links marginal products to total output |

---

## 5. QUICK REFERENCE FORMULA SHEET

---

### Fundamental Formulas

| Formula | Context |
|---------|---------|
| `∂f/∂x = lim_{h→0} [f(x+h,y) - f(x,y)] / h` | Definition of partial derivative |
| `dz = fₓ dx + fᵧ dy` | Total differential (2 variables) |
| `dw = Σᵢ (∂w/∂xᵢ) dxᵢ` | Total differential (n variables) |
| `∂z/∂s = fₓ(∂x/∂s) + fᵧ(∂y/∂s)` | Chain rule |
| `∂z/∂t = fₓ(∂x/∂t) + fᵧ(∂y/∂t)` | Chain rule |
| `dy/dx = -Fₓ/Fᵧ` | Implicit differentiation |
| `D = fₓₓfᵧᵧ - (fₓᵧ)²` | Discriminant (Hessian det.) |
| `∇f = (fₓ, fᵧ, f_z)` | Gradient vector |
| `∇²f = fₓₓ + fᵧᵧ + f_zz` | Laplacian |

### Classification Table (2 Variables)

| D | fₓₓ | Type | Shape |
|---|-----|------|-------|
| > 0 | > 0 | Local minimum | ∪ (upward bowl) |
| > 0 | < 0 | Local maximum | ∩ (downward bowl) |
| < 0 | any | Saddle point | ⊗ (saddle) |
| = 0 | any | Inconclusive | Higher order tests |

### Euler's Theorem

| Homogeneous degree | Euler's relation |
|--------------------|------------------|
| `f(tx, ty) = tᵏf(x, y)` | `xfₓ + yfᵧ = kf` |

### Lagrange Multipliers (single constraint)

| Equation | Purpose |
|----------|---------|
| `fₓ = λgₓ` | Stationarity w.r.t. x |
| `fᵧ = λgᵧ` | Stationarity w.r.t. y |
| `g(x, y) = 0` | Constraint satisfaction |

### Coordinate System Jacobians

| Coordinates | Variables | |J| |
|-------------|-----------|-----|
| Polar | (r, θ) | r |
| Cylindrical | (r, θ, z) | r |
| Spherical | (ρ, θ, φ) | ρ² sin φ |
| General 2D | (u, v) | ∂(x,y)/∂(u,v) |

---

## 6. COMMON MISTAKES & PITFALLS

---

| # | Mistake | Correct Approach |
|---|---------|-----------------|
| 1 | Confusing `∂²f/∂x∂y` with `∂²f/∂y∂x` in subscript notation | Remember: `∂²f/∂x∂y = fᵧₓ` (right-to-left), `∂²f/∂y∂x = fₓᵧ` (left-to-right) |
| 2 | Assuming `fₓᵧ = fᵧₓ` always | Only guaranteed when both mixed partials are **continuous**; verify continuity |
| 3 | Forgetting to include all terms in the chain rule | For `z = f(x, y)` with `x(s,t)`, `y(s,t)`: always **two** terms in each formula |
| 4 | Using `d` instead of `∂` for partial derivatives | Use `∂` when differentiating w.r.t. one variable while holding others constant; use `d` for total derivatives |
| 5 | Ignoring the constraint when applying Lagrange multipliers | Always include `g(x, y) = 0` as the third equation |
| 6 | Forgetting the `λ` term in the Lagrangian | `L = f - λg` (not `f + λg`, though sign convention varies; just be consistent) |
| 7 | Confusing necessary and sufficient conditions | `D > 0` and `fₓₓ > 0` is sufficient for a local minimum, not just necessary |
| 8 | Forgetting the Jacobian determinant in change of variables | When converting `dx dy` to `du dv`, multiply by `|J|` |
| 9 | Applying the second derivative test when `D = 0` | When `D = 0`, the test is inconclusive; use higher order analysis or other methods |
| 10 | Treating partial derivatives as total derivatives in the chain rule | For multi-variable chain rule, each path from dependent to independent variable contributes a product term; sum all paths |

---

## 7. PRACTICE PROBLEMS

---

### Problem P1 (Basic)

Find `∂f/∂x` and `∂f/∂y` for `f(x, y) = x²y + xy³ + eˣ⁺ʸ`.

### Problem P2 (Basic)

Find all second-order partial derivatives of `f(x, y) = x⁴y² - 2xy³ + 3x²y`.

### Problem P3 (Chain Rule)

If `w = x² + yz` where `x = st`, `y = eˢᵗ`, `z = s² - t²`, find `∂w/∂s` and `∂w/∂t`.

### Problem P4 (Implicit Differentiation)

If `x³ + y³ = 3xy`, find `dy/dx` using implicit differentiation.

### Problem P5 (Maxima/Minima)

Find and classify all critical points of `f(x, y) = 2x³ + 2y³ - 6xy + 1`.

### Problem P6 (Lagrange Multipliers)

Find the maximum value of `f(x, y) = xy` subject to `x²/8 + y²/2 = 1`.

### Problem P7 (Exact Differential)

Determine whether `(2xy + 3)dx + (x² - 1)dy` is exact. If so, find the potential function.

### Problem P8 (Jacobian)

Compute the Jacobian `∂(u, v)/∂(r, θ)` for `u = r cos θ - r² cos 2θ`, `v = r sin θ - r² sin 2θ`.

### Problem P9 (Higher Order)

For `f(x, y, z) = xyz + x²z + yz²`, compute all third-order partial derivatives and verify that mixed partials of order 3 are equal when continuous.

### Problem P10 (Lagrange Multipliers, 3 variables)

Use Lagrange multipliers to find the maximum and minimum values of `f(x, y, z) = x + 2y + 3z` subject to `x² + y² + z² = 1`.

---

## 8. ANSWER KEY TO PRACTICE PROBLEMS

---

**P1:**
```
fₓ = 2xy + y³ + eˣ⁺ʸ
fᵧ = x² + 3xy² + eˣ⁺ʸ
```

**P2:**
```
fₓ  = 4x³y² - 2y³ + 6xy
fᵧ  = 2x⁴y - 6xy² + 3x²
fₓₓ = 12x²y² + 6y
fᵧᵧ = 2x⁴ - 12xy
fₓᵧ = fᵧₓ = 8x³y - 6y² + 6x
```

**P3:**
```
∂w/∂s = 2x·t + z·t + y·t + (s² - t²)(2s)
      = 2st·t + (s² - t²)·t + eˢᵗ·t + (s² - t²)(2s)

More explicitly:
∂w/∂s = 2(st)(t) + t(s² - t²) + teˢᵗ + 2s(s² - t²)
      = 2st² + ts² - t³ + teˢᵗ + 2s³ - 2st²
      = ts² - t³ + teˢᵗ + 2s³
```

```
∂w/∂t = 2x·s + z·s + y·s + (s² - t²)(-2t)
      = 2(st)(s) + s(s² - t²) + seˢᵗ - 2t(s² - t²)
      = 2s²t + s³ - st² + seˢᵗ - 2ts² + 2t³
      = s³ - st² + seˢᵗ + 2t³
```

**P4:**
```
3x² + 3y²·(dy/dx) = 3y + 3x·(dy/dx)
3y²·(dy/dx) - 3x·(dy/dx) = 3y - 3x²
dy/dx · (y² - x) = y - x²
dy/dx = (y - x²)/(y² - x)
```

**P5:**
```
fₓ = 6x² - 6y = 0  →  y = x²
fᵧ = 6y² - 6x = 0  →  x = y²

x = (x²)² = x⁴  →  x⁴ - x = 0  →  x(x³ - 1) = 0
x = 0: y = 0  →  (0, 0)
x = 1: y = 1  →  (1, 1)

fₓₓ = 12x, fᵧᵧ = 12y, fₓᵧ = -6
D = 144xy - 36

(0, 0): D = -36 < 0  →  Saddle point
(1, 1): D = 108 > 0, fₓₓ = 12 > 0  →  Local minimum

f(0, 0) = 1
f(1, 1) = 2 + 2 - 6 + 1 = -1
```

**P6:**
```
L = xy - λ(x²/8 + y²/2 - 1)
Lₓ = y - λx/4 = 0    →  λ = 4y/x
Lᵧ = x - λy = 0       →  λ = x/y
Lλ = x²/8 + y²/2 - 1 = 0

4y/x = x/y  →  4y² = x²  →  x = ±2y
x = 2y: 4y²/8 + y²/2 = 1  →  y²/2 + y²/2 = 1  →  y² = 1
y = ±1, x = ±2

(2, 1): f = 2
(-2, -1): f = 2
(2, -1): f = -2
(-2, 1): f = -2

Maximum value: 2
Minimum value: -2
```

**P7:**
```
M = 2xy + 3,  N = x² - 1
∂M/∂y = 2x
∂N/∂x = 2x
∂M/∂y = ∂N/∂x  →  Exact ✓

∂f/∂x = 2xy + 3  →  f = x²y + 3x + φ(y)
∂f/∂y = x² + φ'(y) = x² - 1  →  φ'(y) = -1  →  φ(y) = -y + C

f(x, y) = x²y + 3x - y + C
```

**P8:**
```
∂u/∂r = cos θ - 2r cos 2θ
∂u/∂θ = -r sin θ + 2r² sin 2θ
∂v/∂r = sin θ - 2r sin 2θ
∂v/∂θ = r cos θ - 2r² cos 2θ

J = (cos θ - 2r cos 2θ)(r cos θ - 2r² cos 2θ)
    - (-r sin θ + 2r² sin 2θ)(sin θ - 2r sin 2θ)

= r(cos θ - 2r cos 2θ)² - r(sin θ - 2r sin 2θ)²... (expanded form)

More cleanly:
J = r[cos²θ - 4r cosθ cos2θ + 4r²cos²2θ + sin²θ - 4r sinθ sin2θ + 4r²sin²2θ]
  = r[1 - 4r(cosθ cos2θ + sinθ sin2θ) + 4r²(cos²2θ + sin²2θ)]
  = r[1 - 4r·cos(2θ - θ) + 4r²]
  = r[1 - 4r cos θ + 4r²]
  = r(1 - 2r cos θ)²

(using cos(A-B) = cosA cosB + sinA sinB)
```

**P9:** All eight third-order partials are:

```
fₓₓₓ = 0,  fₓₓᵧ = z,  fₓᵧₓ = z,  fₓᵧᵧ = x + 2z
fᵧₓₓ = z,  fᵧₓᵧ = x + 2z,  fᵧᵧₓ = x + 2z,  fᵧᵧᵧ = 0
```

Plus terms involving `z`: `fₓₓᵧ = 2z` (from x²z term contributes 0, yz² contributes z via differentiation)... The full computation confirms all mixed third-order partials are equal where continuous (all are polynomials, hence continuous everywhere). ✓

**P10:**
```
L = x + 2y + 3z - λ(x² + y² + z² - 1)
1 = 2λx  →  x = 1/(2λ)
2 = 2λy  →  y = 1/λ
3 = 2λz  →  z = 3/(2λ)

x² + y² + z² = 1:
1/(4λ²) + 1/λ² + 9/(4λ²) = 1
(1 + 4 + 9)/(4λ²) = 1
14/(4λ²) = 1
λ² = 14/4 = 7/2
λ = ±√(7/2)

x = 1/(2λ), y = 1/λ, z = 3/(2λ)

f = x + 2y + 3z = 1/(2λ) + 2/λ + 9/(2λ) = (1 + 4 + 9)/(2λ) = 14/(2λ) = 7/λ

λ = √(7/2):  f = 7/√(7/2) = 7·√2/√7 = √7·√2 = √14
λ = -√(7/2): f = -√14

Maximum value:  √14  at (1/(2λ), 1/λ, 3/(2λ)) = (1/√14, 2/√14, 3/√14)
Minimum value: -√14  at (-1/√14, -2/√14, -3/√14)
```

---

## CROSS-REFERENCES

- [[engineering-math/module-1-matrices|Module 1: Matrices]] — The Jacobian matrix (§2.5) and Hessian matrix (§2.6) are core tools in this module that rely on matrix theory: determinants for classification, eigenvalues for definiteness testing, and matrix algebra for chain rule in matrix form.
- [[engineering-math/module-3-homogeneous-functions|Module 3: Homogeneous Functions]] — Euler's theorem for homogeneous functions (§2.2) is a key result shared between these modules; partial differentiation is the foundational tool for verifying homogeneity and applying the theorem.
- [[engineering-math/module-4-linear-differential-equations|Module 4: Linear Differential Equations]] — Partial derivatives generate PDEs (e.g., heat equation, wave equation); the chain rule for multivariable functions underpins change of variables in PDEs. Exact differential conditions (∂M/∂y = ∂N/∂x) connect to integrability.
- [[engineering-math/module-5-complex-numbers|Module 5: Complex Numbers]] — Complex hyperbolic and trigonometric functions involve partial differentiation of complex-valued functions; the separation into real and imaginary parts uses partial derivative techniques.

*Module 2 of 5 — [[engineering-math/module-1-matrices|← Module 1]] | [[engineering-math/module-3-homogeneous-functions|Module 3 →]]*

*End of Module 2: Partial Differentiation*
