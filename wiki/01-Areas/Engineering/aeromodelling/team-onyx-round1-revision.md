---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Round 1"
unit: "Round-1 Revision and Mock MCQs"
date: 2026-09-19
description: "Two-day sprint plan for the 21-22 Sept Team Onyx test: rapid-fire aero facts, 15 mock MCQs with answers, 11th-12th math-physics and aptitude checklists."
tags: [btech, team-onyx, aeromodelling, revision, mock-test, aptitude]
last_updated: "2026-09-19"
confidence: medium
---

## For future agent
Exam-prep companion to [[INDEX]] for Team Onyx Round-1 (40 MCQs: 15 math+physics, 15 aptitude, 10 aero; 6 PM A020, 21–22 Sept 2026). Aero facts and mock Qs are grounded in `[[raw-sources/Aerodynamics_and_Avionics_Study_Material.pdf]]`; math/physics/aptitude sections are generic 11th–12th guidance pointing at existing vault formula sheets. Expires as a schedule after the test; keep the mock bank as drill material.

# Team Onyx Round-1 Revision

> Hub: [[INDEX]] · Theory: [[aerodynamics-foundations]] · [[wings-controls]] · [[avionics-rc-stack]]
> Logistics: Batch 1 Mon 21 Sept · Batch 2 Tue 22 Sept · **6:00 PM, A020 Workshop**. Attend your assigned batch.

## 1. Two-day sprint (serves: coursework + builds portfolio via Team Onyx)

- **Today (19th):** [[aerodynamics-foundations]] + [[wings-controls]] §1–5 (2 hrs). Closed-book recall of §3 below.
- **Tomorrow (20th):** [[wings-controls]] §6–7 + [[avionics-rc-stack]] (1.5 hrs). Then attempt all 15 mocks closed-book.
- **Test eve:** re-drill only missed mocks + formulas in §4. Sleep; no advanced math — the notice says **11th–12th basics only**.

## 2. Aero rapid-fire (the 10-Q syllabus in 20 lines)

1. Climb ⇔ Lift > Weight; accelerate ⇔ Thrust > Drag.
2. Bernoulli: faster air ⇒ lower pressure. $P + \frac12\rho v^2 + \rho gh$ = const.
3. Coanda: flow sticks to curved wing ⇒ downwash (air pushed down).
4. Newton 3rd: downwash reaction = lift. Both theories together = lift.
5. **Equal Transit = wrong** (molecules need not reunite at trailing edge).
6. Bluff = wake + pressure-drag dominated; $C_D = C_{D,PRESS} + C_{D,FRICTION}$.
7. Cambered airfoil lifts at 0° AoA; symmetrical gives none (tails/rotors).
8. Lowest induced drag = **elliptical**; all-regime = **delta**; transonic = **swept**.
9. Parasol = struts above fuselage. Anhedral on fighters AND high-wing heavies (kill excess spiral stability).
10. $AR = span^2 / area$. Stall ≈ 16°: separation moves forward, wake grows, lift drops.
11. Roll = ailerons (opposite) about **longitudinal**; Pitch = elevator (together) about **lateral**; Yaw = rudder about **vertical**.
12. Prop 8×5 = 8″ diameter, 5″ pitch; bigger number ⇒ stronger motor needed.
13. Brushless = AC, 3-wire, efficient standard; brushed = DC, 2-wire, obsolete in RC.
14. kV = rpm/V: 1800 kV × 12 V = **21,600 rpm**.
15. LiPo: 3.7 V/cell; limits 3.3–4.21 V; 2.2 Ah × 25C = **55 A**.
16. ESC: 10 A motor ⇒ **15–18 A** ESC; supplies 5 V BEC to Rx.
17. Tx/Rx: **2.4 GHz**; 6-ch standard; Rx binds per-protocol only.
18. Servo: torque = force × arm; speed = time per **60° at max torque**.

## 3. Mock aero MCQs (15 — answers at the end)

1. Level constant-speed flight requires: (a) L>W, T=D (b) L=W, T=D (c) L=W, T>D (d) L>W, T>D
2. Pressure above the wing vs below at positive lift: (a) above higher (b) below higher (c) equal (d) zero above
3. Downwash reaction producing lift is an application of: (a) Bernoulli (b) Newton 3rd (c) Equal transit (d) Archimedes
4. Equal Transit Theory is rejected because: (a) wings are flat (b) molecules need not meet at trailing edge (c) air is incompressible (d) Coanda disproves Bernoulli
5. A brick-shaped body in airflow is drag-dominated by: (a) friction (b) pressure/form (c) induced (d) wave
6. Airfoil that produces NO lift at 0° AoA: (a) cambered (b) symmetrical (c) delta (d) swept
7. Most aerodynamically efficient planform (lowest induced drag): (a) rectangular (b) tapered (c) elliptical (d) delta
8. Wing raised clear above fuselage on struts: (a) high (b) shoulder (c) parasol (d) mid
9. Military fighters use anhedral primarily to: (a) increase lift (b) reduce spiral stability for manoeuvrability (c) cut weight (d) raise aspect ratio
10. Span 12 m, area 24 m². AR = (a) 2 (b) 4 (c) 6 (d) 12
11. Right aileron up + left aileron down rolls the aircraft: (a) left (b) right (c) pitches up (d) yaws only
12. 8×5 propeller: (a) 8″ pitch 5″ diameter (b) 8″ diameter 5″ pitch (c) 8 blades 5″ (d) 8 V 5 A
13. 1800 kV motor on 12 V spins at: (a) 150 rpm (b) 1,800 rpm (c) 21,600 rpm (d) 216,000 rpm
14. 2200 mAh 25C LiPo delivers continuously: (a) 2.2 A (b) 25 A (c) 55 A (d) 220 A
15. Servo speed spec is defined as time to rotate: (a) 30° unloaded (b) 60° at max torque (c) 90° unloaded (d) 360° at stall

<details><summary>Answers + one-line why</summary>

1. **(b)** — balanced forces = unaccelerated flight.
2. **(b)** — fast air above ⇒ low pressure; slow air below ⇒ high pressure.
3. **(b)** — action downwash, reaction lift.
4. **(b)** — experiment disproves simultaneous reunion.
5. **(b)** — bluff ⇒ pressure/form drag dominates.
6. **(b)** — symmetrical camber line = chord line.
7. **(c)** — elliptical lift distribution; hard to manufacture.
8. **(c)** — parasol on cabane struts/pylon.
9. **(b)** — less dihedral effect ⇒ less spiral stability ⇒ agility.
10. **(c)** — $12^2/24 = 6$.
11. **(b)** — right wing loses lift ⇒ rolls right.
12. **(b)** — diameter × pitch in inches.
13. **(c)** — $1800 \times 12$.
14. **(c)** — $2.2 \times 25$.
15. **(b)** — 60° at max rated torque.
</details>

## 4. Math + Physics checklist (15 Qs, 11th–12th basics — no advanced prep)

- **Math:** quadratic roots/discriminant, AP/GP sums, basic trig identities, limits-derivative basics, matrices/determinants 2×2–3×3, vectors dot/cross, probability basics. Drill: [[01-Areas/Engineering/mathematics/formula-sheet-master]] · [[01-Areas/Engineering/mathematics/quick-revision-cards]] · [[01-Areas/Engineering/engineering-math/module-1-matrices]]
- **Physics:** kinematics ($v = u + at$, $s = ut + \frac12at^2$), Newton's laws + friction, work-energy-power, gravitation basics, electrostatics/Coulomb + Ohm's law, Bernoulli + continuity (bonus: links straight into aero Qs). Drill: [[01-Areas/Engineering/physics/formula-sheet-mechanics]] · [[01-Areas/Engineering/physics/formula-sheet-electrodynamics]] · [[01-Areas/Engineering/physics/formula-sheet-thermal-waves]]
- Trap per the notice: "Amplitude" is a typo for **Aptitude** — don't prep wave-amplitude physics for it.

## 5. Aptitude checklist (15 Qs)

Time-speed-distance, percentages/profit-loss, ratios-ages-averages, time-work, simple/compound interest, number series, coding-decoding, blood relations, direction sense, syllogisms, statement-conclusion. Strategy: 1 min/Q cap, eliminate options, attempt all (no negative marking mentioned — confirm in hall).

## 6. Exam-day traps

- Bernoulli-vs-Newton options: correct answer is usually **both together**, never one alone.
- "Symmetrical airfoil at 0° AoA lifts" → always false.
- ESC rating = motor amps: pick the **next size up**, never exact.
- kV ≠ kilovolt. S in 2S ≠ seconds — it's **cell count**.
- Parasol vs high wing: struts = parasol.
