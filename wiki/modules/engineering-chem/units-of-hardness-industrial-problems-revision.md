---
module: "engineering-chem"
topic: "Revision: Units of Hardness + Industrial Problems of Water"
tags: [engineering-chemistry, water-technology, hardness, units, ppm, clarke, french, german, scale, sludge, caustic-embrittlement, boiler-corrosion, priming, foaming, revision]
last_updated: "2026-08-21"
prerequisites: ["CaCO₃ Equivalent Concept", "Temporary vs Permanent Hardness", "Boiler Basics"]
---

# Revision: Units of Hardness + Industrial Problems of Water

> One-page revision of the two exam topics: **how hardness is expressed** (with conversions) and the **four industrial problems hard water causes** (mostly in boilers). Memorize the numbers, understand the *why*.

---

## Part A — Units of Hardness

### The rule that rules everything
Hardness is **never** expressed as the actual salt — it is always converted to **mg/L (ppm) as CaCO₃**. Reason: one common unit so different waters are directly comparable.

$$\text{Hardness as CaCO}_3 = \text{mass of salt} \times \frac{\text{Eq. wt CaCO}_3\ (50)}{\text{Eq. wt of salt}}$$

### The five units

| Unit | Symbol | Definition | → ppm (as CaCO₃) |
|---|---|---|---|
| Parts per million | ppm | 1 part CaCO₃ per 10⁶ parts water | **1 ppm = 1 mg/L** |
| Milligrams per litre | mg/L | mg CaCO₃ per litre | 1 mg/L = 1 ppm |
| Degree Clarke | °Cl | 1 grain (64.8 mg) CaCO₃ per Imp. gallon (4.546 L) | **1 °Cl = 14.25 ppm** |
| Degree French | °Fr | 1 part CaCO₃ per 10⁵ parts water | **1 °Fr = 10 ppm** |
| Degree German | °dH | 10 mg CaO per litre | **1 °dH = 17.9 ppm** |

**Memorize:** 1 ppm = 1 mg/L · 1 °Cl = 14.25 ppm · 1 °Fr = 10 ppm · 1 °dH = 17.9 ppm

### Mini worked examples

- $5^\circ\text{Cl}$: $5 \times 14.25 = 71.25$ ppm
- $7^\circ\text{Fr}$: $7 \times 10 = 70$ ppm
- $10^\circ\text{dH}$: $10 \times 17.9 = 179$ ppm
- **Reverse:** 100 ppm → $\frac{100}{14.25} = 7.02^\circ\text{Cl}$

---

## Part B — Industrial Problems of Water

### The four boiler troubles

| Trouble | Cause | Effect | Prevention |
|---|---|---|---|
| **1. Scale** | CaSO₄ (has **inverse solubility** — less soluble as T↑) deposits on hot surfaces | Poor heat transfer → hot spots → tube rupture, fuel waste | Soften feed water, blow-down, internal treatment |
| **1. Sludge** | CaCO₃, Mg(OH)₂, MgCO₃ (normal solubility) precipitate in bulk water | Soft loose deposit; may blanket metal / scale up later | Blow-down, sludge conditioners |
| **2. Caustic embrittlement** | Na₂CO₃ → NaOH at high T; NaOH concentrates in cracks, dissolves cementing Fe₃O₄ | Cracking of boiler metal (inter-granular) | Na₂SO₄/Na₃PO₄ inhibitor, keep **Na₂SO₄ : NaOH ≈ 1 : 1** |
| **3. Boiler corrosion** | Dissolved O₂, CO₂, acidic water attack metal (Fe → Fe²⁺) | Pitting, thinning of tubes | Deaeration, Na₂SO₃ (O₂ scavenger), alkaline pH |
| **4. Priming** | High dissolved/suspended solids, sudden steam demand → water droplets carried with steam | Wet steam, carry-over of salts | Blow-down, avoid overloading boiler |
| **4. Foaming** | Oily/suds-producing substances, high solids | Persistent froth → same carry-over trouble | Anti-foam agents, filtration |

### Quick memory hooks

- **Scale = hard & dangerous** (inverse-solubility CaSO₄ sticks to hot metal). **Sludge = soft & loose** (normal-solubility salts settle out).
- **Caustic embrittlement = cracks** (NaOH + cracks). **Corrosion = thinning/holes** (O₂ attack). **Priming/Foaming = wet steam** (carry-over).
- Oxygen is the corrosion villain → **deaerate + Na₂SO₃**.

### Two numbers worth remembering

- CaSO₄ starts scaling badly above ~**1500 ppm**.
- Blow-down keeps dissolved solids ≤ **3000 ppm** (typical limit).

---

## Quick-revision checklist

- [x] Hardness always expressed as CaCO₃ equivalent (Eq. wt 50)
- [x] The 3 conversion numbers: °Cl 14.25 · °Fr 10 · °dH 17.9
- [x] Scale vs sludge — cause difference (inverse vs normal solubility)
- [x] Caustic embrittlement inhibitor + ratio
- [ ] Corrosion → O₂ scavenging + deaeration
- [ ] Priming vs foaming → carry-over, control by blow-down

## CROSS-REFERENCES

- Full module: [[module-1-water-technology-hardness]] (§1.3 Units, §1.6 Scale vs Sludge, §1.7 Boiler Troubles)
- Softening methods: lime-soda · zeolite · ion-exchange · RO (same module)
- Related: [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics]] · [[module-3-electrochemistry-corrosion]]