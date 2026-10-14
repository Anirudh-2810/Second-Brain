---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "MSE Revision — Module 1: Water Technology (Hardness)"
date: "2026-10-15"
tags: [btech, engineering-chemistry, water-technology, hardness, edta, zeolite, ion-exchange, boiler-troubles, exam-prep, mse, revision]
last_updated: "2026-10-15"
description: "MSE revision pack for Engineering Chemistry Module 1 (Water Technology): hardness units, EDTA/zeolite/ion-exchange/lime-soda calculation shortcuts, industrial effects and boiler troubles, plus traps. Condensed exam-facing review linking the deep numericals banks."
confidence: high
---

## For future agent

Exam-facing consolidation of Engineering Chemistry **Module 1 (Water Technology / Hardness)** for the MSE. It is a recall surface — units, calculation shortcuts, definitions, traps — that links to the deep pages: [[module-1-water-technology-hardness]] (theory home), [[edta-numericals-worked-bank]], [[zeolite-process-numericals]], [[ion-exchange-numericals]], [[units-of-hardness-industrial-problems-revision]], [[hard-water-industry-effects]]. Module 1 is numerical-heavy; nearly all marks come from the calculation methods below. If a formula here disagrees with a module page, the module page wins. As of 2026-10-15.

# MSE Revision — Chemistry Module 1: Water Technology

## Hardness — definition & units

- **Hardness** = soap-destroying / scale-forming property of water, due to dissolved **Ca²⁺ and Mg²⁺ salts**. Where the anion is HCO₃⁻ the hardness is **temporary (carbonate)**; with SO₄²⁻/Cl⁻ it is **permanent (non-carbonate)**.
- **Always express as mg/L (ppm) as CaCO₃** — the universal reference (eq. weight CaCO₃ = 100/2 = **50**).
- Do **NOT** count Na⁺/K⁺ salts (NaCl, NaHCO₃, K₂CO₃…), SiO₂, NaAlO₂, dissolved CO₂, HCl — they cause salinity/alkalinity, not hardness. **Classic exam trap.**

| Unit | Conversion (as CaCO₃) |
|---|---|
| ppm | 1 ppm = 1 mg/L |
| °Clark (°Cl) | 1 °Cl = 14.25 ppm |
| °French (°Fr) | 1 °Fr = 10 ppm |
| °German (°dH) | 1 °dH = 17.9 ppm |
| meq/L | 1 ppm = 0.02 meq/L |

Full conversion drill: [[units-of-hardness-industrial-problems-revision]].

## Method 1 — EDTA titration (deep: [[edta-numericals-worked-bank]])

**Principle:** EDTA (disodium salt of ethylenediaminetetraacetic acid) is a powerful hexadentate ligand that forms 1:1 stable complexes with Ca²⁺/Mg²⁺. Indicator: **EBT (Eriochrome Black-T)** — wine-red → blue at the endpoint, buffered to pH ≈ 10 with NH₄Cl + NH₄OH.

**Shortcuts (V₁ = mL of hard-water sample, V₂ = mL EDTA for total, V₃ = mL EDTA for permanent after boiling):**

$$1\ \text{mL EDTA} \equiv \frac{50}{V_1}\ \text{mg CaCO}_3 \qquad \text{Total} = \frac{V_2}{V_1}\times 1000\ \text{ppm}$$

$$\text{Permanent} = \frac{V_3}{V_1}\times 1000\ \text{ppm} \qquad \text{Temporary} = \text{Total} - \text{Permanent}$$

Also: **1 mL of 1 M EDTA ≡ 100 mg CaCO₃** (M-basis, since eq. wt = 50 and it is 1:1 but 1 M = 2 eq/L).

⚠️ Temporary hardness is removed by **boiling** ($\mathrm{Ca(HCO_3)_2 \xrightarrow{\Delta} CaCO_3\downarrow + H_2O + CO_2}$); permanent is not — that is what the third titration measures.

## Method 2 — Zeolite / Permutit process (deep: [[zeolite-process-numericals]])

- Sodium zeolite: $\mathrm{Na_2O\cdot Al_2O_3\cdot xSiO_2\cdot yH_2O}$ ($x=2$–$10$, $y=2$–$6$); swaps Na⁺ for Ca²⁺/Mg²⁺.
- Resin **58.5 mg NaCl ≡ 50 mg CaCO₃**, i.e. **117 g NaCl ↔ 100 g CaCO₃** (1 mol NaCl = 1 eq = 1 eq CaCO₃).
- Resin treated to **~10 ppm** residual hardness; no sludge; but adds Na salts (→ boiler problems).

Worked set: Z1 500 ppm · Z2 300 ppm · Z3 15,262.5 L · Z4 187.2 L.

## Method 3 — Ion-exchange / Demineralization (deep: [[ion-exchange-numericals]])

- Cation resin (RH⁺) swaps **H⁺** for Ca²⁺/Mg²⁺; anion resin (R'OH) swaps **OH⁻** for Cl⁻/SO₄²⁻/HCO₃⁻; H⁺ + OH⁻ → H₂O.
- Regeneration: cation with **HCl**, anion with **NaOH**.
- Residual hardness **~2 ppm** — best for high-pressure boilers. Needs turbidity < 10 ppm.

**Governing formula:**

$$\text{Hardness (ppm as CaCO}_3) = \frac{N \times V_{\text{acid}} \times 50{,}000}{V_{\text{water}}}$$

$N$ = normality of HCl, $V_{\text{acid}}$ = L HCl used, $V_{\text{water}}$ = L treated. Works reversed for volume/normality. Worked set: IE1 100 ppm · IE2 37.5 · IE3 50 · IE4 40 · IE5 25 · IE6 50 · IE7 160 L · IE8 25,000 L.

## Method 4 — Lime-soda (context)

- Cold process (room temp, needs coagulant like alum/NaAlO₂) → residual **50–60 ppm**; hot process (80–150 °C, no coagulant) → **15–30 ppm**.
- Zeolite/ion-exchange beat it for boiler-grade water.

## Industrial effects & boiler troubles (deep: [[hard-water-industry-effects]])

- Per-industry: **textile** (soap waste, bad dye shade), **sugar** (hindered crystallisation), **dyeing** (dye precipitation), **paper** (kills gloss, eats alum), **laundry** (grey fabric, fibre weakening), **pharma/beverage** (needs ultra-pure / non-alkaline).
- **Boiler corrosion** (general): dissolved O₂, CO₂→H₂CO₃, MgCl₂ hydrolysis→HCl. Prevent by deaeration + Na₂SO₃ scavenger.
- **Caustic embrittlement** (specific): Na₂CO₃ → NaOH at boiler temp, concentrates in cracks → inter-granular cracking. Prevent by phosphate conditioning, cap NaOH, tannin/lignin/Na₂SO₄ inhibitors.
- **Scale** = hard adherent deposit on hot walls (CaCO₃, CaSO₄ — inverse solubility, SiO₂); **sludge** = soft loose, settles in cool zones (Mg salts, CaCl₂). Both waste fuel and risk explosion.

## Exam traps checklist

1. Report hardness **as CaCO₃** unless told otherwise — never raw Ca/Mg mg/L.
2. Exclude Na/K salts, SiO₂, CO₂ from hardness.
3. EDTA total − permanent = temporary; boiling removes only temporary.
4. Zeolite factor is 58.5→50 (NaCl→CaCO₃), not 40 or 100.
5. Ion-exchange formula uses **normality × volume** = equivalents, × 50,000 mg/eq.
6. Zeolite adds Na salts → caustic embrittlement in boilers; ion-exchange removes anions too.

## See also

- [[module-1-water-technology-hardness]] — theory home (source of truth)
- [[edta-numericals-worked-bank]] · [[zeolite-process-numericals]] · [[ion-exchange-numericals]] — worked numericals
- [[units-of-hardness-industrial-problems-revision]] · [[hard-water-industry-effects]] — units & industry effects
- [[lab-edta-hardness-water]] — lab counterpart
- [[mse-2026-10-26-5-day-plan]] — the day-by-day plan this pack feeds
