---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Green Chemistry — Twelve Principles & Atom Economy"
tags: [btech, engineering-chemistry, green-chemistry, atom-economy, sustainability, fy-btech]
last_updated: "2026-09-09"
description: "FY BTech green chemistry: twelve Anastas–Warner principles, atom-economy numericals, metathesis Nobel 2005, and link to the biodiesel lab synthesis."
---

## For future agent

Detailed ingest of `Chem/green chem/Green Chemistry FYBTech.pdf` (57 slides) for the engineering-chem domain. Pairs with the hands-on companion [[lab-biodiesel-green-synthesis]] (Expt 4 transesterification). For reaction-level detail see [[reaction-mechanisms-named-reactions]]; for fuels context see [[module-5-polymers-fuels]].

# Green Chemistry — Twelve Principles & Atom Economy

> Green chemistry = design of chemical products and processes that reduce or eliminate hazardous substances (Anastas & Warner). FY syllabus focus: the 12 principles as one-liners + **atom-economy numericals** + landmark examples (metathesis Nobel 2005, Bhopal MIC case).

## 1. Why it exists

Conventional manufacture of medicines, dyes, polymers, pesticides generates toxic waste → end-of-pipe treatment is costly and legislated. Green chemistry moves prevention **into the synthesis design**: choice of feedstock, solvent, catalyst, energy, and degradability. Sustainable development of the chemical industry is the stated objective.

## 2. Twelve principles (exam one-liners)

| # | Principle | One-line meaning + FY example |
|---|-----------|-------------------------------|
| 1 | Prevention of waste | Better to prevent waste than clean it up (waste-treatment plants raise process cost) |
| 2 | Atom economy | Maximize incorporation of all reactant atoms into product (see §3) |
| 3 | Less hazardous synthesis | Avoid toxic reagents/intermediates — e.g. methyl isocyanate (MIC, Bhopal tragedy) as the cautionary case |
| 4 | Safer chemicals | Preserve function, cut toxicity — e.g. replace DDT/gamaxane with biopesticides; clinical-trial screening of drugs |
| 5 | Safer solvents/auxiliaries | Avoid benzene, ether (flammable), CCl₄/CHCl₃ (ozone depletion); water is the universal safer solvent; perchloroethylene in dry cleaning replaced |
| 6 | Energy efficiency | Ambient-T/P processes; avoid reflux/distillation energy where possible |
| 7 | Renewable feedstocks | Vegetable oils, biomass over fossil feed (direct link: [[lab-biodiesel-green-synthesis]]) |
| 8 | Avoid derivatives | No protection/deprotection steps that add reagents + waste |
| 9 | Catalysis over stoichiometry | Catalytic NaOH in transesterification beats stoichiometric reagents |
| 10 | Design for degradation | Products break down post-use (biodegradable biodiesel vs petroleum diesel) |
| 11 | Real-time analysis | In-process monitoring prevents hazardous excursions |
| 12 | Accident prevention | Inherently safer chemistry (low-volatility, non-flammable choices) |

## 3. Atom economy — the numerical core

$$\%\,\text{Atom Economy} = \frac{\text{MW of desired product}}{\sum \text{MW of all reactants}} \times 100$$

Worked FY examples (from source slides):

- Phenyl acetate route: $\mathrm{C_6H_5OH + CH_3COCl \to C_6H_5OCOCH_3 + HCl}$ gives $\%AE = 92/(78+50.5) \approx 71.6\%$ — HCl is waste mass.
- Acetophenone: $\mathrm{C_6H_6 + CH_3COCl \to C_6H_5COCH_3 + HCl}$: $\%AE = 120/(78+78.5) \approx 76.7\%$.
- Acetanilide: $\mathrm{C_6H_5NH_2 + (CH_3CO)_2O \to C_6H_5NHCOCH_3 + CH_3COOH}$: $\%AE = 135/(93+102) \approx 69.2\%$.
- Contrast addition vs substitution: $\mathrm{C_6H_5OH + CO \to C_6H_5COOH}$ incorporates **all** reactant atoms → $\%AE = 100\%$. Addition/carbonylation chemistry is intrinsically greener than substitution (which always ejects a leaving group).

Exam trap: atom economy ≠ yield. A 100%-yield reaction can still have poor atom economy if a heavy by-product (HCl, acetic acid) is ejected.

## 4. Landmark example — olefin metathesis (Nobel 2005)

Chauvin, Grubbs, Schrock: metathesis catalysts cut reaction steps, run at ambient T/P in benign solvents, and slash hazardous waste — cited in-source as the model green reaction for pharma and advanced plastics.

## 5. How the biodiesel lab maps to principles

[[lab-biodiesel-green-synthesis]] demonstrates principles 7 (renewable oil), 9 (catalytic NaOH), 6 (55–60 °C water bath, below MeOH bp), 5 (methanol + water wash only), 10 (biodegradable product). Quote this mapping verbatim in viva.

## Source registry

| File | Status |
|------|--------|
| `Chem/green chem/Green Chemistry FYBTech.pdf` | Read fully — basis of this page |
| `Chem/Reaction Mechanism/Peter Sykes Organic Chem Mechanism.pdf` | Reference textbook — catalogued in [[source-map-chem-sem1]], not ingested |
