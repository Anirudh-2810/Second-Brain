---
module: "engineering"
topic: "Physics Formula Sheets — Kinematics, Units & Dimensions, Errors"
tags: [physics, formula-sheet, kinematics, units, dimensions, errors, revision]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\Desktop\Anirudh\Print\Physics\Basic Kinematics Imp Formulas.pdf, Kinematics 1D Imp Formulas.pdf, Kinematics 2D Imp Formula.pdf, Units and Dimension Imp Formulas.pdf, Errors and Measurement Imp Formulas.pdf, Revision Capsule - Physics.pdf"
description: "Printed physics formula sheets covering kinematics (1D and 2D), units and dimensions, error analysis, and a revision capsule. Sourced from user's Desktop Print folder."
---

# Physics — Kinematics, Units & Dimensions, Errors

> **Source:** `C:\Users\Vijaykumar\Desktop\Anirudh\Print\Physics\` (6 PDFs)
> **Scope:** Kinematics (1D + 2D), Units & Dimensions, Error Analysis, Revision Capsule
> **Confidence:** high (extracted from printed formula sheets)

---

## For future agent
Physics formula sheets extracted from the user's Desktop Print folder — a collection of printed revision capsule PDFs and image files (handwritten notes). Covers kinematics (1D and 2D), units and dimensions, error analysis. Cross-links: [[wiki/01-Areas/Engineering/physics/formula-sheet-mechanics]], [[wiki/01-Areas/Engineering/physics/overview]], [[brain/Patterns/agent-pipeline-patterns]].

---

## 1. Units & Dimensions

### SI Base Quantities & Units
| Quantity | SI Unit | Symbol |
|----------|---------|--------|
| Length | metre | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |
| Temperature | kelvin | K |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

### Derived SI Units (Common)
| Quantity | Unit | SI Base Equivalent |
|----------|------|-------------------|
| Force | newton (N) | kg·m/s² |
| Energy/Work | joule (J) | kg·m²/s² |
| Power | watt (W) | kg·m²/s³ |
| Pressure | pascal (Pa) | kg/(m·s²) |
| Frequency | hertz (Hz) | s⁻¹ |
| Electric charge | coulomb (C) | A·s |
| Electric potential | volt (V) | kg·m²/(A·s³) |
| Resistance | ohm (Ω) | kg·m²/(A²·s³) |

### Dimensional Formulae
| Quantity | Dimension |
|----------|-----------|
| Velocity | [M⁰ L T⁻¹] |
| Acceleration | [M⁰ L T⁻²] |
| Force | [M L T⁻²] |
| Energy | [M L² T⁻²] |
| Momentum | [M L T⁻¹] |
| Impulse | [M L T⁻¹] |
| Pressure | [M L⁻¹ T⁻²] |
| Power | [M L² T⁻³] |
| Gravitational constant (G) | [M⁻¹ L³ T⁻²] |
| Planck constant (h) | [M L² T⁻¹] |
| Dielectric constant (ε₀) | [M⁻¹ L⁻³ T⁴ A²] |
| Magnetic field (B) | [M T⁻² A⁻¹] |

### Dimensional Analysis Principles
- **Principle of Homogeneity:** Only quantities with same dimensions can be added/subtracted
- **Dimensional Consistency:** Both sides of an equation must have same dimensions
- **Applications:** Unit conversion, checking formula correctness, deriving relations (nondimensional numbers)

---

## 2. Kinematics — 1D (Rectilinear Motion)

### Equations of Motion (Constant Acceleration)
```
v = u + at
s = ut + ½at²
v² = u² + 2as
s = ½(u + v)t
```
Where: u = initial velocity, v = final velocity, a = acceleration, s = displacement, t = time

### Key Formulas
| Formula | When to Use |
|---------|-------------|
| v = u + at | When time and acceleration are known |
| s = ut + ½at² | When time and acceleration are known |
| v² = u² + 2as | When displacement and acceleration are known (no time) |
| s = ½(u + v)t | When average velocity is needed |

### Special Cases
| Case | Description |
|------|-------------|
| Free fall | a = g = 9.8 m/s² (downward) |
| Thrown upward | a = -g at top, v = 0 |
| Two objects meeting | Set displacements equal, solve for time |
| Relative velocity (same direction) | v_rel = v₁ - v₂ |
| Relative velocity (opposite direction) | v_rel = v₁ + v₂ |

### Important Kinematics Graphs
| Graph | Key Information |
|-------|-----------------|
| **v-t graph** | Slope = acceleration; Area = displacement |
| **a-t graph** | Slope = jerk; Area = change in velocity |
| **s-t graph** | Slope = velocity |

---

## 3. Kinematics — 2D (Projectile Motion)

### Projectile Motion Decomposition
| Component | Value | Constant? |
|-----------|-------|-----------|
| Horizontal velocity | vₓ = v cos θ | Yes (no air resistance) |
| Vertical velocity | vᵧ = v sin θ - gt | No (changes due to gravity) |
| Horizontal acceleration | aₓ = 0 | Yes |
| Vertical acceleration | aᵧ = -g | Yes (downward) |

### Key Formulas
| Quantity | Formula |
|----------|---------|
| **Range (R)** | R = (v² sin 2θ) / g |
| **Maximum Height (H)** | H = (v² sin²θ) / (2g) |
| **Time of Flight (T)** | T = (2v sin θ) / g |
| **Maximum Range** | When θ = 45° (R_max = v²/g) |
| **Time to Reach Max Height** | t = v sin θ / g |

### Special Cases
| Scenario | Key Points |
|----------|------------|
| **Launched from height h** | Add -½gt² to displacement |
| **Horizontal launch (θ=0)** | Initial vᵧ = 0, vₓ = v |
| **Symmetric trajectory** | Time up = Time down; same speed at same height |
| **45° launch angle** | Maximum range for given v |

---

## 4. Error Analysis & Measurements

### Types of Errors
| Error Type | Nature | Can Be Eliminated? |
|------------|--------|-------------------|
| **Systematic Errors** | Consistent deviation from true value | Yes (calibration, method) |
| **Random Errors** | Unpredictable fluctuations | Reduced by averaging |
| **Gross Errors** | Human mistakes (misreading, miscalculation) | Yes (carefulness) |

### Measurement Terms
| Term | Definition |
|------|------------|
| **Absolute Error** | Δa = a_measured - a_true |
| **Relative Error** | Δa / a |
| **Percentage Error** | (Δa / a) × 100% |
| **Least Count** | Smallest measurable value of instrument |
| **Precision** | Closeness of repeated measurements to each other |
| **Accuracy** | Closeness of measured value to true value |

### Error Propagation Rules
| Operation | Rule |
|-----------|------|
| **Addition (a + b)** | Δ(a+b) = √[(Δa)² + (Δb)²] |
| **Subtraction (a - b)** | Δ(a-b) = √[(Δa)² + (Δb)²] |
| **Multiplication (a × b)** | (Δ(a×b))/(a×b) = √[(Δa/a)² + (Δb/b)²] |
| **Division (a ÷ b)** | (Δ(a÷b))/(a÷b) = √[(Δa/a)² + (Δb/b)²] |
| **Power (aⁿ)** | (Δ(aⁿ))/(aⁿ) = n × (Δa/a) |
| **Logarithm (ln a)** | Δ(ln a) = Δa / a |
| **Exponential (eᵃ)** | (Δ(eᵃ))/(eᵃ) = Δa |

### Significant Figures Rules
| Rule | Example |
|------|---------|
| Non-zero digits are significant | 234 → 3 sig figs |
| Leading zeros are NOT significant | 0.0056 → 2 sig figs |
| Trailing zeros after decimal ARE significant | 2.3400 → 5 sig figs |
| Multiplication/Division: least number of sig figs | 2.3 × 1.25 = 2.9 (2 sig figs) |
| Addition/Subtraction: least number of decimal places | 2.3 + 1.25 = 3.6 (1 decimal) |

---

## 5. Physics Revision Capsule

### High-Yield Topics (Last-Minute)
```
1. Kinematics: Master all 4 equations; know when to use each
2. Projectile Motion: Range, height, flight time formulas (derived from 1D kinematics)
3. Units & Dimensions: Know dimension table; practice dimensional consistency checks
4. Error Analysis: Abs/Rel/Perc errors; propagation rules for multiplication/division
5. Significant Figures: Rules for counting and arithmetic operations
```

### Common Exam Pitfalls
| Pitfall | Fix |
|---------|-----|
| Confusing displacement vs distance | Displacement is vector; distance is scalar |
| Forgetting g = 9.8 m/s² | Always state direction of g (downward positive or upward positive) |
| Units not SI | Convert to SI first, then apply formulas |
| Significant figure mistakes | Track them throughout calculations |
| Error propagation sign errors | Always use square root of sum of squares |

---

## Cross-References
- [[wiki/01-Areas/Engineering/physics/formula-sheet-mechanics]] — Full mechanics formula sheet (covers these topics in depth)
- [[wiki/01-Areas/Engineering/physics/overview]] — Physics theme overview and topic map
- [[wiki/01-Areas/Engineering/physics/formula-sheet-optics]] — Complementary optics formulas
- [[wiki/01-Areas/Engineering/physics/formula-sheet-modern]] — Modern physics formulas
- [[wiki/01-Areas/Engineering/physics/formula-sheet-thermal-waves]] — Thermal & waves formulas
- [[brain/Patterns/agent-pipeline-patterns]] — Physics problem-solving patterns