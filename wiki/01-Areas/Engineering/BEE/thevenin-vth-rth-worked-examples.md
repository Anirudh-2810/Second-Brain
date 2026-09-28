---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "Module 1 — Thevenin Vth/Rth Worked Examples"
date: "2026-09-28"
tags: [btech, bee, thevenin, vth, rth, dc-circuits, network-theorems, worked-examples, exam-prep]
last_updated: "2026-09-28"
description: "All three worked Thevenin examples from Chapter_1.8_THEVENIN_DC.pdf with Vth, Rth and load values recomputed: 10Ω load (5.2V/1.2Ω/0.464A), mesh+star-delta example (10.93V/8.33Ω) and source-rich example (81V/8Ω/16.2V)."
confidence: high
source: "raw-sources/.../Semester 1/Bee/Module 1 DC Circuits/Chapter_1.8_THEVENIN_DC.pdf (9 pp, slides) + Bee Lab/Expt_2_Thevenin Theorem_25-26.docx"
---

## For future agent

Example bank distilled from the Ch 1.8 Thevenin slide deck — theory home is [[module-1-dc-circuits]] §6, bench procedure is [[lab-dc-theorems-expts-2-5]] §1, formulas in [[formula-sheet-bee]]. Nothing here duplicates those pages: only the statement wording, the 5-step recipe as taught, and the **three solved numericals with their final Vth/Rth/IL answers**. Arithmetic of each answer was re-derived during ingest; one handwritten corner value on Ex. 2 is flagged (TBC).

# Thevenin — Statement, Method & 3 Worked Examples

## 1. Statement (as taught)

Any **linear, active, bilateral network** can be replaced by a voltage source $V_{th}$ in series with a resistance $R_{th}$, where

- $V_{th}$ = **open-circuit voltage** across the two terminals (voltage with $R_L$ removed)
- $R_{th}$ = internal resistance of the network **as viewed back into open-circuited terminals A–B**, with all energy sources replaced by their internal resistance — ideal **voltage sources → 0 Ω (short)**, ideal **current sources → ∞ Ω (open)**.

## 2. Five-step recipe

1. **Remove** load resistance $R_L$ from the network.
2. Find **$V_{th}$** = open-circuit voltage across A–B by any suitable method (mesh / nodal / source transformation).
3. Find **$R_{th}$** = resistance looking back into A–B with sources killed.
4. Draw the **Thevenin equivalent** ($V_{th}$ series $R_{th}$).
5. Reconnect $R_L$ and read off $I_L = \dfrac{V_{th}}{R_{th} + R_L}$ (or $V_L$ by division).

## 3. Example 1 — two parallel source branches, $R_L = 10\ \Omega$

*Branches: 6 V with 2 Ω ‖ 4 V with 3 Ω; load 10 Ω across the pair.*

1. **Remove $R_L = 10\ \Omega$** → single loop of the two branches.
2. **$V_{th}$:** KVL, $-4 - 3I - 2I + 6 = 0 \Rightarrow 5I = 2 \Rightarrow I = 0.4$ A.
   $V_{3\Omega} = 3 \times 0.4 = 1.2$ V → $V_{th} = 4 + 1.2$
   $$\boxed{V_{th} = 5.2\ \text{V}}$$
3. **$R_{th}$:** both sources shorted → 2 Ω ‖ 3 Ω:
   $$R_{th} = \frac{3 \times 2}{3 + 2} = \frac{6}{5} \Rightarrow \boxed{R_{th} = 1.2\ \Omega}$$
4. Equivalent: 5.2 V source with 1.2 Ω, terminals A–B.
5. $$I_{10\Omega} = \frac{5.2}{1.2 + 10} = \boxed{0.464\ \text{A}}$$

## 4. Example 2 — mesh analysis + star→delta, $R_L = 15\ \Omega$

*Network: 20 V / 60 V / 40 V sources with 15 Ω, 20 Ω, 15 Ω, 10 Ω, 5 Ω, 5 Ω resistors; load 15 Ω (value read off slide (TBC) — topology per slide diagram).*

1. **Remove $R_L = 15\ \Omega$**, terminals A–B across the removed branch.
2. **$V_{th}$ by mesh analysis** (two meshes, currents $I_1$ bottom, $I_2$ top):
   - Mesh 1: $40 - 10I_1 - 5(I_1 - I_2) - 5I_1 = 0 \Rightarrow 20I_1 - 5I_2 = 40$
   - Mesh 2: $-60 - 15I_2 - 5(I_2 - I_1) - 20I_2 = 0 \Rightarrow 5I_1 - 40I_2 = 60$
   - Solving: $I_1 = 1.67$ A, $I_2 = -1.29$ A
   - Walk A→B: $V_{th} = 20 + V_{10\Omega} + V_{20\Omega} = 20 + (1.67 \times 10) - (1.29 \times 20) = 20 + 16.7 - 25.8$
   $$\boxed{V_{th} \approx 10.9\ \text{V}\ (\text{slide answer } 10.93\ \text{V})}$$
3. **$R_{th}$ by star→delta** on the 10/20/5 star (sources killed):
   $$\Sigma R = R_1R_2 + R_2R_3 + R_3R_1 = (10 \times 20) + (20 \times 5) + (10 \times 5) = 350$$
   $$R_A = \frac{350}{5} = 70\ \Omega,\quad R_B = \frac{350}{10} = 35\ \Omega,\quad R_C = \frac{350}{20} = 17.5\ \Omega$$
   then series/parallel reduction → slide answer $\boxed{R_{th} = 8.33\ \Omega}$ (reduction not written out on the slide (TBC)).
4. Equivalent + load: $I_{15\Omega} = \dfrac{10.93}{8.33 + 15} \approx 0.469$ A — slide corner note read as ≈0.469 A (handwriting (TBC)).
   $$\boxed{I_L \approx 0.469\ \text{A}}$$

## 5. Example 3 — mixed sources, find voltage across $2\ \Omega$

*5 V source with 5 Ω, 4 A current source, 3 Ω, load 2 Ω, 7 A current source.*

1. **Remove $R_L = 2\ \Omega$** (terminals A–B).
2. **$V_{th}$ by nodal** at the node above the 4 A source (KCL: entering = leaving):
   $$7 + 4 = \frac{V - 5}{5} \Rightarrow 11 = \frac{V-5}{5} \Rightarrow V - 5 = 55 \Rightarrow V = 60\ \text{V}$$
   So $V_{4A} = V = 60$ V, and the 7 A feeds the open A–B path through 3 Ω: $I = 7$ A.
   $$V_{th} = 3I + V_{4A} = 3 \times 7 + 60 \Rightarrow \boxed{V_{th} = 81\ \text{V}}$$
   *Mesh cross-check on the slide:* $I_2 = -7$ A, $I_1 + 4 = I_2 \Rightarrow I_1 = -11$ A, $V_{4A} = 11 \times 5 + 5 = 60$ V → same 81 V.
3. **$R_{th}$:** V-source short, both current sources open → looking into A–B: $5 + 3$
   $$\boxed{R_{th} = 8\ \Omega}$$
4. Reconnect 2 Ω, voltage division:
   $$V_{2\Omega} = \frac{2 \times 81}{2 + 8} = \frac{162}{10} \Rightarrow \boxed{V_{2\Omega} = 16.2\ \text{V}}$$

## 6. Lab linkage (BEEL Expt 2, course 316U06L102)

Bench steps, observation table and viva live in [[lab-dc-theorems-expts-2-5]] §1 (set 10 V → measure $V_{th}$ open-circuit → kill sources → measure $R_{th}$ → build equivalent → $I_L$ → verify theory; record theoretical vs practical for $V_{th}$, $R_{th}$, $I_L$).

Post-lab questions from the record (CO1, /20): **"State what is meant by linear network"** and **"State the different applications of a linear network."** (left blank in the docx). Standard answer anchor: a linear network obeys **superposition + homogeneity** — its V–I relation is a straight line through the origin for resistive elements; applications = any analysis that lets you replace a complex block by $V_{th}$–$R_{th}$ (source simplification, load matching, amplifier/sensor interfacing) `(standard theory, not from the docx)`.

## Self-check

1. Restate the statement — why must the network be *linear* and *active*?
2. Example 1 without looking: get 5.2 V / 1.2 Ω / 0.464 A.
3. Example 3: why does 7 A pass through the 3 Ω once $R_L$ is removed?
4. Star→delta in Ex. 2: reproduce ΣR = 350 → 70/35/17.5.
5. $R_{th}$ source-killing rule for ideal V and ideal I sources — one line each.

## See also

- [[module-1-dc-circuits]] — theorem theory, mesh/nodal method, star–delta formulas, exam failure modes
- [[lab-dc-theorems-expts-2-5]] — Expt 2 bench procedure + observation table
- [[formula-sheet-bee]] — $I_L = V_{th}/(R_{th}+R_L)$, Norton conversion
- [[source-map-bee-sem1]] — file registry (Ch 1.8 row)
- [[modules/../01-Areas/Engineering/engineering-math/module-1-matrices|eng-math M1]] — solving the mesh pair by matrices
