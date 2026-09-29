---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Module 1 — Ion-Exchange / Demineralization Numericals"
date: "2026-09-30"
tags: [btech, engineering-chemistry, water-technology, ion-exchange, demineralization, numericals, exam-prep]
last_updated: "2026-09-30"
description: "Ion-exchange (demineralization) process theory — cation/anion resins, forward/regeneration reactions, pros/cons — plus all 4 worked HCl/NaOH↔CaCO3 numericals from the Dipanwita Das slides, answers recomputed. Formula: Hardness (mg/L as CaCO3) = N × V_acid × 50,000 / V_water."
confidence: high
source: "raw-sources/ion exchange _numericals with solutions.pdf (Dr. Dipanwita Das, KJSCE-SVU, 15 pp)"
---

## For future agent

Theory + problem companion to [[module-1-water-technology-hardness]] §2.5 (which owns the ion-exchange concept summary) — this page adds the full resin chemistry, regeneration equations, and the **4 worked ion-exchange numericals verbatim from the slides** plus 3 practice Qs with answers. Every answer was recomputed during ingest and checks out. Units/conversions: [[units-of-hardness-industrial-problems-revision]]; EDTA-side numericals: [[edta-numericals-worked-bank]]; zeolite-side numericals: [[zeolite-process-numericals]].

# Ion-Exchange Process — Theory + Numericals

## 1. Process Overview

**Ion-Exchange / Demineralization:** Complete removal of **both cations and anions** from water using synthetic resins. Produces water of very low residual hardness (~2 ppm) — suitable for high-pressure boilers.

### Resin Types

| Resin | Base Polymer | Functional Group | Exchanges |
|-------|--------------|------------------|-----------|
| **Cation Exchanger** | Styrene-divinylbenzene copolymer | –SO₃H (sulphonated) or –COOH (carboxylated) | H⁺ for Ca²⁺, Mg²⁺, Na⁺, etc. |
| **Anion Exchanger** | Styrene-divinylbenzene copolymer | –N⁺(CH₃)₃ (quaternary ammonium, from amination/nitration) | OH⁻ for Cl⁻, SO₄²⁻, HCO₃⁻, etc. |

**Notation:** RH⁺ = cation resin in H⁺ form; R'OH = anion resin in OH⁻ form.

---

## 2. Forward Reactions (Softening)

### Cation Exchanger (removes cations)

$$\mathrm{RH^+ + Ca^{2+} \to R_2Ca + 2H^+}$$
$$\mathrm{RH^+ + Mg^{2+} \to R_2Mg + 2H^+}$$

Hardness ions (Ca²⁺, Mg²⁺) replace H⁺ on resin; H⁺ goes into water.

### Anion Exchanger (removes anions)

$$\mathrm{R'OH + Cl^- \to R'Cl + OH^-}$$
$$\mathrm{2R'OH + SO_4^{2-} \to R'_2SO_4 + 2OH^-}$$

Anions (Cl⁻, SO₄²⁻, HCO₃⁻) replace OH⁻ on resin; OH⁻ goes into water.

### Overall Neutralisation

$$\mathrm{H^+ + OH^- \to H_2O}$$

The H⁺ from cation exchanger and OH⁻ from anion exchanger combine to form water — net result: demineralised water.

---

## 3. Regeneration Reactions (Restoring Resin Capacity)

### Cation Exchanger Regeneration (with HCl)

$$\mathrm{R_2Ca + 2HCl \to 2RH^+ + CaCl_2}$$
$$\mathrm{R_2Mg + 2HCl \to 2RH^+ + MgCl_2}$$

HCl strips Ca²⁺/Mg²⁺ off resin, restores H⁺ form. Wash away CaCl₂/MgCl₂.

### Anion Exchanger Regeneration (with NaOH)

$$\mathrm{R'_2SO_4 + 2NaOH \to 2R'OH + Na_2SO_4}$$

NaOH strips anions off resin, restores OH⁻ form. Wash away Na₂SO₄.

---

## 4. Advantages & Disadvantages

| **Advantages** | **Disadvantages** |
|----------------|-------------------|
| Softens highly acidic or alkaline water | Equipment is **costly** |
| **Residual hardness ~2 ppm** — excellent for high-pressure boilers | Expensive chemicals (HCl, NaOH) needed |
| Complete demineralisation (removes anions too) | Turbidity must be **< 10 ppm**; else pre-treat by coagulation/filtration |
| | Resin fouling by organics/Fe/Mn reduces output |

---

## 5. Key Formula

**For cation-exchange resin regeneration (hardness calculation):**

$$\text{Hardness (mg/L as CaCO₃)} = \frac{N \times V_{\text{acid}} \times 50{,}000}{V_{\text{water}}}$$

Where:
- $N$ = normality of HCl (eq/L)
- $V_{\text{acid}}$ = volume of HCl used for regeneration (L)
- $V_{\text{water}}$ = volume of water treated (L)
- $50{,}000$ = equivalent weight of CaCO₃ (50 g/eq) × 1000 (mg/g)

> **Logic:** $N \times V_{\text{acid}}$ = equivalents of HCl = equivalents of cations removed = equivalents of CaCO₃ hardness.  
> Equivalent weight of CaCO₃ = 100/2 = 50 g/eq = 50,000 mg/eq.  
> Multiply by equivalents → mg CaCO₃. Divide by $V_{\text{water}}$ → mg/L = ppm.

---

## 6. Worked Numericals (Slides 8–15, Answers Recomputed)

### IE1 — Hardness from Regeneration Acid

**Given:** 10,000 L water treated. Cationic resin required 200 L of 0.1 N HCl. Anionic resin required 200 L of 0.1 N NaOH (not needed for hardness calc).

**Find:** Hardness of water sample.

**Solution:**

Step 1: Equivalents of HCl = $N \times V = 0.1 \times 200 = 20$ eq  
→ 10,000 L water contained **20 eq of hardness cations**.

Step 2: Convert to CaCO₃ equivalent  
Eq. weight of CaCO₃ = 100/2 = 50 g/eq = 50,000 mg/eq  
Mass CaCO₃ = $20 \times 50 = 1000$ g = 1,000,000 mg

Step 3: Hardness = $\frac{1{,}000{,}000\ \text{mg}}{10{,}000\ \text{L}} = 100\ \text{mg/L} = \boxed{100\ \text{ppm as CaCO₃}}$

> **Check:** Using formula: $\frac{0.1 \times 200 \times 50{,}000}{10{,}000} = 100$ ppm ✓

---

### IE2 — Hardness from Regeneration Acid (Larger Scale)

**Given:** 50,000 L water treated. Cationic resin required 150 L of 0.25 N HCl. Anionic resin required 150 L of 0.25 N NaOH.

**Find:** Hardness of water sample.

**Solution:**

Step 1: Equivalents of HCl = $0.25 \times 150 = 37.5$ eq

Step 2: Mass CaCO₃ = $37.5 \times 50 = 1875$ g = 1,875,000 mg

Step 3: Hardness = $\frac{1{,}875{,}000}{50{,}000} = 37.5\ \text{mg/L} = \boxed{37.5\ \text{ppm as CaCO₃}}$

> **Check:** Using formula: $\frac{0.25 \times 150 \times 50{,}000}{50{,}000} = 37.5$ ppm ✓

> **Note:** NaOH data (150 L of 0.25 N) is for anion-exchanger regeneration — not used in hardness calc.

---

### IE3 — Practice Q1 (from Slide 13)

**Given:** 10,000 L water treated. Cationic resin requires 100 L of 0.1 N HCl.

**Find:** Hardness.

**Solution:**

$$\text{Hardness} = \frac{0.1 \times 100 \times 50{,}000}{10{,}000} = \boxed{50\ \text{ppm as CaCO₃}}$$

---

### IE4 — Practice Q2 (from Slide 13)

**Given:** 20,000 L water. Cationic resin requires 80 L of 0.2 N HCl.

**Find:** Hardness.

**Solution:**

$$\text{Hardness} = \frac{0.2 \times 80 \times 50{,}000}{20{,}000} = \boxed{40\ \text{ppm as CaCO₃}}$$

---

### IE5 — Practice Q3 (from Slide 13)

**Given:** 25,000 L water treated. Exhausted cationic resin requires 125 L of 0.1 N HCl.

**Find:** Hardness as CaCO₃.

**Solution:**

$$\text{Hardness} = \frac{0.1 \times 125 \times 50{,}000}{25{,}000} = \boxed{25\ \text{ppm as CaCO₃}}$$

---

### IE6 — Practice Q4 (from Slide 13)

**Given:** 40,000 L water passed through ion-exchange unit. Cation resin requires 200 L of 0.2 N HCl.

**Find:** Hardness.

**Solution:**

$$\text{Hardness} = \frac{0.2 \times 200 \times 50{,}000}{40{,}000} = \boxed{50\ \text{ppm as CaCO₃}}$$

---

### IE7 — Reverse: Volume of HCl Needed (Slide 14)

**Given:** Water hardness = 80 ppm as CaCO₃. Volume treated = 20,000 L. HCl normality = 0.2 N.

**Find:** Volume of HCl required for regeneration.

**Solution:**

$$80 = \frac{0.2 \times V \times 50{,}000}{20{,}000}$$
$$V = \frac{80 \times 20{,}000}{0.2 \times 50{,}000} = \frac{1{,}600{,}000}{10{,}000} = \boxed{160\ \text{L}}$$

---

### IE8 — Reverse: Volume of Water Treated (Slide 15)

**Given:** Regenerated using 100 L of 0.25 N HCl. Water hardness = 50 ppm as CaCO₃.

**Find:** Volume of water treated.

**Solution:**

$$50 = \frac{0.25 \times 100 \times 50{,}000}{V_{\text{water}}}$$
$$V_{\text{water}} = \frac{0.25 \times 100 \times 50{,}000}{50} = \frac{1{,}250{,}000}{50} = \boxed{25{,}000\ \text{L}}$$

---

## 7. Self-Check (Exam-Style)

1. **Resin chemistry:** Write the cation-exchange forward reaction for Ca²⁺ and Mg²⁺; write the regeneration reaction with HCl.
2. **Anion exchanger:** Write the forward reaction for Cl⁻ and SO₄²⁻; write the regeneration reaction with NaOH.
3. **Overall reaction:** What neutralises the H⁺ and OH⁻ produced? Why is the final water demineralised?
4. **Formula recall:** Derive the hardness formula $N \times V \times 50{,}000 / V_{\text{water}}$ from equivalents logic.
5. **IE1 reproduction:** 10,000 L, 200 L of 0.1 N HCl → 100 ppm in 3 lines.
6. **Reverse problem:** 80 ppm hardness, 20,000 L, 0.2 N HCl → reproduce 160 L.
7. **Advantage/disadvantage:** Why is ion-exchange water better for high-pressure boilers than zeolite water? What are the two boiler risks of zeolite-softened water?
8. **Turbidity limit:** If raw water has 50 ppm turbidity, can it go directly to ion-exchange? What pre-treatment is needed?

---

## See Also

- [[module-1-water-technology-hardness]] — ion-exchange concept summary + units + lime-soda/zeolite theory
- [[zeolite-process-numericals]] — NaCl↔CaCO₃ numericals (zeolite softening)
- [[edta-numericals-worked-bank]] — titration-side numericals (same slide author)
- [[units-of-hardness-industrial-problems-revision]] — ppm / °Clark / °Fr conversions
- [[hard-water-industry-effects]] — why hardness matters per industry
- [[lab-edta-hardness-water]] — lab counterpart