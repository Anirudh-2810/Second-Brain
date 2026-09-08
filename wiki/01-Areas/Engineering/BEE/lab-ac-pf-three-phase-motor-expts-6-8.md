---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "BEEL Expts 1, 6–8 — Components, PF, 3-Ph Power, DC Motor"
tags: [btech, bee, beel-lab, power-factor, two-wattmeter, three-phase, dc-motor]
last_updated: "2026-09-09"
description: "BEE lab Expts 1 and 6–8 bench guide: components and instruments study, power-factor improvement with parallel capacitor, three-phase two-wattmeter power, DC-motor speed control."
---

## For future agent

Bench ingest of `Bee Lab/Expt_1_Components_Instruments_25-26 (3).docx`, `Expt_6_PF_improvement_parallel.docx` (CO2), `Expt_7_Power_Measurement_25-26.docx` (CO3), `Expt_8_Speed Control of DC Motor (Virtual Lab).docx` (CO5). Theory: [[module-2-ac-circuits]] (PF/resonance), [[module-3b-three-phase-ac-circuits]] (two-wattmeter derivation), [[module-4-dc-machines-and-induction-motors]] (motor speed control). DC-theorem labs: [[lab-dc-theorems-expts-2-5]]; registry: [[source-map-bee-sem1]].

# BEEL Expts 1, 6–8

## 1. Expt 1 — Components & instruments (CO1)

Breadboard: each half-row (A–E / F–J) is one node; A1↔B1–E1 connected, A1↛A2, A1↛F1. Resistors: fixed (carbon-composition, wire-wound — constantan/manganin, metal-film) vs variable pots; specs = resistance + power rating + tolerance (colour code). Capacitors: ceramic/RF, electrolytic (polarised), tantalum, film — type sets frequency/voltage use. Instruments: CRO (waveform/phase/frequency display) + function generator (test source). Outcome: identify, read values, state one application each.

## 2. Expt 6 — PF improvement, parallel capacitor (CO2)

**Aim**: raise PF of a single-phase R–L load with a parallel capacitor. Motor magnetising (lagging) current is "wasted" reactive power — same $P$ then needs less $I$: thinner wires, lower installation + energy cost.

Procedure: R–L across 50 V/50 Hz via autotransformer → record $V, I$ → $P = I^2R$, $S = V_S I_L$, $\mathrm{PF} = P/S$ (before) → connect parallel $C$ → re-measure (after) → compare theory vs practical. Design equation for the capacitor:

$$Q_C = P\,(\tan\phi_1 - \tan\phi_2),\qquad C = \frac{Q_C}{2\pi f V^2}$$

($\phi_1$ before, $\phi_2$ target angle). Parallel (not series) connection is used so load voltage is undisturbed. Viva: benefits = reduced current/losses, released feeder capacity, avoided utility PF penalty.

## 3. Expt 7 — Three-phase power, two-wattmeter (CO3)

**Aim**: measure 3-ph power with two wattmeters. For balanced load: $P = W_1 + W_2 = \sqrt{3}\,V_L I_L\cos\phi$ (verify against lamp-bank rating: count × 100 W, $\cos\phi = 1$ resistive).

$$W_1 = V_L I_L\cos(30^\circ+\phi),\qquad W_2 = V_L I_L\cos(30^\circ-\phi)$$

Procedure: connect per diagram → raise lamp load in steps → log $V_L, I_L, W_1, W_2$ (TH vs PR) → check $W_1+W_2$ vs $\sqrt{3}V_LI_L$ and vs lamp kW. Derivation of the $30^\circ\pm\phi$ split: [[module-3b-three-phase-ac-circuits]]. Viva: at $\phi = 0$, $W_1 = W_2$; at $\phi = 60^\circ$, $W_1 = 0$; beyond $60^\circ$ one reading goes negative (reverse the coil, subtract).

## 4. Expt 8 — DC-motor speed control, armature-resistance (VLab, ems-iitr, CO5)

Field across supply ($\phi$ const) + series $R_{ext}$ in armature: drop $I_aR_{ext}$ cuts armature voltage → speed falls. With constant load torque ($T_e = T_L = k\phi I_a$), $I_a$ stays rated while speed steps $n \to n_1 \to n_2$ for $R_{ext} = 0 \to R_{ext1} \to R_{ext2}$ (operating points C→D→E on the $n$–$I_a$ family). From $E_b = V - I_a(R_a + R_{ext}) = k\phi n$: raising $R_{ext}$ lowers $n$ smoothly down to zero — **below-base-speed** control at constant torque, at the cost of $I_a^2R_{ext}$ loss (poor efficiency). VLab: sweep $R_{ext}$, attach $n$–$I_a$ screenshots.
