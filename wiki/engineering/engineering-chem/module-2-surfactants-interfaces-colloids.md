---
module: "engineering-chem"
topic: "Module 2: Surfactants, Interfaces & Colloidal Chemistry — Micelles, CMC, Emulsions & Detergency"
tags: [engineering-chemistry, surfactants, colloids, micelles, critical-micelle-concentration, kraft-temperature, detergency, emulsification, solubilization, wetting-agents, soaps]
last_updated: "2026-08-19"
prerequisites: ["Hydrophobic & Hydrophilic Interactions", "Surface Tension", "Gibbs Free Energy", "Thermodynamics of Mixing"]
---

# Module 2: Surfactants, Interfaces & Colloidal Chemistry

> Deep dive into surface-active chemistry: the amphiphilic molecule, the four surfactant classes, the thermodynamics of micellization (CMC and Kraft point), and the applied phenomena — detergency, emulsification, solubilization, and wetting — that power soaps, shampoos, emulsion paints, pharmaceuticals and enhanced-oil-recovery.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Mathematical Formulation & Explicit Derivations](#2-mathematical-formulation--explicit-derivations)
3. [High-Yield Exam Problems & Worked Solutions](#3-high-yield-exam-problems--worked-solutions)
4. [Engineering Applications Map](#4-engineering-applications-map)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.1 The Amphiphilic Molecule — Structure

A surfactant molecule has two fused halves with opposite solvent affinities:

```
        ┌───────────────────────────────┬────────────────────────┐
        │     HYDROPHILIC (Polar) HEAD  │   HYDROPHOBIC (Tail)   │
        │     "water-loving"            │   "water-repelling"    │
        ├───────────────────────────────┼────────────────────────┤
        │  –COO⁻ Na⁺ (soap)            │  C₁₂–C₁₈ hydrocarbon   │
        │  –SO₃⁻ Na⁺ (sulfonate)       │  chain (alkyl)         │
        │  –OSO₃⁻ Na⁺ (sulfate)        │  alkylbenzene          │
        │  –N⁺(CH₃)₃ Cl⁻ (quat)        │  fluorocarbon          │
        │  –(CH₂CH₂O)ₙOH (PEO)         │  siloxane              │
        └───────────────────────────────┴────────────────────────┘
                 │                                    │
                 ▼                                    ▼
        dissolves in water                      avoided by water
        (ion–dipole / H-bonding)                (entropy-driven exclusion)
```

### 1.2 Hydrophilic vs. Hydrophobic — Comparison Table

| Property | Hydrophilic Head | Hydrophobic Tail |
|---|---|---|
| **Affinity** | Water-loving (polar / ionic) | Water-repelling (non-polar) |
| **Origin of interaction** | Ion–dipole, dipole–dipole, H-bonding | Dispersion forces; water "structuring" |
| **Example groups** | –COO⁻, –SO₃⁻, –OSO₃⁻, –N⁺R₃, –OH, –(EO)ₙ | C₁₂H₂₅–, C₁₆H₃₃–, C₆H₅–CH₂–, (CF₂)ₙ |
| **Effect of longer tail** | — (unchanged) | ↑ hydrophobicity, ↓ solubility, ↓ CMC |
| **Energy sign in water** | Favorable ΔG (mixing) | Unfavorable ΔG (entropy loss) |

### 1.3 Classification of Surfactants — Master Table

| Class | Head Group | Charge | Typical Examples | Properties |
|---|---|---|---|---|
| **Anionic** | –COO⁻, –SO₃⁻, –OSO₃⁻ | Negative | SDS (C₁₂H₂₅SO₄Na), Soap (RCOONa), LAS (linear alkylbenzene sulfonate) | Best detergency; strong foaming; incompatible with hard water (Ca²⁺/Mg²⁺ scum) |
| **Cationic** | –N⁺(CH₃)₃, –N⁺(CH₃)₂R | Positive | CTAB (cetyltrimethylammonium bromide), Benzalkonium chloride | Fabric softeners, germicides/antiseptics; adsorb on negatively charged surfaces; not good detergents |
| **Non-ionic** | –(OCH₂CH₂)ₙOH, sugar | Neutral | Triton X-100, Tween/Span (sorbitan esters), Brij | Low foam, hard-water tolerant; used with enzymes & cold water |
| **Zwitterionic (amphoteric)** | both signs | + and – (net 0 at isoelectric) | Betaines, Phospholipids (lecithin) | Mild, low irritation → baby shampoos; pH-responsive |

**HLB concept (memory hook):** HLB (hydrophilic-lipophilic balance) on a 0–20 scale — low HLB (3–6) → W/O emulsifier; high HLB (8–18) → O/W emulsifier; HLB ≈ 0 pure lipophilic, ≈ 20 pure hydrophilic.

### 1.4 Micellization — Formation Flowchart

```
        LOW concentration (monomers)          HIGH concentration (> CMC)
        ──────────────────────────────        ─────────────────────────────
        SURFACTANT MOLECULES                  SPHERICAL MICELLE (~50-100)
        DISSOLVED SEPARATELY                  hydrophobic tails INWARDS
        adsorbed at interfaces                polar heads OUTWARDS (water contact)
                 │                                     │
                 │  add more surfactant                 │
                 ▼                                     ▼
        ┌────────────────────────┐           ┌──────────────────────────────┐
        │ surface tension ↓      │           │ surface tension ~ constant    │
        │ (monomer adsorbs)      │           │ monomers ~ constant (= CMC)   │
        │                         │           │ excess forms micelles         │
        └────────────────────────┘           └──────────────────────────────┘
                                                          │
                CMC = concentration where micelles        │
                just begin to form; kink in the plot      ▼
                (surface tension, conductivity,           Aggregation number N
                 dye solubility vs C)                     (N ≈ 60-80 for ionic,
                                                          N ≈ 100-200 non-ionic)
```

**Hydrophobic effect (thermodynamic driving force):** Dissolving a hydrocarbon chain in water forces water molecules to form ordered "cages" (clathrate-like) around the chain — a large **negative entropy** penalty. When chains cluster into a micelle, those cages are released → **entropy increases**, and $\Delta G = \Delta H - T\Delta S < 0$ even when ΔH is slightly endothermic.

### 1.5 Cleansing Action of Soap — Detergency Flowchart

```
   DIRTY SURFACE (oil/grease + dirt)
        │
        ▼
   SOAP SOLUTION (micelles + monomers)
        │
        ▼
 1. WETTING — surfactant lowers surface tension,
    solution penetrates fabric / spreads on grease
        │
        ▼
 2. EMULSIFICATION — hydrophobic tail penetrates grease,
    polar head stays in water → grease breaks into droplets
        │
        ▼
 3. MICELLAR SOLUBILIZATION — oil droplets & dirt are
    encapsulated in micelle interiors (solubilization)
        │
        ▼
 4. DETACHMENT & SUSPENSION — negatively charged micelles
    repel each other & the fabric (electrostatic), dirt stays
    suspended, rinse carries it away
        │
        ▼
   CLEAN SURFACE + WASH WATER (no redeposition)
```

**Limitation of soap:** In hard water, Na⁺ soaps exchange with Ca²⁺/Mg²⁺ → insoluble calcium/magnesium soaps (scum) that waste soap and deposit on fabric. Detergents (sulfonates, sulfates) form **soluble** Ca/Mg salts → superior hard-water detergency. This is the core reason detergents replaced soap in laundry.

### 1.6 Emulsions — Classification Flowchart

```
                    EMULSION (dispersion of one liquid in another)
                                   │
                       ┌───────────┴─────────────┐
                       ▼                         ▼
                   O/W (oil in water)         W/O (water in oil)
                   oil droplets in water      water droplets in oil
                       │                         │
         emulsifier: high-HLB (8-18)      emulsifier: low-HLB (3-6)
         e.g. Tween, SDS, milk, cream     e.g. Span, butter, cold cream
                       │                         │
                       ▼                         ▼
        Type test: water-soluble dye        oil-soluble dye spreads
        spreads/colors continuous phase     → continuous phase is oil
```

### 1.7 Kraft Temperature — Solubility vs. Micellization Decision Tree

```
  Ionic surfactant + water
        │
        ▼
  Heating?
  ────────
  below Kraft point (T < TK):  surfactant solubility too low
                               for micelles → NO micellization
                               (salt exists as solid/hydrate)
        │
        ▼
  at T = TK (Kraft point):     solubility curve meets CMC curve —
                               a single temperature where solubility
                               = CMC; micelles can finally form
        │
        ▼
  above T > TK:                solubility rises steeply; micelles
                               form readily (CMC nearly constant)
        │
        ▼
  WHY?  micellization releases the ordered water "cages" → large
  entropic gain; the crystalline surfactant hydrate itself must
  first melt/dissolve, which costs heat (enthalpy) — both balance
  exactly at TK
```

**Note:** Non-ionic surfactants have a **cloud point** (upper temperature) instead — above it they separate into two phases.

---

## 2. MATHEMATICAL FORMULATION & EXPLICIT DERIVATIONS

### 2.1 Thermodynamics of Micellization — The Entropy Driver

**Step 1 — dissolve the monomer.** For a single surfactant monomer S, the Gibbs energy change of going from free monomer to micelle is:

$$\Delta G_m = \Delta H_m - T \Delta S_m$$

**Step 2 — evaluate signs.** $\Delta H_m$ is typically small and slightly positive (van der Waals attractions among tails give mild exothermic contribution; hydration changes give mild endothermic part). The entropy term dominates because **removing the ordered hydration cages** around each tail raises the system's entropy significantly:

$$\Delta S_m > 0 \qquad \Rightarrow \qquad \Delta G_m < 0$$

**Step 3 — pseudo-phase model.** Treat the micelle as a separate phase; then at equilibrium (CMC) the standard free energy change is:

$$\boxed{\Delta G_m^{\circ} = R T \ln(\text{CMC})}$$

**Step 4 — ionic correction.** For an ionic surfactant of concentration $C$, with degree of counter-ion binding $\beta$ (fraction of counterions bound to micelle surface), the effective monomer activity is (CMC) and the counter-ion term enters:

$$\Delta G_m^{\circ} = (1 + \beta)\, R T \ln(\text{CMC})$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Delta G_m^{\circ}$ | standard molar free energy of micellization | kJ/mol |
| R | gas constant (8.314) | J mol⁻¹ K⁻¹ |
| T | absolute temperature | K |
| CMC | critical micelle concentration (as mole fraction or mol/L) | mol/L |
| β | degree of counter-ion binding (0 to 1) | — |

**Consequences (exam favorites):**
- CMC **decreases** with increasing hydrocarbon tail length (longer tail → stronger hydrophobic effect).
- CMC decreases with added salt (ionic surfactants) — salt screens head-group repulsion.
- CMC of non-ionic surfactants is ~1-2 orders of magnitude **lower** than ionic of same chain length (no head-group charge repulsion).
- CMC decreases with decreasing temperature for non-ionic; increases for ionic near Kraft point.

### 2.2 Gibbs Adsorption Isotherm — Surface Concentration

The excess surface concentration (surface excess) of a surfactant at the interface:

$$\Gamma = -\frac{1}{nRT}\left(\frac{\partial \gamma}{\partial \ln C}\right)_T$$

where $n = 1$ for non-ionic, $n = 2$ for 1:1 ionic surfactant (surfactant + counterion).

| Symbol | Meaning | Unit |
|---|---|---|
| Γ | surface excess concentration | mol/m² |
| γ | surface tension | N/m (mN/m) |
| C | bulk concentration | mol/L |
| n | number of species adsorbing (1 or 2) | — |

**Reading the isotherm:** below CMC, $\frac{\partial \gamma}{\partial \ln C}$ is negative (γ falls steeply) → Γ > 0 (adsorption). At/above CMC, γ is flat → Γ is fixed — no more monomers to adsorb; micelles take up the surplus.

### 2.3 Micellar Aggregation Number & Solubilization Capacity

**Aggregation number** (number of monomers per micelle):

$$N = \frac{4\pi R^2}{a_0} \quad \text{(spherical micelle, head area } a_0 \text{ per monomer)}$$

More usefully, from the micelle core radius $R$ (≈ fully extended tail length $\ell$) and core volume $v$ per monomer:

$$N = \frac{4\pi R^3}{3 v} \approx \frac{4\pi \ell^3}{3 v}$$

| Symbol | Meaning | Unit |
|---|---|---|
| N | aggregation number | — |
| R | micelle core radius ≈ tail length ℓ | m (nm) |
| v | volume per hydrophobic tail (~0.027 n₍C₎ nm³) | nm³ |
| a₀ | area per polar head at interface | nm² |

**Critical packing parameter (CPP):**

$$CPP = \frac{v}{\ell \cdot a_0}$$

| CPP | Preferred Structure |
|---|---|
| < 1/3 | spherical micelles |
| 1/3 – 1/2 | cylindrical micelles |
| 1/2 – 1 | flexible bilayers / vesicles |
| = 1 | planar bilayer |
| > 1 | inverted (W/O) micelles |

### 2.4 HLB Scale — Formulation Math

HLB of a non-ionic surfactant from its composition:

$$HLB = 20 \times \frac{M_{hydrophilic}}{M_{hydrophilic} + M_{hydrophobic}}$$

For ester-based emulsifiers:

$$HLB = 20 \left(1 - \frac{S}{A}\right)$$

| Symbol | Meaning |
|---|---|
| M_hydrophilic | mass of hydrophilic (EO or OH) portion |
| S | saponification number |
| A | acid number of the parent fatty acid |

**Rule of thumb:** HLB 3–6 → W/O emulsifier; HLB 8–18 → O/W emulsifier; HLB 13–15 → detergent; HLB 15–18 → solubilizer. In practice one **blends** emulsifiers to reach the required HLB of the oil phase (required HLB method).

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: CMC and ΔG° of Micellization

**Problem.** The CMC of a non-ionic surfactant is 8 × 10⁻⁴ mol/L at 25 °C. Calculate the standard free energy of micellization $\Delta G_m^{\circ}$ (R = 8.314 J mol⁻¹ K⁻¹).

---

**Solution:**

**Step 1 — write the pseudo-phase relation.**

$$\Delta G_m^{\circ} = RT \ln(\text{CMC})$$

**Step 2 — substitute values.**

$$\Delta G_m^{\circ} = 8.314 \times (25 + 273.15) \times \ln(8 \times 10^{-4})$$

$$= 8.314 \times 298.15 \times (-7.1309)$$

**Step 3 — compute.**

$$= 2478.8 \times (-7.1309) = -17675\ \text{J/mol}$$

**Step 4 — answer.**

$$\boxed{\Delta G_m^{\circ} = -17.68\ \text{kJ/mol}}$$

(Negative → micellization is spontaneous above CMC; consistent with the entropy-driven hydrophobic effect.)

---

### Problem 2: Surface Excess (Gibbs Isotherm) from Surface Tension Data

**Problem.** For a non-ionic surfactant, surface tension falls from 72 to 40 mN/m when ln C changes from −14 to −8 (C in mol/L) at 300 K. Estimate the surface excess concentration Γ.

---

**Solution:**

**Step 1 — compute the slope.**

$$\frac{\partial \gamma}{\partial \ln C} = \frac{40 - 72}{-8 - (-14)} = \frac{-32}{6} = -5.333\ \text{mN/m} = -5.333 \times 10^{-3}\ \text{N/m}$$

**Step 2 — apply the Gibbs isotherm (n = 1, non-ionic).**

$$\Gamma = -\frac{1}{RT}\left(\frac{\partial \gamma}{\partial \ln C}\right) = -\frac{1}{8.314 \times 300} \times (-5.333 \times 10^{-3})$$

**Step 3 — compute.**

$$= \frac{5.333 \times 10^{-3}}{2494.2} = 2.138 \times 10^{-6}\ \text{mol/m}^2$$

**Step 4 — answer.**

$$\boxed{\Gamma = 2.14 \times 10^{-6}\ \text{mol/m}^2}$$

---

### Problem 3: Effect of Chain Length on CMC (Traube's Rule Check)

**Problem.** The CMC of sodium dodecyl sulfate (C₁₂, CMC = 8.2 mM) is known. Estimate the CMC of sodium decyl sulfate (C₁₀) and sodium tetradecyl sulfate (C₁₄) using Traube's rule (CMC halves for each added –CH₂– group).

---

**Solution:**

**Step 1 — Traube's rule.** Adding one methylene group to the tail reduces CMC by ~half (i.e. factor 0.5 per CH₂). It is a consequence of the linear relation:

$$\log_{10}(\text{CMC}) = A - B\, n_C \quad \text{with B ≈ 0.3}$$

**Step 2 — C₁₀ is 2 CH₂ shorter than C₁₂** (more soluble, higher CMC):

$$\text{CMC}_{C_{10}} = 8.2 \times 2^2 = 32.8\ \text{mM}$$

**Step 3 — C₁₄ is 2 CH₂ longer than C₁₂** (more hydrophobic, lower CMC):

$$\text{CMC}_{C_{14}} = \frac{8.2}{2^2} = 2.05\ \text{mM}$$

**Step 4 — answers.**

$$\boxed{\text{CMC (C}_{10}\text{) ≈ 32.8 mM}} \qquad
\boxed{\text{CMC (C}_{14}\text{) ≈ 2.05 mM}}$$

(Reason: longer tail → larger hydrophobic driving force → micelles form at lower concentration.)

---

### Problem 4: HLB Blend Calculation for Emulsion Formulation

**Problem.** An O/W emulsion requires HLB = 10. Two emulsifiers are available: Span 80 (HLB 4.3) and Tween 80 (HLB 15). Determine the mass fraction of each needed to give the target HLB.

---

**Solution:**

**Step 1 — blend rule (linear mixing on a mass basis).**

$$HLB_{blend} = f_A \cdot HLB_A + (1 - f_A) \cdot HLB_B$$

where f_A is the mass fraction of Span 80.

**Step 2 — substitute.**

$$10 = 4.3\, f_A + 15\,(1 - f_A) = 15 - 10.7\, f_A$$

**Step 3 — solve.**

$$10.7\, f_A = 15 - 10 = 5 \qquad \Rightarrow \qquad f_A = \frac{5}{10.7} = 0.467$$

**Step 4 — fractions.**

$$\boxed{\text{Span 80: } 46.7\%} \qquad
\boxed{\text{Tween 80: } 53.3\%}$$

---

### Problem 5: Aggregation Number from Hydrocarbon Chain Volume

**Problem.** A C₁₆ non-ionic surfactant forms spherical micelles. Given tail volume v = 0.43 nm³ per monomer and fully extended tail length ℓ = 2.2 nm, estimate the aggregation number N.

---

**Solution:**

**Step 1 — use the geometric relation.**

$$N = \frac{4\pi \ell^3}{3v}$$

**Step 2 — substitute.**

$$N = \frac{4\pi (2.2)^3}{3 \times 0.43} = \frac{4\pi \times 10.648}{1.29}$$

**Step 3 — compute.**

$$= \frac{133.81}{1.29} = 103.7$$

**Step 4 — answer.**

$$\boxed{N \approx 104\ \text{monomers per micelle}}$$

---

## 4. ENGINEERING APPLICATIONS MAP

| Principle | Industrial / Field Application |
|---|---|
| **CMC & micellization** | Detergent formulation (operate above CMC for maximum solubilization efficiency); laundry & dishwash chemistry; hard-surface cleaning |
| **Anionic surfactants (SDS/LAS)** | Laundry detergents, shampoo, dishwashing liquids, industrial degreasers (best soil removal, cheap) |
| **Cationic surfactants (CTAB, quats)** | Fabric softeners, hair conditioners (deposit on negatively charged fibres/hair), disinfectants & antiseptics (benzalkonium chloride) |
| **Non-ionic surfactants** | Enzyme-compatible cold-water detergents, low-foam dishwasher/industrial formulations, emulsion paints, pesticide adjuvants |
| **Zwitterionics (betaines)** | Mild baby shampoos, body washes, contact-lens cleaning solutions (low irritation) |
| **Emulsification (HLB method)** | Milk/cream processing, mayonnaise & sauces, cosmetic creams, emulsion paints, asphalt emulsions, cutting fluids, pharmaceuticals (o/w and w/o drug delivery) |
| **Solubilization in micelles** | Enhanced Oil Recovery (surfactant flooding), drug solubilization of poorly-soluble actives, flavour/fragrance encapsulation, soil remediation |
| **Wetting agents** | Spreading of sprays/inks/pesticides, textile wetting, soldering fluxes, photographic film processing, fire-fighting foams |
| **Foaming control** | Defoamers (silicone) in fermentation, pulp & paper, boiler water; foam fractionation |
| **Kraft point / cloud point engineering** | Selecting the right surfactant & temperature window for a given industrial process (hot washing, cold-water detergents) |

---

## APPENDIX: Formula & Data Quick Reference

| Quantity | Formula | Notes |
|---|---|---|
| Free energy of micellization | $\Delta G_m^{\circ} = RT\ln(\text{CMC})$ | ionic: ×(1+β) |
| Gibbs adsorption isotherm | $\Gamma = -\frac{1}{nRT}\left(\frac{\partial\gamma}{\partial\ln C}\right)_T$ | n=1 non-ionic, n=2 ionic |
| Traube's rule | CMC halves per added CH₂ | log CMC = A − B·nC |
| HLB (non-ionic) | $20 \times \frac{M_{hydrophilic}}{M_{total}}$ | 3-6 W/O, 8-18 O/W |
| Blend HLB | $HLB = \sum f_i HLB_i$ | mass fractions |
| Aggregation number | $N = \frac{4\pi\ell^3}{3v}$ | spherical micelles |
| CPP | $CPP = \frac{v}{\ell a_0}$ | predicts micelle shape |
| Osmotic pressure (colloid) | $\Pi = CRT$ | for micellar solutions |

## CROSS-REFERENCES

- Related modules: [[module-1-water-technology-hardness]] (hard-water effect on soap) · [[module-3-electrochemistry-corrosion]] (surfactant adsorption in corrosion inhibition) · [[chemistry/formula-sheet-physical]] (surface chemistry: Langmuir/Freundlich) · [[chemistry/overview]] (colloids, emulsions)
