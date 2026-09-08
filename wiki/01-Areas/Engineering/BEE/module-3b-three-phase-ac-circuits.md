---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "Module 3B — Three-Phase AC Circuits & Two-Wattmeter Method"
tags: [btech, bee, three-phase, star-delta, two-wattmeter, active-reactive-power]
last_updated: "2026-09-09"
description: "Three-phase AC circuits from Module-3 sources: star–delta systems, line vs phase quantities, balanced power formulas and the two-wattmeter derivation with a worked example."
---

## For future agent

New theory page built from `Bee/Module 3 Three Phase AC Circuits/Chapter_3_Three phase ac.pdf` + `3 Phase AC.pdf` (read; content is scanned-image style so derivations are reconstructed standard theory — high confidence). This fills the gap between [[module-2-ac-circuits]] (single-phase) and [[module-4-dc-machines-and-induction-motors]] (loads). Bench companion: [[lab-ac-pf-three-phase-motor-expts-6-8]] (Expt 7). Formulas duplicated in [[formula-sheet-bee]] (suggested addition — see return notes).

# Three-Phase AC Circuits

## 1. Why three phase

Three windings spaced $120^\circ$ give constant instantaneous power (no pulsation), 1.5× power per conductor mass vs single phase, self-starting rotating field for motors, and a neutral for single-phase tapping (4-wire star).

## 2. Star (Y) vs Delta (Δ)

| | Star | Delta |
|---|---|---|
| Connection | Similar ends joined → neutral N; 4-wire ($3\phi$ + N) | End-to-start loop; 3-wire, no neutral |
| Line vs phase | $V_L = \sqrt{3}\,V_{ph}$, $I_L = I_{ph}$ | $V_L = V_{ph}$, $I_L = \sqrt{3}\,I_{ph}$ |
| Neutral | Carries unbalance current; $V_{ph}$ available L–N | No neutral; one L–L fault circulates in loop |
| Use | Distribution (230 V L–N / 400 V L–L), lighting loads | Motor run connection, heavy balanced loads |

Phase sequence R–Y–B (RYB); reversed sequence reverses motor rotation.

## 3. Balanced-load power (one formula rules all)

Per phase $P_{ph} = V_{ph}I_{ph}\cos\phi$. Three phases, substituting §2 relations, collapse to a single line-quantity form for **both** connections:

$$P = \sqrt{3}\,V_L I_L\cos\phi,\qquad Q = \sqrt{3}\,V_L I_L\sin\phi,\qquad S = \sqrt{3}\,V_L I_L$$

Worked example: 400 V, 10 A, $\cos\phi = 0.8$ lag → $P = \sqrt{3}(400)(10)(0.8) \approx 5.54\ \mathrm{kW}$; $Q \approx 4.16\ \mathrm{kVAR}$; $S \approx 6.93\ \mathrm{kVA}$.

## 4. Two-wattmeter method (derive this)

Current coils in R and B lines, pressure coils to Y line. With phase angle $\phi$:

$$W_1 = V_L I_L\cos(30^\circ+\phi),\qquad W_2 = V_L I_L\cos(30^\circ-\phi)$$

$$P = W_1+W_2 = \sqrt{3}V_LI_L\cos\phi,\qquad \tan\phi = \frac{\sqrt{3}\,(W_2-W_1)}{W_1+W_2}$$

so PF follows from the two readings alone. Landmarks: $\phi=0 \Rightarrow W_1=W_2$; $\phi=60^\circ \Rightarrow W_1=0$; $\phi>60^\circ \Rightarrow$ one reading negative (reverse coil, subtract). Expt 7 verifies this on a unity-PF lamp bank where $W_1 = W_2$ is expected.

## 5. Unbalance note (theory only)

Unbalanced star needs the neutral ($I_N \ne 0$); breaking N shifts phase voltages (floating neutral — lighting burns out). Unbalanced delta circulates zero-sequence current internally. Numericals in this course stay balanced.
