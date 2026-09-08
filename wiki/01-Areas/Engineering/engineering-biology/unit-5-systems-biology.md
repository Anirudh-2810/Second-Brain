---
course_code: "ENG-BIO"
course_name: "Engineering Biology"
unit: "Unit 5 — Systems Biology & Modelling"
tags: [btech, engineering-biology, systems-biology, metabolic-networks, sir-model, kegg, flux-balance]
last_updated: "2026-09-09"
description: "Unit 5 notes: networks-over-parts mindset, pathway databases and visualisation tools, E. coli and human metabolic models, Warburg effect, SIR modelling and agri/climate uses."
---

## For future agent

Ingest of `Bio/Unit 5 Systems Biology/Systems Lecture 1.pptx` (networks, tools, case studies), `Systems Lecture 2.pdf` (six modelling steps; medicine/agri/climate — read fully), `Systems Lecture 3.pptx` (dynamics/control/optimisation — skimmed, vocabulary-level). Data layer: [[unit-2b-bioinformatics-fasta-blast]]; manufacture layer: [[unit-3-bioprocess-fermentation]].

# Unit 5 — Systems Biology

## 1. Mindset

"The whole is greater than the sum of its parts": genes + proteins + metabolites as an interaction **network**, modelled and simulated — not isolated parts. Six modelling steps (exam list): define boundaries → identify components → collect data → develop model → simulate & validate → predict & optimise.

## 2. Toolbox

Databases: **KEGG** (metabolic maps + enzyme links) · **BioCyc/MetaCyc** (curated reactions + regulation) · **Reactome** (human pathways + disease links). Visualisation/analysis: **Cytoscape** (network graphs) · **CellDesigner** (SBGN biochemical maps) · **COBRA toolbox** (constraint-based reconstruction, flux-balance analysis in MATLAB).

## 3. Case studies

- **E. coli network**: genome + metabolome reconstruction predicting growth per nutrient — used to optimise industrial fermentation (ties to [[unit-3-bioprocess-fermentation]]).
- **Human Recon3D**: most complete human metabolic map — disease metabolism, drug targets, personalised medicine, diet response.
- **Warburg effect**: cancer cells favour glycolysis over oxidative phosphorylation even with $O_2$ — a systems-level therapeutic target. Also diabetes/obesity/CVD network models.
- **Metabolic engineering**: rewire pathways for biofuels, antibiotics, bioplastics; synthetic biology builds custom circuits/sensors de novo.

## 4. SIR disease modelling

Compartments Susceptible → Infected → Recovered with transmission rate $\beta$ and recovery rate $\gamma$:

$$\frac{dS}{dt} = -\beta SI,\qquad \frac{dI}{dt} = \beta SI - \gamma I,\qquad \frac{dR}{dt} = \gamma I$$

guides vaccination/quarantine (COVID-19 as cited case). Companion medical models: systems pharmacology (drug–target–pathway), organ conduction/neural sims, personalised dosing.

## 5. Agriculture & climate

Crops: DSSAT/APSIM growth–yield forecasts; precision agri (remote sensing + GIS + soil sensors → smart irrigation); nutrient-cycle sims, pest forecasting (locusts), genome-to-phenome breeding. Climate: coupled atmosphere–ocean–land–biosphere models for prediction and policy. Advantages: integrative, predictive, in-silico testing; challenges: data hunger, parameter uncertainty, validation cost.
