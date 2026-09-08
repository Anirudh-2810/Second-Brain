---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Chem Lab Expt 5 — Corrosion Assessment of Rebar (PZT/EMI)"
tags: [btech, engineering-chemistry, chem-lab, corrosion, rebar, pzt, emi-technique, ndt]
last_updated: "2026-09-09"
description: "Chem Lab Expt 5 simulation write-up: PZT-patch EMI technique for bare vs embedded rebar corrosion, RMSD damage metric, stiffness–mass extraction and corrosion-rate formula."
---

## For future agent

Ingest of `Chem Lab/Corrosion analysis of rebar_.docx` + `Chem Lab/EXP 5 CORROSION ANALYSIS IN RC STRUCTURES.pdf` (same Expt 5; simulation based on Talakokula & Bhalla 2015 accelerated-corrosion data). Corrosion theory companion: [[module-3-electrochemistry-corrosion]].

# Expt 5 — Corrosion Assessment in Rebars via PZT Patches

**Objectives**: (5A) bare rebar, (5B) embedded rebar in a 150 mm concrete cube — assess corrosion non-destructively from PZT conductance signatures.

## 1. Setup (accelerated corrosion cell)

- Anode: rebar (bare or concrete-embedded); cathode: copper rod; electrolyte: brine, salinity 35 ppt.
- PZT patch bonded to rebar, wired to LCR meter; conductance spectrum recorded vs baseline at successive exposure hours (animation + Excel plotting in the simulation).

## 2. Damage metric — RMSD

Root-mean-square deviation of conductance from baseline over $n$ frequency points ($G_i^0$ baseline, $G_i^1$ damaged):

$$\mathrm{RMSD} = \sqrt{\frac{\sum_{i=1}^{n}\,(G_i^1 - G_i^0)^2}{\sum_{i=1}^{n}\,(G_i^0)^2}} \times 100\%$$

Plot RMSD histogram across damage states: rising RMSD + shifting resonance peaks = progressive corrosion. Extract equivalent stiffness $K$ (falls) and mass $M$ from the signatures.

## 3. Corrosion rate from mass loss

$$\mathrm{CR\;(mm/yr)} = \frac{K\,\Delta m}{a\,T\,D}$$

$K = 8.76\times10^4$, $\Delta m$ = mass loss (g), $a$ = exposed area ($\mathrm{cm^2}$), $T$ = exposure (h), $D = 7.8\ \mathrm{g/cm^3}$ for steel.

## 4. Bare vs embedded (viva contrast)

Bare rebar corrodes faster (direct brine contact); embedded bar is delayed by concrete cover (chloride diffusion + carbonation control access). Same PZT/EMI pipeline quantifies both — the technique's value is **in-situ RC-structure monitoring** without breaking concrete.

## 5. Conclusion template

"Corrosion of bare/embedded rebar was assessed via PZT-EMI signatures; RMSD rose monotonically with exposure; corrosion rate computed as ___ mm/yr."
