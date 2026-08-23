---
module: "engineering-chem"
topic: "Module 3: Electrochemistry & Corrosion Engineering — Nernst, Reference Electrodes, Conductometry & Corrosion Protection"
tags: [engineering-chemistry, electrochemistry, nernst-equation, reference-electrodes, calomel, glass-electrode, conductometric-titration, corrosion, galvanic-series, pitting-corrosion, cathodic-protection, sacrificial-anode, electroplating, galvanization]
last_updated: "2026-08-19"
prerequisites: ["Redox Reactions", "Gibbs Free Energy", "Ionic Equilibrium", "Faraday's Laws"]
---

# Module 3: Electrochemistry & Corrosion Engineering

> The electrochemical engine of engineering chemistry: predicting cell voltages with the Nernst equation, building reference electrodes (calomel, glass), reading conductometric titration curves, understanding why metals corrode (dry vs. wet, galvanic series, differential aeration, pitting), and the four industrial shields — sacrificial anodes, impressed current, electroplating and galvanization.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Mathematical Formulation & Explicit Derivations](#2-mathematical-formulation--explicit-derivations)
3. [High-Yield Exam Problems & Worked Solutions](#3-high-yield-exam-problems--worked-solutions)
4. [Engineering Applications Map](#4-engineering-applications-map)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.1 The Electrochemical Cell — Architecture

```
   ┌─────────────┐   SALT BRIDGE (KCl/agar, maintains neutrality)   ┌─────────────┐
   │  ANODE      │ ◄══════════════════════════════════════════════► │  CATHODE    │
   │ (oxidation) │   external circuit: e⁻ flow (voltmeter/load)    │ (reduction) │
   └──────┬──────┘                                                 └──────┬──────┘
          │                                                                  │
     Zn ⟶ Zn²⁺ + 2e⁻                                              Cu²⁺ + 2e⁻ ⟶ Cu
     (metal loses mass)                                            (metal gains mass)
          │                                                                  │
     1 M Zn²⁺                                                        1 M Cu²⁺
   ─────────────────────────────────────────────────────────────────────────────
   Cell notation (IUPAC): Zn | Zn²⁺(a=1) ∥ Cu²⁺(a=1) | Cu
   Anode (LHS) written as oxidation; cathode (RHS) as reduction.
   E°cell = E°cathode(RP) − E°anode(RP) = +0.34 − (−0.76) = +1.10 V
```

**Golden rules:**
- Oxidation happens at the **anode** (electron donor, − terminal in a galvanic cell).
- Reduction happens at the **cathode** (electron acceptor, + terminal).
- Salt bridge maintains charge balance; electrons flow anode → cathode in the external wire.
- $E^\circ_{cell} > 0$ → spontaneous (ΔG < 0). $E^\circ_{cell} < 0$ → non-spontaneous (needs external voltage = electrolytic cell).

### 1.2 Reference Electrodes — Comparison Table

| Electrode | Construction | Half-reaction | Potential (25 °C) | Use |
|---|---|---|---|---|
| **Standard Hydrogen Electrode (SHE)** | Pt|H₂(1 atm)|H⁺(a=1) | $2\mathrm{H^+} + 2e^- \rightleftharpoons \mathrm{H_2}$ | 0.000 V (by definition) | Primary standard |
| **Calomel (SCE)** | Hg|Hg₂Cl₂(s)|KCl(sat) | $\mathrm{Hg_2Cl_2 + 2e^- \rightleftharpoons 2Hg + 2Cl^-}$ | +0.242 V (sat. KCl) | Most common lab reference |
| **Silver/Silver Chloride** | Ag|AgCl(s)|KCl | $\mathrm{AgCl + e^- \rightleftharpoons Ag + Cl^-}$ | +0.222 V (sat. KCl) | Portable, rugged |
| **Glass electrode** | Ag|AgCl|HCl|glass membrane|H⁺ | membrane potential ∝ pH | pH-dependent (not fixed) | pH meter |

### 1.3 Glass Electrode & pH Measurement — Flowchart

```
      GLASS ELECTRODE                       CALOMEL (reference)
   ┌──────────────────────┐              ┌─────────────────────┐
   │ internal ref Ag/AgCl │              │ Hg | Hg₂Cl₂ | KCl   │
   │ in dilute HCl (pH~7) │              │ +0.242 V constant   │
   │ thin glass membrane  │              │                     │
   └──────────┬───────────┘              └──────────┬──────────┘
              │   membrane potential                 │
              │   E = k + (2.303RT/F)·pH             │
              └──────────────┬───────────────────────┘
                             ▼
              Combined cell: E_cell = E_calomel − E_glass
              pH = (E_cell − K) / (0.0591)   at 25 °C
```

**Why glass works:** the membrane binds H⁺ selectively; an asymmetric "boundary potential" develops across it proportional to the difference in pH between internal buffer and test solution.

### 1.4 Conductometric Titration — Curve Shapes

```
   STRONG ACID vs STRONG BASE            WEAK ACID vs STRONG BASE
   (HCl + NaOH)                         (CH₃COOH + NaOH)
   conductivity                          conductivity
     |\                                   |\
     | \________                          | \_____________
     |  \       /\
     |   \     /  \      H⁺ OH⁻ (mobile) |  \           /\
     |    \   /    \                     |   \         /  \
     |     \_/______\___  OH⁻ excess     |    \_______/____\___
     +──────────────── C              +──────────────── C
       Veq = equivalence point          Veq (weak acid: high initial,
     (min. of V)                        slow fall — CH₃COOH barely
     symmetric V-shape                  dissociates; then buffering;
                                        sharp rise after Veq)
```

| Curve | Initial conductivity | At equivalence | After equivalence |
|---|---|---|---|
| **Strong acid + strong base** | High (H⁺ mobile, λ°=349.8) | Minimum (only salt Na⁺Cl⁻) | Rises (OH⁻ λ°=198.5) |
| **Weak acid + strong base** | Low (CH₃COOH weakly dissociated) | Flat/minor (salt + undissociated acid buffering) | Rises sharply (excess OH⁻) |

**Key rule:** conductivity is carried chiefly by the **highly mobile H⁺ and OH⁻** ions; salt ions are much slower. Hence minima/turning points mark the equivalence volume without needing an indicator.

### 1.5 Corrosion — Dry vs. Wet — Decision Tree

```
   METAL EXPOSED TO ENVIRONMENT
        │
        ├─────────────────────────────┬───────────────────────────────┐
        ▼                             ▼                               ▼
   DRY / CHEMICAL CORROSION      WET / ELECTROCHEMICAL          OTHER (stray
   (no moisture/electrolyte)     (moisture + electrolyte)       currents, bio)
        │                             │
        ▼                             ▼
   Direct oxidation by gases:     Galvanic cell is formed:
   e.g. 3Fe + 2O₂ → Fe₃O₄          anode (oxidizes, corrodes)
   2Fe + 3Cl₂ → 2FeCl₃            cathode (reduction: O₂ or H⁺)
   Oxide film thickens with time   Requires: anode, cathode,
   (no e⁻ flow in solution)        electrolyte, metallic contact
        │                             │
        ▼                             ▼
   Found: hot gases, acid          Types:
   vapours, Cl₂, SO₂               • Galvanic corrosion (dissimilar
   atmospheres                     metals joined) — galvanic series
                                   • Differential aeration (O₂-poor
                                   anode region, e.g. waterline)
                                   • Pitting (localized, Cl⁻ attack)
                                   • Stress corrosion, intergranular
```

### 1.6 Galvanic Series — Ordering & Prediction

Metals are ranked by their corrosion tendency in **seawater**. A metal lower in the list (more noble) is protected; the higher one (less noble/active) corrodes when the pair is coupled.

**Partial galvanic series (most active → most noble):** Mg → Zn → Al → Cd → Steel/Fe → Pb → Sn → Ni → Cu → Ag → Pt → Au

**Rule:** When two metals are in electrical contact in an electrolyte, the **more active (higher on the list) metal is the anode and corrodes**; the more noble metal is cathodically protected.

### 1.7 Corrosion Protection — Master Flowchart

```
        METAL TO BE PROTECTED
              │
   ┌──────────┼───────────────────────────────┐
   ▼          ▼                               ▼
CATHODIC      ANODIC/COATING              DESIGN / MEDIA
PROTECTION    (barrier)                   CONTROL
   │          │                               │
   ├──────────┼───────────────┐               ├──────────┐
   ▼          ▼               ▼               ▼          ▼
SACRIFICIAL  IMPRESSED    GALVANIZATION   ELECTRO-    MEDIA
ANODE        CURRENT       (Zn coating)   PLATING     CONTROL
Mg/Zn/Al     (rectifier,                  (Cr, Ni,    (inhibitors,
more active  inert anode                  Cd, Cu      deaeration,
than metal)  Ti/Pb/graphite               plating)    paint, anodize,
    │             │                               │     sacrificial Zn
    ▼             ▼                               ▼     bars in tanks
attached to  negative DC forced                sacrificial /
metal; it    onto metal → metal                barrier
corrodes;    becomes cathode,                  coating
metal is     cannot corrode
cathode      (used for large
             buried/offshore
             structures)
```

---

## 2. MATHEMATICAL FORMULATION & EXPLICIT DERIVATIONS

### 2.1 The Nernst Equation — Full Derivation

**Step 1 — connect cell potential to free energy.** For a general redox reaction with $n$ electrons transferred:

$$\Delta G = -n F E \qquad\text{and}\qquad \Delta G^{\circ} = -n F E^{\circ}$$

| Symbol | Meaning | Unit |
|---|---|---|
| n | number of electrons transferred in the balanced cell reaction | — |
| F | Faraday constant (96,485) | C/mol e⁻ |
| E | cell potential under non-standard conditions | V |
| E° | standard cell potential (1 M, 1 atm, 25 °C) | V |

**Step 2 — thermodynamics of a chemical reaction.** The free energy of a reaction as a function of the reaction quotient Q:

$$\Delta G = \Delta G^{\circ} + R T \ln Q$$

**Step 3 — substitute the electrochemical identities.**

$$-n F E = -n F E^{\circ} + R T \ln Q$$

**Step 4 — divide through by −nF.**

$$\boxed{E = E^{\circ} - \frac{R T}{n F} \ln Q}$$

**Step 5 — engineering form at 25 °C.** Use $\log_{10}$ (conversion factor ln ↔ log₁₀ = 2.3026):

$$\frac{2.3026\,RT}{F} = \frac{2.3026 \times 8.314 \times 298.15}{96485} = 0.0592\ \text{V} \approx 0.0591\ \text{V}$$

$$\boxed{E = E^{\circ} - \frac{0.0591}{n} \log_{10} Q \qquad (25^\circ\text{C})}$$

**Step 6 — separate electrode form (each half-cell):**

$$E = E^{\circ} + \frac{0.0591}{n} \log_{10}\left(\frac{[\text{oxidized}]}{[\text{reduced}]}\right)$$

**Nernst at the endpoint of a cell calculation:**

$$E_{cell} = E^{\circ}_{cell} - \frac{0.0591}{n}\log_{10} Q, \qquad Q = \frac{\prod[\text{products}]}{\prod[\text{reactants}]}$$

### 2.2 Nernst Equation Applied to pH (Glass Electrode)

The glass electrode potential vs. SHE:

$$E_{glass} = E^{\circ}_{glass} + \frac{2.303 RT}{F} \log[\mathrm{H^+}] = E^{\circ}_{glass} - 0.0591\,pH$$

For a cell built with calomel:

$$E_{cell} = E_{calomel} - E_{glass} = E_{calomel} - E^{\circ}_{glass} + 0.0591\,pH$$

**Calibration:** a pH-meter is calibrated with standard buffers; then unknown pH is read from the linear 59.1 mV/pH slope. Nernstian response means ±1 pH unit = ±59.1 mV at 25 °C.

### 2.3 Conductance, Molar Conductivity & Kohlrausch

$$\kappa = \frac{1}{\rho} = \frac{l}{R\,a} \quad (\text{cell constant } G^* = \frac{l}{a})$$

$$\Lambda_m = \frac{1000\,\kappa}{C} \quad \left(\kappa \text{ in S/cm, C in mol/L}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| κ | specific conductivity | S/cm (S m⁻¹) |
| ρ | resistivity | Ω·cm |
| l, a | electrode separation, area | cm, cm² |
| G* | cell constant | cm⁻¹ |
| Λₘ | molar conductivity | S cm² mol⁻¹ |
| C | molar concentration | mol/L |

**Kohlrausch's law of independent migration:**

$$\Lambda_m^{\circ} = \lambda_+^{\circ} + \lambda_-^{\circ}$$

**Degree of dissociation (weak electrolyte):**

$$\alpha = \frac{\Lambda_m}{\Lambda_m^{\circ}}$$

### 2.4 Corrosion Electrochemistry — Thermodynamic Driving Force

Wet corrosion of iron in neutral water:

$$\mathrm{Fe \longrightarrow Fe^{2+} + 2e^-} \quad (\text{anode, } E^\circ = -0.44\ \text{V})$$

$$\mathrm{O_2 + 2H_2O + 4e^- \longrightarrow 4OH^-} \quad (\text{cathode, } E^\circ = +0.40\ \text{V at pH 7})$$

$$E^\circ_{cell} = 0.40 - (-0.44) = +0.84\ \text{V} > 0 \quad \Rightarrow \quad \text{spontaneous corrosion}$$

The corrosion rate is proportional to the corrosion current $i_{corr}$ via Faraday's law:

$$m = \frac{i\,t\,M}{n\,F}$$

| Symbol | Meaning | Unit |
|---|---|---|
| m | mass of metal corroded/deposited | g |
| i | corrosion current | A |
| t | time | s |
| M | molar mass of metal | g/mol |
| n | electrons per metal atom oxidized | — |
| F | Faraday constant | C/mol e⁻ |

### 2.5 Faraday's Laws for Electroplating & Cathodic Protection Sizing

**Faraday I:** mass of substance deposited/produced ∝ quantity of electricity:

$$m = Z\,Q = Z\,i\,t \qquad \text{where } Z = \frac{E_{eq}}{F} = \frac{M}{n F}$$

**Faraday II:** same charge deposits weights proportional to equivalent weights:

$$\frac{m_1}{m_2} = \frac{E_{eq,1}}{E_{eq,2}}$$

**Electroplating thickness:** volume of deposit = $\frac{m}{\rho}$, thickness $t_{dep} = \frac{m}{\rho A}$ where A = plated area.

**Impressed-current sizing:** required current for a buried pipeline = current density × exposed area × safety factor; sacrificial anode mass sized from $m = \dfrac{i\,t\,M}{nF}$ with anode utilization factor.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: Nernst Equation — Cell Potential Under Non-Standard Conditions

**Problem.** For the cell Zn | Zn²⁺(0.1 M) ∥ Cu²⁺(1.0 M) | Cu at 25 °C, calculate E_cell. (E°(Cu²⁺/Cu) = +0.34 V; E°(Zn²⁺/Zn) = −0.76 V; log₁₀ 0.1 = −1.)

---

**Solution:**

**Step 1 — standard cell potential.**

$$E^{\circ}_{cell} = E^{\circ}_{Cu^{2+}/Cu} - E^{\circ}_{Zn^{2+}/Zn} = 0.34 - (-0.76) = +1.10\ \text{V}$$

**Step 2 — net cell reaction and n.**

$$\mathrm{Zn + Cu^{2+} \longrightarrow Zn^{2+} + Cu}, \qquad n = 2$$

**Step 3 — reaction quotient.**

$$Q = \frac{[\mathrm{Zn^{2+}}]}{[\mathrm{Cu^{2+}}]} = \frac{0.1}{1.0} = 0.1$$

**Step 4 — Nernst.**

$$E = E^{\circ} - \frac{0.0591}{2}\log_{10}(0.1) = 1.10 - 0.02955 \times (-1)$$

$$E = 1.10 + 0.02955$$

**Step 5 — answer.**

$$\boxed{E_{cell} = 1.1296\ \text{V}}$$

---

### Problem 2: Nernst for a Half-Cell — Concentration Effect

**Problem.** Calculate the potential of the Cu²⁺/Cu electrode when [Cu²⁺] = 0.01 M at 25 °C. E° = +0.34 V.

---

**Solution:**

**Step 1 — Nernst for the half cell.**

$$E = E^{\circ} + \frac{0.0591}{n}\log_{10}[\mathrm{Cu^{2+}}], \quad n = 2$$

**Step 2 — substitute.**

$$E = 0.34 + \frac{0.0591}{2}\log_{10}(0.01) = 0.34 + 0.02955 \times (-2)$$

$$E = 0.34 - 0.0591$$

**Step 3 — answer.**

$$\boxed{E = 0.2809\ \text{V}}$$

(Diluting the ion makes reduction less favorable, so potential drops from +0.34 V.)

---

### Problem 3: Conductometric Equivalence Volume

**Problem.** 20 mL of 0.1 M HCl is titrated with 0.1 M NaOH while measuring conductivity. The conductivity first decreases to a minimum, then rises. Find (a) the equivalence volume and (b) the molar conductivity of the salt at equivalence. (λ°(Na⁺)=50.1, λ°(Cl⁻)=76.3 S cm² mol⁻¹.)

---

**Solution:**

**Step 1 — equivalence point (moles H⁺ = moles OH⁻).**

$$V_{NaOH} = \frac{M_{HCl} \times V_{HCl}}{M_{NaOH}} = \frac{0.1 \times 20}{0.1} = 20\ \text{mL}$$

$$\boxed{\text{Equivalence volume} = 20\ \text{mL NaOH}}$$

**Step 2 — at equivalence, solution contains NaCl (0.1 M × 20 mL / 40 mL = 0.05 M).**

$$\Lambda^{\circ}_{NaCl} = \lambda^{\circ}_{Na^+} + \lambda^{\circ}_{Cl^-} = 50.1 + 76.3 = 126.4\ \text{S cm}^2 \text{mol}^{-1}$$

**Step 3 — conductivity at equivalence.**

$$\kappa = \frac{\Lambda^{\circ} \times C}{1000} = \frac{126.4 \times 0.05}{1000} = 6.32 \times 10^{-3}\ \text{S/cm}$$

$$\boxed{\Lambda^{\circ}_{NaCl} = 126.4\ \text{S cm}^2 \text{mol}^{-1}, \quad \kappa_{eq} = 6.32 \times 10^{-3}\ \text{S/cm}}$$

---

### Problem 4: Corrosion Mass Loss via Faraday's Law

**Problem.** A sacrificial zinc anode protects a ship hull, supplying an average current of 2.5 A for 6 months (180 days). What mass of zinc is consumed? (Zn: M = 65.4 g/mol, n = 2, F = 96500 C/mol.)

---

**Solution:**

**Step 1 — total charge.**

$$Q = i\,t = 2.5 \times (180 \times 24 \times 3600) = 2.5 \times 1.5552 \times 10^7 = 3.888 \times 10^7\ \text{C}$$

**Step 2 — moles of electrons.**

$$n_e = \frac{Q}{F} = \frac{3.888 \times 10^7}{96500} = 402.9\ \text{mol e}^-$$

**Step 3 — moles of Zn (2 e⁻ per Zn atom).**

$$n_{Zn} = \frac{402.9}{2} = 201.45\ \text{mol}$$

**Step 4 — mass.**

$$m = 201.45 \times 65.4 = 13174.8\ \text{g}$$

**Step 5 — answer.**

$$\boxed{m_{Zn} = 13.17\ \text{kg of zinc consumed}}$$

---

### Problem 5: Electroplating Thickness

**Problem.** A current of 2 A is passed for 1 hour through a nickel-plating bath (Ni²⁺ → Ni). (a) What mass of nickel deposits? (b) If the cathode area is 100 cm² and nickel density is 8.9 g/cm³, find the deposit thickness. (Ni: 58.7 g/mol, n = 2.)

---

**Solution:**

**Step 1 — charge.**

$$Q = 2 \times 3600 = 7200\ \text{C}$$

**Step 2 — moles of Ni.**

$$n_{Ni} = \frac{Q}{nF} = \frac{7200}{2 \times 96500} = 0.03731\ \text{mol}$$

**Step 3 — mass.**

$$m = 0.03731 \times 58.7 = 2.190\ \text{g}$$

**Step 4 — volume and thickness.**

$$V = \frac{m}{\rho} = \frac{2.190}{8.9} = 0.2461\ \text{cm}^3$$

$$t = \frac{V}{A} = \frac{0.2461}{100} = 2.461 \times 10^{-3}\ \text{cm} = 24.6\ \mu\text{m}$$

**Step 5 — answers.**

$$\boxed{m_{Ni} = 2.190\ \text{g}} \qquad
\boxed{t = 24.6\ \mu\text{m}}$$

---

### Problem 6: Galvanic Series Prediction

**Problem.** A steel ship hull (Fe) is riveted with copper plates in seawater. Which metal corrodes, and why? If an Al sacrificial anode is then welded to the hull, does the copper plate remain protected?

---

**Solution:**

**Step 1 — galvanic series positions.** Fe is more active (higher in the series) than Cu. Coupled in seawater, Fe is the **anode** and corrodes; Cu becomes the cathode (protected) but at the expense of accelerated steel corrosion.

$$\boxed{\text{Steel corrodes; copper is cathodically protected}}$$

**Step 2 — add Al anode.** Al (more active than Fe) becomes the new anode; the hull (Fe) becomes the cathode and is protected, and Cu remains protected too.

$$\boxed{\text{Yes — with the Al anode attached, both Fe hull and Cu plate are protected; Al corrodes instead}}$$

---

## 4. ENGINEERING APPLICATIONS MAP

| Principle | Industrial / Field Application |
|---|---|
| **Nernst equation** | Design of batteries & fuel cells, corrosion prediction, sensor calibration, concentration cells, electrochemical machining |
| **Reference electrodes (calomel, Ag/AgCl)** | pH meters, ion-selective electrodes, potentiometric titrations, dissolved-oxygen probes, every electrochemical lab measurement |
| **Glass electrode / pH measurement** | pH control in water treatment, fermentation, pharmaceutical QA, electroplating baths, soil analysis |
| **Conductometric titration** | Coloured/turbid solutions where indicators fail; soap & detergent, wastewater analysis, cement/limestone (carbonate) determination |
| **Galvanic series** | Selecting compatible metals in shipbuilding, heat exchangers, plumbing (avoid galvanic couples) |
| **Differential aeration / pitting** | Corrosion engineering of pipelines, storage tanks (waterline attack), stainless steel pitting in chloride service |
| **Sacrificial anodes (Mg/Zn/Al)** | Ship hulls, offshore platforms, underground pipelines, hot-water tanks, boilers |
| **Impressed current cathodic protection** | Buried trans-continental pipelines, reinforced-concrete bridges, offshore rigs, marine jetties (large structures) |
| **Electroplating** | Chrome/nickel plating for wear & corrosion, gold plating in electronics, zinc plating (electrogalvanizing), decorative finishes |
| **Galvanization (hot-dip Zn)** | Roofing, corrugated sheets, transmission towers, fencing, automotive body panels |

---

## APPENDIX: Formula & Data Quick Reference

| Quantity | Formula | Notes |
|---|---|---|
| Nernst (25 °C) | $E = E^{\circ} - \frac{0.0591}{n}\log_{10}Q$ | Q = reaction quotient |
| ΔG ↔ E | $\Delta G = -nFE$ | n, F, E linked |
| Calomel potential | +0.242 V (sat. KCl) | vs SHE |
| Glass electrode pH | $E_{glass} = E^{\circ} - 0.0591\,pH$ | slope 59.1 mV/pH |
| Molar conductivity | $\Lambda_m = \frac{1000\kappa}{C}$ | κ in S/cm |
| Kohlrausch | $\Lambda_m^{\circ} = \lambda_+^{\circ} + \lambda_-^{\circ}$ | independent migration |
| Faraday I | $m = \frac{i t M}{nF}$ | corrosion/plating |
| Faraday II | $\frac{m_1}{m_2} = \frac{E_1}{E_2}$ | equivalents |
| Corrosion of Fe (pH 7) | Fe + ½O₂ + H₂O → Fe(OH)₂, E°cell = +0.84 V | spontaneous |

## CROSS-REFERENCES

- Related modules: [[module-1-water-technology-hardness]] (boiler corrosion, dissolved O₂) · [[module-2-surfactants-interfaces-colloids]] (corrosion inhibitors as adsorbed films) · [[chemistry/formula-sheet-physical]] (electrochemistry: Kohlrausch, Faraday) · [[engineering-physics/module-4-semiconductors-electromagnetism]]
