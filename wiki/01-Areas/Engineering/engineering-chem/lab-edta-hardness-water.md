---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Chem Lab Expt 3 — EDTA Hardness of Water"
tags: [btech, engineering-chemistry, chem-lab, edta, hardness, complexometric-titration]
last_updated: "2026-09-09"
description: "Chem Lab Expt 3 write-up: EDTA complexometric titration for total, permanent and temporary hardness with EBT indicator, CaCO3-equivalent calculations and viva points."
---

## For future agent

Full ingest of `Chem Lab/EDTA-Hardness.docx` (Expt 3). Theory companion is [[module-1-water-technology-hardness]] — read that for CaCO₃-equivalent convention and boiler troubles; this page is the bench procedure + calculation template.

# Expt 3 — Determination of Hardness by EDTA Method

**Aim**: determine total, permanent, and temporary hardness of a water sample by complexometric titration.

## 1. Principle

EDTA (disodium salt) forms stable 1:1 complexes with $\mathrm{Ca^{2+}}$/$\mathrm{Mg^{2+}}$. At pH 10 ($\mathrm{NH_4OH}$/$\mathrm{NH_4Cl}$ buffer) the complexation is quantitative. Eriochrome Black-T (EBT) forms a **wine-red** metal–indicator complex that is less stable than metal–EDTA; EDTA displaces it at the end point, freeing blue indicator:

$$\mathrm{M\!-\!In\;(wine\;red) + EDTA \to M\!-\!EDTA\;(colourless) + In\;(blue)}$$

## 2. Requirements

Standard hard water (1 mg/mL as $\mathrm{CaCO_3}$), unknown sample, 0.01 M EDTA, EBT indicator, pH-10 buffer; burette, pipette, conical flask.

## 3. Procedure (three parts)

- **Part I (standardisation)**: 10 mL standard hard water + buffer + EBT → titrate with EDTA to wine-red→blue. Reading $V_1$ mL.
- **Part II (total hardness)**: 50 mL unknown sample, same titration. Reading $V_2$ mL.
- **Part III (permanent hardness)**: boil 50 mL sample down to ~12 mL (drives off temporary hardness as $\mathrm{CaCO_3 \downarrow}$: $\mathrm{Ca(HCO_3)_2 \xrightarrow{\Delta} CaCO_3 + H_2O + CO_2}$), cool, filter, titrate filtrate. Reading $V_3$ mL.

## 4. Calculations

Standard: $V_1$ mL EDTA $\equiv 10$ mg $\mathrm{CaCO_3}$ → 1 mL EDTA $\equiv 10/V_1$ mg $\mathrm{CaCO_3}$.

$$ \text{Total hardness} = \frac{V_2}{V_1}\times 10\ \text{mg per 50 mL} \;\Rightarrow\; \times 20 = \text{mg/L (ppm)} $$

$$ \text{Permanent hardness from } V_3 \text{ identically; Temporary} = \text{Total} - \text{Permanent} $$

Endpoint logic: if Part III stays blue without titration, permanent hardness is nil (all hardness was temporary).

## 5. Viva points

- Why pH 10? EDTA complexation is pH-dependent; acidic medium gives incomplete complexation and a fading endpoint.
- Why boil in Part III? Removes bicarbonates (temporary hardness) so the residual titration reads permanent hardness only.
- Units: always report as mg/L as $\mathrm{CaCO_3}$; see [[module-1-water-technology-hardness]] for Clarke/French-degree conversions.
