---
module: "engineering-chem"
topic: "Module 1: Water Technology & Hardness — Water Softening, Boiler Troubles & EDTA Analysis"
tags: [engineering-chemistry, water-technology, hardness, lime-soda, zeolite, ion-exchange, reverse-osmosis, boiler-troubles, edta-titration, scale-sludge, caustic-embrittlement]
last_updated: "2026-08-19"
prerequisites: ["Basic Stoichiometry", "Molarity & Normality", "Equivalent Weight", "Complexometric Titration Basics"]
---

# Module 1: Water Technology & Hardness

> Exam-focused deep dive on water chemistry: why natural water is "hard", how to measure hardness numerically, every industrial softening process, the four classic boiler troubles, and the EDTA complexometric method that ties the whole module together. All problems use the **CaCO₃ equivalent** convention — the single most important skill in this module.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Mathematical Formulation & Explicit Derivations](#2-mathematical-formulation--explicit-derivations)
3. [High-Yield Exam Problems & Worked Solutions](#3-high-yield-exam-problems--worked-solutions)
4. [Engineering Applications Map](#4-engineering-applications-map)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.1 Why Water Is "Hard" — The Root Cause

Hardness is caused exclusively by **dissolved di- and trivalent cations**, the overwhelming majority of it being **Ca²⁺ and Mg²⁺**. These come from minerals dissolved when rain (weakly acidic with dissolved CO₂) percolates through limestone and dolomite beds:

$$\mathrm{CaCO_3 + CO_2 + H_2O \longrightarrow Ca(HCO_3)_2} \quad (\text{soluble})
\qquad
\mathrm{MgCO_3 + CO_2 + H_2O \longrightarrow Mg(HCO_3)_2} \quad (\text{soluble})$$

**Fundamental rules (memorize verbatim):**
- Hardness = concentration of hardness-causing ions, **always expressed as mg/L (ppm) of CaCO₃ equivalents**, never as the actual salt.
- One "equivalent of hardness" = one mole of Ca²⁺ (MW 40) or one mole of Mg²⁺ (MW 24) or one mole of any ion with the same charge contribution.
- CaCO₃ equivalent of an ion $= \text{(mass of ion)} \times \dfrac{\text{Eq wt of CaCO}_3}{\text{Eq wt of ion}} = \text{(mass of ion)} \times \dfrac{50}{\text{(ionic wt/charge)}}$.
- CaCl₂, CaSO₄, MgCl₂, MgSO₄ → **permanent hardness** (not removed by boiling).
- Ca(HCO₃)₂, Mg(HCO₃)₂ → **temporary hardness** (removed by boiling).

### 1.2 Temporary vs. Permanent Hardness — Comparison Table

| Property | Temporary (Carbonate) Hardness | Permanent (Non-carbonate) Hardness |
|---|---|---|
| **Causing salts** | Ca(HCO₃)₂, Mg(HCO₃)₂ | CaCl₂, CaSO₄, Ca(NO₃)₂, MgCl₂, MgSO₄ |
| **Removed by boiling?** | Yes | No |
| **Removed by** | Boiling, lime (Clark's) | Lime-soda, zeolite, ion-exchange, RO |
| **Effect of boiling** | $\mathrm{Ca(HCO_3)_2 \xrightarrow{\Delta} CaCO_3 \downarrow + H_2O + CO_2}$ | None — salts remain |
| **Formula for total** | $T.H. = \text{Temp. H.} + \text{Perm. H.}$ | (same relation) |
| **Primary treatment** | Lime alone is usually sufficient | Lime + soda ash |

### 1.3 Units of Hardness — Conversion Table

| Unit | Symbol | Definition | Relation to CaCO₃ ppm |
|---|---|---|---|
| Parts per million | ppm | 1 part CaCO₃ per 10⁶ parts water | 1 ppm = 1 mg/L (density ≈ 1 g/mL) |
| Milligrams per litre | mg/L | mg of CaCO₃ per litre of water | 1 mg/L = 1 ppm |
| Degree Clarke | °Cl | 1 grain (64.8 mg) CaCO₃ per Imperial gallon (4.546 L) | 1 °Cl = 14.25 ppm |
| Degree French | °Fr | 1 part CaCO₃ per 10⁵ parts water | 1 °Fr = 10 ppm |
| Degree German | °dH | 10 mg CaO per litre | 1 °dH = 17.9 ppm |

**Key conversion factors to memorize:** 1 °Cl = 14.25 ppm · 1 °Fr = 10 ppm · 1 °dH = 17.9 ppm · **1 ppm = 1 mg/L**.

### 1.4 Water Softening — Master Process Flowchart

```
                    RAW HARD WATER (Ca²⁺, Mg²⁺, HCO₃⁻, Cl⁻, SO₄²⁻)
                                        │
                                        ▼
              ┌─────────────────────────────────────────────────┐
              │   SELECT SOFTENING METHOD BY USE-CASE           │
              └───────┬──────────────────────────┬──────────────┘
                      │                          │
        SMALL / DOMESTIC                    INDUSTRIAL / LARGE SCALE
                      │                          │
                      ▼                          ▼
         LIME-SODA PROCESS               +-----------------------------+
         (precipitates hardness          |  ZEOLITE (Permutit)         |
          as CaCO₃ / Mg(OH)₂)            |  PERMANENT PROCESS          |
                      │                  |  Na₂Ze + Ca²⁺ → CaZe + 2Na⁺ |
                      │                  +-------------+---------------+
                      │                                  │
                      │                    +─────────────+─────────────+
                      │                    │                           │
                      │                    ▼                           ▼
                      │        ION-EXCHANGE (Demineralization)   HIGH-PURITY
                      │        H⁺-resin + OH⁻-resin             required? YES → RO
                      │        removes ALL ions → ultrapure      (membrane rejects
                      │        deionized water                   ~99% of salts)
                      ▼                    │
            SLUDGE/FILTRATE  ◄─────────────┘
                 │
                 ▼
        BOILER / PROCESS WATER FEED
```

### 1.5 Lime-Soda Process — Reaction Logic Flowchart

```
 LIME  Ca(OH)₂   ── removes TEMPORARY hardness + CO₃²⁻-precipitables + acidity
 SODA  Na₂CO₃    ── removes PERMANENT hardness (non-carbonate Ca & Mg salts)

  TEMPORARY (LIME ONLY):
   Ca(HCO₃)₂ + Ca(OH)₂  ──► 2CaCO₃↓  + 2H₂O
   Mg(HCO₃)₂ + 2Ca(OH)₂ ──► Mg(OH)₂↓ + 2CaCO₃↓ + 2H₂O

  PERMANENT (LIME + SODA):
   CaCl₂     + Na₂CO₃    ──► CaCO₃↓  + 2NaCl
   CaSO₄     + Na₂CO₃    ──► CaCO₃↓  + Na₂SO₄
   MgCl₂     + Ca(OH)₂   ──► Mg(OH)₂↓+ CaCl₂  (CaCl₂ now removed by soda)
   MgSO₄     + Ca(OH)₂   ──► Mg(OH)₂↓+ CaSO₄  (then CaSO₄ removed by soda)

  RESIDUAL HARDNESS: caused by Ca(OH)₂ and Na₂CO₃ excess (back-titration
  required in the *cold* process; the *hot* process controls it by heating).
```

### 1.6 Scale vs. Sludge — Comparison Table

| Feature | Scale | Sludge |
|---|---|---|
| **Formation** | Hard, adherent deposits on boiler heating surface | Soft, loose, slimy/settling deposits |
| **Cause** | CaSO₄ (>1500 ppm) has **inverse** solubility (decreases with T↑) — precipitates on hot metal | CaCO₃, Mg(OH)₂, MgCO₃ with **normal** solubility — precipitate in bulk water, settle out |
| **Location** | Directly on heating surfaces | In areas of low flow (drums, headers) |
| **Effect** | Poor heat transfer, hot spots, tube rupture, fuel waste | Sludge can blanket metal, may scale-up on baking |
| **Prevention** | Low hard-water scale formers, softening, internal treatment | Blow-down, removal via sludge conditioners |

### 1.7 The Four Boiler Troubles — Snapshot Table

| Trouble | Cause | Prevention |
|---|---|---|
| **Scale & Sludge** | Hardness salts deposited at heat surfaces | Soften feed water, blow-down, colloid addition (tannin) |
| **Caustic Embrittlement** | Na₂CO₃ decomposes → NaOH; NaOH concentrates at cracks, dissolves cementing Fe₃O₄ inter-granular material | Add Na₂SO₄/Na₃PO₄ as inhibitor, keep Na₂SO₄ : NaOH ratio ~1:1, remove cracked regions |
| **Boiler Corrosion** | Dissolved O₂, CO₂ and acidic water attack metal (Fe → Fe²⁺; 2e⁻ used to reduce O₂) | Deaeration, Na₂SO₃/Na₂CO₃ (oxygen scavengers), maintain alkaline pH |
| **Priming & Foaming** | Oily matter, suspended solids, high dissolved solids, sudden steam demand (priming); soap/suds-producing substances (foaming) | Blow-down, anti-foam agents, filtration, avoid overloading boiler |

### 1.8 EDTA Hardness Titration — Analytical Flowchart

```
        WATER SAMPLE
            │
            ▼
  ┌─────────────────────────────┐
  │  PART A — TOTAL HARDNESS    │
  │  Buffer pH = 10 (NH₄Cl/NH₄OH)│
  │  Indicator: Eriochrome Black T│
  │  Titrate with standard EDTA   │
  └──────────────┬──────────────┘
                 │  colour change: wine-red → steel-blue
                 ▼
        Total hardness (Ca + Mg)
            │
            ▼
  ┌─────────────────────────────┐
  │  PART B — PERMANENT HARDNESS│
  │  Boil sample, filter CaCO₃  │
  │  pH = 10 buffer, EBT        │
  │  Titrate filtrate w/ EDTA   │
  └──────────────┬──────────────┘
                 ▼
        Permanent hardness
            │
            ▼
  Temporary hardness = Total − Permanent
```

**Reaction core of the titration (1:1 stoichiometry):**

$$\mathrm{Ca^{2+} + Na_2H_2EDTA \longrightarrow [Ca-EDTA]^{2-} + 2H^+}$$

**Indicator action:** Eriochrome Black T (HIn²⁻, blue) first forms a wine-red $\mathrm{MgIn^-}$ complex; EDTA pulls Mg²⁺ out at the endpoint, freeing HIn²⁻ (steel-blue) — endpoint colour change **wine-red → steel-blue**.

---

## 2. MATHEMATICAL FORMULATION & EXPLICIT DERIVATIONS

### 2.1 The CaCO₃ Equivalency Principle — Full Derivation

**Problem this solves:** Different hardness ions carry different masses per unit charge. We need one common measure. CaCO₃ (MW = 40.08 + 12.01 + 3×16.00 ≈ 100) is chosen because it is insoluble, harmless, abundant, and its equivalent weight is a round **50**.

**Step 1 — define equivalent weight:**

$$\text{Eq. wt} = \frac{\text{Molecular (or atomic/ionic) weight}}{\text{Valency (charge magnitude)}}$$

| Ion / Salt | Ionic/Molecular Weight | Valency | Eq. wt |
|---|---|---|---|
| Ca²⁺ | 40 | 2 | 20 |
| Mg²⁺ | 24 | 2 | 12 |
| CaCO₃ | 100 | 2 | **50** |
| Ca(HCO₃)₂ | 162 | 2 | 81 |
| Mg(HCO₃)₂ | 146 | 2 | 73 |
| CaCl₂ | 111 | 2 | 55.5 |
| CaSO₄ | 136 | 2 | 68 |
| MgCl₂ | 95 | 2 | 47.5 |
| MgSO₄ | 120 | 2 | 60 |
| Na₂CO₃ | 106 | 2 | 53 |
| Ca(OH)₂ | 74 | 2 | 37 |

**Step 2 — one equivalent of any ion neutralizes one equivalent of any other:**

Hardness is a charge-conserving quantity: 1 eq of Ca²⁺ ≈ 1 eq of Mg²⁺ ≈ 1 eq of CaCO₃. Therefore the mass of CaCO₃ equivalent to a given mass of a salt is:

$$\text{Hardness (as CaCO}_3\text{)} = \text{mass of salt} \times \frac{\text{Eq. wt of CaCO}_3}{\text{Eq. wt of salt}} = \text{mass of salt} \times \frac{50}{\text{Eq. wt of salt}}$$

**Step 3 — worked plug-in.** 100 g of CaCl₂ (Eq. wt 55.5):

$$\text{CaCO}_3\text{ equiv.} = 100 \times \frac{50}{55.5} = 90.09\ \text{g}$$

i.e. 100 g CaCl₂ in water produces the same hardness as 90.09 g of CaCO₃.

### 2.2 EDTA Hardness Formula — Derivation

**Setup.** Molarity $M$ of EDTA, volume $V$ of water sample, volume $V_1$ of EDTA consumed.

**Step 1 — moles of EDTA reacted (1:1 with Ca²⁺/Mg²⁺):**

$$n_{EDTA} = \frac{M V_1}{1000}\ \text{mol}$$

**Step 2 — each mole of EDTA = 1 mol of hardness ions = 1 mol of CaCO₃-equivalent hardness (mass = 100 g/mol).**

$$\text{mass of hardness as CaCO}_3 = \frac{M V_1}{1000} \times 100\ \text{g} = \frac{M V_1}{10}\ \text{g}$$

**Step 3 — convert to mg/L. If $V$ mL of sample was titrated, hardness per litre:**

$$\boxed{\text{Hardness (mg/L or ppm)} = \frac{M \times V_1 \times 100}{V} \times 1000\ \text{mg}}$$

where the final ×1000 converts g → mg and the whole expression already normalizes to 1 L. Equivalently, if the hardness salt mass is known in mg and the sample is $V$ mL:

$$\boxed{\text{Hardness (ppm)} = \frac{\text{mg of CaCO}_3\text{-equivalents} \times 10^6}{V\ (\text{mL}) \times 1000}}$$

**Reference table for the formula:**

| Symbol | Meaning | Unit |
|---|---|---|
| M | Molarity of standard EDTA | mol/L |
| V₁ | Volume of EDTA consumed in titration | mL |
| V | Volume of water sample titrated | mL |
| 100 | Molar mass of CaCO₃ | g/mol |
| 1000 | mL → L conversion | mL/L |

**Total, temporary, permanent link:**

$$\text{Temp. H.} = \text{Total H.} - \text{Perm. H.}$$

### 2.3 Lime-Soda Dosage — Full Derivation

**Step 1 — recognize each impurity consumes a stoichiometric quantity of lime and/or soda:**

| Impurity | Lime Ca(OH)₂ consumed | Soda Na₂CO₃ consumed |
|---|---|---|
| Ca(HCO₃)₂ | 1 mol lime → 2CaCO₃ | — |
| Mg(HCO₃)₂ | 2 mol lime (Mg(OH)₂ + CaCO₃) | — |
| CaSO₄ / CaCl₂ / Ca(NO₃)₂ | — | 1 mol soda |
| MgSO₄ / MgCl₂ / Mg(NO₃)₂ | 1 mol lime (precipitate Mg(OH)₂) | 1 mol soda (removes the Ca²⁺ set free) |
| CO₂ (free) | 1 mol lime | — |
| H⁺ (acidity, e.g. HCl) | 1 mol lime | — |
| FeSO₄ / Al₂(SO₄)₃ etc. | proportionate | proportionate |

**Step 2 — dosage formulas (in terms of mg/L, all converted to CaCO₃ equivalents):**

$$\text{Lime needed} = \frac{74}{100}\Big[ \text{Temp. H.} + 2\,(\text{Mg}^{2+}\text{ as CaCO}_3) + \text{CO}_2 + \text{H}^+\ \text{(acidity)} \Big]$$

$$\text{Soda needed} = \frac{106}{100}\Big[ \text{Perm. H.} + \text{Mg}^{2+}\text{ as CaCO}_3 \Big]$$

where:
- **Temp. H.** = all carbonate hardness (Ca(HCO₃)₂ + Mg(HCO₃)₂), ppm as CaCO₃
- **Perm. H.** = non-carbonate hardness, ppm as CaCO₃
- **Mg²⁺ as CaCO₃** = the part of total hardness contributed by Mg (needed again because Mg consumes soda *after* lime sets Ca²⁺ free)
- Factors $\frac{74}{100}$ and $\frac{106}{100}$ = (mol wt of lime)/(mol wt of CaCO₃) and (mol wt of soda ash)/(mol wt of CaCO₃) — the price of expressing everything in CaCO₃ equivalents.

**Why Mg²⁺ appears twice:** Mg(HCO₃)₂ needs 2 lime (carbonate + the Mg→Mg(OH)₂ step). MgSO₄/MgCl₂ first react with lime to give Mg(OH)₂↓ *and CaSO₄/CaCl₂*, which then requires soda. So every Mg²⁺ costs extra soda over and above its carbonate removal.

**Step 3 — excess reagents in cold process:** commercial lime/soda ~90-95% pure; also a small excess (say 5 ppm each) is intentionally added in the cold process to ensure completion; subtract purity factor: $\text{actual} = \frac{\text{theoretical} \times 100}{\text{purity (\%)}}$.

### 2.4 Zeolite / Permutit Process — Exchange Equations

**Softening (forward):**

$$\mathrm{Ca^{2+} + Na_2Ze \longrightarrow CaZe + 2Na^+}
\qquad
\mathrm{Mg^{2+} + Na_2Ze \longrightarrow MgZe + 2Na^+}$$

**Regeneration with brine (10% NaCl):**

$$\mathrm{CaZe + 2NaCl \longrightarrow Na_2Ze + CaCl_2}
\qquad
\mathrm{MgZe + 2NaCl \longrightarrow Na_2Ze + MgCl_2}$$

**Notes:** removes only Ca/Mg (leaves other salts); outlet hardness ~5-10 ppm; does **not** remove acidic H⁺ or other dissolved salts.

### 2.5 Reverse Osmosis — Osmotic Pressure & the Driving Force

Osmotic pressure:

$$\Pi = i C R T$$

| Symbol | Meaning | Unit |
|---|---|---|
| i | van't Hoff factor (ions per solute formula unit) | — |
| C | molar concentration of solute | mol/m³ |
| R | gas constant (8.314) | J mol⁻¹ K⁻¹ |
| T | absolute temperature | K |

If applied pressure $P > \Pi$ across the semipermeable membrane, solvent flows **against** the osmotic gradient (reverse of normal osmosis) — pure water leaves, salts are retained. Rejection $R_e = 1 - \dfrac{C_p}{C_f}$ where $C_p$, $C_f$ are permeate and feed concentrations.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: CaCO₃ Equivalents of a Mixed Salt Water

**Problem.** A water sample contains 100 ppm CaCl₂ and 90 ppm MgSO₄. Calculate total hardness in ppm as CaCO₃. (Atomic weights: Ca=40, Mg=24, Cl=35.5, S=32, O=16, C=12.)

---

**Solution:**

**Step 1 — molar masses.**
- CaCl₂: 40 + 2(35.5) = **111**; Eq. wt = 111/2 = **55.5**
- MgSO₄: 24 + 32 + 4(16) = **120**; Eq. wt = 120/2 = **60**

**Step 2 — CaCO₃ equivalents.**

$$\text{CaCl}_2 \to 100 \times \frac{50}{55.5} = 90.09\ \text{ppm as CaCO}_3$$

$$\text{MgSO}_4 \to 90 \times \frac{50}{60} = 75.00\ \text{ppm as CaCO}_3$$

**Step 3 — total.**

$$\text{Total hardness} = 90.09 + 75.00 = \boxed{165.09\ \text{ppm (mg/L) as CaCO}_3}$$

---

### Problem 2: Total, Temporary & Permanent Hardness from EDTA Data

**Problem.** 100 mL of a water sample consumed 20 mL of 0.01 M EDTA (wine-red → steel-blue). A second 100 mL sample was boiled, filtered, and the filtrate consumed 12 mL of the same EDTA. Find total, permanent and temporary hardness in ppm.

---

**Solution:**

**Step 1 — total hardness (un-boiled).**

$$\text{Total} = \frac{M \times V_1 \times 100}{V} = \frac{0.01 \times 20 \times 100}{100} = 0.2\ \text{g} = 200\ \text{mg}$$

$$\boxed{\text{Total hardness} = 200\ \text{ppm as CaCO}_3}$$

**Step 2 — permanent hardness (filtrate of boiled sample).**

$$\text{Permanent} = \frac{0.01 \times 12 \times 100}{100} = 0.12\ \text{g} = 120\ \text{mg}$$

$$\boxed{\text{Permanent hardness} = 120\ \text{ppm as CaCO}_3}$$

**Step 3 — temporary hardness.**

$$\text{Temporary} = 200 - 120 = \boxed{80\ \text{ppm as CaCO}_3}$$

---

### Problem 3: Lime-Soda Dosage Calculation

**Problem.** A water has the following analysis (all ppm as CaCO₃): Ca(HCO₃)₂ = 120, Mg(HCO₃)₂ = 40, CaSO₄ = 80, MgSO₄ = 60, free CO₂ = 22, and HCl (acidity) = 36.5. Calculate the lime (Ca(OH)₂) and soda (Na₂CO₃) required in mg/L for complete softening.

---

**Solution:**

**Step 1 — tabulate impurities and their demands (all in CaCO₃ equivalents).**

| Impurity | ppm (as CaCO₃) | Lime units | Soda units |
|---|---|---|---|
| Ca(HCO₃)₂ | 120 | 1 | 0 |
| Mg(HCO₃)₂ | 40 | 2 | 0 |
| CaSO₄ | 80 | 0 | 1 |
| MgSO₄ | 60 | 1 | 1 |
| CO₂ | 22 | 1 | 0 |
| HCl acidity | 36.5 | 1 | 0 |

**Step 2 — total lime units (as CaCO₃).**

$$\text{Lime units} = 120 + 2(40) + 60 + 22 + 36.5 = 318.5$$

**Step 3 — total soda units (as CaCO₃).**

$$\text{Soda units} = 80 + 60 = 140$$

**Step 4 — convert to actual reagent mass.**

$$\text{Lime} = 318.5 \times \frac{74}{100} = 235.69\ \text{mg/L}$$

$$\text{Soda} = 140 \times \frac{106}{100} = 148.4\ \text{mg/L}$$

**Step 5 — state answers.**

$$\boxed{\text{Lime Ca(OH)}_2 = 235.69\ \text{mg/L}} \qquad
\boxed{\text{Soda Na}_2\text{CO}_3 = 148.4\ \text{mg/L}}$$

---

### Problem 4: Unit Conversion — Clarke to ppm, and Zeolite Regeneration

**Problem (a).** A sample has 5°Cl hardness. Express in ppm (1 °Cl = 14.25 ppm).
**Problem (b).** A zeolite softener (CaNa₂Ze form) processes water containing 300 ppm (as CaCO₃) hardness at a flow of 5000 L/day. After 5 days, the bed is regenerated with 10% NaCl. Estimate the minimum NaCl required per regeneration cycle (NaCl: 58.5 g/mol; assume 100% regeneration efficiency).

---

**Solution (a):**

$$\text{ppm} = 5 \times 14.25 = \boxed{71.25\ \text{ppm}}$$

**Solution (b):**

**Step 1 — total hardness removed.**

$$\text{Hardness} = 300\ \text{ppm} = 300\ \text{mg/L} = 0.3\ \text{g/L}$$

$$\text{Total removed} = 0.3\ \text{g/L} \times 5000\ \text{L/day} \times 5\ \text{days} = 7500\ \text{g as CaCO}_3$$

**Step 2 — convert to moles of CaCO₃ equivalents (Mw = 100).**

$$n = \frac{7500}{100} = 75\ \text{mol}$$

**Step 3 — regeneration chemistry.** Each equivalent of hardness (1 mol Ca²⁺) replaces 2 Na⁺; each mole of NaCl supplies 1 Na⁺:

$$\mathrm{CaZe + 2NaCl \longrightarrow Na_2Ze + CaCl_2}$$

$$\text{NaCl needed} = 2 \times 75 = 150\ \text{mol}$$

**Step 4 — mass.**

$$\text{NaCl} = 150 \times 58.5 = \boxed{8775\ \text{g} = 8.775\ \text{kg NaCl per cycle}}$$

---

### Problem 5: Boiler Feed Water — Blow-Down / Scale Prevention Numeric

**Problem.** Boiler water contains 450 ppm of hardness salts. Continuous blow-down keeps dissolved solids ≤ 3000 ppm. If feed make-up is 1000 L/day, estimate the blow-down rate (assume perfect mixing, feed solids = make-up solids).

---

**Solution:**

**Step 1 — mass-balance principle.** Blow-down concentrates dissolved solids until the concentration equals the blow-down concentration limit. At steady state:

$$\text{Feed rate} \times C_{feed} = \text{Blow-down rate} \times C_{max}$$

**Step 2 — substitute.**

$$1000 \times 450 = Q_{bd} \times 3000$$

$$Q_{bd} = \frac{450000}{3000} = 150\ \text{L/day}$$

**Step 3 — answer.**

$$\boxed{\text{Blow-down rate} = 150\ \text{L/day} \ (=15\%\ \text{of make-up})}$$

---

## 4. ENGINEERING APPLICATIONS MAP

| Principle | Industrial / Field Application |
|---|---|
| **CaCO₃-equivalent hardness measurement** | Universal specification of feed water for boilers, cooling towers, laundries, textile dyeing and paper mills — one common unit across suppliers |
| **Lime-Soda process** | Municipal water softening plants, medium-pressure industrial boiler plants (large volume, cheap reagents) |
| **Zeolite / Permutit process** | Domestic water softeners, laundries, dye-houses, hospitals — convenient continuous operation with brine regeneration |
| **Ion-exchange demineralization** | Nuclear power stations, thermal power boilers, pharmaceutical/electronics ultrapure water (conductivity < 1 µS/cm) |
| **Reverse Osmosis** | Desalination plants (e.g. Arabian Gulf SWRO), brackish water treatment, ultrapure water pre-treatment, beverage industry, wastewater reclamation |
| **EDTA complexometric titration** | Standard lab method (APHA/ASTM) for hardness in drinking water, cooling water, boiler feed and effluent compliance monitoring |
| **Scale/sludge control & blow-down** | Preventing boiler tube failure, fuel waste and downtime in thermal power plants |
| **Oxygen scavenging (Na₂SO₃) & deaeration** | Corrosion control of boiler tubes, pre-heaters and condensate return lines |
| **Caustic embrittlement inhibitors** | Phosphate / sulphate ratio control in riveted & welded high-pressure boiler drums |
| **Priming/foaming control** | Anti-foam additives and blow-down scheduling in steam turbines and process steam plants |

---

## APPENDIX: Formula & Data Quick Reference

| Quantity | Formula | Notes |
|---|---|---|
| CaCO₃ equivalent | mass × 50 / (Eq. wt of salt) | Eq. wt = M / valency |
| EDTA total hardness | $M \times V_1 \times 100 / V$ | g/L scale; ×1000 for mg/L |
| Unit conversions | 1 °Cl = 14.25 ppm · 1 °Fr = 10 ppm · 1 °dH = 17.9 ppm | ppm = mg/L |
| Lime dosage | $\frac{74}{100}\,[\text{Temp} + 2\text{Mg} + \text{CO}_2 + \text{acidity}]$ | all in CaCO₃ equiv |
| Soda dosage | $\frac{106}{100}\,[\text{Perm} + \text{Mg}]$ | all in CaCO₃ equiv |
| Osmotic pressure | $\Pi = iCRT$ | RO needs P > Π |
| Boiling removal | $\mathrm{Ca(HCO_3)_2 \to CaCO_3 + H_2O + CO_2}$ | removes temp. hardness only |

## CROSS-REFERENCES

- Related modules: [[module-2-surfactants-interfaces-colloids]] · [[module-3-electrochemistry-corrosion]] · [[chemistry/formula-sheet-physical]] · [[engineering-physics/module-4-semiconductors-electromagnetism]]
