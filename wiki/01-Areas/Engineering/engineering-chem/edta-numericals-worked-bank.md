---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Module 1 — EDTA Numericals Bank"
date: "2026-09-17"
tags: [btech, engineering-chemistry, water-technology, edta, hardness, numericals, exam-prep]
last_updated: "2026-09-17"
description: "Seven fully worked EDTA hardness numericals from Dr. Dipanwita Das class slides (SHW-standardization and molarity variants) with verified answers, plus V1/V2/V3 shortcut formulas and unit-conversion drills."
---

## For future agent

Problem bank companion to [[module-1-water-technology-hardness]] §3 (which holds 5 worked problems of other types). Every answer here was recomputed during ingest — one slide typo corrected (N4 permanent hardness 200 → 220 ppm, flagged inline). Bench procedure lives in [[lab-edta-hardness-water]]; unit conversions in [[units-of-hardness-industrial-problems-revision]].

# EDTA Numericals — Worked Bank (7 + drills)

## 0. Shortcut box (memorize first)

Standard 50 mL SHW $\equiv V_1$ mL EDTA (SHW = 1 mg/mL as $\mathrm{CaCO_3}$ unless the question prepares it differently):

$$\boxed{1\ \text{mL EDTA} \equiv \frac{50}{V_1}\ \text{mg CaCO}_3} \qquad \boxed{\text{Total} = \frac{V_2}{V_1}\times 1000\ \text{ppm}} \qquad \boxed{\text{Permanent} = \frac{V_3}{V_1}\times 1000\ \text{ppm}}$$

$$\boxed{\text{Temporary} = \text{Total} - \text{Permanent}} \qquad \boxed{1\ \text{mL of 1 M EDTA} \equiv 100\ \text{mg CaCO}_3}$$

Molarity rule (1:1 complex, MW $\mathrm{CaCO_3} = 100$): 1 mL of $M$-molar EDTA $\equiv 100 \times M$ mg $\mathrm{CaCO_3}$. So M/20 (0.05 M) $\to$ 5 mg/mL; M/15 ($\approx$ 0.067 M) $\to$ 6.7 mg/mL.

---

## N1 — Classic SHW standardisation

**Given.** 50 mL SHW $\equiv$ 38 mL EDTA; 100 mL sample $\equiv$ 21 mL; 100 mL boiled $\equiv$ 10 mL.

**Solution.** 1 mL EDTA $\equiv 50/38 = 1.316$ mg $\mathrm{CaCO_3}$.
Total: $21 \times 1.316 = 27.636$ mg per 100 mL $\to \boxed{276.36\ \text{ppm}}$.
Permanent: $10 \times 1.316 = 13.16$ per 100 mL $\to \boxed{131.6\ \text{ppm}}$.
Temporary: $276.36 - 131.6 = \boxed{144.76\ \text{ppm}}$.

## N2 — Same volumes, different titre

**Given.** 50 mL SHW $\equiv$ 21 mL EDTA; 50 mL sample $\equiv$ 21 mL; 50 mL boiled $\equiv$ 7 mL.

**Solution.** 1 mL EDTA $\equiv 50/21 = 2.381$ mg.
Total: $21 \times 2.381 = 50.001$ mg per 50 mL $\to \times 20 = \boxed{1000.02\ \text{ppm}}$.
Permanent: $7 \times 2.381 = 16.667$ per 50 mL $\to \boxed{333.34\ \text{ppm}}$.
Temporary: $\boxed{666.68\ \text{ppm}}$.
Pattern note: sample titre $=$ SHW titre $\Rightarrow$ sample $\approx$ 1000 ppm by construction — quick sanity check in exams.

## N3 — Non-standard SHW (0.38 g/L)

**Given.** 0.38 g $\mathrm{CaCO_3}}$/L made up as SHW; 100 mL SHW $\equiv$ 25 mL EDTA; 100 mL sample $\equiv$ 37 mL; 100 mL boiled $\equiv$ 10 mL.

**Solution.** SHW strength $= 380$ mg/L $\Rightarrow$ 1 mL SHW $\equiv 0.38$ mg. 100 mL SHW $\equiv 38$ mg $\equiv$ 25 mL EDTA $\Rightarrow$ 1 mL EDTA $\equiv 38/25 = 1.52$ mg.
Total: $37 \times 1.52 = 56.24$ per 100 mL $\to \boxed{562.4\ \text{ppm}}$.
Permanent: $10 \times 1.52 = 15.2 \to \boxed{152\ \text{ppm}}$.
Temporary: $\boxed{410.4\ \text{ppm}}$.
Exam trap: the slide's struck-off "1 mL SHW = 1 mg" does NOT apply when SHW is prepared non-standard — always recompute from the weighed mass.

## N4 — Non-standard SHW (1.2 g/L) ⚠️ slide erratum

**Given.** 1.2 g $\mathrm{CaCO_3}}$/L; 50 mL SHW $\equiv$ 30 mL EDTA; 100 mL sample $\equiv$ 27 mL; 100 mL boiled $\equiv$ 11 mL.

**Solution.** 1 mL SHW $\equiv 1.2$ mg; 50 mL $\equiv 60$ mg $\equiv$ 30 mL EDTA $\Rightarrow$ 1 mL EDTA $\equiv 2$ mg.
Total: $27 \times 2 = 54$ per 100 mL $\to \boxed{540\ \text{ppm}}$.
Permanent: $11 \times 2 = 22$ per 100 mL $\to \boxed{220\ \text{ppm}}$ — **slide prints "200 ppm", arithmetic error** (its own subtraction $540 - 220 = 320$ confirms 220).
Temporary: $\boxed{320\ \text{ppm}}$.

## N5 — Odd boiled volume (10 mL)

**Given.** 0.55 g/L SHW; 20 mL SHW $\equiv$ 10 mL EDTA; 50 mL sample $\equiv$ 17 mL; 10 mL boiled $\equiv$ 1.1 mL.

**Solution.** 1 mL SHW $\equiv 0.55$ mg; 20 mL $\equiv 11$ mg $\equiv$ 10 mL EDTA $\Rightarrow$ 1 mL $\equiv 1.1$ mg.
Total: $17 \times 1.1 = 18.7$ per 50 mL $\to \boxed{374\ \text{ppm}}$.
Permanent: $1.1 \times 1.1 = 1.21$ per 10 mL $\to \boxed{121\ \text{ppm}}$.
Temporary: $\boxed{253\ \text{ppm}}$.
Scale-up note: boiled volume (10 mL) $\neq$ sample volume (50 mL) — scale each to 1 L independently ($\times 100$ vs $\times 20$).

## N6 — Molarity EDTA (M/20, no SHW step)

**Given.** 50 mL sample $\equiv$ 10.2 mL of M/20 disodium EDTA; boiled filtrate $\equiv$ 6.5 mL.

**Solution.** M/20 $=$ 0.05 M $\Rightarrow$ 1 mL $\equiv 100 \times 0.05 = 5$ mg $\mathrm{CaCO_3}}$.
Total: $10.2 \times 5 = 51$ per 50 mL $\to \boxed{1020\ \text{ppm}}$.
Permanent: $6.5 \times 5 = 32.5 \to \boxed{650\ \text{ppm}}$.
Temporary: $\boxed{370\ \text{ppm}}$.

## N7 — Molarity EDTA (M/15)

**Given.** 50 mL sample $\equiv$ 15.3 mL of M/15 EDTA; boiled $\equiv$ 9.5 mL.

**Solution.** M/15 $\approx$ 0.067 M $\Rightarrow$ 1 mL $\equiv 6.7$ mg (slide convention; exact $100/15 = 6.667$).
Total: $15.3 \times 6.7 = 102.51$ per 50 mL $\to \boxed{2050.2\ \text{ppm}}$.
Permanent: $9.5 \times 6.7 = 63.65 \to \boxed{1273\ \text{ppm}}$.
Temporary: $\boxed{777.2\ \text{ppm}}$.

---

## Drills — units & salt-equivalents (solved)

$1\ \text{ppm} = 1\ \text{mg/L} = 0.1^\circ\text{Fr} = 0.07^\circ\text{Cl} = 0.02\ \text{meq/L}$.

- **20.23 °Cl** $\to 20.23 \times 14.25 = \boxed{288.28\ \text{ppm}}$, $\times 0.02 = \boxed{5.77\ \text{meq/L}}$.
- **31.3 °Fr** $\to \boxed{313\ \text{ppm}}$, $\boxed{6.26\ \text{meq/L}}$.
- **208 ppm** $\to$ 208 mg/L · $20.8^\circ\text{Fr}$ · $208/14.25 = 14.60^\circ\text{Cl}$ · $4.16\ \text{meq/L}$.
- **FeSO₄ for 210.5 ppm hardness:** MW 152 $\Rightarrow 210.5 \times 152/100 = 319.96$ mg/L $= \boxed{0.320\ \text{g/L}}$.
- **CaCl₂ for 150 ppm hardness:** MW 111 $\Rightarrow 150 \times 111/100 = 166.5$ mg/L $= \boxed{0.1665\ \text{g/L}}$.
- **Mixed salts** (Mg(HCO₃)₂ 14.6, Mg(NO₃)₂ 29.6, Ca(HCO₃)₂ 8.1, MgCl₂ 19, MgSO₄ 24 ppm): temporary $= 14.6(50/73) + 8.1(50/81) = 10.0 + 5.0 = \boxed{15\ \text{ppm}}$; permanent $= 20 + 20 + 20 = \boxed{60\ \text{ppm}}$.
- **Classify** Ca(HCO₃)₂, MgSO₄, CaCl₂, CO₂, HCl, Mg(HCO₃)₂ → temporary: Ca(HCO₃)₂, Mg(HCO₃)₂ · permanent: MgSO₄, CaCl₂ · non-hardness: CO₂ (acidity), HCl (acid).

## CROSS-REFERENCES

- Core theory + 5 more problems: [[module-1-water-technology-hardness]] (§2.2 EDTA formula, §3 problems)
- Bench procedure + V1/V2/V3 template: [[lab-edta-hardness-water]]
- Unit conversions: [[units-of-hardness-industrial-problems-revision]] (Part A)
