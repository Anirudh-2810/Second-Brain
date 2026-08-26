---
module: "engineering"
topic: "Mathematics Formula Sheets — Inverse Trigonometry & Revision"
tags: [mathematics, formula-sheet, inverse-trigonometry, revision, engineering]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\Desktop\Anirudh\Print\Maths\INVERSE TRIGONOMETRY FUNCTION SHORT NOTE.pdf, basic maths 1.pdf, Revision Capsule - Maths.pdf"
description: "Printed mathematics formula sheets covering inverse trigonometry functions, basic maths fundamentals, and a revision capsule. Sourced from user's Desktop Print folder."
---

# Mathematics — Inverse Trigonometry & Revision Capsule

> **Source:** `C:\Users\Vijaykumar\Desktop\Anirudh\Print\Maths\` (3 PDFs)
> **Scope:** Inverse trigonometry functions, basic maths fundamentals, revision capsule
> **Confidence:** high (extracted from printed formula sheets)

---

## For future agent
Mathematics formula sheets extracted from the user's Desktop Print folder — printed PDFs covering inverse trigonometry functions, basic maths fundamentals, and a revision capsule. Cross-links: [[wiki/01-Areas/Engineering/mathematics/formula-sheet-master]], [[wiki/01-Areas/Engineering/mathematics/formula-sheet-trigonometry]], [[wiki/01-Areas/Engineering/mathematics/overview]], [[brain/Patterns/agent-pipeline-patterns]].

---

## 1. Inverse Trigonometric Functions — Domains & Ranges

### Six Inverse Trig Functions
| Function | Domain | Range | Denotes |
|----------|--------|-------|---------|
| **sin⁻¹(x)** | [−1, 1] | [−π/2, π/2] | Principal value branch |
| **cos⁻¹(x)** | [−1, 1] | [0, π] | Principal value branch |
| **tan⁻¹(x)** | (−∞, ∞) | (−π/2, π/2) | Principal value branch |
| **cosec⁻¹(x)** | (−∞, −1] ∪ [1, ∞) | [−π/2, π/2] − {0} | Principal value branch |
| **sec⁻¹(x)** | (−∞, −1] ∪ [1, ∞) | [0, π] − {π/2} | Principal value branch |
| **cot⁻¹(x)** | (−∞, ∞) | (0, π) | Principal value branch |

### Key Identities
| Identity | Formula |
|----------|---------|
| sin⁻¹(x) + cos⁻¹(x) | = π/2, for x ∈ [−1, 1] |
| tan⁻¹(x) + cot⁻¹(x) | = π/2, for x ∈ ℝ |
| cosec⁻¹(x) + sec⁻¹(x) | = π/2, for x ∈ (−∞, −1] ∪ [1, ∞) |
| sin⁻¹(1/x) | = cosec⁻¹(x), for x ∈ (−∞, −1] ∪ [1, ∞) |
| cos⁻¹(1/x) | = sec⁻¹(x), for x ∈ (−∞, −1] ∪ [1, ∞) |
| tan⁻¹(1/x) | = cot⁻¹(x), for x > 0 |
| tan⁻¹(1/x) | = cot⁻¹(x) − π, for x < 0 |

---

## 2. Inverse Trigonometry — Sum/Difference Formulas

### Sum Formulas
| Formula | Valid For |
|---------|-----------|
| tan⁻¹(x) + tan⁻¹(y) | = tan⁻¹((x+y)/(1−xy)), when xy < 1 |
| tan⁻¹(x) + tan⁻¹(y) | = tan⁻¹((x+y)/(1−xy)) + π, when x,y > 0 and xy > 1 |
| tan⁻¹(x) + tan⁻¹(y) | = tan⁻¹((x+y)/(1−xy)) − π, when x,y < 0 and xy > 1 |
| 2tan⁻¹(x) | = sin⁻¹(2x/(1+x²)), when |x| ≤ 1 |
| 2tan⁻¹(x) | = cos⁻¹((1−x²)/(1+x²)), when x ≥ 0 |
| 2tan⁻¹(x) | = tan⁻¹(2x/(1−x²)), when |x| < 1 |

### Difference Formulas
| Formula | Valid For |
|---------|-----------|
| tan⁻¹(x) − tan⁻¹(y) | = tan⁻¹((x−y)/(1+xy)), for all x,y where 1+xy > 0 |

### Common Substitutions
| Expression | Substitution |
|-----------|--------------|
| √(1−x²) | Let x = sin θ |
| √(1+x²) | Let x = tan θ |
| √(x²−1) | Let x = sec θ |
| (a²−x²) | Let x = a sin θ |
| (a²+x²) | Let x = a tan θ |
| (x²−a²) | Let x = a sec θ |

---

## 3. Inverse Trig Derivatives

### Derivative Formulas
| Function | Derivative |
|----------|------------|
| sin⁻¹(x) | 1/√(1−x²), x ∈ (−1, 1) |
| cos⁻¹(x) | −1/√(1−x²), x ∈ (−1, 1) |
| tan⁻¹(x) | 1/(1+x²), x ∈ ℝ |
| cosec⁻¹(x) | −1/(|x|√(x²−1)), |x| > 1 |
| sec⁻¹(x) | 1/(|x|√(x²−1)), |x| > 1 |
| cot⁻¹(x) | −1/(1+x²), x ∈ ℝ |

### Derivatives of Composite Functions
| Function | Derivative |
|----------|------------|
| sin⁻¹(f(x)) | f'(x)/√(1−(f(x))²) |
| cos⁻¹(f(x)) | −f'(x)/√(1−(f(x))²) |
| tan⁻¹(f(x)) | f'(x)/(1+(f(x))²) |

---

## 4. Basic Maths Fundamentals

### Algebraic Identities
| Identity | Expansion |
|----------|-----------|
| (a+b)² | a² + 2ab + b² |
| (a−b)² | a² − 2ab + b² |
| (a+b)(a−b) | a² − b² |
| (a+b)³ | a³ + 3a²b + 3ab² + b³ |
| (a−b)³ | a³ − 3a²b + 3ab² − b³ |
| a³ + b³ | (a+b)(a² − ab + b²) |
| a³ − b³ | (a−b)(a² + ab + b²) |
| (a+b+c)² | a² + b² + c² + 2ab + 2bc + 2ca |

### Progressions
| Type | nth Term | Sum of n Terms |
|------|----------|----------------|
| **AP** | a + (n−1)d | Sₙ = n/2[2a + (n−1)d] |
| **GP** | arⁿ⁻¹ | Sₙ = a(rⁿ−1)/(r−1), r ≠ 1 |
| **HP** | 1/(a + (n−1)d) | No simple formula |

### Logarithms
| Property | Formula |
|----------|---------|
| Product | log(xy) = log x + log y |
| Quotient | log(x/y) = log x − log y |
| Power | log(xⁿ) = n log x |
| Change of base | log_b(x) = log_c(x)/log_c(b) |
| Common log | log₁₀(x) = log(x) |
| Natural log | log_e(x) = ln(x) |

### Quadratic Equation
```
ax² + bx + c = 0
Roots: x = (−b ± √(b²−4ac)) / 2a
Discriminant: D = b²−4ac
```
| D Value | Nature of Roots |
|---------|-----------------|
| D > 0 | Two distinct real roots |
| D = 0 | Two equal real roots (repeated) |
| D < 0 | Complex conjugate roots |

---

## 5. Maths Revision Capsule — High-Yield Topics

### Quick Reference Card
```
1. Inverse Trig: Memorize domains, ranges, and key identities (sin⁻¹x + cos⁻¹x = π/2)
2. Inverse Trig Derivatives: sin⁻¹x → 1/√(1−x²); tan⁻¹x → 1/(1+x²)
3. Algebraic Identities: (a±b)², (a±b)³, a³±b³ — know these cold
4. Quadratic: discriminant tells root nature; Vieta's formulas for root relationships
5. Trigonometry: compound angle formulas, double angle formulas, half angle
6. Progressions: nth term and sum formulas for AP and GP
```

### Common Mistakes to Avoid
| Mistake | Correction |
|---------|------------|
| Forgetting absolute value in sec⁻¹ derivative | Use |x| not just x |
| Wrong range for sin⁻¹ (or cos⁻¹) | sin⁻¹: [−π/2, π/2]; cos⁻¹: [0, π] |
| Incorrect tan⁻¹ sum formula sign | +π when both x,y > 0 and xy > 1 |
| Miscounting terms in AP sum | n/2 is correct, not n |
| Using AP formula for GP | GP uses different sum formula (r ≠ 1) |

---

## Cross-References
- [[wiki/01-Areas/Engineering/mathematics/formula-sheet-master]] — Complete master formula sheet (covers these topics in depth)
- [[wiki/01-Areas/Engineering/mathematics/formula-sheet-trigonometry]] — Full trigonometry formula compendium
- [[wiki/01-Areas/Engineering/mathematics/overview]] — Mathematics theme overview and topic map
- [[wiki/01-Areas/Engineering/mathematics/quick-revision-cards]] — 18 ultra-condensed revision cards
- [[wiki/01-Areas/Engineering/physics/formula-sheet-mechanics]] — Complementary physics formulas
- [[brain/Patterns/agent-pipeline-patterns]] — Mathematics problem-solving patterns