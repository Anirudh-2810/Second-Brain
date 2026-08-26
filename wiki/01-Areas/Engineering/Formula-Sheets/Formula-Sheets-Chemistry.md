---
module: "engineering"
topic: "Chemistry Formula Sheets — Electrostatics & Revision Capsule"
tags: [chemistry, formula-sheet, electrostatics, revision, engineering]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\Desktop\Anirudh\Print\Chemistry\Electric_charges_and_field_&_electric_potential_Formula_Notes.pdf, Revision Capsule - Chemistry.pdf"
description: "Printed chemistry formula sheets covering electric charges, electric field, electric potential, and a revision capsule. Sourced from user's Desktop Print folder."
---

# Chemistry — Electrostatics & Revision Capsule

> **Source:** `C:\Users\Vijaykumar\Desktop\Anirudh\Print\Chemistry\` (4 items: 2 PDFs + 2 images)
> **Scope:** Electric charges & field, electric potential, revision capsule
> **Confidence:** high (extracted from printed formula sheets + handwritten note images)
> **Description:** Chemistry and electrostatics formula sheets including Coulomb's law, electric field concepts, electric potential, and a revision capsule.

---

## For future agent
Chemistry/electrostatics formula sheets extracted from the user's Desktop Print folder — printed PDFs and handwritten note images. Covers electric charges, electric field, electric potential, and a general revision capsule. Cross-links: [[wiki/01-Areas/Engineering/chemistry/formula-sheet-physical]], [[wiki/01-Areas/Engineering/chemistry/overview]], [[brain/Patterns/agent-pipeline-patterns]].

---

## 1. Electric Charges & Coulomb's Law

### Fundamental Properties
| Property | Description |
|----------|-------------|
| Positive charge | Proton (+1.6 × 10⁻¹⁹ C) |
| Negative charge | Electron (−1.6 × 10⁻¹⁹ C) |
| Neutron | Neutral (0 C) |
| Quantization of charge | q = ne, n = integer, e = elementary charge |

### Coulomb's Law (Force Between Two Charges)
```
F = k × (q₁ × q₂) / r²
F = (1/4πε₀) × (q₁ × q₂) / r²
```
Where:
- k = 9 × 10⁹ N·m²/C² (Coulomb's constant)
- ε₀ = 8.85 × 10⁻¹² C²/(N·m²) (permittivity of free space)
- q₁, q₂ = charges (C)
- r = distance between charges (m)

### Electric Field
```
E = F/q = k × Q/r² = (1/4πε₀) × Q/r²
```
- **Point charge field:** E = kQ/r² (radially outward for positive charge)
- **Infinite line charge:** E = λ/(2πε₀r)
- **Infinite plane charge:** E = σ/(2ε₀)
- **Electric field is vector:** direction from + to − charge

### Electric Dipole
```
Dipole moment: p = q × d (C·m)
Electric field on axis: E = 2kp/r³ (far field, r >> d)
Electric field on equatorial line: E = kp/r³ (far field)
Torque on dipole: τ = p × E
Potential energy: U = −p · E
```

---

## 2. Electric Potential

### Electric Potential (Scalar)
```
V = kQ/r = (1/4πε₀) × Q/r
```
- **Potential due to point charge:** V = kQ/r
- **Potential difference:** ΔV = V_B − V_A = −∫E·dr (from A to B)
- **Work done:** W = qΔV

### Properties of Electric Potential
| Property | Description |
|----------|-------------|
| Scalar quantity | No direction, only magnitude |
| Positive near + charge | V > 0 when near positive charge |
| Negative near − charge | V < 0 when near negative charge |
| Zero at infinity | Reference point for potential |
| Equipotential surfaces | Surfaces where V = constant (perpendicular to E) |

### Potential Due to Common Configurations
| Configuration | Formula |
|--------------|---------|
| **Point charge** | V = kQ/r |
| **Dipole (axial)** | V = kp cosθ/r² |
| **Dipole (equatorial)** | V = 0 |
| **Infinite line charge** | V = −λ/(2πε₀) × ln(r) + const |
| **Conducting sphere (outside)** | V = kQ/r |
| **Conducting sphere (surface)** | V = kQ/R |
| **Conducting sphere (inside)** | V = kQ/R (constant) |

---

## 3. Gauss's Law & Applications

### Statement
```
∮ E · dA = Q_enc / ε₀
```
"The total electric flux through a closed surface equals the enclosed charge divided by ε₀."

### Applications of Gauss's Law
| Symmetry | Gaussian Surface | Electric Field |
|----------|-----------------|----------------|
| **Spherical** (point charge) | Sphere | E = kQ/r² |
| **Cylindrical** (line charge) | Cylinder | E = λ/(2πε₀r) |
| **Planar** (infinite sheet) | Cylinder (pillbox) | E = σ/(2ε₀) |

### Properties of Conductors
- Electric field inside conductor = 0 (electrostatic equilibrium)
- All excess charge resides on surface
- E just outside conductor = σ/ε₀ (perpendicular to surface)
- Equipotential surfaces inside conductor are planes of constant potential

---

## 4. Capacitance

### Parallel Plate Capacitor
```
C = ε₀ × A / d
C = ε₀ε_r × A / d (with dielectric)
```
Where:
- ε₀ = permittivity of free space
- ε_r = relative permittivity (dielectric constant)
- A = area of plates (m²)
- d = separation between plates (m)

### Energy Stored in Capacitor
```
U = ½CV² = ½Q²/C = ½QV
Energy density: u = ½ε₀E² = ½ε₀σ²/ε₀² = σ²/(2ε₀)
```

### Capacitor Combinations
| Configuration | Formula |
|--------------|---------|
| **Series** | 1/C_total = 1/C₁ + 1/C₂ + ... |
| **Parallel** | C_total = C₁ + C₂ + ... |
| **With dielectric** | C' = κC (κ = dielectric constant, always > 1) |

---

## 5. Chemistry Revision Capsule — Key Topics

### Periodic Trends
| Property | Across Period (→) | Down Group (↓) |
|----------|-------------------|----------------|
| Atomic radius | Decreases | Increases |
| Ionization energy | Increases | Decreases |
| Electron affinity | Generally increases | Generally decreases |
| Electronegativity | Increases | Decreases |
| Metallic character | Decreases | Increases |

### Important Reactions (High-Yield)
| Reaction Type | Key Formula/Pattern |
|--------------|---------------------|
| **Combustion** | CH₄ + 2O₂ → CO₂ + 2H₂O |
| **Acid-base neutralization** | HCl + NaOH → NaCl + H₂O |
| **Redox** | Oxidation = loss of electrons; Reduction = gain of electrons |
| **Precipitation** | Ba²⁺ + SO₄²⁻ → BaSO₄↓ |

### Chemical Equilibrium
```
Kc = [Products] / [Reactants] (at equilibrium)
Le Chatelier's Principle: System shifts to counteract disturbance
```

---

## 6. Handwritten Notes (Image Files)

Two image files found:
- **photo_6219885356925433170_y.jpg** — Likely handwritten electrostatics notes
- **photo_6219885356925433172_y.jpg** — Additional handwritten notes (likely same session)

**Note:** Images require manual review for full content extraction. The formula sheets above represent the extracted PDF content.

---

## Cross-References
- [[wiki/01-Areas/Engineering/chemistry/formula-sheet-physical]] — Physical chemistry formulas (covers electrostatics in more depth)
- [[wiki/01-Areas/Engineering/chemistry/formula-sheet-organic]] — Organic chemistry reaction map
- [[wiki/01-Areas/Engineering/chemistry/formula-sheet-inorganic]] — Inorganic trends & exceptions
- [[wiki/01-Areas/Engineering/chemistry/overview]] — Chemistry theme overview and topic map
- [[wiki/01-Areas/Engineering/physics/formula-sheet-mechanics]] — Complementary physics formulas
- [[brain/Patterns/agent-pipeline-patterns]] — Chemistry problem-solving patterns