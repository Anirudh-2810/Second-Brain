---
course_code: "ENG-CHEM (316106C103)"
course_name: "Engineering Chemistry"
unit: "MSE Past Paper (Aug–Nov 2025) — Solved Walkthrough"
date: "2026-10-19"
tags: [btech, engineering-chemistry, water-technology, hardness, edta, zeolite, lime-soda, green-chemistry, atom-economy, exam-prep, mse, past-paper]
last_updated: "2026-10-19"
description: "Solved walkthrough of the Aug–Nov 2025 Engineering Chemistry MSE paper (photo source): ELI5 concept notes for hardness/softening/atom-economy, every numerical solved step-by-step (lime-soda, EDTA, zeolite, atom economy, adipic acid), practice set, cheat card."
confidence: high
---

## For future agent

Full walkthrough of the **last year's Engineering Chemistry MSE paper** (KJSCE, Sem 1, COMPETRXEXC/MECH, max 30 marks; source = photo taken by owner 2026-10-19, paper not in raw-sources). Contains: ELI5 concept notes for the five topics the paper tests (hardness types, EDTA titration, lime-soda, zeolite, atom economy + green synthesis of adipic acid); every numerical solved step-by-step; a matching practice set with answers; exam-day cheat card. **Flag:** Q1A-OR prints standard hard water as "15 g/L CaCO₃" — numbers below use it as printed; if the intended value is 1.5 g/L, divide total/permanent/temporary by 10 (method identical). This is an application/recall surface — deep theory lives in [[module-1-water-technology-hardness]], [[zeolite-process-numericals]], [[edta-numericals-worked-bank]], [[green-chemistry-twelve-principles]]. As of 2026-10-19.

# Chem MSE 2025 Past Paper — Solved + ELI5 Notes

## Paper map

| Q | Type | Topic | Deep page |
|---|---|---|---|
| Q1A | Numerical | Lime-soda dose + purity OR EDTA 3-titration | [[module-1-water-technology-hardness]] |
| Q1B | Theory | Temporary vs permanent hardness | same |
| Q2A | Theory | Cold lime-soda process OR zeolite method | [[zeolite-process-numericals]] |
| Q2B | Numerical | Zeolite hardness from NaCl regeneration | [[zeolite-process-numericals]] |
| Q3A | Theory/Calc | Atom economy principle + 2 calculations | [[green-chemistry-twelve-principles]] |
| Q3B | Theory | Adipic acid: traditional vs green synthesis | [[green-chemistry-twelve-principles]] |

Atomic masses given: Ca 40 · Cl 35.5 · H 1 · C 12 · O 16 · S 32 · Si 28 · Mg 24 · Na 23.

---

## Part A — Concepts, ELI5

### 1. Hardness (the core idea)

Soap is a tiny magnet made to grab dirt. In hard water, **Ca²⁺/Mg²⁺ salts grab the soap first** — no lather, soap wasted. Hardness = dissolved Ca/Mg salts, always reported as **mg/L as CaCO₃** (everything converted to one comparison scale). **Na⁺/K⁺ salts, SiO₂, NaCl are NOT hardness** — classic trap: the paper lists them to be ignored.

### 2. Temporary vs permanent (Q1B guaranteed)

| | Temporary | Permanent |
|---|---|---|
| Cause | Bicarbonates: Ca(HCO₃)₂, Mg(HCO₃)₂ | Sulfates/chlorides: CaSO₄, MgSO₄, CaCl₂, MgCl₂ |
| Removed by | **Boiling** — bicarbonates decompose → insoluble CaCO₃↓/Mg(OH)₂↓ settles out | Nothing chemical-free; needs lime-soda/zeolite |
| Analogy | Dirt that unpacks and falls out when heated | Dirt that refuses to leave, however hot |

$$Ca(HCO_3)_2 \xrightarrow{\Delta} CaCO_3\!\downarrow + H_2O + CO_2 \qquad Mg(HCO_3)_2 \xrightarrow{\Delta} Mg(OH)_2\!\downarrow + 2CO_2$$

### 3. Lime-soda process (Q2A + Q1A)

Two cleaning powders: **lime Ca(OH)₂** and **soda Na₂CO₃**. In water they turn dissolved hardness into insoluble sludge (CaCO₃↓, Mg(OH)₂↓) that settles. **Cold process:** room temperature in big stirred tanks → slower, needs a coagulant (alum) at times, residual hardness ~50–60 ppm. **Hot process:** 80–150 °C → faster, no coagulant, residual ~15–30 ppm.

Lime handles **all temporary + all Mg**; soda handles **all Ca-permanent** (including the CaSO₄ that lime creates from MgSO₄):

$$Ca(HCO_3)_2 + Ca(OH)_2 \rightarrow 2CaCO_3\!\downarrow + 2H_2O$$
$$Mg(HCO_3)_2 + 2Ca(OH)_2 \rightarrow Mg(OH)_2\!\downarrow + 2CaCO_3\!\downarrow + 2H_2O$$
$$MgSO_4 + Ca(OH)_2 \rightarrow Mg(OH)_2\!\downarrow + CaSO_4 \quad(\text{lime converts Mg-hardness into Ca-hardness})$$
$$CaSO_4 + Na_2CO_3 \rightarrow CaCO_3\!\downarrow + Na_2SO_4$$

**Dose formulas** (74 = M(Ca(OH)₂); 106 = M(Na₂CO₃)):
$$\text{Lime} = \frac{74}{100}\big[Ca(HCO_3)_2 + 2{\times}Mg(HCO_3)_2 + MgSO_4 + MgCl_2\big]_{\text{as CaCO}_3}$$
$$\text{Soda} = \frac{106}{100}\big[CaSO_4 + CaCl_2 + MgSO_4 + MgCl_2\big]_{\text{as CaCO}_3}$$

Convert impurity → CaCO₃ equivalent: multiply by 100/M (Ca(HCO₃)₂ ×100/162 · Mg(HCO₃)₂ ×100/146 · CaSO₄ ×100/136 · MgSO₄ ×100/120 · MgCl₂ ×100/95 · CaCl₂ ×100/111). Mg(HCO₃)₂ counts **twice** for lime (its Mg(OH)₂ step + carbonate step). Cold process adds ~5 ppm excess reagent; purity handled as theoretical × 100/purity%. Full table incl. free CO₂/H⁺ rows: [[module-1-water-technology-hardness]].

### 4. Zeolite (permutit) method (Q2A-OR + Q2B)

Zeolite = a **sponge pre-loaded with Na⁺**: hard water flows through, sponge swaps Na⁺ for Ca²⁺/Mg²⁺. Na salts don't eat soap → water soft.

$$Na_2Z + CaSO_4 \rightarrow CaZ + Na_2SO_4$$

Exhausted sponge regenerated by **brine (NaCl)**: $CaZ + 2NaCl \rightarrow Na_2Z + CaCl_2$. The money formula: **117 g NaCl ⇄ 100 g CaCO₃ equivalent** (2 mol NaCl per mol exchange).

$$\text{Hardness} = \frac{m_{NaCl}\,(\text{g})}{V_{water}\,(\text{L})}\times\frac{100}{117}\ \text{g/L as CaCO}_3$$

### 5. EDTA titration (Q1A-OR)

EDTA = a super-soap that grabs Ca²⁺/Mg²⁺ **1:1, perfectly**. Indicator **EBT**: wine-red while hardness remains → blue at endpoint (pH ≈ 10 buffer). Every 3-line problem is the same recipe:

1. **Standard water** (known hardness) → price of EDTA: $1\ \text{mL EDTA} \equiv \dfrac{V_{std}\times \text{str}_{std}}{V_{EDTA}}$ mg CaCO₃
2. **Sample titration** → **total** hardness
3. **Boiled sample** titration → **permanent** hardness (temporary was boiled away)
4. $\text{Temporary} = \text{Total} - \text{Permanent}$

### 6. Atom economy (Q3A)

You buy a LEGO set to build one car, but half the bricks make the box. Atom economy = **how much of the input mass ends up in the part you want**:
$$AE = \frac{M_r\ \text{of desired product}}{M_r\ \text{of ALL reactants}}\times 100\%$$
Coined by **Barry Trost (1991)**. Not the same as yield: yield = how much product you *actually got* vs theoretical; AE = how much input mass *could ever* become product. 100% yield + 10% AE possible → efficient reaction, wasteful process. Addition reactions → high AE; substitutions (salt/water byproducts) → low. Full context: [[green-chemistry-twelve-principles]].

### 7. Adipic acid: traditional vs green (Q3B)

Adipic acid = the backbone brick of **nylon-6,6**.

- **Traditional:** KA oil (cyclohexanol/cyclohexanone) oxidized with hot conc. **HNO₃** → adipic acid + **N₂O** (laughing-gas greenhouse gas, ~300× CO₂ global-warming potential) + acidic nitrate waste.
- **Green:** **cyclohexene + H₂O₂ (30%)** with **tungstate catalyst (Na₂WO₄)** + phase-transfer catalyst, in **water** near ambient conditions → adipic acid, byproduct **water only** (Sato method; catalyst details vary by source — TBC per your notes).
- **Principles involved:** **Prevention** (N₂O waste never created, not treated later) · **Catalysis** (tungsten catalyst) · **Safer reagents** (H₂O₂ breaks down to water vs toxic HNO₃) · **Benign solvents** (water replaces organics) · **Atom economy** (far less mass wasted).

---

## Part B — Every numerical on the paper, solved

### Q1A.1 — Lime-soda (10,000 L; lime 85%, soda 90%)

Water: Ca(HCO₃)₂ 16.2 · CaSO₄ 6.8 · SiO₂ 8.0 · MgSO₄ 6.0 · NaCl 14 · Mg(HCO₃)₂ 8.4 mg/L.

**Step 1 — CaCO₃ equivalents:**

| Salt | mg/L | ×100/M | as CaCO₃ |
|---|---|---|---|
| Ca(HCO₃)₂ | 16.2 | 100/162 | 10.00 |
| Mg(HCO₃)₂ | 8.4 | 100/146 | 5.75 |
| CaSO₄ | 6.8 | 100/136 | 5.00 |
| MgSO₄ | 6.0 | 100/120 | 5.00 |
| SiO₂, NaCl | — | — | **ignored (not hardness)** |

**Step 2 — Lime:** $0.74[10 + 2(5.75) + 5] = 0.74 \times 26.5 = 19.61$ mg/L. For 10,000 L: 196.1 g pure → ÷0.85 purity = **≈230.7 g commercial lime**.

**Step 3 — Soda:** $1.06[5 + 5] = 10.6$ mg/L. For 10,000 L: 106 g pure → ÷0.90 = **≈117.8 g commercial soda**.

⚠️ MgSO₄ appears in **both** (lime kills the Mg, soda kills the CaSO₄ lime created). Mg(HCO₃)₂ counts **×2** for lime only.

### Q1A.OR — EDTA temporary hardness

Standard: 15 g/L CaCO₃ = 15 mg/mL; 20 mL contains 300 mg, captured by 25 mL EDTA → **1 mL EDTA ≡ 12 mg CaCO₃**.

- Sample, 100 mL × 18 mL EDTA: total = 18 × 12 = 216 mg/100 mL = **2160 mg/L**
- After boiling, 12 mL EDTA: permanent = 12 × 12 = 144 mg/100 mL = **1440 mg/L**
- **Temporary = 2160 − 1440 = 720 mg/L (720 ppm)**

(If the printed strength was really 1.5 g/L, factor is 1.2 mg/mL and the answers are 216 / 144 / **72 ppm** — method unchanged.)

### Q2B — Zeolite hardness

NaCl for regeneration: 25 L × 100 g/L = 2500 g. Exchange ratio 117 g NaCl ⇄ 100 g CaCO₃:

$$\text{Removed} = 2500 \times \frac{100}{117} = 2136.75\ \text{g CaCO}_3 \quad\Rightarrow\quad \frac{2136.75}{3500} = 0.6105\ \text{g/L} = \boxed{610\ \text{ppm}}$$

### Q3A — Atom economy calculations

**1) CH₃–CH=CH–CH₃ + 3 O₂ → maleic anhydride (C₄H₂O₃) + 3 H₂O**

- Desired: C₄H₂O₃ = 48+2+48 = **98**. Reactants: C₄H₈ 56 + 3O₂ 96 = **152** → AE = 98/152 = **64.5%**

**2) C₆H₅NH₂ (93) + (CH₃CO)₂O (102) → C₆H₅NHCOCH₃ (acetanilide, 135) + CH₃COOH (60)**

- Reactants 195; desired acetanilide 135 → AE = 135/195 = **69.2%** (waste = acetic acid, 30.8% of mass)

---

## Part C — Practice set (same pattern)

**P1.** Lime (90% pure) and soda (95% pure) for 20,000 L containing Ca(HCO₃)₂ 24.3, Mg(HCO₃)₂ 14.6, CaSO₄ 13.6, MgCl₂ 9.5, CaCl₂ 11.1, SiO₂ 10 mg/L.
> [!success]- Answer
> CaCO₃-eq: 15 + 10 + 10 + 10(MgCl₂) + 10(CaCl₂) = 55. Lime = 0.74[15 + 2(10) + 10(MgCl₂)] = 33.3 mg/L → 666 g pure → **740 g**. Soda = 1.06[10 + 10 + 10] = 31.8 mg/L → 636 g pure → **669.5 g**.

**P2.** 25 mL standard hard water (1.5 g/L) needed 30 mL EDTA; 75 mL sample needed 25 mL EDTA; after boiling 15 mL EDTA. Find all three hardnesses.
> [!success]- Answer
> 1 mL EDTA ≡ (25 × 1.5)/30 = 1.25 mg. Total = 25 × 1.25/75 = **416.7 ppm**; permanent = 15 × 1.25/75 = **250 ppm**; temporary = **166.7 ppm**.

**P3.** Zeolite softener treats 6000 L/day, regeneration uses 30 L of 80 g/L NaCl. Hardness?
> [!success]- Answer
> 2400 × 100/117 = 2051.3 g → 2051.3/6000 = **0.342 g/L = 342 ppm**.

**P4.** Atom economy: (a) C₆H₆ + CH₃Cl → C₆H₅CH₃ + HCl (toluene desired); (b) CH₄ + 2O₂ → CO₂ + 2H₂O (CO₂ desired; then water desired).
> [!success]- Answer
> (a) 92/(78+50.5) = 92/128.5 = **71.6%**. (b) CO₂ desired: 44/80 = **55%**; H₂O desired: 36/80 = **45%** — direction (which product you want) changes AE.

**P5.** Theory bank: temporary vs permanent (5 differences incl. which salts boiler-scale) · cold vs hot lime-soda (residuals, coagulant) · zeolite pros/cons · why zeolite is "base-exchange" · EDTA principle + EBT colours + buffer · 任意 4 green-chemistry principles with examples.

---

## Exam-day cheat card

| Concept | One-liner |
|---|---|
| Hardness | Ca/Mg salts eating soap; report as CaCO₃ ppm |
| Temporary | Bicarbonates → boiled away |
| Permanent | Sulfates/chlorides → need chemicals |
| Lime | 74/100 × [temp + Mg salts]; Mg(HCO₃)₂ ×2 |
| Soda | 106/100 × [Ca-permanent + Mg-permanent] |
| Never counted | SiO₂, NaCl, Na⁺/K⁺ salts (trick data) |
| Zeolite | hardness = m(NaCl) × (100/117) ÷ volume |
| EDTA | get mg/mL from standard → sample → boiled sample; temp = total − perm |
| EBT colour | wine-red (hardness) → blue (endpoint) |
| Atom economy | M(desired)/M(all reactants) ×100; not the same as yield |
| Adipic acid | HNO₃→N₂O bad / H₂O₂ + Na₂WO₄ in water good (prevention, catalysis, benign reagents/solvents) |

## Cross-Links

- [[module-1-water-technology-hardness]] — theory home for all Q1/Q2 content
- [[mse-revision-chem-m1-water]] — condensed exam-facing pack (methods 1–4)
- [[edta-numericals-worked-bank]] · [[zeolite-process-numericals]] · [[ion-exchange-numericals]] — more worked numericals of each type
- [[green-chemistry-twelve-principles]] — Q3 theory depth
- [[mse-flashcards-chem-m1]] · [[mse-recall-test-chem-m1]] — other half of the MSE drill set ([[mse-study-method]], [[mse-2026-10-26-5-day-plan]])
- [[01-Areas/Engineering/engineering-chem/INDEX|Chem Module Index]]
