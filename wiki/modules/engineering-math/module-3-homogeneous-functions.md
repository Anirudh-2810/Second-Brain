---
module: "engineering-math"
topic: "Module 3: Homogeneous Functions — Euler's Theorem & Deductions"
tags: [homogeneous-functions, euler-theorem, calculus, partial-differentiation]
last_updated: "2026-08-18"
prerequisites: ["Partial Differentiation", "Basic Algebra"]
---

# Module 3: Homogeneous Functions

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

---

### 1.1 Homogeneous Function Definition & Examples Table

#### Definition

A function `f(x, y)` is called **homogeneous of degree `n`** if, for every real number `t > 0`:

```
f(tx, ty) = t^n * f(x, y)
```

In `N` variables, a function `f(x_1, x_2, ..., x_N)` is **homogeneous of degree `n`** if:

```
f(t*x_1, t*x_2, ..., t*x_N) = t^n * f(x_1, x_2, ..., x_N)
```

The exponent `n` is the **degree of homogeneity**.

#### Symbol Reference Table

| Symbol | Meaning |
|--------|---------|
| `f(x, y)` | A function of two variables |
| `t` | A positive real scaling parameter |
| `n` | The degree of homogeneity (a real number) |
| `x, y` | Independent variables |
| `k` | General integer degree in N-variable case |
| `u_i` | Substitution variable `u_i = x_i / t` used in proofs |
| `φ`, `ψ` | Arbitrary single-variable functions in decomposition |
| `∂f/∂x` | Partial derivative of `f` with respect to `x` |
| `Σ` | Summation symbol |

#### How to Determine Degree

**Step 1:** Replace every occurrence of `x` with `tx` and every occurrence of `y` with `ty`.

**Step 2:** Simplify the expression algebraically.

**Step 3:** Factor out the highest power of `t` possible from every term.

**Step 4:** If the result can be written as `t^n * [original expression]`, then the function is homogeneous of degree `n`.

**Step 5:** If no single exponent `n` works for all terms simultaneously, the function is **not homogeneous**.

#### Comprehensive Examples Table

| Function `f(x, y)` | `f(tx, ty)` | Factored Form | Degree | Homogeneous? |
|---------------------|-------------|---------------|--------|--------------|
| `x² + y²` | `(tx)² + (ty)² = t²(x² + y²)` | `t² · f(x,y)` | 2 | Yes |
| `x³ + x²y + xy² + y³` | `t³(x³ + x²y + xy² + y³)` | `t³ · f(x,y)` | 3 | Yes |
| `(x² + y²) / xy` | `t²(x²+y²) / t²xy = f(x,y)` | `t⁰ · f(x,y)` | 0 | Yes |
| `√(x² + y²)` | `t√(x² + y²)` | `t¹ · f(x,y)` | 1 | Yes |
| `sin(y/x)` | `sin(ty/tx) = sin(y/x)` | `t⁰ · f(x,y)` | 0 | Yes |
| `arctan(y/x)` | `arctan(ty/tx) = arctan(y/x)` | `t⁰ · f(x,y)` | 0 | Yes |
| `x² + y` | `t²x² + ty ≠ t^n(x² + y)` | Cannot factor | — | No |
| `x + 1` | `tx + 1 ≠ t^n(x + 1)` | Cannot factor | — | No |
| `(x² + y)²` | Cannot simplify to `t^n · f` | Cannot factor | — | No |
| `ln(x/y)` | `ln(tx/ty) = ln(x/y)` | `t⁰ · f(x,y)` | 0 | Yes |
| `e^(y/x)` | `e^(ty/tx) = e^(y/x)` | `t⁰ · f(x,y)` | 0 | Yes |
| `x³y²` | `t³x³ · t²y² = t⁵x³y²` | `t⁵ · f(x,y)` | 5 | Yes |
| `(x + y) / (x - y)` | `(tx+ty)/(tx-ty) = f(x,y)` | `t⁰ · f(x,y)` | 0 | Yes |
| `√x + √y` | `√(tx) + √(ty) = t^(1/2)(√x+√y)` | `t^(1/2) · f(x,y)` | 1/2 | Yes |
| `x^(3/2) + y^(3/2)` | `t^(3/2)(x^(3/2)+y^(3/2))` | `t^(3/2) · f(x,y)` | 3/2 | Yes |
| `x² + 2xy + y²` | `t²(x²+2xy+y²)` | `t² · f(x,y)` | 2 | Yes |
| `tan(x/y)` | `tan(tx/ty) = tan(x/y)` | `t⁰ · f(x,y)` | 0 | Yes |
| `1/(x+y)` | `1/(tx+ty) = t^(-1)/(x+y)` | `t^(-1) · f(x,y)` | -1 | Yes |
| `(x+y)²/(x²+y²)` | `t²(x+y)² / t²(x²+y²) = f(x,y)` | `t⁰ · f(x,y)` | 0 | Yes |
| `x⁴ + x²y² + y⁴` | `t⁴(x⁴+x²y²+y⁴)` | `t⁴ · f(x,y)` | 4 | Yes |

---

### 1.2 Degree Determination Flowchart (ASCII)

```
                    ┌─────────────────────────┐
                    │   START: Given f(x, y)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Replace x → tx, y → ty │
                    │  Form f(tx, ty)         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Simplify algebraically  │
                    │  Expand all terms        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Factor out powers of t  │
                    │  from each term           │
                    └────────────┬────────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │ Can you write result │
                      │ as t^n · f(x,y)     │
                      │ for a single n?      │
                      └─────────┬───────────┘
                           ╱         ╲
                         YES          NO
                        ╱               ╲
                       ▼                 ▼
            ┌──────────────────┐  ┌──────────────────┐
            │ f is HOMOGENEOUS │  │ f is NOT          │
            │ of degree n      │  │ HOMOGENEOUS       │
            └──────────────────┘  └──────────────────┘
```

**Detailed Substitution Example:**

```
Given: f(x, y) = x³ + x²y + xy² + y³

Step 1: f(tx, ty) = (tx)³ + (tx)²(ty) + (tx)(ty)² + (ty)³
Step 2:           = t³x³ + t³x²y + t³xy² + t³y³
Step 3:           = t³(x³ + x²y + xy² + y³)
Step 4:           = t³ · f(x, y)

∴ Homogeneous of degree n = 3
```

**Non-Homogeneous Example:**

```
Given: f(x, y) = x² + y

Step 1: f(tx, ty) = (tx)² + (ty)
Step 2:           = t²x² + ty
Step 3: Can we factor t^n from both terms?
          t²x² has factor t²
          ty has factor t¹
          DIFFERENT powers → no common t^n

∴ NOT HOMOGENEOUS
```

---

### 1.3 Euler's Theorem Flowchart (ASCII)

```
              ┌──────────────────────────────────────┐
              │  INPUT: f(x, y) is homogeneous       │
              │         of degree n                   │
              └───────────────────┬──────────────────┘
                                  │
                                  ▼
              ┌──────────────────────────────────────┐
              │  Compute partial derivatives:         │
              │  p = ∂f/∂x    q = ∂f/∂y              │
              └───────────────────┬──────────────────┘
                                  │
                                  ▼
              ┌──────────────────────────────────────┐
              │  Form Euler expression:               │
              │  x·(∂f/∂x) + y·(∂f/∂y) = x·p + y·q │
              └───────────────────┬──────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │  Result equals n·f(x,y)?│
                    └─────────┬───────────────┘
                         ╱         ╲
                       YES          NO
                      ╱               ╲
                     ▼                 ▼
        ┌──────────────────┐  ┌──────────────────────┐
        │  VERIFIED!       │  │  Re-check:           │
        │  Euler's Theorem │  │  - computation errors?│
        │  holds:          │  │  - f truly homogeneous?│
        │  xp + yq = nf   │  │  - correct degree n?  │
        └──────────────────┘  └──────────────────────┘
```

**Verification Pattern:**

```
For f(x,y) homogeneous of degree n:

  ┌────────────────────────────────────────────────────┐
  │  STEP A: Identify n (the degree)                   │
  │  STEP B: Compute ∂f/∂x and ∂f/∂y                  │
  │  STEP C: Compute x·(∂f/∂x) + y·(∂f/∂y)           │
  │  STEP D: Simplify the result                        │
  │  STEP E: Check if result = n · f(x,y)              │
  │  STEP F: If equal, Euler's theorem verified ✓       │
  └────────────────────────────────────────────────────┘
```

---

### 1.4 Deductions of Euler's Theorem

#### Deduction 1: Degree Zero Functions

If `f(x, y)` is homogeneous of degree **zero** (`n = 0`), then:

```
x · (∂f/∂x) + y · (∂f/∂y) = 0 · f(x, y) = 0
```

This means for any function where the degree of homogeneity is zero, the Euler equation reduces to the **partial differential equation**:

```
x · p + y · q = 0
```

where `p = ∂f/∂x` and `q = ∂f/∂y`.

#### Deduction 2: Higher-Order Euler's Theorem

If `f(x, y)` is homogeneous of degree `n`, then for any positive integer `m`:

```
(x·∂/∂x + y·∂/∂y)^m · f = [n · (n-1) · (n-2) · ... · (n-m+1)] · f
```

Or equivalently using falling factorial notation:

```
(x·∂/∂x + y·∂/∂y)^m · f = n^(m) · f
```

where `n^(m) = n(n-1)(n-2)...(n-m+1)` is the falling factorial.

**Second-order form (m = 2):**

```
(x·∂/∂x + y·∂/∂y)² · f = n(n-1) · f
```

Expanding:

```
x²·(∂²f/∂x²) + 2xy·(∂²f/∂x∂y) + y²·(∂²f/∂y²) = n(n-1) · f
```

#### Deduction 3: Three Variables

For a function `f(x, y, z)` homogeneous of degree `n`:

```
x·(∂f/∂x) + y·(∂f/∂y) + z·(∂f/∂z) = n · f
```

#### Deduction 4: N Variables

For `f(x_1, x_2, ..., x_N)` homogeneous of degree `n`:

```
Σ_{i=1}^{N} x_i · (∂f/∂x_i) = n · f
```

---

## 2. MATHEMATICAL FORMULATION & CORE THEOREMS

---

### 2.1 Definition of Homogeneous Functions (General Form)

**Definition (N-Variable):** A function `f: ℝ^N → ℝ` is called **homogeneous of degree `k`** if for all `t > 0` and all `(x_1, x_2, ..., x_N)` in the domain of `f`:

```
f(t·x_1, t·x_2, ..., t·x_N) = t^k · f(x_1, x_2, ..., x_N)
```

where `k` is a real constant called the **degree of homogeneity**.

**Key Properties:**

1. **Domain:** The domain must be a cone (closed under positive scaling).
2. **Degree:** The degree `k` need not be an integer; it can be any real number.
3. **Zero function:** The zero function is homogeneous of every degree.
4. **Additivity:** If `f` is homogeneous of degree `m` and `g` is homogeneous of degree `n`, then `f + g` is not necessarily homogeneous (unless `m = n`).

**Properties of Homogeneous Functions:**

| Property | Statement |
|----------|-----------|
| Sum | If `f, g` are both degree `n`, then `f + g` is degree `n` |
| Product | If `f` is degree `m` and `g` is degree `n`, then `f·g` is degree `m+n` |
| Quotient | If `f` is degree `m` and `g` is degree `n`, then `f/g` is degree `m-n` |
| Scalar multiple | If `f` is degree `n`, then `c·f` is degree `n` (for constant `c`) |
| Composition | If `g` is degree `m` and `φ` is degree 1, then `φ∘g` is degree `m` (if applicable) |
| Partial derivative | If `f` is degree `n`, then `∂f/∂x_i` is degree `n-1` |

**Important Note on Partial Derivatives:**

If `f(x, y)` is homogeneous of degree `n`, then:
- `∂f/∂x` is homogeneous of degree `n - 1`
- `∂f/∂y` is homogeneous of degree `n - 1`
- `∂²f/∂x²` is homogeneous of degree `n - 2`
- `∂²f/∂x∂y` is homogeneous of degree `n - 2`

This can be verified by direct substitution.

---

### 2.2 Euler's Theorem (Statement, Proof, Corollaries)

#### STATEMENT

**Euler's Theorem on Homogeneous Functions:**

If `f(x_1, x_2, ..., x_N)` is a homogeneous function of degree `n`, where `f` has continuous first-order partial derivatives, then:

```
x_1 · (∂f/∂x_1) + x_2 · (∂f/∂x_2) + ... + x_N · (∂f/∂x_N) = n · f(x_1, x_2, ..., x_N)
```

In compact notation:

```
Σ_{i=1}^{N} x_i · (∂f/∂x_i) = n · f
```

Or using the Euler operator `E`:

```
E[f] = n · f
```

where `E = Σ x_i · (∂/∂x_i)` is the **Euler operator** (also called the **dilation operator** or **scaling operator**).

#### COMPLETE PROOF (Two-Variable Case)

**Given:** `f(tx, ty) = t^n · f(x, y)` for all `t > 0`.

**To prove:** `x · (∂f/∂x) + y · (∂f/∂y) = n · f(x, y)`.

**Proof:**

**Step 1:** Define a substitution. Let `u = tx` and `v = ty`. Then by the homogeneity condition:

```
f(u, v) = f(tx, ty) = t^n · f(x, y)
```

**Step 2:** Differentiate both sides of `f(tx, ty) = t^n · f(x, y)` with respect to `t`, treating `x` and `y` as constants.

Left side (using chain rule):

```
d/dt [f(tx, ty)] = (∂f/∂u) · (du/dt) + (∂f/∂v) · (dv/dt)
                  = (∂f/∂u) · x + (∂f/∂v) · y
                  = x · (∂f/∂u) + y · (∂f/∂v)
```

Right side:

```
d/dt [t^n · f(x, y)] = n · t^(n-1) · f(x, y)
```

**Step 3:** Equate both sides:

```
x · (∂f/∂u) + y · (∂f/∂v) = n · t^(n-1) · f(x, y)
```

**Step 4:** Now set `t = 1`. When `t = 1`, we have `u = x` and `v = y`, so:

```
x · (∂f/∂x) + y · (∂f/∂y) = n · 1^(n-1) · f(x, y) = n · f(x, y)
```

**Q.E.D.**

#### COMPLETE PROOF (N-Variable Case)

**Given:** `f(t·x_1, t·x_2, ..., t·x_N) = t^n · f(x_1, x_2, ..., x_N)`.

**Proof:**

Define `g(t) = f(t·x_1, t·x_2, ..., t·x_N)`. By homogeneity, `g(t) = t^n · f(x_1, ..., x_N)`.

Differentiate with respect to `t`:

```
g'(t) = Σ_{i=1}^{N} (∂f/∂x_i)|_{(tx_1,...,tx_N)} · x_i
```

From the right side:

```
g'(t) = n · t^(n-1) · f(x_1, ..., x_N)
```

Set `t = 1`:

```
Σ_{i=1}^{N} x_i · (∂f/∂x_i) = n · f(x_1, ..., x_N)
```

**Q.E.D.**

#### COROLLARY 1: Degree Zero

If `f` is homogeneous of degree `n = 0`, then:

```
x · (∂f/∂x) + y · (∂f/∂y) = 0
```

This is a **partial differential equation** (PDE) satisfied by all degree-zero homogeneous functions.

**Example:** `f(x, y) = arctan(y/x)` is homogeneous of degree 0.

```
∂f/∂x = -y/(x² + y²)
∂f/∂y = x/(x² + y²)
x · (-y/(x²+y²)) + y · (x/(x²+y²)) = (-xy + xy)/(x² + y²) = 0  ✓
```

#### COROLLARY 2: Generalization to Higher Orders

If `f` is homogeneous of degree `n`, then for any positive integer `m`:

```
(x·∂/∂x + y·∂/∂y)^m [f] = n · (n-1) · (n-2) · ... · (n-m+1) · f
```

This is called the **higher-order Euler's theorem**.

**Derivation for m = 2:**

Apply Euler's operator `E = x·∂/∂x + y·∂/∂y` twice:

```
E²[f] = E[E[f]] = E[n·f] = n · E[f] = n · n · f = n² · f   [WRONG — need to be careful]
```

Actually, the correct derivation requires expanding the operator:

```
E²[f] = (x·∂/∂x + y·∂/∂y)(x·∂f/∂x + y·∂f/∂y)
```

Expanding:

```
= x·∂/∂x(x·∂f/∂x) + x·∂/∂x(y·∂f/∂y) + y·∂/∂y(x·∂f/∂x) + y·∂/∂y(y·∂f/∂y)
```

Computing each term:

```
x·∂/∂x(x·∂f/∂x) = x·(∂f/∂x + x·∂²f/∂x²) = x·∂f/∂x + x²·∂²f/∂x²

x·∂/∂x(y·∂f/∂y) = x·y·∂²f/∂x∂y

y·∂/∂y(x·∂f/∂x) = x·y·∂²f/∂y∂x

y·∂/∂y(y·∂f/∂y) = y·(∂f/∂y + y·∂²f/∂y²) = y·∂f/∂y + y²·∂²f/∂y²
```

Summing all four terms:

```
E²[f] = (x·∂f/∂x + y·∂f/∂y) + x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y²
       = n·f + x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y²
```

But also from the theorem, `E²[f] = n(n-1)·f`. Therefore:

```
n·f + x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y² = n(n-1)·f
```

So:

```
x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y² = n(n-1)·f - n·f = n(n-2)·f
```

Wait — let us re-derive more carefully.

Since `∂f/∂x` is homogeneous of degree `n-1`, by Euler's theorem applied to `∂f/∂x`:

```
x·∂²f/∂x² + y·∂²f/∂y∂x = (n-1)·∂f/∂x
```

Similarly, applied to `∂f/∂y`:

```
x·∂²f/∂x∂y + y·∂²f/∂y² = (n-1)·∂f/∂y
```

Now multiply the first by `x` and the second by `y`:

```
x²·∂²f/∂x² + xy·∂²f/∂y∂x = (n-1)·x·∂f/∂x
xy·∂²f/∂x∂y + y²·∂²f/∂y² = (n-1)·y·∂f/∂y
```

Adding:

```
x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y² = (n-1)·(x·∂f/∂x + y·∂f/∂y) = (n-1)·n·f
```

Therefore:

```
x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y² = n(n-1) · f
```

This is the **second-order Euler's theorem**.

#### CONVERSE of Euler's Theorem

**Statement (Converse):** If `f` is continuously differentiable and satisfies:

```
x · (∂f/∂x) + y · (∂f/∂y) = n · f(x, y)
```

then `f` is homogeneous of degree `n` (on each connected component of its domain, for domains that are cones).

**Proof of Converse (sketch):**

Define `g(t) = f(tx, ty) / t^n` for `t > 0`. Then:

```
g'(t) = [t^n · (x·∂f/∂x|_{(tx,ty)} + y·∂f/∂y|_{(tx,ty)}) - n·t^(n-1)·f(tx,ty)] / t^(2n)
```

Using the PDE condition at point `(tx, ty)`:

```
tx · (∂f/∂x)|_{(tx,ty)} + ty · (∂f/∂y)|_{(tx,ty)} = n · f(tx, ty)
```

This gives `g'(t) = 0` for all `t > 0`, so `g(t)` is constant, and `g(t) = g(1) = f(x, y)`. Thus `f(tx, ty) = t^n · f(x, y)`.

---

### 2.3 Higher-Order Euler's Theorem

#### General Statement

If `f(x, y)` is a homogeneous function of degree `n` with continuous partial derivatives of order up to `m`, then:

```
(x·∂/∂x + y·∂/∂y)^m [f] = n · (n-1) · (n-2) · ... · (n-m+1) · f
```

Using the notation `n^(m)` for the falling factorial:

```
n^(m) = n · (n-1) · (n-2) · ... · (n-m+1) = n! / (n-m)!
```

#### Explicit Forms for Low Orders

**First order (m = 1):**

```
x·∂f/∂x + y·∂f/∂y = n · f
```

**Second order (m = 2):**

```
x²·∂²f/∂x² + 2xy·∂²f/∂x∂y + y²·∂²f/∂y² = n(n-1) · f
```

**Third order (m = 3):**

```
x³·∂³f/∂x³ + 3x²y·∂³f/∂x²∂y + 3xy²·∂³f/∂x∂y² + y³·∂³f/∂y³ = n(n-1)(n-2) · f
```

**General m-th order for two variables:**

```
Σ_{k=0}^{m} C(m,k) · x^(m-k) · y^k · ∂^m f / (∂x^(m-k) · ∂y^k) = n^(m) · f
```

where `C(m,k) = m! / (k!(m-k)!)` is the binomial coefficient.

#### N-Variable Higher-Order Form

For `f(x_1, x_2, ..., x_N)` homogeneous of degree `n`:

```
(Σ_{i=1}^{N} x_i · ∂/∂x_i)^m [f] = n^(m) · f
```

Expanding using the multinomial theorem:

```
Σ_{|α|=m} (m! / α!) · x^α · D^α f = n^(m) · f
```

where `α = (α_1, ..., α_N)` is a multi-index, `x^α = x_1^{α_1} · ... · x_N^{α_N}`, and `D^α = ∂^{|α|} / ∂x_1^{α_1} · ... · ∂x_N^{α_N}`.

---

### 2.4 Composite Functions

#### Operations on Homogeneous Functions

**Theorem (Algebraic Operations):** Let `f` and `g` be homogeneous functions defined on the same domain.

| Operation | Degree of Result |
|-----------|-------------------|
| `f + g` | `n` (only if both have degree `n`) |
| `f - g` | `n` (only if both have degree `n`) |
| `f · g` | `m + n` (if `f` has degree `m`, `g` has degree `n`) |
| `f / g` | `m - n` (if `f` has degree `m`, `g` has degree `n`) |
| `f^k` | `k · n` (if `f` has degree `n`) |
| `c · f` | `n` (for any constant `c`) |
| `√f` | `n/2` (if `f` has degree `n`) |

**Proof of Product Rule:**

If `f(tx, ty) = t^m · f(x, y)` and `g(tx, ty) = t^n · g(x, y)`, then:

```
(f·g)(tx, ty) = f(tx,ty) · g(tx,ty) = t^m·f(x,y) · t^n·g(x,y) = t^(m+n) · (f·g)(x,y)
```

#### Composition of Homogeneous Functions

**Theorem (Composition):** If `g(x, y)` is homogeneous of degree `m`, and `φ(u)` is homogeneous of degree `p` (as a function of one variable, where `φ(tu) = t^p · φ(u)`), then the composition `h(x, y) = φ(g(x, y))` is homogeneous of degree `m · p`.

**Proof:**

```
h(tx, ty) = φ(g(tx, ty)) = φ(t^m · g(x, y))
```

Since `φ` is homogeneous of degree `p`:

```
φ(t^m · g(x,y)) = (t^m)^p · φ(g(x,y)) = t^(mp) · h(x,y)
```

**Special case — `φ` is a power function:** If `φ(u) = u^p`, then:

```
h(x,y) = [g(x,y)]^p
```

is homogeneous of degree `m · p`.

**Special case — `φ` is exponential:** If `φ(u) = e^u`, then `φ` is NOT homogeneous in the traditional sense (unless restricted), so composition results may not apply directly.

**Special case — `φ` is a ratio of powers:** If `f` is degree `m` and `g` is degree `n`, then `f/g` is degree `m-n` (as shown above).

#### Composition with Linear Functions

**Theorem:** If `f(u, v)` is homogeneous of degree `n`, and `u = a·x + b·y`, `v = c·x + d·y` (linear functions), then `F(x, y) = f(a·x+b·y, c·x+d·y)` is homogeneous of degree `n`.

**Proof:**

```
F(tx, ty) = f(a·tx + b·ty, c·tx + d·ty) = f(t(ax+by), t(cx+dy)) = t^n · f(ax+by, cx+dy) = t^n · F(x,y)
```

#### Chain Rule and Homogeneity

If `f(x, y)` is homogeneous of degree `n` and `x = r·cos(θ)`, `y = r·sin(θ)` (polar coordinates), then:

```
f(r·cosθ, r·sinθ) = r^n · f(cosθ, sinθ)
```

This decomposition into radial and angular parts is extremely useful in engineering applications.

---

### 2.5 Deductions and Applications

#### Deduction 1: Logarithmic Decomposition

**Theorem:** Any homogeneous function `f(x, y)` of degree `n` (with `x > 0`) can be written as:

```
f(x, y) = x^n · φ(y/x)
```

where `φ` is a function of a single variable `u = y/x`.

**Proof:**

Since `f(tx, ty) = t^n · f(x, y)`, set `t = 1/x`:

```
f(1, y/x) = (1/x)^n · f(x, y)
```

Therefore:

```
f(x, y) = x^n · f(1, y/x) = x^n · φ(y/x)
```

where `φ(u) = f(1, u)`.

**Similarly**, if `y ≠ 0`:

```
f(x, y) = y^n · ψ(x/y)
```

where `ψ(v) = f(v, 1)`.

#### Deduction 2: Implicit Homogeneous Functions

If `F(x, y, z) = 0` defines `z` implicitly as a function of `x` and `y`, and `F` is homogeneous of degree `n`, then:

```
x · (∂z/∂x) + y · (∂z/∂y) = z · (n · F_z - F) / F_z
```

(under appropriate non-degeneracy conditions where `F_z ≠ 0`).

A simpler special case: if `F(x, y, z) = 0` where `F` is homogeneous of degree 0 in all three variables, then:

```
x · (∂z/∂x) + y · (∂z/∂y) = 0
```

#### Deduction 3: The Substitution y = vx

For a homogeneous function `f(x, y)` of degree `n`, the substitution `y = vx` (where `v = y/x`) transforms the function into:

```
f(x, vx) = x^n · φ(v)
```

This is the basis for reducing certain ordinary differential equations (ODEs) to separable form.

**Application to ODEs:** If a first-order ODE has the form:

```
dy/dx = F(y/x)
```

where `F` is a function of the ratio `y/x`, then the substitution `y = vx` gives:

```
v + x·dv/dx = F(v)
x·dv/dx = F(v) - v
```

This is now a **separable ODE** in `v` and `x`.

#### Deduction 4: Relationship to Dimensional Analysis

A function `f(x, y)` that depends on physical quantities `x` and `y` (with the same dimensions) and is homogeneous of degree `n` satisfies:

```
f(λx, λy) = λ^n · f(x, y)
```

This is the mathematical foundation of **dimensional analysis** and **Buckingham Pi theorem**. The degree `n` encodes how the quantity scales with the input variables.

#### Deduction 5: Partial Differential Equations

The general solution of the PDE:

```
x · p + y · q = n · f(x, y, z)
```

(where `p = ∂z/∂x`, `q = ∂z/∂y`) can be found using the method of characteristics. The characteristic equations are:

```
dx/x = dy/y = dz/(n·f(x,y,z))
```

From `dx/x = dy/y`:

```
y/x = c₁ (constant)
```

The general solution is:

```
Φ(y/x, F(x,y,z)) = 0
```

where `Φ` is an arbitrary function and `F` is a particular integral.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: Homogeneity Verification and Euler's Theorem

**Problem:** Show that `f(x, y) = x³ + x²y + xy² + y³` is homogeneous of degree 3, and verify Euler's theorem.

**Solution:**

**Part A: Verify Homogeneity**

Replace `x → tx` and `y → ty`:

```
f(tx, ty) = (tx)³ + (tx)²(ty) + (tx)(ty)² + (ty)³
          = t³x³ + t³x²y + t³xy² + t³y³
          = t³(x³ + x²y + xy² + y³)
          = t³ · f(x, y)
```

Since `f(tx, ty) = t³ · f(x, y)`, the function is **homogeneous of degree 3**.

**Part B: Verify Euler's Theorem**

Euler's theorem states: `x·(∂f/∂x) + y·(∂f/∂y) = n·f = 3f`.

Compute partial derivatives:

```
∂f/∂x = 3x² + 2xy + y²
∂f/∂y = x² + 2xy + 3y²
```

Form the Euler expression:

```
x·(∂f/∂x) + y·(∂f/∂y) = x(3x² + 2xy + y²) + y(x² + 2xy + 3y²)
                         = 3x³ + 2x²y + xy² + x²y + 2xy² + 3y³
                         = 3x³ + 3x²y + 3xy² + 3y³
                         = 3(x³ + x²y + xy² + y³)
                         = 3 · f(x, y)
```

**Euler's theorem is verified.**

**Final Answer:** `x·(∂f/∂x) + y·(∂f/∂y) = 3(x³ + x²y + xy² + y³) = 3f` ✓

---

### Problem 2: Arctangent Function (Degree 0)

**Problem:** If `f(x, y) = arctan(y/x)`, show it is homogeneous of degree 0 and verify Euler's theorem.

**Solution:**

**Part A: Verify Homogeneity**

Replace `x → tx` and `y → ty`:

```
f(tx, ty) = arctan(ty / tx) = arctan(y/x) = f(x, y) = t⁰ · f(x, y)
```

The function is **homogeneous of degree 0**.

**Part B: Verify Euler's Theorem**

Euler's theorem for degree 0 states: `x·(∂f/∂x) + y·(∂f/∂y) = 0`.

Compute partial derivatives. Recall `d/du[arctan(u)] = 1/(1+u²)`.

Let `u = y/x`. Then:

```
∂f/∂x = [1/(1 + (y/x)²)] · ∂/∂x(y/x) = [1/(1 + y²/x²)] · (-y/x²)
       = [-y/x²] / [(x² + y²)/x²] = -y/(x² + y²)

∂f/∂y = [1/(1 + (y/x)²)] · ∂/∂y(y/x) = [1/(1 + y²/x²)] · (1/x)
       = [1/x] / [(x² + y²)/x²] = x/(x² + y²)
```

Form the Euler expression:

```
x·(∂f/∂x) + y·(∂f/∂y) = x · [-y/(x² + y²)] + y · [x/(x² + y²)]
                         = -xy/(x² + y²) + xy/(x² + y²)
                         = 0
```

Since `0 = 0 · f(x, y)`, **Euler's theorem is verified** for degree 0.

**Final Answer:** `x·(∂f/∂x) + y·(∂f/∂y) = 0` ✓

---

### Problem 3: Statement, Proof, and Verification for a Rational Function

**Problem:** State and prove Euler's theorem for `f(x, y) = (x² + y²) / (xy)`.

**Solution:**

**Part A: Verify Homogeneity**

```
f(tx, ty) = [(tx)² + (ty)²] / [(tx)(ty)]
          = [t²x² + t²y²] / [t²xy]
          = t²(x² + y²) / (t²xy)
          = (x² + y²) / (xy)
          = f(x, y)
          = t⁰ · f(x, y)
```

Homogeneous of **degree 0**.

**Part B: State Euler's Theorem**

**Theorem (Euler):** If `f(x, y)` is a homogeneous function of degree `n` with continuous first-order partial derivatives, then:

```
x · (∂f/∂x) + y · (∂f/∂y) = n · f(x, y)
```

For degree 0: `x · (∂f/∂x) + y · (∂f/∂y) = 0`.

**Part C: Proof of Euler's Theorem (for this function)**

First, simplify `f(x, y)`:

```
f(x, y) = (x² + y²)/(xy) = x/y + y/x
```

Compute partial derivatives:

```
∂f/∂x = ∂/∂x(x/y) + ∂/∂x(y/x) = 1/y - y/x²
∂f/∂y = ∂/∂y(x/y) + ∂/∂y(y/x) = -x/y² + 1/x
```

Form the Euler expression:

```
x·(∂f/∂x) + y·(∂f/∂y) = x(1/y - y/x²) + y(-x/y² + 1/x)
                        = x/y - y/x - x/y + y/x
                        = (x/y - x/y) + (-y/x + y/x)
                        = 0 + 0
                        = 0
```

Since `n = 0` and `0 = 0 · f(x, y)`, Euler's theorem is verified.

**Final Answer:** `x·(∂f/∂x) + y·(∂f/∂y) = 0` ✓

---

### Problem 4: Composite Function with Three Variables

**Problem:** If `u = f(x - y, y - z, z - x)`, show that `∂u/∂x + ∂u/∂y + ∂u/∂z = 0`.

**Solution:**

**Part A: Setup**

Let `p = x - y`, `q = y - z`, `r = z - x`. Then `u = f(p, q, r)`.

Note that `p + q + r = (x - y) + (y - z) + (z - x) = 0`.

**Part B: Compute Partial Derivatives Using Chain Rule**

```
∂u/∂x = (∂f/∂p)(∂p/∂x) + (∂f/∂q)(∂q/∂x) + (∂f/∂r)(∂r/∂x)
       = (∂f/∂p)(1) + (∂f/∂q)(0) + (∂f/∂r)(-1)
       = ∂f/∂p - ∂f/∂r

∂u/∂y = (∂f/∂p)(∂p/∂y) + (∂f/∂q)(∂q/∂y) + (∂f/∂r)(∂r/∂y)
       = (∂f/∂p)(-1) + (∂f/∂q)(1) + (∂f/∂r)(0)
       = -∂f/∂p + ∂f/∂q

∂u/∂z = (∂f/∂p)(∂p/∂z) + (∂f/∂q)(∂q/∂z) + (∂f/∂r)(∂r/∂z)
       = (∂f/∂p)(0) + (∂f/∂q)(-1) + (∂f/∂r)(1)
       = -∂f/∂q + ∂f/∂r
```

**Part C: Sum All Three Derivatives**

```
∂u/∂x + ∂u/∂y + ∂u/∂z = (∂f/∂p - ∂f/∂r) + (-∂f/∂p + ∂f/∂q) + (-∂f/∂q + ∂f/∂r)
                        = (∂f/∂p - ∂f/∂p) + (∂f/∂q - ∂f/∂q) + (∂f/∂r - ∂f/∂r)
                        = 0 + 0 + 0
                        = 0
```

**Final Answer:** `∂u/∂x + ∂u/∂y + ∂u/∂z = 0` ✓

**Connection to Homogeneous Functions:** This result can also be understood through the lens of Euler's theorem. The function `f(p, q, r)` evaluated at arguments that sum to zero means the "effective" degree of homogeneity relationship between the partial derivative directions cancels out, yielding the zero result.

---

### Problem 5: Second-Order Euler's Theorem Application

**Problem:** Find the value of `x²(∂²f/∂x²) + 2xy(∂²f/∂x∂y) + y²(∂²f/∂y²)` if `f` is homogeneous of degree 2.

**Solution:**

**Part A: Recall Second-Order Euler's Theorem**

From the higher-order Euler's theorem (derived in Section 2.3), for `f` homogeneous of degree `n`:

```
x²·(∂²f/∂x²) + 2xy·(∂²f/∂x∂y) + y²·(∂²f/∂y²) = n(n - 1) · f
```

**Part B: Apply with n = 2**

```
x²·(∂²f/∂x²) + 2xy·(∂²f/∂x∂y) + y²·(∂²f/∂y²) = 2(2 - 1) · f = 2 · f
```

**Part C: Verification with a Specific Example**

Let `f(x, y) = x² + xy + y²` (homogeneous of degree 2).

Compute second-order partial derivatives:

```
∂f/∂x = 2x + y          →  ∂²f/∂x² = 2
∂f/∂y = x + 2y          →  ∂²f/∂y² = 2
∂²f/∂x∂y = 1
```

Now compute:

```
x²·(2) + 2xy·(1) + y²·(2) = 2x² + 2xy + 2y² = 2(x² + xy + y²) = 2·f
```

This confirms the result.

**Another verification:** Let `f(x, y) = x³y²` (homogeneous of degree 5, not 2, but let us use it to check the general formula).

For `f(x, y) = x³y²`, degree `n = 5`:

```
∂f/∂x = 3x²y²       →  ∂²f/∂x² = 6xy²
∂f/∂y = 2x³y        →  ∂²f/∂y² = 2x³
∂²f/∂x∂y = 6x²y
```

Compute:

```
x²·(6xy²) + 2xy·(6x²y) + y²·(2x³) = 6x³y² + 12x³y² + 2x³y² = 20x³y² = 20·f
```

And `n(n-1) = 5 · 4 = 20` ✓

**Final Answer:** `x²(∂²f/∂x²) + 2xy(∂²f/∂x∂y) + y²(∂²f/∂y²) = 2f` when `n = 2`

---

### Problem 6 (Bonus): Three-Variable Euler's Theorem

**Problem:** Verify Euler's theorem for `f(x, y, z) = x²y + y²z + z²x`, and find its degree.

**Solution:**

**Part A: Determine Degree**

```
f(tx, ty, tz) = (tx)²(ty) + (ty)²(tz) + (tz)²(tx)
              = t³x²y + t³y²z + t³z²x
              = t³(x²y + y²z + z²x)
              = t³ · f(x, y, z)
```

Degree `n = 3`.

**Part B: Verify Euler's Theorem (3 Variables)**

Theorem: `x·(∂f/∂x) + y·(∂f/∂y) + z·(∂f/∂z) = 3f`.

```
∂f/∂x = 2xy + z²
∂f/∂y = x² + 2yz
∂f/∂z = y² + 2zx
```

Compute:

```
x(2xy + z²) + y(x² + 2yz) + z(y² + 2zx)
= 2x²y + xz² + x²y + 2y²z + y²z + 2z²x
= 3x²y + 3y²z + 3z²x
= 3(x²y + y²z + z²x)
= 3f
```

**Final Answer:** `x(∂f/∂x) + y(∂f/∂y) + z(∂f/∂z) = 3f` ✓, degree `n = 3`

---

### Problem 7 (Bonus): Product of Homogeneous Functions

**Problem:** If `f(x, y) = x³ + y³` (degree 3) and `g(x, y) = x + y` (degree 1), find the degree of `f·g` and `f/g`, and verify.

**Solution:**

**Part A: Product `h = f·g`**

```
h(tx, ty) = f(tx,ty) · g(tx,ty) = t³·f(x,y) · t¹·g(x,y) = t⁴ · (f·g)(x,y)
```

Degree of `f·g` is **4**.

**Verification:**

```
h(x, y) = (x³ + y³)(x + y) = x⁴ + x³y + xy³ + y⁴
h(tx, ty) = t⁴x⁴ + t⁴x³y + t⁴xy³ + t⁴y⁴ = t⁴ · h(x, y) ✓
```

**Part B: Quotient `k = f/g`**

```
k(tx, ty) = f(tx,ty) / g(tx,ty) = t³·f(x,y) / t¹·g(x,y) = t² · (f/g)(x,y)
```

Degree of `f/g` is **2**.

**Verification:**

```
k(x, y) = (x³ + y³)/(x + y) = x² - xy + y²    [for x + y ≠ 0]
k(tx, ty) = (t³x³ + t³y³)/(tx + ty) = t³(x³+y³) / t(x+y) = t² · k(x, y) ✓
```

**Final Answer:** `f·g` has degree **4**; `f/g` has degree **2**.

---

## 4. ENGINEERING APPLICATIONS MAP

---

### 4.1 Comprehensive Applications Table

| Application Domain | Homogeneous Function Concept | Euler's Theorem Role | Specific Use |
|-------------------|------------------------------|----------------------|--------------|
| **Thermodynamics** | Equations of state (e.g., ideal gas `PV = nRT`) | Internal energy `U(T,V)` is degree 1 → `U = T(∂U/∂T) + V(∂U/∂V)` | Deriving thermodynamic identities |
| **Fluid Mechanics** | Similarity solutions in boundary layers | Scaling laws for velocity profiles | Blasius boundary layer equation |
| **Heat Transfer** | Temperature distributions with geometric symmetry | Heat flux scaling in radial coordinates | Steady-state conduction in cylinders |
| **Structural Engineering** | Stress and strain scaling | Stress function homogeneity | Beam deflection theory |
| **Electrical Engineering** | Power dissipation `P = I²R` (degree 3 in `I`) | Component scaling laws | Circuit element scaling |
| **Economics** | Production functions `Q(K, L)` — Cobb-Douglas `Q = AK^αL^β` | Returns to scale = degree of homogeneity | If `α + β = 1` → constant returns to scale |
| **Chemical Engineering** | Reaction rate laws | Rate scaling with concentration | Dimensionless groups in reactors |
| **Dimensional Analysis** | Buckingham Pi Theorem | Ensuring dimensional consistency | Reducing number of variables in experiments |
| **Ordinary Differential Equations** | `dy/dx = F(y/x)` reduction | Substitution `y = vx` yields separable ODE | Engineering model simplification |
| **Partial Differential Equations** | Self-similar solutions | Scaling transformations | Heat equation, wave equation solutions |
| **Control Systems** | Transfer function scaling | Gain margin scaling | System identification |
| **Probability & Statistics** | Power-law distributions `p(x) ∝ x^(-α)` | Moments of heavy-tailed distributions | Pareto distribution analysis |
| **Image Processing** | Scale-invariant features | Image pyramid construction | Feature detection at multiple scales |
| **Robotics** | Kinematic scaling | Workspace volume scaling | Manipulator design |

### 4.2 Detailed Engineering Examples

#### Example 1: Thermodynamics — Ideal Gas Law

The internal energy of an ideal gas `U(T, V)` satisfies:

```
U(λT, λV) = λ · U(T, V)
```

This means `U` is homogeneous of degree 1 in `T` and `V`. By Euler's theorem:

```
T · (∂U/∂T) + V · (∂U/∂V) = 1 · U = U
```

Since `∂U/∂T = C_v` (heat capacity at constant volume) and `∂U/∂V = T(∂P/∂T)_V - P` (from the thermodynamic identity), this yields:

```
T · C_v + V · [T(∂P/∂T)_V - P] = U
```

This is a fundamental thermodynamic identity.

#### Example 2: Economics — Cobb-Douglas Production Function

The Cobb-Douglas production function:

```
Q(K, L) = A · K^α · L^β
```

is homogeneous of degree `n = α + β`.

- If `α + β = 1`: Constant returns to scale (CRS)
- If `α + β > 1`: Increasing returns to scale (IRS)
- If `α + β < 1`: Decreasing returns to scale (DRS)

By Euler's theorem (for CRS case, `n = 1`):

```
K · (∂Q/∂K) + L · (∂Q/∂L) = Q
```

This means: `K · (marginal product of capital) + L · (marginal product of labor) = total output`.

#### Example 3: ODE Reduction — Engineering Model

Consider the ODE arising in chemical reactor design:

```
dy/dx = (x² + 2xy) / (x² + y²)
```

The right-hand side is homogeneous of degree 0 (both numerator and denominator are degree 2). Substitute `y = vx`:

```
v + x·dv/dx = (x² + 2x·vx) / (x² + v²x²) = (1 + 2v) / (1 + v²)
```

This gives:

```
x·dv/dx = (1 + 2v)/(1 + v²) - v = (1 + 2v - v - v³) / (1 + v²) = (1 + v - v³) / (1 + v²)
```

This is now separable and can be solved.

#### Example 4: Fluid Mechanics — Similarity Solutions

In boundary layer theory, the velocity profile `u(x, y)` near a flat plate satisfies:

```
u(x, y) = U_∞ · g(η), where η = y / √(νx/U_∞)
```

The similarity variable `η` is dimensionless, and the velocity field exhibits scaling homogeneity. The Blasius equation:

```
2g''' + g·g'' = 0
```

arises from imposing that the Navier-Stokes equations are invariant under the scaling transformation that preserves homogeneity.

#### Example 5: Dimensional Analysis

In any physical experiment, if a quantity `Q` depends on parameters `p_1, p_2, ..., p_k` all sharing the same dimensions, and `Q` is homogeneous of degree `n` in these parameters, then:

```
Q(λp_1, ..., λp_k) = λ^n · Q(p_1, ..., p_k)
```

Dividing by `p_1^n`:

```
Q/p_1^n = (p_2/p_1, p_3/p_1, ..., p_k/p_1) = φ(π_2, ..., π_k)
```

where `π_i = p_i/p_1` are dimensionless groups. This is the essence of the **Buckingham Pi Theorem**.

### 4.3 Summary: Why Engineers Need Homogeneous Functions

```
┌──────────────────────────────────────────────────────────────────┐
│                    ENGINEERING VALUE CHAIN                        │
│                                                                  │
│  Homogeneous Function Properties                                 │
│         │                                                        │
│         ├──→ Scaling Laws: How do quantities change with size?   │
│         │         │                                              │
│         │         └──→ Model Simplification (reduce variables)   │
│         │                                                        │
│         ├──→ Euler's Theorem: Energy/partition identities        │
│         │         │                                              │
│         │         └──→ Fundamental physical constraints          │
│         │                                                        │
│         ├──→ Degree Analysis: Returns to scale, efficiency       │
│         │         │                                              │
│         │         └──→ Design optimization                       │
│         │                                                        │
│         ├──→ Substitution y = vx: ODE reduction                  │
│         │         │                                              │
│         │         └──→ Analytical solutions for engineering      │
│         │               models                                   │
│         │                                                        │
│         └──→ Similarity Solutions: Self-similar profiles         │
│                   │                                              │
│                   └──→ Universal curves for experimental data    │
└──────────────────────────────────────────────────────────────────┘
```

---

## 5. REFERENCE SUMMARY

---

### 5.1 Key Formulas Quick Reference

| Formula | Description |
|---------|-------------|
| `f(tx, ty) = t^n · f(x, y)` | Definition of homogeneous degree `n` |
| `x·(∂f/∂x) + y·(∂f/∂y) = n·f` | Euler's theorem (2 variables) |
| `Σ x_i · (∂f/∂x_i) = n·f` | Euler's theorem (N variables) |
| `x·(∂f/∂x) + y·(∂f/∂y) = 0` | Euler's theorem for degree 0 |
| `x²·f_xx + 2xy·f_xy + y²·f_yy = n(n-1)·f` | Second-order Euler's theorem |
| `(x∂/∂x + y∂/∂y)^m [f] = n^(m)·f` | m-th order Euler's theorem |
| `f(x, y) = x^n · φ(y/x)` | Decomposition form |
| `f(x, y) = y^n · ψ(x/y)` | Alternative decomposition |
| `∂f/∂x` is degree `n-1` | Partial derivative reduces degree by 1 |
| `f·g` is degree `m+n` | Product rule for degrees |
| `f/g` is degree `m-n` | Quotient rule for degrees |
| `f^k` is degree `kn` | Power rule for degrees |
| `y = vx` substitution | Reduces homogeneous ODEs to separable form |

### 5.2 Common Pitfalls and Errors

| Pitfall | Correction |
|---------|------------|
| Assuming all functions are homogeneous | Always verify by substitution `t` before applying theorems |
| Getting the degree wrong | Carefully track the exponent of `t` that factors out |
| Forgetting the converse requires regularity conditions | The converse needs continuous differentiability |
| Applying Euler's theorem to non-differentiable functions | Ensure `f` has continuous partial derivatives |
| Confusing homogeneity with linearity | Linearity: `f(x+y) = f(x)+f(y)`; Homogeneity: `f(tx) = t^n·f(x)` |
| Incorrectly computing the second-order form | Remember: `n(n-1)`, not `n²` |
| Forgetting to check the domain is a cone | Homogeneity only holds on domains closed under positive scaling |

### 5.3 Notation Guide

| Notation | Full Name | Context |
|----------|-----------|---------|
| `f_x` or `∂f/∂x` | Partial derivative with respect to `x` | Calculus |
| `f_{xx}` or `∂²f/∂x²` | Second partial derivative with respect to `x` | Calculus |
| `f_{xy}` or `∂²f/∂x∂y` | Mixed partial derivative | Calculus |
| `E[f]` or `(x∂/∂x + y∂/∂y)[f]` | Euler operator applied to `f` | PDE theory |
| `n^(m)` or `[n]_m` | Falling factorial `n(n-1)...(n-m+1)` | Combinatorics |
| `C(m,k)` or `binom(m,k)` | Binomial coefficient `m!/(k!(m-k)!)` | Combinatorics |
| `α` (multi-index) | `(α_1, ..., α_N)` with `\|α\| = Σα_i` | Multivariable calculus |
| `∇` (nabla) | Gradient operator `(∂/∂x_1, ..., ∂/∂x_N)` | Vector calculus |
| `λ` or `t` | Scaling parameter | Homogeneity |
| `φ`, `ψ` | Arbitrary single-variable functions | General notation |

---

## CROSS-REFERENCES

- [[engineering-math/module-2-partial-differentiation|Module 2: Partial Differentiation]] — Partial differentiation is the essential tool for applying Euler's theorem: computing ∂f/∂x and ∂f/∂y, verifying homogeneity via substitution, and deriving the higher-order Euler identities. The chain rule and total differential concepts underpin the proofs.
- [[engineering-math/module-4-linear-differential-equations|Module 4: Linear Differential Equations]] — The substitution y = vx for homogeneous ODEs (dy/dx = F(y/x)) directly uses the property that homogeneous functions of degree 0 depend only on the ratio y/x, reducing the ODE to separable form.
- [[engineering-math/module-1-matrices|Module 1: Matrices]] — Homogeneous systems of linear equations (Ax = 0) use the term "homogeneous" in a different but related sense; the null space concept connects to degree-zero homogeneous functions via linear algebra.
- [[engineering-math/module-5-complex-numbers|Module 5: Complex Numbers]] — Complex hyperbolic functions (sinh, cosh) and their relationships to circular trigonometric functions arise in the context of homogeneous functions of complex arguments; the exponential form e^(iθ) connects to degree analysis.

*Module 3 of 5 — [[engineering-math/module-2-partial-differentiation|← Module 2]] | [[engineering-math/module-4-linear-differential-equations|Module 4 →]]*

*End of Module 3: Homogeneous Functions — Euler's Theorem & Deductions*
