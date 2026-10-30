---
course_code: "316U06C104"
course_name: "Basic Electrical Engineering (BEE)"
unit: "MSE (full paper)"
tags: [btech, bee, thevenin, superposition, equivalent-resistance, ac-circuits, rms, form-factor, exam-prep, mse, past-paper]
last_updated: "2026-10-21"
confidence: medium
date: "2026-10-21"
description: "Solved walkthrough of the Aug-Dec 2025 BEE MSE paper (midsems-pyp.pdf): Thevenin + superposition, equivalent-resistance networks, source transformation + max power transfer, AC basic i=62.35sin(323t) quantities, half-wave RMS - each question explained in easy language with worked numbers, figure-read caveats, and similar problems."
---

## For future agent
Full walkthrough of the actual **Augâ€“Dec 2025 BEE MSE paper** (source: [[raw-sources/midsems-pyp.pdf|midsems-pyp.pdf]], 30 marks, 1 hr 15 min). Q1 = Thevenin OR superposition (10M), Q2 = equiv resistance (5M) + theory, Q3 = AC basics + waveform RMS. **Caveat:** the circuit values below are read from the scanned figure â€” topologies were reconstructed; verify against the original print before memorising exact answers. Deep theory: [[module-1-dc-circuits]], [[module-2-ac-circuits]]. As of 2026-10-21.

# BEE MSE 2025 â€” Solved Paper Walkthrough

## Pattern & verdict

| Q | Type | Marks | Difficulty | Yield |
|---|------|-------|-----------|-------|
| Q1 | Thevenin OR superposition | 10 | Med (procedure) | â­â­â­ |
| Q2A | Equivalent resistance | 5 | Med (star-delta/bridge) | â­â­ |
| Q2B | Source transformation + Max Power Transfer | 2+3 | Easy (theory) | â­â­â­ |
| Q3A | i = 62.35 sin(323t) â†’ 5 quantities | 5 | Easy | â­â­â­ gimme |
| Q3B | RMS of a waveform | 5 | Med | â­â­ |

**Verdict: the most repeatable paper.** Thevenin + AC basics alone = ~15M of pure procedure. Practice circuits > reading.

---

## Q1 (10M) â€” Thevenin: current through R_L = 10Î©

**The idea:** Thevenin = replace EVERYTHING except the load by one source and one resistor in series. Recipe (memorise as V-R-I):
1. **Remove** R_L, find open-circuit voltage V_th across its terminals.
2. **Kill sources** (short the ideal voltage source, open the current source); find R_th = resistance looking into the load terminals.
3. **Reconnect** R_L: I = V_th/(R_th + R_L).

**Structure of the circuit (as read from the figure):** 100 V source between nodes Câ€“D. One branch C â†’20Î©â†’ A â†’80Î©â†’ D. Second branch C â†’40Î©â†’ B â†’50Î©â†’ D. Load R_L between A and B.

**Solution.** With R_L removed, those two branches are simply **each across the 100 V source** (taking D = 0):

- Branch 1 (20+80 = 100Î©): Iâ‚ = 1 A â‡’ V_A = 100 âˆ’ 20Â·1 = **80 V**
- Branch 2 (40+50 = 90Î©): Iâ‚‚ = 100/90 A â‡’ V_B = 100 âˆ’ 44.4 = **55.6 V**

$$V_{th}=V_A-V_B=24.4\ \text{V}$$

Kill the source (Câ€“D short): from A: 20âˆ¥80 = **16Î©**; from B: 40âˆ¥50 = **22.2Î©**; the two meet through the short â†’ series:
$$R_{th}=16+22.2=38.2\ \Omega$$

$$I_L=\frac{24.4}{38.2+10}=\frac{24.4}{48.2}\approx \boxed{0.51\ \text{A}}$$

**Method marks:** remove-load open-circuit analysis, silence-the-source redraw, final Ohm's law â€” show all three numbered steps.

*(Figure-read caveat: the answer depends on exactly how A/B hang off the branches; the METHOD is what repeats. Verify numbers against the original.)*

**Note on the OR option (superposition on a 1A source network):** superposition = solve once per source, with **every other voltage source shorted and current source opened**, then algebraically add the partial currents. Same network shows 1A current source, 3Î©, 2Î©'s and the 1Î© target; the scan's node letters are ambiguous so I won't invent numbers â€” but the drill is identical to lab expt: [[thevenin-vth-rth-worked-examples]] has the superposition siblings; [[lab-dc-theorems-expts-2-5]].

**Similar problems:** Thevenin with a current source (V_th by KVL, R_th with source opened), Norton counterpart ("same but current source âˆ¥ R_th"), max-transfer sanity check. â†’ [[module-1-dc-circuits]], [[lab-dc-theorems-expts-2-5]].

---

## Q2.A (5M) â€” Equivalent resistance between A and B (network 1)

**The idea:** when a network has a symmetric middle node, current enters/leaves symmetrically and mirror nodes sit at the SAME potential â€” you may merge them (or cut the middle resistor: no current in it). That shortcut beats brute star-delta.

**Structure (as read from figure):** A at top; Câ€“F bottom corners; B centre; outer legs Aâ€“C = Aâ€“F = 6Î©; middle Câ€“B = Bâ€“F = 12Î©; bottom Câ€“D 3Î©, Dâ€“E 12Î©, Eâ€“F 3Î©; B down to D and E via 12Î© each. *(Interpretation caveat â€” verify.)*

**Solution by symmetry** (about the vertical axis through Aâ€“B): Câ†”F, Dâ†”E are equipotential pairs â†’ merge them in pairs:

- Aâ€“(Câ‰¡F): 6âˆ¥6 = **3Î©**
- (Câ‰¡F)â€“B: 12âˆ¥12 = **6Î©**
- (Câ‰¡F)â€“(Dâ‰¡E): 3âˆ¥3 = **1.5Î©**
- Bâ€“(Dâ‰¡E): 12âˆ¥12 = **6Î©**
- internal Dâ€“E (12Î©): both ends merged â†’ carries nothing, delete it.

Paths from A to B: direct 3+6 = **9Î©**; or 3+1.5+6 = **10.5Î©**. Parallel:

$$R_{AB} = \frac{9\times10.5}{9+10.5}= \boxed{4.85\ \Omega}$$

## Q2.A (OR variant, 5M) â€” Equivalent resistance between X and Y

**Structure (as read):** X â€”2Î©â€” M; then a bridge M..N: Mâ€“top 4Î©, Mâ€“bottom 6Î©, middle 8Î©, Nâ€“top 2Î©, Nâ€“bottom 7Î©; N â€”2Î©â€” Y. Bridge 4/6 vs 2/7 â†’ unbalanced â‡’ **deltaâ†’star** the Mâ€“Aâ€“B triangle (4, 6, 8).

**Star arms:** r_M = (4Â·6)/18 = 1.33Î© Â· r_top-node = (4Â·8)/18 = 1.78Î© Â· r_bottom-node = (6Â·8)/18 = 2.67Î©.

$$R_{XY} = 2 + 1.33 + \frac{(1.78+2)(2.67+7)}{(1.78+2)+(2.67+7)} = 2+1.33+ (3.78\parallel 9.67)=2+1.33+2.72=\boxed{\approx 8.05\ \Omega}$$

**Takeaway skill:** if a bridge isn't balanced (ratio test: 4/6 â‰  2/7), deltaâ†’star the outer triangle, then series/parallel collapses. Practice 3 of these and the 5M is yours. â†’ [[module-1-dc-circuits]], [[formula-sheet-bee]].

---

## Q2.B.i (2M) â€” Source transformation rules

Convert between the two source models when a series/parallel resistor pairs with them:

- **Voltage source V in series with R** â‡” **current source V/R in parallel with the same R** (and back: I âˆ¥ R â‡” IÂ·R in series with R).
- Rules: only the source TYPE flips; R keeps its value; polarity/arrow must match; only a source **with its series/parallel R** can be transformed; can't transform an ideal source alone.
- Example (draw it): 10 V in series 2Î© â‡” 5 A current source in parallel 2Î©.

## Q2.B.ii (3M) â€” Maximum Power Transfer theorem

Statement: a source/network with Thevenin equivalent (V_th, R_th) delivers **maximum power when R_L = R_th**, and then P_max = V_thÂ²/4R_th with Î· = 50%.

Proof in one line: $P = V_{th}^2R_L/(R_{th}+R_L)^2$ â†’ set dP/dR_L = 0 â†’ R_L = R_th. Draw the small circuit (V_th â€”R_thâ€”R_L loop) â€” 1 of the 3M hides there. â†’ [[module-1-dc-circuits]].

---

## Q3.A (5M) â€” i = 62.35 sin(323t) A: the five quantities

For $i=I_m\sin(\omega t)$: compare term by term.

| Quantity | Formula | Value |
|----------|---------|-------|
| Maximum value | the amplitude | **62.35 A** |
| Frequency | f = Ï‰/2Ï€ = 323/6.28 | **51.4 Hz** |
| RMS | I_m/âˆš2 | **44.1 A** |
| Average (half-cycle) | 2I_m/Ï€ = 0.637 I_m | **39.7 A** |
| Form factor | RMS/Avg = 1.11 (sine) | **1.11** |

Pure recall. Five gimme marks if you know `f=Ï‰/2Ï€, 1/âˆš2=0.707, 2/Ï€=0.637, 1.11`. â†’ [[formula-sheet-bee]].

---

## Q3.B (5M) â€” RMS of the given waveform

**The curve:** v = V_m sin Î¸ for 0â†’Ï€, zero afterwards (the printed 0.866 V_m at Î¸ = Ï€/3 is just sin(Ï€/3) = 0.866 â€” it confirms a plain half-sine, half-wave-rectified).

**RMS recipe:**

$$V_{rms}=\sqrt{\frac{1}{2\pi}\int_0^{\pi}V_m^2\sin^2\theta\,d\theta}
=\sqrt{\frac{V_m^2}{2\pi}\cdot\frac{\pi}{2}}=\boxed{\frac{V_m}{2}}$$

(use $\sin^2\theta=\frac{1-\cos2\theta}{2}$ to integrate quickly). Averages factor: V_avg = V_m/Ï€ if they ask. The genre = "RMS/avg of clipped/chopped sine" â€” split the waveform into flat pieces, integrate each over the period, add under one âˆš.

**Similar problems:** RMS of square wave (V_m), triangular wave (V_m/âˆš3), quarter semicircle-ish weird shapes â€” always âˆ«vÂ²/T. â†’ [[module-2-ac-circuits]], [[mse-recall-test-physics]] for the sibling drill style.

---

## Exam-day strategy

1. **Q3A + Q2B first** (~10 min for 8M of recall).
2. **Q1 Thevenin** strictly as Vâ†’Râ†’I numbered steps, even if the OR superposition tempts.
3. Q2A: check bridge balance FIRST (ratio test) â€” merged symmetry if balanced, deltaâ†’star if not.
4. Leave Q3B last; don't mix average vs RMS formulas.

**Siblings:** [[thevenin-vth-rth-worked-examples]] Â· [[bee-ia1-2026-solutions-and-viva]] Â· [[formula-sheet-bee]] Â· labs: [[lab-dc-theorems-expts-2-5]]. Chem/AM twins: [[mse-past-paper-chem-2025-solved]] Â· [[mse-past-paper-am1-2025-solved]] Â· physics: [[mse-past-paper-physics-2025-solved]].

**Relations:** relates_to [[module-1-dc-circuits]] Â· [[module-2-ac-circuits]] Â· depends_on [[thevenin-vth-rth-worked-examples]] Â· source: [[raw-sources/midsems-pyp.pdf|midsems-pyp.pdf]].


