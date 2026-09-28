---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Module 1 — Zeolite Process & Softening Numericals"
date: "2026-09-28"
tags: [btech, engineering-chemistry, water-technology, zeolite, lime-soda, softening, numericals, exam-prep]
last_updated: "2026-09-28"
description: "Zeolite (permutit) softening theory — cold vs hot lime-soda, column construction, exchange/regeneration reactions, pros-cons — plus all 4 worked NaCl↔CaCO3 numericals from the Dipanwita Das slides, answers recomputed."
confidence: high
source: "raw-sources/Zeolite Process with Numericals.pdf (Dr. Dipanwita Das, KJSCE-SVU, 14 pp)"
---

## For future agent

Theory + problem companion to [[module-1-water-technology-hardness]] §2.3–2.4 (which owns the dosage formulas and exchange equations) — this page adds the cold/hot lime-soda comparison the module lacks, the column diagram, and the **4 worked zeolite numericals verbatim from the slides**. Every answer was recomputed during ingest and checks out. Units/conversions: [[units-of-hardness-industrial-problems-revision]]; EDTA-side numericals: [[edta-numericals-worked-bank]].

# Zeolite Process — Theory + Numericals

## 1. Lime-soda: the two variants (context)

| | **Cold lime-soda** | **Hot lime-soda** |
|---|---|---|
| Principle | Lime + soda added at **room temperature** | Lime + soda at **80–150 °C**, near boiling |
| Precipitate | Finely divided → won't settle/filter → needs **coagulant** (alum, Al₂(SO₄)₃, sodium aluminate → gelatinous Al(OH)₃ entraps fines) | Settles rapidly → **no coagulant needed** |
| Extras | NaAlO₂ as coagulant also removes silica + oil | Dissolved CO₂/air driven out; lower viscosity → easier filtration |
| Residual hardness | **50–60 ppm** | **15–30 ppm** |

Coagulant reactions (cold process): $\mathrm{NaAlO_2 + 2H_2O \to NaOH + Al(OH)_3}$; $\mathrm{Al_2(SO_4)_3 + 3Ca(HCO_3)_2 \to 2Al(OH)_3 + 3CaSO_4 + 6CO_2}$

**Advantages of lime-soda (general):** economical · with sedimentation+coagulation less coagulant needed · raises pH → less pipe corrosion · reduces mineral content overall · removes some Fe/Mn · alkaline water kills pathogens.

**Disadvantages:** needs careful operation + skilled supervision · bulky sludge disposal (use: raising low-lying city land) · only softens to ~15 ppm — **not good enough for boilers**.

## 2. Zeolite / permutit process

**Sodium zeolite:** $\mathrm{Na_2O \cdot Al_2O_3 \cdot xSiO_2 \cdot yH_2O}$ where $x = 2\text{–}10$, $y = 2\text{–}6$.

A sodium aluminosilicate that **reversibly exchanges its Na⁺ ions for the hardness-causing Ca²⁺/Mg²⁺ ions** in water.

| Type | Nature | Example / preparation |
|---|---|---|
| **Natural** | Non-porous | Natrolite, $\mathrm{Na_2O \cdot Al_2O_3 \cdot 4SiO_2 \cdot 2H_2O}$ |
| **Synthetic** | Porous, gel structure | Heated together: china clay + feldspar + soda ash |

**Column construction** (slide diagram): hard-water inlet → spray/distributor → **zeolite bed** → **gravel** layer → soft-water outlet at bottom; side **NaCl solution storage + injector** leads in for regeneration; waste goes "to sink".

**Softening (forward):**

$$\mathrm{Na_2Ze + Ca(HCO_3)_2 \to CaZe + 2NaHCO_3} \qquad \mathrm{Na_2Ze + Mg(HCO_3)_2 \to MgZe + 2NaHCO_3}$$

**Regeneration (brine):**

$$\mathrm{CaZe + 2NaCl \to Na_2Ze + CaCl_2} \qquad \mathrm{MgZe + 2NaCl \to Na_2Ze + MgCl_2}$$

> Equivalents used in numericals: **58.5 mg NaCl ≡ 50 mg CaCO₃** (1 mol NaCl = 1 eq = 1 eq CaCO₃), i.e. **117 g NaCl ↔ 100 g CaCO₃** — the slide's "1 eq NaCl = 1 eq CaCO₃" bridge.

### Advantages

- Hardness removed **almost completely → ~10 ppm** water
- Compact equipment, small footprint
- **No precipitate/sludge** → no later sludge danger in treated water
- Self-adjusts to variation in incoming hardness
- Clean process, fast, low skill needed for operation & maintenance

### Disadvantages

- More sodium salts than lime-soda water
- Only swaps Ca²⁺/Mg²⁺ for Na⁺ — **acidic ions (HCO₃⁻, CO₃²⁻) stay**
- In boilers: Na₂CO₃ decomposes → CO₂ (corrosion) and hydrolyses → NaOH (**caustic embrittlement**)
- High-turbidity water not treated efficiently

## 3. Worked numericals (slides 11–14, answers recomputed)

### Z1 — hardness from brine consumed

**Given.** 10,000 L hard water fully softened by a zeolite softener that took 5,000 L NaCl solution of 1,170 mg NaCl/L.

$$5000 \times 1170 = 5{,}850{,}000\ \text{mg NaCl} \;\xrightarrow{\;58.5\,\to\,50\;}\; 5{,}850{,}000 \times \frac{50}{58.5} = 5{,}000{,}000\ \text{mg CaCO}_3$$

$$\text{Hardness} = \frac{5{,}000{,}000}{10{,}000} = 500\ \text{mg/L} \Rightarrow \boxed{500\ \text{ppm}}$$

### Z2 — hardness from regeneration brine

**Given.** Exhausted softener regenerated with 75 L NaCl at 75 g/L; then 1.6 × 10⁴ L hard water passed.

$$75 \times 75 = 5625\ \text{g} = 5.625 \times 10^6\ \text{mg NaCl} \to 5.625\times10^6 \times \frac{50}{58.5} = 4.81 \times 10^6\ \text{mg CaCO}_3$$

$$\text{Hardness} = \frac{4.81 \times 10^6}{1.6 \times 10^4} = \boxed{300\ \text{ppm}}$$

### Z3 — volume of sample from brine

**Given.** Regenerated with 125 L NaCl at 50 g/L; sample hardness 350 ppm → find volume.

$$125 \times 50 = 6250\ \text{g} = 6{,}250{,}000\ \text{mg NaCl} \to 6{,}250{,}000 \times \frac{50}{58.5} = 5{,}341{,}880\ \text{mg CaCO}_3$$

$$V = \frac{5{,}341{,}880}{350} = \boxed{15{,}262.5\ \text{L}}$$

### Z4 — brine volume needed for regeneration (reverse direction)

**Given.** 10,000 L at 200 ppm exhausts the bed; NaCl strength 12.5 g/L → volume for regeneration.

**Step 1 — hardness removed:** $200 \times 10{,}000 = 2\times10^6\ \text{mg} = 2000\ \text{g CaCO}_3$

**Step 2 — NaCl:** regeneration $\mathrm{CaZe + 2NaCl \to Na_2Ze + CaCl_2}$, and 100 g CaCO₃ hardness ↔ 2 × 58.5 = **117 g NaCl**:

$$\text{NaCl} = 2000 \times \frac{117}{100} = 2340\ \text{g}$$

**Step 3 — volume:** $V = 2340 / 12.5 = \boxed{187.2\ \text{L}}$

## 4. Self-check (exam-style)

1. Why does cold lime-soda need a coagulant and hot not? Quote both residual-hardness figures.
2. Write the zeolite formula with the ranges of x and y; how do synthetic and natural zeolites differ?
3. Z1 in one line: what conversion factor bridges NaCl mass and CaCO₃ hardness, and why (eq-weight logic)?
4. A bed passes 1.6 × 10⁴ L after 75 L of 75 g/L brine — reproduce 300 ppm.
5. Reverse problem: 10,000 L @ 200 ppm, 12.5 g/L brine → reproduce 187.2 L.
6. Name two boiler-specific risks of softened-by-zeolite water.

## See also

- [[module-1-water-technology-hardness]] — units, lime-soda dosage formulas, exchange equations (theory home)
- [[units-of-hardness-industrial-problems-revision]] — ppm/°Clark/°Fr conversions
- [[edta-numericals-worked-bank]] — titration-side numericals (same slide author)
- [[hard-water-industry-effects]] — why hardness matters per industry
- [[lab-edta-hardness-water]] — lab counterpart
