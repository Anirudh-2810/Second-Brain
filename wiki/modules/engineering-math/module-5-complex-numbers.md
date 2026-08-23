---
module: "engineering-math"
topic: "Module 5: Complex Numbers — De Moivre, Roots, Hyperbolic & Logarithmic Functions"
tags: [complex-numbers, de-moivre, roots, hyperbolic-functions, logarithm, polar-form, euler-formula]
last_updated: "2026-08-18"
prerequisites: ["Trigonometry", "Exponential Functions", "Basic Algebra"]
---

# Module 5: Complex Numbers

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.1 Complex Number Forms Table

| Form | Representation | Modulus | Argument | Conversion |
|------|---------------|---------|----------|------------|
| **Rectangular** | `z = a + ib` | `r = √(a² + b²)` | `θ = arctan(b/a)` | Given form |
| **Polar** | `z = r ∠ θ` | `r` | `θ` | `a = r cosθ, b = r sinθ` |
| **Exponential** | `z = re^(iθ)` | `r` | `θ` | `r = √(a²+b²), θ = arctan(b/a)` |
| **Trigonometric** | `z = r(cosθ + i sinθ)` | `r` | `θ` | `r = √(a²+b²), θ = arctan(b/a)` |

**Key Symbol Reference:**

| Symbol | Meaning | Range/Notes |
|--------|---------|-------------|
| `i` | Imaginary unit, `i² = -1` | `i = √(-1)` |
| `a` | Real part of z | `Re(z) = a` |
| `b` | Imaginary part of z | `Im(z) = b` |
| `r` | Modulus (magnitude) of z | `r = \|z\| ≥ 0` |
| `θ` | Argument (angle) of z | `-π < θ ≤ π` (principal) |
| `z̄` | Complex conjugate of z | `z̄ = a - ib` |
| `e` | Euler's number | `e ≈ 2.71828` |
| `arg(z)` | Argument set of z | `arg(z) = θ + 2kπ` |
| `Arg(z)` | Principal argument | `Arg(z) ∈ (-π, π]` |

**Conversion Examples:**

```
Rectangular → Polar:
  z = 3 + 4i
  r = √(3² + 4²) = √25 = 5
  θ = arctan(4/3) = 53.13° = 0.9273 rad
  z = 5(cos 53.13° + i sin 53.13°) = 5e^(i·0.9273)

Polar → Rectangular:
  z = 2(cos 60° + i sin 60°)
  a = 2 cos 60° = 2(0.5) = 1
  b = 2 sin 60° = 2(√3/2) = √3
  z = 1 + i√3

Exponential → Rectangular:
  z = 3e^(iπ/4)
  a = 3 cos(π/4) = 3(√2/2) = 3√2/2
  b = 3 sin(π/4) = 3(√2/2) = 3√2/2
  z = 3√2/2 + i(3√2/2)
```

**Rectangular → Exponential (Direct):**

```
z = a + ib → z = r·e^(iθ)
where r = √(a² + b²)  and  θ = atan2(b, a)

Note: atan2 handles all four quadrants correctly.
```

---

### 1.2 De Moivre's Theorem Flowchart (ASCII)

```
╔══════════════════════════════════════════════════════════════════════╗
║                    DE MOIVRE'S THEOREM FLOWCHART                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  START: Given z = a + ib (rectangular form)                          ║
║  ┌──────────────────────────────────────────────┐                     ║
║  │  Step 1: Convert to Polar Form               │                     ║
║  │  r = √(a² + b²)                              │                     ║
║  │  θ = arctan(b/a) with quadrant check         │                     ║
║  │  z = r(cosθ + i sinθ) = re^(iθ)              │                     ║
║  └──────────────────┬───────────────────────────┘                     ║
║                     ▼                                                 ║
║  ┌──────────────────────────────────────────────┐                     ║
║  │  Step 2: Choose Application                  │                     ║
║  │         ┌────────┬─────────┬────────┐        │                     ║
║  │         ▼        ▼         ▼        ▼        │                     ║
║  │      POWERS    ROOTS   TRIG IDENTITY  PROOF   │                    ║
║  └──────────────────┬───────────────────────────┘                     ║
║                     │                                                 ║
║  ┌──────────────────┴───────────────────────────┐                     ║
║  │  APPLICATION A: POWERS (zⁿ)                  │                     ║
║  │  zⁿ = rⁿ(cos nθ + i sin nθ)                  │                    ║
║  │                                               │                     ║
║  │  Sub-steps:                                   │                     ║
║  │  (1) Compute rⁿ                               │                    ║
║  │  (2) Compute nθ (multiply angle by n)         │                    ║
║  │  (3) Write result in polar or rectangular     │                    ║
║  │  (4) If rectangular needed: expand            │                    ║
║  │      rⁿ cos nθ + i · rⁿ sin nθ               │                   ║
║  └──────────────────┬───────────────────────────┘                     ║
║                     │                                                 ║
║  ┌──────────────────┴───────────────────────────┐                     ║
║  │  APPLICATION B: ROOTS (z^(1/n))              │                     ║
║  │  zₖ = r^(1/n)[cos((θ+2kπ)/n) + i sin((θ+2kπ)/n)]               ║
║  │  for k = 0, 1, 2, ..., n-1                   │                     ║
║  │                                               │                     ║
║  │  Sub-steps:                                   │                     ║
║  │  (1) Compute r^(1/n)                          │                     ║
║  │  (2) For each k = 0 to n-1:                   │                     ║
║  │      θₖ = (θ + 2kπ) / n                       │                    ║
║  │  (3) Write zₖ = r^(1/n)(cos θₖ + i sin θₖ)   │                   ║
║  │  (4) Convert each to rectangular if needed    │                     ║
║  └──────────────────┬───────────────────────────┘                     ║
║                     │                                                 ║
║  ┌──────────────────┴───────────────────────────┐                     ║
║  │  APPLICATION C: TRIG IDENTITIES               │                    ║
║  │  (cosθ + i sinθ)ⁿ = cos nθ + i sin nθ        │                   ║
║  │                                               │                     ║
║  │  Sub-steps:                                   │                     ║
║  │  (1) Expand LHS using Binomial Theorem        │                     ║
║  │  (2) Equate real parts → identity for cos nθ  │                    ║
║  │  (3) Equate imaginary parts → sin nθ          │                    ║
║  │  (4) Simplify using known cos²θ + sin²θ = 1  │                    ║
║  └──────────────────────────────────────────────┘                     ║
║                                                                      ║
║  END                                                                  ║
╚══════════════════════════════════════════════════════════════════════╝
```

**Quick Reference — De Moivre's Theorem:**

| Problem Type | Formula | Key Step |
|-------------|---------|----------|
| zⁿ (power) | `(re^(iθ))ⁿ = rⁿe^(inθ)` | Multiply angle by n |
| z^(1/n) (root) | `r^(1/n)e^(i(θ+2kπ)/n)` | k = 0, 1, ..., n-1 |
| cos nθ | `Re[(cosθ + i sinθ)ⁿ]` | Extract real part |
| sin nθ | `Im[(cosθ + i sinθ)ⁿ]` | Extract imaginary part |

---

### 1.3 nth Roots of Complex Numbers Flowchart (ASCII)

```
╔══════════════════════════════════════════════════════════════════════════╗
║                  nth ROOTS OF COMPLEX NUMBERS FLOWCHART                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  Given: z = r(cosθ + i sinθ), find all nth roots                       ║
║                                                                          ║
║  Step 1: Compute the modulus of each root                                ║
║  ┌────────────────────────────────────────────────────────────┐          ║
║  │  R = r^(1/n)                                               │          ║
║  │  Each root has the SAME modulus R                          │          ║
║  │  All roots lie on a circle of radius R                     │          ║
║  └────────────────────────┬───────────────────────────────────┘          ║
║                           ▼                                              ║
║  Step 2: Compute the arguments of each root                             ║
║  ┌────────────────────────────────────────────────────────────┐          ║
║  │  θₖ = (θ + 2kπ) / n   for k = 0, 1, 2, ..., n-1          │          ║
║  │                                                            │          ║
║  │  First root (k=0):  θ₀ = θ/n                              │          ║
║  │  Second root (k=1): θ₁ = (θ + 2π)/n                       │          ║
║  │  Third root (k=2):  θ₂ = (θ + 4π)/n                       │          ║
║  │  ...                                                       │          ║
║  │  nth root (k=n-1): θ_{n-1} = (θ + 2(n-1)π)/n             │          ║
║  └────────────────────────┬───────────────────────────────────┘          ║
║                           ▼                                              ║
║  Step 3: Write the roots                                                ║
║  ┌────────────────────────────────────────────────────────────┐          ║
║  │  zₖ = R(cos θₖ + i sin θₖ)   for k = 0, 1, ..., n-1      │          ║
║  │                                                            │          ║
║  │  Convert to rectangular if required:                       │          ║
║  │  zₖ = R cos θₖ + i · R sin θₖ                             │          ║
║  └────────────────────────────────────────────────────────────┘          ║
║                                                                          ║
║  GEOMETRIC INTERPRETATION:                                               ║
║  ┌────────────────────────────────────────────────────────────┐          ║
║  │                                                            │          ║
║  │              * z₁ = 1·e^(i·2π/3)                          │          ║
║  │             / \                                            │          ║
║  │            /   \         n = 3 (cube roots of unity)       │          ║
║  │           /  1  \        R = 1                             │          ║
║  │          /       \       Angular spacing = 2π/3 = 120°     │          ║
║  │         /    O    \                                         │          ║
║  │        /           \                                        │          ║
║  │       *─────────────*                                       │          ║
║  │    z₂ = 1·e^(i·4π/3)  z₀ = 1·e^(i·0) = 1                 │          ║
║  │                                                            │          ║
║  │  → Roots form a REGULAR n-gon on the circle |z| = R        │          ║
║  │  → Vertices equally spaced by 2π/n radians                 │          ║
║  └────────────────────────────────────────────────────────────┘          ║
║                                                                          ║
║  SPECIAL CASES:                                                          ║
║  ┌────────────────────────────────────────────────────────────┐          ║
║  │  nth roots of unity: zⁿ = 1                                │          ║
║  │  zₖ = e^(i·2kπ/n)  for k = 0, 1, ..., n-1                │          ║
║  │                                                            │          ║
║  │  n=2 (square roots of 1): 1, -1                           │          ║
║  │  n=3 (cube roots of unity): 1, ω, ω²                       │          ║
║  │    where ω = e^(i·2π/3) = -1/2 + i√3/2                    │          ║
║  │         ω² = e^(i·4π/3) = -1/2 - i√3/2                    │          ║
║  │    Property: 1 + ω + ω² = 0                                │          ║
║  │  n=4 (fourth roots of 1): 1, i, -1, -i                    │          ║
║  └────────────────────────────────────────────────────────────┘          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**Roots on the Complex Plane — Unit Circle Example (n=5):**

```
                        Im(z)
                          │
                    z₂ ●  │  ● z₁
                   ╱      │      ╲
                  ╱       │       ╲
                 ╱        │        ╲
    ───────────●──────────┼──────────●─────────── Re(z)
    z₃        ╱           │           ╲         z₀ = 1
                 ╲        │        ╱
                  ╲       │       ╱
                   ╲      │      ╱
                    z₄ ●  │
                          │

    All 5 roots of z⁵ = 1 lie on the unit circle
    Angular spacing = 2π/5 = 72°
    zₖ = cos(2kπ/5) + i sin(2kπ/5),  k = 0,1,2,3,4
```

---

### 1.4 Hyperbolic Functions Reference Table

**Definitions and Identities:**

| Function | Definition | Identity | Relationship to Trig |
|----------|-----------|----------|---------------------|
| `sinh x` | `(eˣ - e⁻ˣ)/2` | `cosh²x - sinh²x = 1` | `-i sin(ix)` |
| `cosh x` | `(eˣ + e⁻ˣ)/2` | `cosh²x - sinh²x = 1` | `cos(ix)` |
| `tanh x` | `sinh x / cosh x` | `1 - tanh²x = sech²x` | `-i tan(ix)` |
| `sech x` | `1 / cosh x` | `sech²x + tanh²x = 1` | `sec(ix)` |
| `csch x` | `1 / sinh x` | `coth²x - csch²x = 1` | `i csc(ix)` |
| `coth x` | `cosh x / sinh x` | `coth²x - csch²x = 1` | `i cot(ix)` |

**Symbol Reference:**

| Symbol | Meaning |
|--------|---------|
| `sinh x` | Hyperbolic sine |
| `cosh x` | Hyperbolic cosine |
| `tanh x` | Hyperbolic tangent |
| `sech x` | Hyperbolic secant |
| `csch x` | Hyperbolic cosecant |
| `coth x` | Hyperbolic cotangent |
| `eˣ` | Exponential function |

**Key Addition Formulas:**

```
sinh(x ± y) = sinh x cosh y ± cosh x sinh y
cosh(x ± y) = cosh x cosh y ± sinh x sinh y
tanh(x ± y) = (tanh x ± tanh y) / (1 ± tanh x tanh y)
```

**Relationships to Circular Trigonometric Functions:**

```
sinh(ix) = i sin(x)          cosh(ix) = cos(x)
sin(ix)  = i sinh(x)         cos(ix)  = cosh(x)

sin(x + iy) = sin x cosh y + i cos x sinh y
cos(x + iy) = cos x cosh y - i sin x sinh y
```

**Inverse Hyperbolic Functions and Logarithmic Forms:**

| Inverse Function | Logarithmic Form | Domain |
|-----------------|-----------------|--------|
| `sinh⁻¹ x` | `ln(x + √(x² + 1))` | All real x |
| `cosh⁻¹ x` | `ln(x + √(x² - 1))` | x ≥ 1 |
| `tanh⁻¹ x` | `(1/2) ln((1+x)/(1-x))` | \|x\| < 1 |
| `sech⁻¹ x` | `ln((1 + √(1-x²))/x)` | 0 < x ≤ 1 |
| `csch⁻¹ x` | `ln((1 + √(1+x²))/x)` | x ≠ 0 |
| `coth⁻¹ x` | `(1/2) ln((x+1)/(x-1))` | \|x\| > 1 |

---

### 1.5 Separation into Real and Imaginary Parts Flowchart (ASCII)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║            SEPARATION INTO REAL AND IMAGINARY PARTS FLOWCHART               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  START: Given expression involving complex numbers                           ║
║  ┌──────────────────────────────────────────────────────────────┐            ║
║  │  Identify the form of the expression                         │            ║
║  └──────────────────────┬───────────────────────────────────────┘            ║
║                         │                                                    ║
║           ┌─────────────┼─────────────┬──────────────┐                       ║
║           ▼             ▼             ▼              ▼                       ║
║    ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐               ║
║    │ e^(a+ib) │  │ sin/cos  │  │ Fraction │  │ Log(z)       │               ║
║    │    or    │  │ (a+ib)   │  │ 1/(a+ib) │  │ Ln(z)        │               ║
║    │ zⁿ form  │  │          │  │          │  │              │               ║
║    └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘               ║
║         │             │             │               │                         ║
║         ▼             ▼             ▼               ▼                         ║
║  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────────┐              ║
║  │ METHOD A   │ │ METHOD B   │ │ METHOD C   │ │ METHOD D     │              ║
║  │            │ │            │ │            │ │              │              ║
║  │ e^(a+ib)  │ │ sin(a+ib)  │ │ Multiply   │ │ Ln(a+ib)     │              ║
║  │ = eᵃe^(ib)│ │ = sin a    │ │ by the     │ │ = ln|z|      │              ║
║  │ = eᵃ(cos b│ │   cosh b   │ │ conjugate  │ │   + i Arg(z) │              ║
║  │   +i sin b)│ │ + i cos a  │ │ z̄/z̄       │ │              │              ║
║  │           │ │   sinh b   │ │ = (a-ib)/  │ │ = (1/2)ln    │              ║
║  │ Re = eᵃcos│ │            │ │   (a²+b²)  │ │   (a²+b²)    │              ║
║  │ Im = eᵃsin│ │ Re = sin a │ │            │ │ + i arctan   │              ║
║  │           │ │   cosh b   │ │ Re = a/    │ │   (b/a)      │              ║
║  │           │ │ Im = cos a │ │   (a²+b²)  │ │              │              ║
║  │           │ │   sinh b   │ │ Im = -b/   │ │              │              ║
║  │           │ │            │ │   (a²+b²)  │ │              │              ║
║  └────────────┘ └────────────┘ └────────────┘ └──────────────┘              ║
║                                                                              ║
║  GENERAL TECHNIQUE:                                                          ║
║  ┌──────────────────────────────────────────────────────────────┐            ║
║  │  1. Write everything in exponential or trigonometric form    │            ║
║  │  2. Use known expansion formulas for complex arguments       │            ║
║  │  3. Collect real terms and imaginary terms separately        │            ║
║  │  4. Simplify using cos²x + sin²x = 1 or cosh²x - sinh²x=1 │            ║
║  │  5. Final form: u(x,y) + i v(x,y) where u, v are real      │            ║
║  └──────────────────────────────────────────────────────────────┘            ║
║                                                                              ║
║  END: Re(z) = u, Im(z) = v                                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

**Complete Reference — Separation Formulas:**

```
╔═══════════════════════════════════════════════════════════════════╗
║  EXPRESSION              │  REAL PART           │ IMAGINARY PART  ║
╠═══════════════════════════════════════════════════════════════════╣
║  e^(a+ib)               │  eᵃ cos b            │ eᵃ sin b       ║
║  sin(a+ib)              │  sin a cosh b        │ cos a sinh b   ║
║  cos(a+ib)              │  cos a cosh b        │-sin a sinh b   ║
║  tan(a+ib)              │  sin 2a/(cos 2a+cosh 2b)              ║
║                         │                    │ sinh 2b/(cos 2a+cosh 2b) ║
║  Log(a+ib)              │  (1/2)ln(a²+b²)     │ arctan(b/a)    ║
║  1/(a+ib)               │  a/(a²+b²)          │-b/(a²+b²)     ║
║  (a+ib)ⁿ               │  rⁿ cos nθ          │ rⁿ sin nθ      ║
║  sinh(a+ib)             │  sinh a cos b        │ cosh a sin b   ║
║  cosh(a+ib)             │  cosh a cos b        │ sinh a sin b   ║
╚═══════════════════════════════════════════════════════════════════╝

Note: θ = arctan(b/a) and r = √(a² + b²)
```

---

## 2. MATHEMATICAL FORMULATION & CORE THEOREMS

### 2.1 Complex Number Algebra

**Basic Operations:**

```
Let z₁ = a + ib  and  z₂ = c + id

ADDITION:
  z₁ + z₂ = (a + c) + i(b + d)
  Example: (3 + 2i) + (1 - 4i) = 4 - 2i

SUBTRACTION:
  z₁ - z₂ = (a - c) + i(b - d)
  Example: (3 + 2i) - (1 - 4i) = 2 + 6i

MULTIPLICATION:
  z₁ · z₂ = (ac - bd) + i(ad + bc)
  Alternative (using FOIL):
    z₁ · z₂ = (a + ib)(c + id) = ac + iad + ibc + i²bd
            = ac - bd + i(ad + bc)
  Example: (3 + 2i)(1 - 4i) = (3 + 8) + i(2 - 12) = 11 - 10i

DIVISION:
  z₁ / z₂ = (z₁ · z̄₂) / (z₂ · z̄₂) = [(ac + bd) + i(bc - ad)] / (c² + d²)
  Example: (3 + 2i) / (1 - 4i) = [(3 + 8) + i(2 + 12)] / (1 + 16)
                                = (11 + 14i) / 17
                                = 11/17 + 14i/17
```

**Conjugate Properties:**

```
If z = a + ib, then z̄ = a - ib

Properties:
  (1)  z + z̄ = 2a = 2 Re(z)          (always real)
  (2)  z - z̄ = 2ib = 2i Im(z)         (always pure imaginary)
  (3)  z · z̄ = a² + b² = |z|²         (always real, non-negative)
  (4)  (z₁ + z̄₂)̄ = z̄₁ + z̄₂           (conjugate of sum = sum of conjugates)
  (5)  (z₁ · z̄₂)̄ = z̄₁ · z̄₂           (conjugate of product = product of conjugates)
  (6)  (z̄̄) = z                        (double conjugate returns original)
  (7)  z / z̄ = (a + ib)² / (a² + b²)  (ratio gives unit modulus if |z|=1)
```

**Modulus Properties:**

```
|z| = √(a² + b²) = √(z · z̄)

Properties:
  (1)  |z₁ · z₂| = |z₁| · |z₂|
  (2)  |z₁ / z₂| = |z₁| / |z₂|      (z₂ ≠ 0)
  (3)  |zⁿ| = |z|ⁿ
  (4)  |z + z̄| ≤ |z| + |z̄|          (triangle inequality: |z₁+z₂| ≤ |z₁|+|z₂|)
  (5)  ||z₁| - |z₂|| ≤ |z₁ - z₂|
```

**Argument Properties:**

```
arg(z) = θ such that z = |z|(cosθ + i sinθ)

For z₁ = r₁e^(iθ₁) and z₂ = r₂e^(iθ₂):

  arg(z₁ · z₂) = arg(z₁) + arg(z₂)     (mod 2π)
  arg(z₁ / z₂) = arg(z₁) - arg(z₂)     (mod 2π)
  arg(zⁿ) = n · arg(z)                   (mod 2π)

Principal argument: Arg(z) ∈ (-π, π]
General argument: arg(z) = Arg(z) + 2kπ,  k ∈ ℤ
```

---

### 2.2 Euler's Formula and Its Consequences

**Euler's Formula:**

```
e^(iθ) = cosθ + i sinθ
```

**Derivation from Taylor Series:**

```
Recall the Taylor series expansions (valid for all x ∈ ℝ):

eˣ = 1 + x + x²/2! + x³/3! + x⁴/4! + x⁵/5! + ...

Substitute x = iθ:

e^(iθ) = 1 + iθ + (iθ)²/2! + (iθ)³/3! + (iθ)⁴/4! + (iθ)⁵/5! + (iθ)⁶/6! + ...

Note the powers of i:
  i⁰ = 1
  i¹ = i
  i² = -1
  i³ = -i
  i⁴ = 1
  i⁵ = i
  i⁶ = -1
  (pattern: 1, i, -1, -i, repeating with period 4)

Therefore:
  e^(iθ) = 1 + iθ - θ²/2! - iθ³/3! + θ⁴/4! + iθ⁵/5! - θ⁶/6! - ...

Separate real and imaginary parts:
  e^(iθ) = [1 - θ²/2! + θ⁴/4! - θ⁶/6! + ...] + i[θ - θ³/3! + θ⁵/5! - ...]

Recognize:
  cosθ = 1 - θ²/2! + θ⁴/4! - θ⁶/6! + ...
  sinθ = θ - θ³/3! + θ⁵/5! - θ⁷/7! + ...

Therefore:
  e^(iθ) = cosθ + i sinθ    ∎
```

**Euler's Identity (Special Case θ = π):**

```
e^(iπ) = cosπ + i sinπ = -1 + 0 = -1

Therefore: e^(iπ) + 1 = 0

This connects five fundamental constants: e, i, π, 1, 0
Called "the most beautiful equation in mathematics."
```

**Consequences and Derivations:**

```
From e^(iθ) = cosθ + i sinθ, let θ → -θ:

e^(-iθ) = cos(-θ) + i sin(-θ) = cosθ - i sinθ

Adding e^(iθ) and e^(-iθ):
  e^(iθ) + e^(-iθ) = 2 cosθ
  cosθ = (e^(iθ) + e^(-iθ)) / 2

Subtracting e^(-iθ) from e^(iθ):
  e^(iθ) - e^(-iθ) = 2i sinθ
  sinθ = (e^(iθ) - e^(-iθ)) / (2i)
```

**Exponential Form of Complex Numbers:**

```
z = a + ib = r(cosθ + i sinθ) = re^(iθ)

where:
  r = |z| = √(a² + b²)   (modulus)
  θ = arg(z) = arctan(b/a)   (argument, with quadrant consideration)

Conversions:
  Rectangular → Exponential:  a + ib → √(a²+b²) · e^(i·arctan(b/a))
  Exponential → Rectangular:  re^(iθ) → r cosθ + i(r sinθ)
```

---

### 2.3 De Moivre's Theorem

**Statement:**

```
For any real number θ and any integer n:

  (cosθ + i sinθ)ⁿ = cos(nθ) + i sin(nθ)

Equivalently, in exponential form:

  (e^(iθ))ⁿ = e^(inθ)
```

**Proof by Mathematical Induction:**

```
Statement P(n): (cosθ + i sinθ)ⁿ = cos(nθ) + i sin(nθ)

BASE CASE (n = 1):
  LHS = (cosθ + i sinθ)¹ = cosθ + i sinθ
  RHS = cos(1·θ) + i sin(1·θ) = cosθ + i sinθ
  LHS = RHS  ✓

INDUCTIVE STEP:
  Assume P(k) is true for some positive integer k:
    (cosθ + i sinθ)ᵏ = cos(kθ) + i sin(kθ)

  Show P(k+1) is true:
    (cosθ + i sinθ)^(k+1)
    = (cosθ + i sinθ)ᵏ · (cosθ + i sinθ)
    = [cos(kθ) + i sin(kθ)] · [cosθ + i sinθ]     (by inductive hypothesis)
    = cos(kθ)cosθ + i cos(kθ)sinθ + i sin(kθ)cosθ + i² sin(kθ)sinθ
    = cos(kθ)cosθ - sin(kθ)sinθ + i[sin(kθ)cosθ + cos(kθ)sinθ]
    = cos(kθ + θ) + i sin(kθ + θ)                    (angle addition formulas)
    = cos((k+1)θ) + i sin((k+1)θ)

  Therefore P(k+1) is true. ∎
```

**Extension to Rational Exponents:**

```
De Moivre's Theorem extends to n = 1/m (roots):

  (cosθ + i sinθ)^(1/m) = cos(θ/m) + i sin(θ/m)

Note: When m > 1, there are m distinct values (see Section 2.4 on roots).
```

**Applications to Derive Trig Identities:**

**Double Angle Identities (n = 2):**

```
(cosθ + i sinθ)² = cos 2θ + i sin 2θ

Expand LHS:
  cos²θ + 2i cosθ sinθ + i² sin²θ
  = cos²θ - sin²θ + i(2 sinθ cosθ)

Equate real and imaginary parts:
  cos 2θ = cos²θ - sin²θ = 2cos²θ - 1 = 1 - 2sin²θ
  sin 2θ = 2 sinθ cosθ
```

**Triple Angle Identities (n = 3):**

```
(cosθ + i sinθ)³ = cos 3θ + i sin 3θ

Expand LHS:
  cos³θ + 3i cos²θ sinθ + 3i² cosθ sin²θ + i³ sin³θ
  = cos³θ + 3i cos²θ sinθ - 3 cosθ sin²θ - i sin³θ
  = (cos³θ - 3 cosθ sin²θ) + i(3 cos²θ sinθ - sin³θ)

Equate real and imaginary parts:
  cos 3θ = cos³θ - 3 cosθ sin²θ
         = cos³θ - 3 cosθ(1 - cos²θ)
         = 4 cos³θ - 3 cosθ

  sin 3θ = 3 cos²θ sinθ - sin³θ
         = 3(1 - sin²θ) sinθ - sin³θ
         = 3 sinθ - 4 sin³θ
```

**General Power Reduction (Binomial Expansion):**

```
(cosθ + i sinθ)ⁿ = Σ(k=0 to n) C(n,k) · cos^(n-k)(θ) · (i sinθ)ᵏ

where C(n,k) = n! / (k!(n-k)!)

Separate real (even k) and imaginary (odd k) parts:

  cos nθ = Σ(k even) (-1)^(k/2) · C(n,k) · cos^(n-k)(θ) · sinᵏ(θ)
  sin nθ = Σ(k odd)  (-1)^((k-1)/2) · C(n,k) · cos^(n-k)(θ) · sinᵏ(θ)
```

---

### 2.4 Roots of Complex Numbers

**nth Roots Formula:**

```
For z = r(cosθ + i sinθ) ≠ 0, the n distinct nth roots are:

  zₖ = r^(1/n) [ cos((θ + 2kπ)/n) + i sin((θ + 2kπ)/n) ]
       for k = 0, 1, 2, ..., n-1

Equivalently:
  zₖ = r^(1/n) · e^(i(θ + 2kπ)/n)
```

**Complete Derivation:**

```
We seek all w such that wⁿ = z = r(cosθ + i sinθ).

Write w = R(cosφ + i sinφ) in polar form, where R > 0.

Then: wⁿ = Rⁿ(cos(nφ) + i sin(nφ))

Setting wⁿ = z:
  Rⁿ = r        →  R = r^(1/n)    (positive real n-th root)
  nφ = θ + 2kπ  →  φ = (θ + 2kπ)/n

For k = 0, 1, ..., n-1, we get distinct values of φ.
For k = n, we get φ = (θ + 2nπ)/n = θ/n + 2π, which gives the same
  complex number as k = 0.

Therefore the n distinct roots are:
  zₖ = r^(1/n) [ cos((θ + 2kπ)/n) + i sin((θ + 2kπ)/n) ]
  for k = 0, 1, ..., n-1.  ∎
```

**Properties of nth Roots:**

```
(1) All n roots have the same modulus: |zₖ| = r^(1/n)
(2) The roots are equally spaced on a circle of radius r^(1/n)
(3) Angular spacing between consecutive roots: 2π/n
(4) The roots form vertices of a regular n-gon
(5) Sum of all nth roots of z is zero (for n ≥ 2):
      Σ(k=0 to n-1) zₖ = 0
(6) Product of all nth roots: z₀ · z₁ · ... · z_{n-1} = (-1)^(n-1) · z
```

**Special Case: Cube Roots of Unity**

```
Solve w³ = 1, i.e., z = 1 = 1(cos 0 + i sin 0), r = 1, θ = 0, n = 3

  zₖ = 1^(1/3) [cos(2kπ/3) + i sin(2kπ/3)]  for k = 0, 1, 2

  k = 0:  z₀ = cos 0 + i sin 0 = 1
  k = 1:  z₁ = cos(2π/3) + i sin(2π/3) = -1/2 + i√3/2  (denoted ω)
  k = 2:  z₂ = cos(4π/3) + i sin(4π/3) = -1/2 - i√3/2  (denoted ω²)

Properties:
  1 + ω + ω² = 0
  ω³ = 1
  ω̄ = ω²
  1 · ω · ω² = 1
  ω² = ω̄ = conj(ω)
```

**Special Case: Fourth Roots of Unity**

```
Solve w⁴ = 1, z = 1, r = 1, θ = 0, n = 4

  zₖ = e^(ikπ/2)  for k = 0, 1, 2, 3

  k = 0:  z₀ = 1
  k = 1:  z₁ = i
  k = 2:  z₂ = -1
  k = 3:  z₃ = -i

These are: 1, i, -1, -i (equally spaced by π/2 on unit circle)
```

---

### 2.5 Hyperbolic Functions

**Definitions:**

```
sinh x = (eˣ - e⁻ˣ) / 2       (hyperbolic sine)
cosh x = (eˣ + e⁻ˣ) / 2       (hyperbolic cosine)
tanh x = sinh x / cosh x       (hyperbolic tangent)
sech x = 1 / cosh x            (hyperbolic secant)
csch x = 1 / sinh x            (hyperbolic cosecant)
coth x = cosh x / sinh x       (hyperbolic cotangent)
```

**Fundamental Identities:**

```
(1) cosh²x - sinh²x = 1        (fundamental identity)
    (Compare: cos²x + sin²x = 1)

(2) 1 - tanh²x = sech²x

(3) coth²x - 1 = csch²x

(4) sinh(-x) = -sinh x          (odd function)
(5) cosh(-x) = cosh x           (even function)
(6) tanh(-x) = -tanh x          (odd function)

(7) sinh(x + y) = sinh x cosh y + cosh x sinh y
(8) cosh(x + y) = cosh x cosh y + sinh x sinh y
(9) sinh(2x) = 2 sinh x cosh x
(10) cosh(2x) = cosh²x + sinh²x = 2cosh²x - 1 = 1 + 2sinh²x
```

**Relationship to Circular Trigonometric Functions:**

```
(1) cosh(ix) = cos x
(2) sinh(ix) = i sin x
(3) cos(ix) = cosh x
(4) sin(ix) = i sinh x

Proof of (1):
  cosh(ix) = (e^(ix) + e^(-ix)) / 2
           = (cos x + i sin x + cos x - i sin x) / 2
           = (2 cos x) / 2
           = cos x   ∎

Proof of (2):
  sinh(ix) = (e^(ix) - e^(-ix)) / 2
           = (cos x + i sin x - cos x + i sin x) / 2
           = (2i sin x) / 2
           = i sin x   ∎
```

**Derivatives:**

```
d/dx sinh x = cosh x
d/dx cosh x = sinh x
d/dx tanh x = sech²x
d/dx coth x = -csch²x
d/dx sech x = -sech x tanh x
d/dx csch x = -csch x coth x
```

**Integrals:**

```
∫ sinh x dx = cosh x + C
∫ cosh x dx = sinh x + C
∫ sech²x dx = tanh x + C
∫ csch²x dx = -coth x + C
∫ sech x tanh x dx = -sech x + C
∫ csch x coth x dx = -csch x + C
```

**Inverse Hyperbolic Functions (Logarithmic Forms):**

```
sinh⁻¹ x = ln(x + √(x² + 1)),   x ∈ ℝ

cosh⁻¹ x = ln(x + √(x² - 1)),   x ≥ 1

tanh⁻¹ x = (1/2) ln((1+x)/(1-x)),  |x| < 1

coth⁻¹ x = (1/2) ln((x+1)/(x-1)),  |x| > 1

sech⁻¹ x = ln((1 + √(1-x²))/x),   0 < x ≤ 1

csch⁻¹ x = ln((1 + √(1+x²))/x),   x ≠ 0
```

**Derivation of sinh⁻¹:**

```
Let y = sinh⁻¹ x, so x = sinh y = (eʸ - e⁻ʸ)/2

  2x = eʸ - e⁻ʸ
  Multiply by eʸ:
  2x eʸ = e²ʸ - 1
  e²ʸ - 2x eʸ - 1 = 0

  Let u = eʸ > 0:
  u² - 2xu - 1 = 0
  u = [2x ± √(4x² + 4)] / 2 = x ± √(x² + 1)

  Since u = eʸ > 0, we need u > 0:
    x - √(x² + 1) < 0 always (reject)
    x + √(x² + 1) > 0 always (accept)

  eʸ = x + √(x² + 1)
  y = ln(x + √(x² + 1))   ∎
```

---

### 2.6 Logarithm of Complex Numbers

**Definition:**

```
For z = re^(iθ) ≠ 0:

  Log(z) = ln|z| + i arg(z)
         = ln r + i(θ + 2kπ)     for k ∈ ℤ

This is a MULTI-VALUED function (infinite values differing by 2kπi).
```

**Principal Value:**

```
Ln(z) = ln|z| + i Arg(z)

where Arg(z) is the principal argument: Arg(z) ∈ (-π, π]

Ln(z) is the SINGLE-VALUED branch (k = 0).
```

**Properties (with Caveats):**

```
For z₁ = r₁e^(iθ₁) and z₂ = r₂e^(iθ₂):

(1) Log(z₁z₂) = ln(r₁r₂) + i(arg(z₁) + arg(z₂) + 2mπ)
    Note: This differs from Log(z₁) + Log(z₂) by 2mπi
    In general: Log(z₁z₂) ≠ Log(z₁) + Log(z₂)

(2) Log(z₁/z₂) = ln(r₁/r₂) + i(arg(z₁) - arg(z₂) + 2mπ)
    Same caveat applies.

(3) Log(zⁿ) = n ln r + i(nθ + 2mπ)     (for positive integer n)

(4) e^(Log(z)) = z     (always true)
(5) Log(eᶻ) = z + 2kπi     (not equal to z in general)

(6) Log(z̄) = ln|z| - i arg(z) = ln r - i(θ + 2kπ)

(7) Log(iz) = Log(z) + iπ/2 + 2kπi
```

**Worked Example — All Values of Log(1+i):**

```
z = 1 + i

Step 1: Find modulus
  r = |z| = √(1² + 1²) = √2
  ln r = ln(√2) = (1/2) ln 2

Step 2: Find argument
  θ = arctan(1/1) = π/4    (first quadrant)
  Arg(z) = π/4

Step 3: General argument
  arg(z) = π/4 + 2kπ,  k ∈ ℤ

Step 4: Log values
  Log(1+i) = ln(√2) + i(π/4 + 2kπ)
           = (1/2) ln 2 + i(π/4 + 2kπ)

For k = 0:  Ln(1+i) = (1/2) ln 2 + iπ/4        (principal value)
For k = 1:  Log(1+i) = (1/2) ln 2 + i(π/4 + 2π)
For k = -1: Log(1+i) = (1/2) ln 2 + i(π/4 - 2π)

All values differ by multiples of 2πi.
```

**Why Log(z₁z₂) ≠ Log(z₁) + Log(z₂):**

```
Counterexample:
  z₁ = -1,  z₂ = -1

  Log(z₁) = ln 1 + iπ = iπ           (principal)
  Log(z₂) = ln 1 + iπ = iπ           (principal)
  Log(z₁) + Log(z₂) = 2iπ

  z₁z₂ = (-1)(-1) = 1
  Log(z₁z₂) = ln 1 + i(0) = 0         (principal)

  But 0 ≠ 2iπ.

The identity holds modulo 2πi:
  Log(z₁z₂) = Log(z₁) + Log(z₂) - 2πi·m   (for some integer m)
```

---

### 2.7 Separation into Real and Imaginary Parts

**Complete Reference of Key Formulas:**

```
Let z = a + ib where a, b ∈ ℝ.

─────────────────────────────────────────────────────────

(1) EXPONENTIAL: e^(a+ib)

    e^(a+ib) = eᵃ · e^(ib)
             = eᵃ (cos b + i sin b)

    Re[e^(a+ib)] = eᵃ cos b
    Im[e^(a+ib)] = eᵃ sin b

─────────────────────────────────────────────────────────

(2) COMPLEX SINE: sin(a+ib)

    sin(a+ib) = sin a cosh b + i cos a sinh b

    Re[sin(a+ib)] = sin a cosh b
    Im[sin(a+ib)] = cos a sinh b

    Derivation:
      sin(a+ib) = [e^(i(a+ib)) - e^(-i(a+ib))] / (2i)
                = [e^(-b+ia) - e^(b-ia)] / (2i)
                = [e^(-b)(cos a + i sin a) - e^(b)(cos a - i sin a)] / (2i)
                = [(e^(-b) - e^(b)) cos a + i(e^(-b) + e^(b)) sin a] / (2i)
                = [(e^(-b) + e^(b)) sin a / 2] + i[(e^(b) - e^(-b)) cos a / 2] · (i/i)
      ...

    Simpler derivation using sinh and cosh:
      sin(a+ib) = sin a · cosh b + i · cos a · sinh b   ∎

─────────────────────────────────────────────────────────

(3) COMPLEX COSINE: cos(a+ib)

    cos(a+ib) = cos a cosh b - i sin a sinh b

    Re[cos(a+ib)] = cos a cosh b
    Im[cos(a+ib)] = -sin a sinh b

─────────────────────────────────────────────────────────

(4) COMPLEX TANGENT: tan(a+ib)

    tan(a+ib) = sin(2a) / (cos(2a) + cosh(2b))
                + i · sinh(2b) / (cos(2a) + cosh(2b))

    Re[tan(a+ib)] = sin(2a) / (cos(2a) + cosh(2b))
    Im[tan(a+ib)] = sinh(2b) / (cos(2a) + cosh(2b))

─────────────────────────────────────────────────────────

(5) RECIPROCAL: 1/(a+ib)

    1/(a+ib) = (a-ib) / (a²+b²)

    Re[1/(a+ib)] = a / (a²+b²)
    Im[1/(a+ib)] = -b / (a²+b²)

─────────────────────────────────────────────────────────

(6) COMPLEX LOGARITHM: Log(a+ib)

    Log(a+ib) = (1/2) ln(a²+b²) + i·arctan(b/a)   (principal)
    General: ln|z| + i(arg(z) + 2kπ)

    Re[Log(a+ib)] = (1/2) ln(a²+b²) = ln|z|
    Im[Log(a+ib)] = Arg(a+ib) + 2kπ

─────────────────────────────────────────────────────────

(7) COMPLEX POWER: (a+ib)ⁿ

    Write a+ib = re^(iθ) where r = √(a²+b²), θ = arctan(b/a)
    (a+ib)ⁿ = rⁿ (cos nθ + i sin nθ)

    Re[(a+ib)ⁿ] = rⁿ cos(nθ)
    Im[(a+ib)ⁿ] = rⁿ sin(nθ)

─────────────────────────────────────────────────────────

(8) COMPLEX SINH: sinh(a+ib)

    sinh(a+ib) = sinh a cos b + i cosh a sin b

    Re[sinh(a+ib)] = sinh a cos b
    Im[sinh(a+ib)] = cosh a sin b

─────────────────────────────────────────────────────────

(9) COMPLEX COSH: cosh(a+ib)

    cosh(a+ib) = cosh a cos b + i sinh a sin b

    Re[cosh(a+ib)] = cosh a cos b
    Im[cosh(a+ib)] = sinh a sin b

─────────────────────────────────────────────────────────

(10) MODULUS AND ARGUMENT:

     |z| = √(a²+b²)
     Arg(z) = arctan(b/a)   (adjust quadrant)

     Re(z) = a = r cos θ
     Im(z) = b = r sin θ
```

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

### Problem 1: Express (1+i)⁸ in rectangular form using De Moivre's theorem

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Express (1+i)⁸ in rectangular form using De Moivre's theorem.

SOLUTION:

Step 1: Convert z = 1 + i to polar form.
  r = |1+i| = √(1² + 1²) = √2
  θ = Arg(1+i) = arctan(1/1) = π/4

  So: 1 + i = √2 (cos(π/4) + i sin(π/4)) = √2 · e^(iπ/4)

Step 2: Apply De Moivre's Theorem.
  (1+i)⁸ = [√2 (cos(π/4) + i sin(π/4))]⁸
          = (√2)⁸ · (cos(8·π/4) + i sin(8·π/4))
          = (2^(1/2))⁸ · (cos(2π) + i sin(2π))
          = 2⁴ · (1 + 0)
          = 16

Step 3: Verify using direct computation.
  (1+i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i
  (1+i)⁴ = ((1+i)²)² = (2i)² = 4i² = -4
  (1+i)⁸ = ((1+i)⁴)² = (-4)² = 16  ✓

FINAL ANSWER:  (1+i)⁸ = 16

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Problem 2: Find all cube roots of -8

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Find all cube roots of -8. Express each root in a+ib form.

SOLUTION:

Step 1: Express z = -8 in polar form.
  r = |-8| = 8
  θ = Arg(-8) = π    (since -8 is on the negative real axis)

  -8 = 8(cos π + i sin π) = 8e^(iπ)

Step 2: Apply the nth roots formula.
  n = 3 (cube roots), r = 8, θ = π

  zₖ = 8^(1/3) [cos((π + 2kπ)/3) + i sin((π + 2kπ)/3)]
      for k = 0, 1, 2

  8^(1/3) = 2

Step 3: Compute each root.

  k = 0:
    θ₀ = π/3
    z₀ = 2(cos(π/3) + i sin(π/3))
       = 2(1/2 + i√3/2)
       = 1 + i√3

  k = 1:
    θ₁ = (π + 2π)/3 = 3π/3 = π
    z₁ = 2(cos π + i sin π)
       = 2(-1 + 0i)
       = -2

  k = 2:
    θ₂ = (π + 4π)/3 = 5π/3
    z₂ = 2(cos(5π/3) + i sin(5π/3))
       = 2(1/2 - i√3/2)
       = 1 - i√3

Step 4: Verify.
  (1+i√3)³ = 1 + 3i√3 + 3(i√3)² + (i√3)³
            = 1 + 3i√3 - 9 - 3i√3
            = -8  ✓

  (-2)³ = -8  ✓

  (1-i√3)³ = 1 - 3i√3 - 9 + 3i√3
            = -8  ✓

FINAL ANSWER:
  The three cube roots of -8 are:
    z₀ = 1 + i√3
    z₁ = -2
    z₂ = 1 - i√3

  These form an equilateral triangle inscribed in the circle |z| = 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Problem 3: Prove cos 3θ = 4cos³θ - 3cosθ using De Moivre's theorem

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Prove that cos 3θ = 4cos³θ - 3cosθ using De Moivre's theorem.

PROOF:

Step 1: Apply De Moivre's Theorem with n = 3.
  (cosθ + i sinθ)³ = cos 3θ + i sin 3θ

Step 2: Expand the left side using the Binomial Theorem.
  (cosθ + i sinθ)³ = C(3,0)cos³θ · (i sinθ)⁰
                    + C(3,1)cos²θ · (i sinθ)¹
                    + C(3,2)cos¹θ · (i sinθ)²
                    + C(3,3)cos⁰θ · (i sinθ)³

  = 1 · cos³θ · 1
  + 3 · cos²θ · (i sinθ)
  + 3 · cosθ · (i sinθ)²
  + 1 · 1 · (i sinθ)³

Step 3: Simplify using i² = -1 and i³ = -i.
  = cos³θ
  + 3i cos²θ sinθ
  + 3 cosθ · (-1) sin²θ     [since i² = -1]
  + (-i) sin³θ               [since i³ = -i]

  = cos³θ + 3i cos²θ sinθ - 3 cosθ sin²θ - i sin³θ

Step 4: Group real and imaginary parts.
  = (cos³θ - 3 cosθ sin²θ) + i(3 cos²θ sinθ - sin³θ)

Step 5: Equate with cos 3θ + i sin 3θ (from Step 1).
  Real part:    cos 3θ = cos³θ - 3 cosθ sin²θ
  Imaginary:    sin 3θ = 3 cos²θ sinθ - sin³θ

Step 6: Convert to cos-only form using sin²θ = 1 - cos²θ.
  cos 3θ = cos³θ - 3 cosθ sin²θ
          = cos³θ - 3 cosθ (1 - cos²θ)
          = cos³θ - 3 cosθ + 3 cos³θ
          = 4 cos³θ - 3 cosθ

Therefore: cos 3θ = 4cos³θ - 3cosθ  ∎

BONUS — sin 3θ formula:
  sin 3θ = 3 cos²θ sinθ - sin³θ
          = 3(1 - sin²θ) sinθ - sin³θ
          = 3 sinθ - 3 sin³θ - sin³θ
          = 3 sinθ - 4 sin³θ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Problem 4: Separate into real and imaginary parts: sin(2+3i)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Express sin(2 + 3i) in the form u + iv where u, v ∈ ℝ.

SOLUTION:

Step 1: Use the formula for sin(a + ib).
  sin(a + ib) = sin a cosh b + i cos a sinh b

  Here a = 2, b = 3.

Step 2: Compute each component.

  sin 2 ≈ 0.9093
  cos 2 ≈ -0.4161
  cosh 3 = (e³ + e⁻³)/2 ≈ (20.0855 + 0.0498)/2 ≈ 10.0677
  sinh 3 = (e³ - e⁻³)/2 ≈ (20.0855 - 0.0498)/2 ≈ 10.0179

Step 3: Compute the real and imaginary parts.

  Re = sin 2 · cosh 3 ≈ (0.9093)(10.0677) ≈ 9.1546
  Im = cos 2 · sinh 3 ≈ (-0.4161)(10.0179) ≈ -4.1685

Step 4: Write in rectangular form.
  sin(2 + 3i) ≈ 9.1546 - 4.1685i

Step 5: Exact symbolic form.
  sin(2+3i) = sin(2) · [(e³ + e⁻³)/2] + i · cos(2) · [(e³ - e⁻³)/2]

FINAL ANSWER (exact):
  sin(2+3i) = (sin 2)(cosh 3) + i(cos 2)(sinh 3)

FINAL ANSWER (decimal):
  sin(2+3i) ≈ 9.1546 - 4.1685i

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Problem 5: Find all values of Log(1+i) and show they differ by 2nπi

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: Find all values of Log(1+i) and show they differ by 2nπi.

SOLUTION:

Step 1: Express z = 1 + i in polar form.
  r = |1+i| = √(1² + 1²) = √2
  θ = Arg(1+i) = arctan(1/1) = π/4   (first quadrant, since Re > 0, Im > 0)

  z = √2 · e^(iπ/4) = √2(cos(π/4) + i sin(π/4))

Step 2: Apply the complex logarithm formula.
  Log(z) = ln|z| + i arg(z)
  arg(z) = π/4 + 2kπ,  k ∈ ℤ

  Log(1+i) = ln(√2) + i(π/4 + 2kπ)
           = (1/2) ln 2 + i(π/4 + 2kπ)

Step 3: List specific values for various k.

  k = 0:  Log(1+i) = (1/2) ln 2 + iπ/4
                     ≈ 0.3466 + 0.7854i

  k = 1:  Log(1+i) = (1/2) ln 2 + i(π/4 + 2π)
                     = (1/2) ln 2 + i(9π/4)
                     ≈ 0.3466 + 7.0686i

  k = -1: Log(1+i) = (1/2) ln 2 + i(π/4 - 2π)
                     = (1/2) ln 2 + i(-7π/4)
                     ≈ 0.3466 - 5.4978i

  k = 2:  Log(1+i) = (1/2) ln 2 + i(π/4 + 4π)
                     ≈ 0.3466 + 13.3518i

Step 4: Show all values differ by 2nπi.
  Let Lₖ = (1/2) ln 2 + i(π/4 + 2kπ)   (k-th value)

  Lₖ - Lₘ = i(π/4 + 2kπ) - i(π/4 + 2mπ)
           = i · 2(k-m)π
           = 2nπi   where n = k - m ∈ ℤ

  Specifically:
    L₁ - L₀ = 2πi
    L₂ - L₁ = 2πi
    L₀ - L₋₁ = 2πi

  All values differ by integer multiples of 2πi.  ∎

Step 5: Verify with a specific case.
  Check: e^(Ln(1+i)) = 1+i
  e^((1/2)ln2 + iπ/4) = e^((1/2)ln2) · e^(iπ/4)
                       = √2 · (cos(π/4) + i sin(π/4))
                       = √2 · (√2/2 + i√2/2)
                       = 1 + i   ✓

FINAL ANSWER:
  Log(1+i) = (1/2) ln 2 + i(π/4 + 2kπ)  for all k ∈ ℤ

  Principal value (k=0): Ln(1+i) = (1/2) ln 2 + iπ/4 ≈ 0.3466 + 0.7854i

  All values differ by multiples of 2πi.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 4. ENGINEERING APPLICATIONS MAP

| Topic | Engineering Application | Description | Key Formula/Concept |
|-------|------------------------|-------------|---------------------|
| Complex numbers | **AC Circuit Analysis** | Impedance Z = R + iX where R = resistance, X = reactance. Phasors represent sinusoidal voltages/currents. | V = IZ, Z = R + iX |
| Complex numbers | **Signal Processing** | Represent signals as complex exponentials. Fourier transform decomposes signals into frequency components. | X(f) = ∫x(t)e^(-i2πft) dt |
| De Moivre's theorem | **Fourier Analysis** | Powers of complex exponentials generate Fourier basis functions. Computing nth harmonics. | e^(inθ) = (e^(iθ))ⁿ |
| De Moivre's theorem | **Signal Processing** | Computing powers of phasors for harmonic analysis and power calculations. | Vⁿ = \|V\|ⁿe^(inθ) |
| nth roots | **Discrete Fourier Transform (DFT)** | Twiddle factors W_N = e^(-i2π/N) are nth roots of unity used in FFT algorithms. | X[k] = Σ x[n]W_N^(kn) |
| nth roots | **Signal Sampling** | Sampling frequency relationships; finding N-point DFT frequencies. | fₖ = k·fₛ/N |
| Hyperbolic functions | **Transmission Line Theory** | Voltage and current along transmission lines: V(x) = V⁺e^(-γx) + V⁻e^(γx) where γ = α + iβ. | V(x) = V₀ cosh(γx) - I₀Z₀ sinh(γx) |
| Hyperbolic functions | **Catenary Curves** | Shape of hanging cables: y = a cosh(x/a). Used in power line and suspension bridge design. | y = a cosh(x/a) |
| Hyperbolic functions | **Heat Transfer** | Temperature distribution in finned surfaces involves hyperbolic functions. | T(x) = T_b cosh(mx)/cosh(mL) |
| Logarithm of complex numbers | **Control Systems (Bode Plots)** | Magnitude and phase of transfer functions: 20 log\|G(iω)\| and arg(G(iω)). | \|G(iω)\| = √(Re² + Im²) |
| Logarithm of complex numbers | **Nyquist Plots** | Plotting G(iω) in complex plane; encirclements determine stability (Nyquist criterion). | G(iω) = \|G\|e^(iφ) |
| Logarithm of complex numbers | **Filter Design** | Z-transform uses complex logarithm for frequency mapping. | z = e^(iωT) |
| Polar form multiplication | **Robotics** | 2D rotations composed by multiplying complex numbers: rotate and scale simultaneously. | z₁z₂: multiply magnitudes, add angles |
| Polar form multiplication | **Computer Graphics** | Rotation of 2D objects: multiply by e^(iθ) to rotate by θ. | z' = z·e^(iθ) |
| Polar form multiplication | **Phasor Analysis** | Multiplying phasors: magnitudes multiply, phases add. | V₁·V₂ = \|V₁\|\|V₂\|e^(i(θ₁+θ₂)) |
| Roots of unity | **Polyphase Commutation** | Symmetrical multi-phase systems (3-phase, 6-phase) described by roots of unity. | 3-phase: 1, e^(i2π/3), e^(i4π/3) |
| Roots of unity | **Cryptography** | Number-theoretic transforms (NTT) use roots of unity for efficient polynomial multiplication. | NTT based on ωₙ = e^(-i2π/N) |
| Roots of unity | **Vibration Analysis** | Natural frequencies and mode shapes of circular membranes involve roots of unity. | Jₙ(ωₙr) = 0 |

**Detailed Application Notes:**

```
╔══════════════════════════════════════════════════════════════════════╗
║                   AC CIRCUIT ANALYSIS EXAMPLE                       ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Series RLC Circuit:                                                 ║
║    Impedance: Z = R + i(ωL - 1/(ωC))                                ║
║    where:                                                            ║
║      R = resistance (Ω)                                              ║
║      L = inductance (H)                                              ║
║      C = capacitance (F)                                             ║
║      ω = angular frequency (rad/s)                                   ║
║                                                                      ║
║  |Z| = √(R² + (ωL - 1/(ωC))²)    (magnitude of impedance)         ║
║  φ = arctan((ωL - 1/(ωC))/R)      (phase angle)                    ║
║                                                                      ║
║  V = IZ   (Ohm's law for AC circuits)                                ║
║                                                                      ║
║  At resonance: ωL = 1/(ωC) → Z = R (purely resistive)              ║
╚══════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════╗
║                 TRANSMISSION LINE THEORY EXAMPLE                    ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Lossless line:                                                      ║
║    V(x,t) = V⁺ cos(ωt - βx) + V⁻ cos(ωt + βx)                     ║
║                                                                      ║
║  In phasor form:                                                     ║
║    V(x) = V⁺e^(-iβx) + V⁻e^(iβx)                                  ║
║                                                                      ║
║  Lossy line (γ = α + iβ):                                           ║
║    V(x) = V⁺e^(-γx) + V⁻e^(γx)                                   ║
║         = V⁺e^(-αx)e^(-iβx) + V⁻e^(αx)e^(iβx)                   ║
║                                                                      ║
║  Using hyperbolic functions for finite-length line:                  ║
║    V(x) = V_L cosh(γ(L-x)) + I_L Z₀ sinh(γ(L-x))                  ║
║                                                                      ║
║  where Z₀ = √(L/C) is the characteristic impedance                  ║
║        L = inductance per unit length                                ║
║        C = capacitance per unit length                               ║
╚══════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════╗
║              DISCRETE FOURIER TRANSFORM EXAMPLE                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  N-point DFT:                                                        ║
║    X[k] = Σ(n=0 to N-1) x[n] · W_N^(kn)                           ║
║                                                                      ║
║  where W_N = e^(-i2π/N) is the principal N-th root of unity         ║
║                                                                      ║
║  W_N^N = e^(-i2π) = 1  (root of unity property)                    ║
║                                                                      ║
║  FFT algorithm exploits:                                              ║
║    W_N^(k+N/2) = -W_N^k     (symmetry property)                    ║
║    W_N^(2k) = W_{N/2}^k     (periodicity property)                 ║
║                                                                      ║
║  Reduces O(N²) DFT to O(N log N) FFT                               ║
╚══════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════╗
║                CONTROL SYSTEMS (BODE PLOT) EXAMPLE                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Transfer function: G(s) = (s + a) / (s² + bs + c)                 ║
║                                                                      ║
║  Frequency response: G(iω)                                          ║
║                                                                      ║
║  Magnitude (dB):                                                     ║
║    20 log₁₀|G(iω)| = 20 log₁₀√(Re² + Im²)                        ║
║                     = 10 log₁₀(Re² + Im²)                          ║
║                                                                      ║
║  Phase:                                                              ║
║    φ(ω) = arg(G(iω)) = arctan(Im/Re)                               ║
║                                                                      ║
║  The complex logarithm of G(iω) = |G|e^(iφ) gives:                 ║
║    ln G(iω) = ln|G| + iφ                                            ║
║                                                                      ║
║  This separates magnitude (real part) from phase (imaginary part)    ║
║  enabling independent design of gain and phase margins.              ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 5. QUICK REFERENCE CHEAT SHEET

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    MODULE 5 — QUICK REFERENCE                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  EULER'S FORMULA:         e^(iθ) = cosθ + i sinθ                       ║
║  EULER'S IDENTITY:        e^(iπ) + 1 = 0                               ║
║  COS FROM EULER:          cosθ = (e^(iθ) + e^(-iθ)) / 2               ║
║  SIN FROM EULER:          sinθ = (e^(iθ) - e^(-iθ)) / (2i)            ║
║                                                                          ║
║  DE MOIVRE:               (cosθ + i sinθ)ⁿ = cos(nθ) + i sin(nθ)      ║
║  nTH ROOTS:               zₖ = r^(1/n)[cos((θ+2kπ)/n) + i sin((θ+2kπ)/n)] ║
║  ROOTS OF UNITY:          ωₖ = e^(i2kπ/n), k = 0, 1, ..., n-1         ║
║  CUBE ROOTS OF UNITY:     1, ω = e^(i2π/3), ω² = e^(i4π/3)           ║
║                                                                          ║
║  HYPERBOLIC SINH:         sinh x = (eˣ - e⁻ˣ)/2                       ║
║  HYPERBOLIC COSH:         cosh x = (eˣ + e⁻ˣ)/2                       ║
║  FUND. HYPERBOLIC ID:     cosh²x - sinh²x = 1                          ║
║                                                                          ║
║  COMPLEX LOG:             Log(z) = ln|z| + i arg(z)                    ║
║  PRINCIPAL LOG:           Ln(z) = ln|z| + i Arg(z)                     ║
║                                                                          ║
║  COMPLEX SINH:            sinh(a+ib) = sinh a cos b + i cosh a sin b    ║
║  COMPLEX COSH:            cosh(a+ib) = cosh a cos b + i sinh a sin b    ║
║                                                                          ║
║  MODULUS:                 |z| = √(a²+b²)                               ║
║  ARGUMENT:                Arg(z) = arctan(b/a)  [quadrant dependent]    ║
║  CONJUGATE:               z̄ = a - ib, z·z̄ = |z|²                      ║
║                                                                          ║
║  CONVERSIONS:                                                          ║
║    a+ib → re^(iθ)  :  r = √(a²+b²), θ = arctan(b/a)                 ║
║    re^(iθ) → a+ib  :  a = r cosθ, b = r sinθ                         ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 6. COMMON MISTAKES & PITFALLS

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    COMMON MISTAKES TO AVOID                             ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  MISTAKE 1: Forgetting quadrant when computing arg(z)                    ║
║  ──────────────────────────────────────────────────────────────────      ║
║  WRONG:  arg(-1+i) = arctan(1/(-1)) = arctan(-1) = -π/4              ║
║  RIGHT:  arg(-1+i) = π + arctan(1/(-1)) = π - π/4 = 3π/4            ║
║          (point is in Q2, so add π)                                     ║
║                                                                          ║
║  MISTAKE 2: Confusing i² = -1 with i² = 1                              ║
║  ──────────────────────────────────────────────────────────────────      ║
║  WRONG:  (2+i)(3+i) = 6 + 5i + i² = 6 + 5i + 1 = 7 + 5i             ║
║  RIGHT:  (2+i)(3+i) = 6 + 5i + i² = 6 + 5i - 1 = 5 + 5i            ║
║                                                                          ║
║  MISTAKE 3: Taking root of only one term                                ║
║  ──────────────────────────────────────────────────────────────────      ║
║  WRONG:  (8i)^(1/3) = 2i                                              ║
║  RIGHT:  (8i)^(1/3) has 3 roots: 1+i√3, -2, 1-i√3                    ║
║          (need to find ALL n roots, not just one)                       ║
║                                                                          ║
║  MISTAKE 4: Log(z₁z₂) = Log(z₁) + Log(z₂) (ALWAYS)                  ║
║  ──────────────────────────────────────────────────────────────────      ║
║  WRONG:  Log((-1)(-1)) = Log(-1) + Log(-1) = 2iπ                      ║
║  RIGHT:  Log((-1)(-1)) = Log(1) = 0                                    ║
║          (identity holds only modulo 2πi)                               ║
║                                                                          ║
║  MISTAKE 5: De Moivre's Theorem applied before converting to polar     ║
║  ──────────────────────────────────────────────────────────────────      ║
║  WRONG:  (1+i)⁸: try to apply directly without converting first        ║
║  RIGHT:  (1+i)⁸: first write 1+i = √2·e^(iπ/4), then apply           ║
║                                                                          ║
║  MISTAKE 6: Forgetting ± in sqrt when separating parts                  ║
║  ──────────────────────────────────────────────────────────────────      ║
║  For inverse functions, remember that the range may exclude values.     ║
║  cosh⁻¹x is only defined for x ≥ 1, and is multi-valued.              ║
║                                                                          ║
║  MISTAKE 7: Mixing hyperbolic and circular function identities           ║
║  ──────────────────────────────────────────────────────────────────      ║
║  WRONG:  cosh²x + sinh²x = 1    (this is WRONG)                       ║
║  RIGHT:  cosh²x - sinh²x = 1    (note the MINUS sign)                  ║
║  RIGHT:  cos²x + sin²x = 1      (note the PLUS sign)                  ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 7. PRACTICE PROBLEMS

**Problem P1:** Express (1 - i√3)⁶ in rectangular form.

**Problem P2:** Find all fourth roots of -16.

**Problem P3:** Prove that sin 5θ = 16sin⁵θ - 20sin³θ + 5sinθ.

**Problem P4:** Separate cos(3 + 2i) into real and imaginary parts.

**Problem P5:** Find all values of Log(-1).

**Problem P6:** Show that |z₁z₂| = |z₁||z₂| for all complex z₁, z₂.

**Problem P7:** Express sinh(2 - iπ/4) in the form u + iv.

**Problem P8:** Find the principal value of i^(i).

**Problem P9:** Verify that the three cube roots of 27 form an equilateral triangle.

**Problem P10:** Derive the formula for cos 4θ using De Moivre's theorem.

**Problem P11:** Find all values of Log(i^i).

**Problem P12:** Show that the product of all n-th roots of unity equals (-1)^(n-1).

---

## 8. ANSWERS TO PRACTICE PROBLEMS

```
P1:  (1-i√3)⁶ = -64
P2:  Fourth roots of -16: √2(1+i), √2(-1+i), √2(-1-i), √2(1-i)
P3:  Expand (cosθ + i sinθ)⁵ and equate imaginary parts.
P4:  cos(3+2i) = cos(3)cosh(2) - i·sin(3)sinh(2) ≈ -99.0198 - (-1.0638)i
     Wait, let me recalculate:
     cos(3)cosh(2) = (-0.98999)(3.76220) = -3.72461
     sin(3)sinh(2) = (0.14112)(3.62686) = 0.51182
     cos(3+2i) ≈ -3.72461 - 0.51182i
P5:  Log(-1) = i(π + 2kπ), k ∈ ℤ. Principal: Ln(-1) = iπ
P6:  |z₁z₂|² = z₁z₂·(z₁z₂)̄ = z₁z₂·z̄₁z̄₂ = (z₁z̄₁)(z₂z̄₂) = |z₁|²|z₂|²
P7:  sinh(2-iπ/4) = sinh(2)cos(π/4) - i·cosh(2)sin(π/4)
     = (√2/2)(sinh(2) - i·cosh(2))
P8:  i^i = e^(-π/2) ≈ 0.2079
P9:  Roots: 3, 3ω, 3ω² where ω = e^(i2π/3). Distances between any two: 3√3.
     All sides equal → equilateral triangle.
P10: cos 4θ = 8cos⁴θ - 8cos²θ + 1
P11: Log(i^i) = Log(e^(-π/2)) = -π/2 + 2kπi (real result, all k)
     Principal: -π/2 ≈ -1.5708
P12: Product = e^(i·2π(0+1+...+(n-1))/n) = e^(i·2π(n-1)n/(2n)) = e^(iπ(n-1))
     = (-1)^(n-1)
```

---

## CROSS-REFERENCES

- [[engineering-math/module-1-matrices|Module 1: Matrices]] — Complex eigenvalues arise when the characteristic polynomial of a real matrix has negative discriminant; the resulting complex eigenvectors encode oscillatory modes in systems of differential equations.
- [[engineering-math/module-4-linear-differential-equations|Module 4: Linear Differential Equations]] — Complex roots α ± iβ of the auxiliary equation yield solutions e^{αx}(C₁cos βx + C₂sin βx) via Euler's formula e^(iθ) = cos θ + i sin θ. The "multiply by x" resonance rule in PI computation parallels complex root analysis.
- [[engineering-math/module-3-homogeneous-functions|Module 3: Homogeneous Functions]] — Complex hyperbolic functions (sinh, cosh) are defined via exponentials and satisfy identities analogous to homogeneous function properties; the relationship cosh(ix) = cos(x) bridges hyperbolic and circular functions.
- [[engineering-math/module-2-partial-differentiation|Module 2: Partial Differentiation]] — The separation of complex functions into real and imaginary parts uses partial differentiation; Cauchy-Riemann equations (implied by analyticity) connect partial derivatives of real and imaginary components.

*Module 5 of 5 — [[engineering-math/module-4-linear-differential-equations|← Module 4]] | [[engineering-math/module-1-matrices|Module 1 →]]*

*End of Module 5: Complex Numbers*