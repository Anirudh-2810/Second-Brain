---
course_code: "ENG-BIO"
course_name: "Engineering Biology"
unit: "Unit 3 — Bioprocess Engineering & Fermentation"
tags: [btech, engineering-biology, bioprocess, fermentation, fermentor, monod-kinetics, downstream-processing]
last_updated: "2026-09-09"
description: "Unit 3 notes: fermentor design (agitator, baffles, sparger), upstream and downstream processing, Monod and Arrhenius kinetics, and in-line/on-line/at-line monitoring."
---

## For future agent

Ingest of `Bio/Unit 3 Bioprocess Engineering/Fermentation - Lectures 1&2` (fermentor design, surface vs submerged, STF), `Lecture 3` (upstream + downstream), `Lecture 4` (Monod/thermal kinetics), `Lecture 5` (monitoring), `Lecture 6` (downstream recap). Systems-scale use of E. coli models: [[unit-5-systems-biology]]. Oil-based bioproduct parallel: [[../engineering-chem/lab-biodiesel-green-synthesis|biodiesel lab]].

# Unit 3 — Bioprocess & Fermentation

## 1. Fermentor anatomy (design logic per part)

- **Agitator/impeller**: Rushton disc turbine (radial flow, high $O_2$ transfer, high shear — microbes OK, animal cells not) · vaned disc (compromise) · open variable-pitch turbine (radial + axial, flexible) · marine propeller (axial, gentle — shear-sensitive lines). Job: mix nutrients/$O_2$/cells, suspend solids, break bubbles, even heat.
- **Baffles** (4 vertical wall strips): kill vortex → turbulence → uniform T/pH/nutrients + better gas–liquid $O_2$ transfer.
- **Sparger** (air in): porous (lab, low throughput, clogs) · orifice/perforated pipe (yeast, effluent, SCP) · nozzle/single-pipe (modern stirred tanks, low ΔP, unblocking).
- **Asepsis**: sterilise vessel + air (membrane filtration) + medium (heat; filter-sterilise heat-labile feeds); sterile inoculum/feed/sampling, foam control, parameter control.

## 2. Fermentation modes & workhorse

Surface (fungi on solid/liquid surface, high $O_2$) vs **submerged** (suspended culture, agitation + aeration — industrial default: antibiotics, enzymes). **Stirred-tank fermentor** = workhorse (agitator + sparger; aerobic and anaerobic, e.g. penicillin).

## 3. Upstream (pre-fermentation order)

Strain selection/screening (primary qualitative agar → secondary quantitative yield; improve via mutation, recombination, cloning, fusion) → media formulation (inoculum-rich vs production C/N-optimal; cheap: molasses, corn-steep liquor, whey, lignocellulosic waste) → sterilisation → inoculum build-up (stepwise seed to cut lag).

## 4. Kinetics (the two equations)

Monod (growth vs limiting substrate):

$$\mu = \mu_{max}\,\frac{[S]}{K_s + [S]}$$

$[S] \ll K_s \Rightarrow \mu \approx (\mu_{max}/K_s)[S]$ (starved, slow); $[S] \gg K_s \Rightarrow \mu \to \mu_{max}$ (saturated). Arrhenius/thermal: $k = A e^{-E_a/RT}$ on $\mu_{max}$ — high $E_a$ = touchy process; past optimum, death/denaturation wins. Engineers set T from this trade-off.

## 5. Downstream (recovery order)

Cell disruption if intracellular (mechanical homogeniser; chemical/physical/lysozyme) → solid–liquid split (filtration, centrifugation, coagulation/flocculation; also flotation, sedimentation, membranes) → concentration (evaporation, precipitation, adsorption) → **purification** (chromatography: ion-exchange by charge, size-exclusion by volume, affinity by specific binding) → formulation (spray/freeze drying, crystallisation, sterile packaging).

## 6. Monitoring ladder (exam table)

| | In-line | On-line | At-line |
|---|---|---|---|
| Location | Inside vessel | External loop | Bench nearby |
| Sampling | None | Automatic | Manual |
| Speed | Real-time | Near-real-time | Minutes |
| Sterility risk | Lowest | Medium | Highest |
| Examples | pH/DO/T/pressure probes | Off-gas $O_2$/$CO_2$, auto-HPLC | Spectrophotometer, cell counts |

Sensors: T (RTD/thermistor), P (diaphragm/Bourdon/piezo), foam (conductivity → antifoam), pH (combination electrode), DO (galvanic/polarographic/fluorometric), $CO_2$ (Severinghaus).
