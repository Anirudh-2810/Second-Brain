---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Source Map — Sem-1 Chemistry Theory & Lab Files"
tags: [btech, engineering-chemistry, source-map, syllabus-map]
last_updated: "2026-09-09"
description: "Complete registry of all Sem-1 Chemistry and Chem Lab raw-source files: what was ingested in depth, what was summarized, and where each experiment lives in the wiki."
---

## For future agent

Catalog of `raw-sources/drive-download-20260908T190927Z-1-001/Semester 1/Chem/` (8 files) and `Chem Lab/` (8 files). Read this before re-ingesting chemistry sources — it records depth decisions so work is not repeated. Detailed pages: [[green-chemistry-twelve-principles]], [[reaction-mechanisms-named-reactions]], [[lab-edta-hardness-water]], [[lab-emf-gibbs-equilibrium]], [[lab-biodiesel-green-synthesis]], [[lab-corrosion-rebar-pzt]].

# Source Map — Sem-1 Chemistry

## 1. Theory (`Chem/`)

| File | Depth | Notes |
|------|-------|-------|
| `Chem/Corrosion/Corrosion.pdf` (49 pp) | Skim-verified | Dry vs wet corrosion, oxide-film types, Pilling–Bedworth rule — already covered in [[module-3-electrochemistry-corrosion]]; no new page |
| `Chem/green chem/Green Chemistry FYBTech.pdf` (57 slides) | **Full ingest** | → [[green-chemistry-twelve-principles]] |
| `Chem/Reaction Mechanism/Reaction mechanism (1).pptx` | **Full ingest** | → [[reaction-mechanisms-named-reactions]] |
| `Chem/Reaction Mechanism/Peter Sykes Organic Chem Mechanism.pdf` | Catalogued only | Standard reference textbook; consult per-reaction on demand, do not bulk-ingest |
| `Chem/Water/Water (given on LMS).pdf` (81 pp) | Skim-verified | Hardness/softening/boiler troubles — already covered in [[module-1-water-technology-hardness]] |
| `Chem/Water/Study Material (3).pdf` | Catalogued only | Variant of LMS water material |
| `Chem/Water/Water-ref.pdf` | Catalogued only | Reference variant of water material |

## 2. Lab (`Chem Lab/`)

| File | Depth | Notes |
|------|-------|-------|
| `GLP.docx` (Expt 1) | Summarized here | Good Lab Practices: coat/closed shoes, no food/phones, fume-hood volatiles, acid→baking-soda / base→vinegar neutralisation, 15-min eye/skin wash, never weigh hot objects, no unauthorised expts |
| `EMF.docx` (Expt 2) | **Full ingest** | → [[lab-emf-gibbs-equilibrium]] |
| `EDTA-Hardness.docx` (Expt 3) | **Full ingest** | → [[lab-edta-hardness-water]] |
| `Biodiesel expt.docx` + `EXP 4 BIODIESEL PRODUCTIOn.pdf` (Expt 4) | **Full ingest (both)** | Same experiment; docx adds assignment Q&A → [[lab-biodiesel-green-synthesis]] |
| `Corrosion analysis of rebar_.docx` + `EXP 5 CORROSION ANALYSIS IN RC STRUCTURES.pdf` | **Full ingest (both)** | Same Expt 5 (PZT/EMI simulation) → [[lab-corrosion-rebar-pzt]] |
| `Write-up Index.docx` | Indexed here | FY26 expt list: 1 GLP · 2 EMF (VLab) · 3 EDTA hardness · 4 biodiesel · **5 benzalacetophenone via Claisen–Schmidt** (no procedure file supplied — theory only in [[reaction-mechanisms-named-reactions]]) · 6 rebar-corrosion NDT |

## 3. Gaps / watchlist

- Claisen–Schmidt bench procedure (Expt 5) has no source file — if supplied later, create `lab-benzalacetophenone-claisen-schmidt.md`.
- JEE-level cross-links live in [[../chemistry/formula-sheet-organic|organic formula sheet]] and [[../chemistry/formula-sheet-physical|physical formula sheet]] — engineering pages link out, never duplicate.
