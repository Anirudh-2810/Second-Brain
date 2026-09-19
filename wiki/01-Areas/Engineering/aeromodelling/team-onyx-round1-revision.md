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

# Team Onyx Round-1 Revision (simple words)

> Hub: [[INDEX]] · Theory: [[aerodynamics-foundations]] · [[wings-controls]] · [[avionics-rc-stack]]
> Test details: Batch 1 Monday 21 Sept, Batch 2 Tuesday 22 Sept, **6:00 PM, A020 Workshop**. Go on YOUR batch day. Pattern: **40 MCQs** — 15 basic Maths+Physics, 15 Aptitude, 10 Aerodynamics from the study PDF.

## 1. Your 2-day plan (this serves: coursework + builds portfolio via Team Onyx)

- **Today (19th, ~2 hrs):** read [[aerodynamics-foundations]] fully, then [[wings-controls]] sections 1–5 (airfoil → aspect ratio). Close the notes and say the rapid-fire lines in §2 out loud.
- **Tomorrow (20th, ~1.5 hrs):** read [[wings-controls]] sections 6–7 (stall + controls) and [[avionics-rc-stack]] fully. Then do all 15 mock questions in §3 with notes CLOSED.
- **Test eve:** only re-read the ones you got wrong + the exam-day traps in §6. Sleep well. The notice says NO advanced maths — only 11th–12th basics, so don't open heavy books.

## 2. Aero rapid-fire — full syllabus in plain lines

Read each line, then cover the right side and recall it.

1. Straight steady flight needs **Lift = Weight** (up-down balanced) AND **Thrust = Drag** (front-back balanced). Climb = Lift wins. Speed up = Thrust wins.
2. **Bernoulli:** fast-moving air pushes LESS (low pressure). On a wing: fast air on top → low pressure on top; slow air below → high pressure below. High below pushes the wing up.
3. **Coanda:** moving air hugs the curved wing (like water hugs a spoon). The air bent downward behind the wing is called **downwash**.
4. **Newton's 3rd law:** wing pushes air down → air pushes wing up. That push-back IS lift. **Lift needs BOTH Bernoulli AND Newton together.**
5. **Equal Transit Theory is WRONG.** Air particles do NOT have to meet again at the back. Any option saying that is false.
6. **Bluff body** (brick, truck, building) = messy wake behind + mostly **pressure drag**. Formula: $C_D = C_{D,PRESS} + C_{D,FRICTION}$. Streamlined (fish, flat wing) = mostly friction drag.
7. **Cambered** (curved) airfoil still lifts at 0° tilt. **Symmetrical** (mirror) airfoil lifts NOTHING at 0° — used on tails and helicopter rotors so they don't pull on their own.
8. Wing shapes from top: **rectangular** = easiest to build. **Elliptical** = most efficient (lowest induced drag) but hard to build. **Swept** = for near-sound-speed flight. **Delta** (triangle) = okay at ALL speeds, used on supersonic jets.
9. Wing positions: low (belly), mid (middle), shoulder (below roof), high (on roof), **parasol** (held ABOVE the roof on sticks/struts). Struts mentioned → parasol.
10. **Dihedral** = wings tilted UP (stable, auto-levelling). **Anhedral** = tilted DOWN (agile, easy turning). Fighters use anhedral to turn fast. Giant high-wing cargo planes also use anhedral to cancel their built-in extra stability (pendulum/keel effect).
11. **Aspect ratio** = how long-skinny the wing is. Formula: $AR = span^2 / area$. Example: span 12, area 24 → $144/24$ = **6**.
12. **Angle of attack** = tilt between wing and incoming air. More tilt → more lift, until the **critical angle (~16°)**, then **stall**: airflow peels off the top (flow separation), wake grows, lift drops, drag jumps.
13. Controls: **ailerons** (wingtips, move OPPOSITE) → **roll** around the nose-to-tail axis. **Elevator** (tail, move TOGETHER) → **pitch** (nose up/down) around the wingtip-to-wingtip axis. **Rudder** (vertical fin) → **yaw** (nose left/right) around the floor-to-roof axis.
14. Propeller stamp **8×5** = 8 inch wide (diameter) × 5 inch steepness (pitch). Bigger second number → needs stronger motor. Small prop = faster top speed. Big prop = quicker acceleration.
15. **Brushless** motor = modern RC standard (3 wires, needs ESC, efficient). **Brushed** = old (2 wires, heavy, wasteful, used in drills).
16. **kV = RPM per 1 volt.** 1800 kV × 12 V = **21,600 rpm**. (kV is NOT kilovolt.)
17. **LiPo battery:** 1 cell = 3.7 V. 2S = 2 cells = 7.4 V. Never below 3.3 V or above 4.21 V per cell. Capacity 2200 mAh = fuel size. Punch: 2.2 A × 25C = **55 A** max current.
18. **ESC:** translator + 5 V supplier. 10 A motor → buy **15–18 A ESC** (always bigger, stays cool, never exact match).
19. **Transmitter + Receiver:** talk on **2.4 GHz**. Standard plane uses **6 channels** (rudder, elevator, ailerons, motor + 2 Aux). Receiver binds to only one brand/type.
20. **Servo:** torque = strength (force × arm length). Speed = time to swing **60° at full load**. Control flaps need FAST servos; landing gear needs slow ones.

## 3. Mock aero MCQs (15 — answers at the end)

Try all 15 with notes closed. Mark your score out of 15. Re-read only the topics you miss.

1. Level flight at steady speed needs: (a) Lift > Weight, Thrust = Drag (b) Lift = Weight, Thrust = Drag (c) Lift = Weight, Thrust > Drag (d) Lift > Weight, Thrust > Drag
2. When a wing is lifting, pressure above vs below is: (a) above higher (b) below higher (c) equal both sides (d) zero on top
3. "Wing pushes air down, air pushes wing up" uses: (a) Bernoulli (b) Newton's 3rd law (c) Equal Transit (d) Archimedes
4. Equal Transit Theory is wrong because: (a) wings are flat (b) air particles need NOT meet again at the back (c) air cannot be compressed (d) Coanda cancels Bernoulli
5. A brick in wind has mostly which drag? (a) friction (b) pressure / form drag (c) induced (d) wave
6. Which airfoil gives NO lift when flat at 0°? (a) cambered (b) symmetrical (c) delta (d) swept
7. Which wing shape is most efficient (lowest induced drag)? (a) rectangular (b) tapered (c) elliptical (d) delta
8. Wing held clear above the body on struts is: (a) high (b) shoulder (c) parasol (d) mid
9. Fighters use downward (anhedral) wings mainly to: (a) get more lift (b) turn faster by reducing stability (c) save weight (d) increase aspect ratio
10. Wing span 12 m, area 24 m². Aspect ratio = (a) 2 (b) 4 (c) 6 (d) 12
11. Right aileron goes UP and left goes DOWN. The plane: (a) rolls left (b) rolls right (c) pitches up (d) only yaws
12. Propeller marked 8×5 means: (a) 8″ pitch, 5″ diameter (b) 8″ diameter, 5″ pitch (c) 8 blades, 5″ long (d) 8 volts, 5 amps
13. An 1800 kV motor with a 12 V battery spins at about: (a) 150 rpm (b) 1,800 rpm (c) 21,600 rpm (d) 216,000 rpm
14. A 2200 mAh 25C LiPo can give continuously about: (a) 2.2 A (b) 25 A (c) 55 A (d) 220 A
15. Servo speed means time to turn: (a) 30° with no load (b) 60° at full load (c) 90° with no load (d) 360° at full load

<details><summary>Answers — with one-line simple reasons</summary>

1. **(b)** — straight + steady = all forces balanced.
2. **(b)** — high pressure below pushes the wing up.
3. **(b)** — push down, get pushed up = Newton.
4. **(b)** — no rule says particles must reunite; tests proved it.
5. **(b)** — blocky bluff shapes = pressure drag.
6. **(b)** — mirror-top-bottom gives no pressure difference when flat.
7. **(c)** — elliptical makes the smoothest lift spread.
8. **(c)** — umbrella on sticks = parasol.
9. **(b)** — less stability = faster turning.
10. **(c)** — $12 × 12 ÷ 24 = 6$.
11. **(b)** — right wing loses lift and drops, so roll goes right.
12. **(b)** — first number width, second number steepness.
13. **(c)** — $1800 × 12 = 21,600$.
14. **(c)** — $2.2 × 25 = 55$.
15. **(b)** — always 60 degrees at maximum push.
</details>

## 4. Maths + Physics checklist (15 Qs — only 11th–12th basics)

Don't open advanced books. The notice is clear: basics only.

- **Maths to touch:** solving quadratic equations + discriminant ($b^2-4ac$), AP and GP sums, basic trig (sin/cos/tan, $sin^2+cos^2=1$), simple limits and derivatives (power rule), 2×2 and 3×3 matrices and determinants, vectors (dot = $a·b$, cross = $a×b$), simple probability (favourable ÷ total). Practice from: [[01-Areas/Engineering/mathematics/formula-sheet-master]] · [[01-Areas/Engineering/mathematics/quick-revision-cards]] · [[01-Areas/Engineering/engineering-math/module-1-matrices]]
- **Physics to touch:** motion formulas ($v = u + at$, $s = ut + \frac{1}{2}at^2$, $v^2 = u^2 + 2as$), Newton's 3 laws + friction, work–energy–power ($W = F·s$, $KE = \frac{1}{2}mv^2$), gravity basics ($F = GmM/r^2$), charge + Coulomb + Ohm's law ($V = IR$), and Bernoulli/continuity (free marks — same as aero). Practice from: [[01-Areas/Engineering/physics/formula-sheet-mechanics]] · [[01-Areas/Engineering/physics/formula-sheet-electrodynamics]] · [[01-Areas/Engineering/physics/formula-sheet-thermal-waves]]
- Note: the notice word "Amplitude" is a typo for **Aptitude**. Don't study wave-amplitude physics for it.

## 5. Aptitude checklist (15 Qs — speed matters)

Most-asked types: percentages, profit–loss, ratios, ages, averages, time–speed–distance (train/boat), time–work, simple + compound interest, number series, coding–decoding, blood relations, direction sense, syllogisms, statement–conclusion.

How to attempt: 1 minute per question max. First solve the easy ones (series, percentages, directions). Cut obviously wrong options. Attempt ALL — no negative marking was announced (confirm in the hall).

## 6. Exam-day traps (read 10 min before entering)

- Bernoulli-vs-Newton question → answer is almost always **"both together"**, never one alone.
- "Symmetrical airfoil lifts at 0°" → ALWAYS false.
- ESC rating equals motor current → NEVER correct; correct is the **next bigger size**.
- kV is NOT kilovolt (it's rpm per volt). 2S is NOT 2 seconds (it's 2 cells).
- Struts/pylon above body → **parasol**, not high wing.
- Stall question → answer mentions **flow separation / critical angle**, not "engine failure".
