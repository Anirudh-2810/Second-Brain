---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "BEEL Expts 2–5 — DC Network Theorems"
tags: [btech, bee, beel-lab, thevenin, norton, superposition, maximum-power-transfer]
last_updated: "2026-09-09"
description: "BEE lab Expts 2–5 bench guide: Thevenin, Norton, superposition and maximum-power-transfer verification with procedures, observation tables and a worked Thevenin example."
---

## For future agent

Bench ingest of `Bee Lab/Expt_2_Thevenin Theorem_25-26.docx`, `Expt_3_Norton_Theorem_25-26.docx` (VLab), `Expt_4_Superposition_Theorem_25-26.docx` (VLab), `Expt_5_Maximum_Power_Theorem_25-26.docx` (all CO1). Theory companion: [[module-1-dc-circuits]]; formulas: [[formula-sheet-bee]]. AC-side labs live in [[lab-ac-pf-three-phase-motor-expts-6-8]]; full file registry in [[source-map-bee-sem1]].

# BEEL Expts 2–5 — DC Theorems

## 1. Expt 2 — Thevenin's theorem (hardware)

**Aim**: verify Thevenin for a given circuit. Statement: any linear active bilateral network → $V_{th}$ in series with $R_{th}$ ($V_{th}$ = open-circuit voltage at load terminals A–B; $R_{th}$ = resistance looking back with sources killed — voltage→short, current→open).

Procedure: (1) connect circuit, set 10 V, measure $V_{th}$ across A–B with $R_L$ removed; (2) kill sources, measure $R_{th}$ across A–B; (3) build equivalent, compute $I_L = V_{th}/(R_{th}+R_L)$; (4) verify theoretically. Observation table: $V_{th}$ / $R_{th}$ / $I_L$ × theoretical vs practical.

Worked example (typical paper pattern): 10 V source, $R_1 = 4\,\Omega$ series from A, $R_2 = 6\,\Omega$ across A–B, load $R_L = 5\,\Omega$ across B branch. $V_{th} = 10\cdot 6/(4+6) = 6\ \mathrm{V}$ (divider); $R_{th} = 4\parallel 6 = 2.4\ \Omega$; $I_L = 6/(2.4+5) \approx 0.81\ \mathrm{A}$. Viva: "linear network" = obeys superposition + homogeneity (V–I straight line through origin for resistors).

## 2. Expt 3 — Norton's theorem (VLab, bes-iitr)

Dual of Thevenin: network → current source $I_N$ (short-circuit current at A–B) in parallel with $R_N$ (= $R_{th}$). VLab procedure: open linked IIT experiment, measure $R_N$ with sources killed, measure $I_{SC}$, build equivalent $I_L = I_N\cdot R_N/(R_N+R_L)$, attach screenshots. Observation table: $R_N$ / $I_N$ / $I_L$ × theoretical vs practical. Conversion check: $V_{th} = I_N R_N$ must match Expt 2's $V_{th}$ for the same network.

## 3. Expt 4 — Superposition (VLab, asnm-iitkgp)

Resultant branch current = algebraic sum of currents from each source acting alone (others replaced by internal resistance). VLab cases: both sources → $V_1$ only ($V_2$ shorted) → $V_2$ only ($V_1$ shorted); verify $I' + I'' = I$ per branch for 5 sets of $R_1,R_2,R_3,V_1,V_2$, one set verified theoretically. Viva trap: valid only for **linear** networks and for current/voltage — never power ($P = I^2R$ is nonlinear; $P' + P'' \ne P$).

## 4. Expt 5 — Maximum power transfer (hardware)

$V_S = 15\ \mathrm{V}$; vary $R_L$ 100 Ω→1 kΩ in 100 Ω steps; record $I_L, V_L$, compute $P_L = I_L^2 R_L$; plot $P_L$ vs $R_L$ — peak at $R_L = R_S$ (source resistance), where $P_{max} = V_S^2/(4R_S)$. Conclusion extension (choose one): a real application (audio-amplifier→speaker matching, RF antenna matching, solar MPPT as dynamic case) with block diagram, or a Thevenin-based sample solution showing $R_L = R_{th}$.

## Common viva lines

Thevenin↔Norton source transformation; why $R_{th} = R_N$; why superposition fails for power; efficiency at max-power point is only 50% (hence used for signal transfer, not power systems).
