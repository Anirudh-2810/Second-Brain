---
module: "engineering-chem"
topic: "Module 5: Engineering Materials, Polymers & Fuels — Thermoplastics, Elastomers, Conducting Polymers, Calorific Value & Coal Analysis"
tags: [engineering-chemistry, polymers, thermoplastics, thermosets, elastomers, vulcanization, conducting-polymers, polyaniline, fuels, calorific-value, gross-calorific-value, net-calorific-value, dulong-formula, bomb-calorimeter, proximate-analysis, ultimate-analysis, coal]
last_updated: "2026-08-19"
prerequisites: ["Addition & Condensation Polymerization", "Thermochemistry (Enthalpy of Combustion)", "Stoichiometry", "Hess's Law"]
---

# Module 5: Engineering Materials, Polymers & Fuels

> The materials-and-energy capstone of engineering chemistry: polymer architecture (thermoplastics vs. thermosets, elastomers, vulcanization, conducting polymers), then the combustion engine of industry — calorific value (gross vs. net), Dulong's formula, bomb calorimetry with full calculations, and proximate/ultimate analysis of coal.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Mathematical Formulation & Explicit Derivations](#2-mathematical-formulation--explicit-derivations)
3. [High-Yield Exam Problems & Worked Solutions](#3-high-yield-exam-problems--worked-solutions)
4. [Engineering Applications Map](#4-engineering-applications-map)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.1 Polymer Classification — Master Decision Tree

```
                        POLYMERS
                           │
        ┌──────────────────┼───────────────────────┐
        ▼                  ▼                       ▼
  HOMOPOLYMER         COPOLYMER             BY THERMAL BEHAVIOUR
  (one monomer)       (two+ monomers)            │
        │                  │              ┌──────┴─────────┐
        ▼                  ▼              ▼                ▼
   e.g. PE, PVC,      random,           THERMO-          THERMOSETS
   PS, PP, PMMA       alternating,      PLASTICS         (irreversible
                      block, graft      (reversible      cure on heating)
                       e.g. ABS,        melt/reshape)
                       Buna-S, SBR            │                │
                                             │                ▼
   e.g. PE, PP, PVC, PS, nylon, PET     linear or lightly   heavily cross-linked
   — soften on heating, recyclable      branched chains;    network: bakelite,
   — 3-D mouldable by melt processing   no cross-links      melamine-formaldehyde,
                                        3-D network         epoxy, urea-formaldehyde
   │                                                  │
   └──────────── BY CHAIN SHAPE: linear │ branched │ cross-linked │ network (3-D)
```

### 1.2 Thermoplastics vs. Thermosets — Comparison Table

| Property | Thermoplastics | Thermosets |
|---|---|---|
| **Structure** | Linear / lightly branched, no cross-links | 3-D cross-linked network |
| **Heating effect** | Softens → melts → remouldable (reversible) | Cures irreversibly; hardens, cannot re-melt |
| **Cooling effect** | Resolidifies retaining shape | Remains rigid |
| **Recyclability** | Recyclable (re-melt) | Not recyclable (decompose) |
| **Solubility** | Soluble in suitable solvents | Insoluble, swell |
| **Mechanical strength** | Lower | Higher, stiffer |
| **Examples** | PE, PP, PVC, PS, PMMA, PTFE, nylon, PET | Bakelite (phenol-formaldehyde), urea-formaldehyde, melamine, epoxy, polyester resin |

### 1.3 Elastomers & Vulcanization — Chemistry Flowchart

```
   NATURAL RUBBER = cis-polyisoprene  (CH₂–C(CH₃)=CH–CH₂)ₙ
   - soft, tacky, thermoplastic-like, low strength
   - long coiled chains slide past each other → elastic when stretched
     (chains uncoil) then return (recoil) — but weak without cross-links
        │
        ▼
   VULCANIZATION (Goodyear): heat rubber + S (2-8%) + accelerators
        │
        ▼
   SULPHUR BRIDGES (–Sx–) join chains into a light 3-D network
        │
   ┌─────┴──────────────────────────────────────────┐
   ▼                                               ▼
   ELASTOMER properties                           OVER-VULCANIZED = hard
   - chains can't slide past each other          ebonite (more S, e.g. 30%)
   - can still stretch & recoil elastically      rigid, brittle
   - high tensile strength, wear & solvent        (hard rubber)
     resistance, shape recovery
   Vulcanization temp ~140-160 °C; time 10-30 min
```

**Key facts:** vulcanization introduces cross-links between polyisoprene chains via S bridges; it converts the thermoplastic rubber into a thermoset-like elastomer. Natural rubber has a glass transition Tg ≈ −70 °C (stays rubbery at room temperature).

### 1.4 Conducting Polymers — From Insulators to Conductors

```
   CONJUGATED POLYMER (π-electrons delocalized along backbone)
   e.g. polyacetylene (CH=CH)ₙ, polyaniline (PANI), polypyrrole,
        polythiophene, PEDOT:PSS
        │
        │  inherently an insulator? YES (band gap, few free carriers)
        ▼
   DOPING (oxidation or reduction — NOT like Si doping)
        │
   p-doping: remove e⁻ (oxidize)   n-doping: add e⁻ (reduce)
        │                                │
        ▼                                ▼
   creates charge carriers (polarons/bipolarons/solitons)
   conductivity jumps up to 10¹⁰ × (semiconductor → metallic range)

   POLYANILINE (PANI): forms depend on oxidation state:
   leucoemeraldine (fully reduced, insulator) → emeraldine salt
   (doped, conducting, green) → pernigraniline (fully oxidized)
   Emeraldine salt is the conducting form — used in sensors,
   anti-static coatings, corrosion protection, flexible electronics
```

### 1.5 Fuels & Combustion — Calorific Value Flowchart

```
                    FUEL
                      │
       ┌──────────────┼──────────────────┐
       ▼              ▼                  ▼
   SOLID           LIQUID              GASEOUS
   coal, coke     petrol, diesel,      CNG, LPG, H₂
   wood           kerosene, HFO
                      │
                      ▼
   COMBUSTION: Fuel + O₂ → CO₂ + H₂O + heat
                      │
       ┌──────────────┴──────────────┐
       ▼                             ▼
   GROSS CALORIFIC VALUE (HCV)    NET CALORIFIC VALUE (LCV)
   — total heat, water vapour       — heat available after
     condensed to liquid (ΔH latent of vapourisation of the
     of H₂O given back)            H₂O formed is lost to flue)
       │                             │
       ▼                             ▼
   Measured in Bomb Calorimeter   LCV = HCV − 0.09 H × 587
   (constant volume, solid &       (H = % hydrogen in fuel;
    liquid fuels)                  587 cal/g = latent heat of steam)
```

### 1.6 Proximate vs. Ultimate Analysis — Comparison Table

| Analysis | Determines | Standard components | Purpose |
|---|---|---|---|
| **Proximate** | Practical behaviour, % by weight | Moisture, Volatile matter, Ash, Fixed carbon | Grading, storage, furnace design, combustion behaviour |
| **Ultimate** | Elemental composition, % by weight | C, H, N, S, O (by difference), Ash | Design of flue gas system, calorific value (Dulong), air requirement |

**Proximate details:** Moisture (loss on heating 105-110 °C), Volatile matter (loss on heating 950 °C, no air, 7 min), Ash (residue on combustion in air 700-750 °C), Fixed carbon = 100 − (Moisture + VM + Ash).

**Ultimate details:** C and H by absorption of CO₂/H₂O after combustion; S by absorption of SO₂; N by Kjeldahl; O by difference = 100 − (C+H+N+S+Ash).

---

## 2. MATHEMATICAL FORMULATION & EXPLICIT DERIVATIONS

### 2.1 Gross (HCV) vs. Net (LCV) Calorific Value — Derivation

**Step 1 — combustion of a hydrocarbon fuel releases water.**

$$\mathrm{C}_x\mathrm{H}_y + \left(x + \frac{y}{4}\right)\mathrm{O}_2 \longrightarrow x\mathrm{CO}_2 + \frac{y}{2}\mathrm{H}_2\mathrm{O}$$

**Step 2 — Gross CV** assumes all water condenses and gives up its latent heat. In a **bomb calorimeter** the measurement is at constant volume; the water of combustion is liquid.

**Step 3 — Net CV** assumes water leaves as steam (as in industrial furnaces and engines), so the latent heat of the water vapour is unavailable:

$$LCV = HCV - (\text{latent heat of water formed})$$

**Step 4 — express per gram of fuel.** If the fuel has H% hydrogen, mass of water formed per gram of fuel:

$$\text{mass H}_2\mathrm{O} = \frac{9H}{100}\ \text{g}$$

(latent heat of steam = 587 cal/g or 2454 kJ/kg):

$$\boxed{LCV = HCV - \frac{9H}{100} \times 587 \quad (\text{cal/g})}$$

$$\boxed{LCV = HCV - 0.09\,H \times 587 \quad \text{or} \quad LCV = HCV - \frac{9H}{100} \times 2454 \quad (\text{kJ/kg})}$$

| Symbol | Meaning | Unit |
|---|---|---|
| HCV | gross (higher) calorific value | cal/g or kJ/kg |
| LCV | net (lower) calorific value | cal/g or kJ/kg |
| H | hydrogen content of fuel | % (mass) |
| 9H/100 | mass of water per unit mass of fuel (each H₂O = 2H + 16O → 9×H mass) | g/g |
| 587 | latent heat of steam | cal/g |
| 2454 | latent heat of steam | kJ/kg |

### 2.2 Dulong's Formula — Estimation of Calorific Value

**Step 1 — empirical relation based on elemental analysis:**

$$\boxed{CV = \frac{1}{100}\Big( 8080\,C + 34500\Big(H - \frac{O}{8}\Big) + 2240\,S \Big) \quad (\text{kcal/kg})}$$

| Symbol | Meaning | Unit |
|---|---|---|
| C, H, O, S | % carbon, hydrogen, oxygen, sulphur in fuel | % |
| 8080 | heat of combustion of carbon → CO₂ | kcal/kg per % |
| 34500 | heat of combustion of hydrogen → liquid water | kcal/kg per % |
| (H − O/8) | "effective hydrogen": oxygen already present in the fuel is assumed combined with hydrogen as water (each 8 g O fixes 1 g H) | % |
| 2240 | heat of combustion of sulphur → SO₂ | kcal/kg per % |

**Step 2 — why subtract O/8.** The fuel's own oxygen is assumed pre-combined with hydrogen as H₂O, which cannot burn. Since 1 g O combines with 1/8 g H, the available combustible hydrogen is H − O/8.

### 2.3 Bomb Calorimeter — Complete Derivation of the Calculation

**Setup:** m g of fuel burnt in a bomb immersed in W g of water; water equivalent of calorimeter = w g; temperature rise = ΔT = (t₂ − t₁) (corrected for radiation/fuse wire by cooling correction).

**Step 1 — heat balance.** Heat liberated by fuel = heat absorbed by water + heat absorbed by calorimeter + accessories:

$$HCV \times m = (W + w)\, \Delta T \times s$$

**Step 2 — specific heat of water s = 1 cal/g °C:**

$$\boxed{HCV = \frac{(W + w)\, \Delta T \times 1}{m} \quad (\text{cal/g})}$$

**Step 3 — corrections.**
- **Fuse wire correction:** heat from burning fuse wire is subtracted: $HCV = \dfrac{(W+w)\Delta T - (\text{fuse heat})}{m}$.
- **Cooling/radiation correction:** experimentally determined rate of cooling × time, added to ΔT.
- **Acid correction:** sulphur/nitrogen produce H₂SO₄/HNO₃; their formation heat is exothermic — subtract (e.g., 2.85 cal per mg S as H₂SO₄, ~1 cal per 0.1 mg HNO₃). Acids also form from N₂ — subtracted.

**Step 4 — kJ/kg conversion:** 1 cal/g = 4.184 kJ/kg → multiply by 4.184 (or by 1000 for cal → kcal, then by 4.184).

### 2.4 Air Requirement for Combustion — Stoichiometry

For complete combustion of 1 kg of fuel:

$$\mathrm{O}_2 \text{ required (kg)} = \frac{8}{3}C + 8\Big(H - \frac{O}{8}\Big) + S$$

$$\text{Air required (kg)} = \mathrm{O}_2 \text{ required} \times \frac{100}{23} \quad (\text{since air ≈ 23% O}_2 \text{ by mass})$$

| Symbol | Meaning | Unit |
|---|---|---|
| C, H, O, S | % of element in fuel | % |
| 8/3 | O₂ per unit C (CO₂: 32/12) | kg O₂/kg C |
| 8 | O₂ per unit H (H₂O: 32/4) | kg O₂/kg H |
| S | O₂ per unit S (SO₂: 32/32) | kg O₂/kg S |
| 100/23 | mass of air per unit O₂ | — |

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: Bomb Calorimeter — HCV & LCV

**Problem.** 0.5 g of a fuel was burnt in a bomb calorimeter with water equivalent 500 g. The water temperature rose from 25.0 °C to 27.0 °C. Fuse wire correction = 12 cal. Calculate (a) HCV and (b) LCV if the fuel contains 6% hydrogen. (Latent heat of steam = 587 cal/g.)

---

**Solution:**

**Step 1 — observed temperature rise.**

$$\Delta T = 27.0 - 25.0 = 2.0\ ^\circ\text{C}$$

**Step 2 — heat balance (total water equivalent W + w = 500 g, s = 1).**

$$\text{Heat released} = (W + w)\Delta T = 500 \times 2.0 = 1000\ \text{cal}$$

**Step 3 — subtract fuse correction.**

$$\text{Net heat from fuel} = 1000 - 12 = 988\ \text{cal}$$

**Step 4 — HCV.**

$$HCV = \frac{988}{0.5} = 1976\ \text{cal/g} = 1976 \times 4.184 = 8268\ \text{kJ/kg}$$

**Step 5 — LCV (H = 6%).**

$$LCV = HCV - \frac{9H}{100} \times 587 = 1976 - \frac{9 \times 6}{100} \times 587 = 1976 - 317$$

$$LCV = 1659\ \text{cal/g} = 1659 \times 4.184 = 6941\ \text{kJ/kg}$$

**Step 6 — answers.**

$$\boxed{HCV = 1976\ \text{cal/g}\ (8268\ \text{kJ/kg})} \qquad
\boxed{LCV = 1659\ \text{cal/g}\ (6941\ \text{kJ/kg})}$$

---

### Problem 2: Dulong's Formula

**Problem.** A coal sample has ultimate analysis: C = 78%, H = 5%, O = 8%, S = 2%, N = 2%, Ash = 5%. Estimate its calorific value by Dulong's formula.

---

**Solution:**

**Step 1 — apply Dulong.**

$$CV = \frac{1}{100}\Big(8080\,C + 34500\Big(H - \frac{O}{8}\Big) + 2240\,S\Big)$$

**Step 2 — effective hydrogen.**

$$H - \frac{O}{8} = 5 - \frac{8}{8} = 5 - 1 = 4$$

**Step 3 — substitute.**

$$CV = \frac{1}{100}\Big(8080 \times 78 + 34500 \times 4 + 2240 \times 2\Big)$$

$$= \frac{1}{100}\Big(630240 + 138000 + 4480\Big)$$

$$= \frac{1}{100}(772720) = 7727.2\ \text{kcal/kg}$$

**Step 4 — answer.**

$$\boxed{CV \approx 7727\ \text{kcal/kg}}$$

---

### Problem 3: Proximate Analysis — Fixed Carbon by Difference

**Problem.** A coal on proximate analysis gives: Moisture 2.0%, Volatile matter 28.0%, Ash 15.0%. Compute (a) fixed carbon and (b) if this coal's HCV measured is 7200 kcal/kg, comment on quality vs. a coal with 45% volatile matter.

---

**Solution:**

**Step 1 — fixed carbon.**

$$\text{Fixed carbon} = 100 - (M + VM + Ash) = 100 - (2.0 + 28.0 + 15.0) = 55.0\%$$

$$\boxed{\text{Fixed carbon} = 55.0\%}$$

**Step 2 — quality comment.**

$$\boxed{\text{Higher volatile matter (45\%) } \Rightarrow \text{ easier ignition, more smoke/gas, often lower fixed carbon}}$$

Coals are graded largely by fixed carbon and ash; a 55% FC coal is a fair-quality steam coal.

---

### Problem 4: Air Requirement for Combustion

**Problem.** Using the coal of Problem 2 (C 78%, H 5%, O 8%, S 2%), calculate the minimum air required per kg of coal burnt.

---

**Solution:**

**Step 1 — oxygen requirement.**

$$O_2 = \frac{8}{3}C + 8\Big(H - \frac{O}{8}\Big) + S = \frac{8}{3}(78) + 8(5 - 1) + 2$$

$$= 208 + 32 + 2 = 242\ \text{parts O}_2 \text{ per 100 parts coal}$$

**Step 2 — per kg of coal.**

$$O_2 = 2.42\ \text{kg O}_2/\text{kg coal}$$

**Step 3 — air (air ≈ 23% O₂ by mass).**

$$\text{Air} = 2.42 \times \frac{100}{23} = 10.52\ \text{kg air/kg coal}$$

**Step 4 — answer.**

$$\boxed{\text{Air required} \approx 10.5\ \text{kg per kg coal (minimum, no excess)}}$$

---

### Problem 5: Hydrogen Content from HCV and LCV

**Problem.** The HCV of a fuel is 9500 kcal/kg and LCV is 8650 kcal/kg. Estimate the hydrogen percentage. (Latent heat = 587 cal/g.)

---

**Solution:**

**Step 1 — difference between HCV and LCV is the latent heat of water formed.**

$$HCV - LCV = 9500 - 8650 = 850\ \text{kcal/kg}$$

**Step 2 — per gram fuel:**

$$\frac{9H}{100} \times 587 = 0.85\ \text{kcal/g} = 850\ \text{cal/g}$$

**Step 3 — solve for H.**

$$\frac{9H}{100} = \frac{850}{587} = 1.448$$

$$H = \frac{1.448 \times 100}{9} = 16.09\%$$

**Step 4 — answer.**

$$\boxed{\text{Hydrogen content} \approx 16.1\%}$$

---

## 4. ENGINEERING APPLICATIONS MAP

| Principle | Industrial / Field Application |
|---|---|
| **Thermoplastics (PE, PP, PVC, PET, PS)** | Packaging, pipes, cable insulation, automotive interiors, bottles, household goods — fully recyclable melt-processing |
| **Thermosets (bakelite, epoxy, melamine)** | Switchgear & electrical insulators, adhesives, composites (GFRE), laminates, brake pads, encapsulation of electronics |
| **Elastomers & vulcanization** | Tyres, seals, gaskets, conveyor belts, hoses, shoe soles, vibration mounts — cross-linked for strength & durability |
| **Conducting polymers (PANI, PEDOT:PSS)** | Anti-static coatings, EMI shielding, OLEDs & flexible displays, organic solar cells, gas/chemical sensors, biosensors, corrosion-protection coatings |
| **Polymer composites** | Aerospace/automotive structural panels (carbon-fibre epoxy), wind-turbine blades, sports equipment |
| **Calorific value & bomb calorimetry** | Fuel grading & pricing in power stations, boiler efficiency audits, coal trading contracts, food calorimetry |
| **Proximate & ultimate analysis** | Coal classification (lignite→bituminous→anthracite), furnace & stoker design, flue-gas & ESP sizing, blending strategy |
| **Dulong / air-requirement calc** | Combustion engineering: air/fuel ratio control, excess-air tuning, boiler thermal efficiency, CO₂ monitoring |
| **LCV/HCV distinction** | Condensing boilers recover latent heat (approach HCV); gas turbines & IC engines operate on LCV basis |
| **Vulcanization & rubber chemistry** | Automotive tyre manufacture, industrial rubber goods — the single largest elastomer market |

---

## APPENDIX: Formula & Data Quick Reference

| Quantity | Formula | Notes |
|---|---|---|
| Net calorific value | $LCV = HCV - 0.09H \times 587$ (cal/g) | 2454 kJ/kg form |
| Dulong (kcal/kg) | $CV = \frac{8080C + 34500(H - O/8) + 2240S}{100}$ | effective H = H − O/8 |
| Bomb calorimeter | $HCV = \frac{(W + w)\Delta T}{m}$ (cal/g) | minus fuse/acid corrections |
| Conversions | 1 cal = 4.184 J · 1 kcal = 1000 cal | — |
| Oxygen required | $\frac{8}{3}C + 8(H - O/8) + S$ | kg per unit fuel |
| Air required | O₂ × 100/23 | air ≈ 23% O₂ mass |
| Water from H | 9H/100 g per g fuel | 9 = (2+16)/2 |
| Fixed carbon | 100 − (M + VM + Ash) | proximate |

## CROSS-REFERENCES

- Related modules: [[module-4-spectroscopy-instrumental]] (IR for polymer functional groups) · [[module-3-electrochemistry-corrosion]] (conducting polymers in corrosion protection) · [[chemistry/formula-sheet-organic]] (polymers: addition/condensation) · [[chemistry/formula-sheet-physical]] (thermochemistry) · [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics]] (OLED/photovoltaic materials)
