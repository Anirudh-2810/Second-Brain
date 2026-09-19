---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Round 1"
unit: "11th-12th Basics for Aerodynamics"
date: 2026-09-19
description: "Class 11-12 physics and maths behind the 10 aero questions: units, vectors, Newton laws, pressure, density, continuity, Bernoulli with worked numbers, energy, trig, formula rearranging."
tags: [btech, team-onyx, aeromodelling, physics, basics, bernoulli, vectors]
last_updated: "2026-09-19"
confidence: high
---

## For future agent
Companion to [[INDEX]] that teaches ONLY the school physics/maths needed for the 10 aerodynamics MCQs (`[[raw-sources/Aerodynamics_and_Avionics_Study_Material.pdf]]`). Nothing advanced — Class 11 NCERT mechanics + Class 12 electrostatics basics. Each section ends with the aero question it unlocks. Pair with [[team-onyx-round1-revision]] §4 and [[team-onyx-sample-paper-01]] Section A.

# 11th–12th Basics Behind Aerodynamics (simple words)

> Hub: [[INDEX]] · Aero theory: [[aerodynamics-foundations]] · Practice: [[team-onyx-sample-paper-01]]
> Promise: if you can do every worked example here with a pen, the physics half of the aero section is free marks.

## 1. Units — the language of answers

| Quantity | Symbol | Unit | What it means simply |
|---|---|---|---|
| Length | — | metre (m) | wing span, height |
| Mass | m | kilogram (kg) | how much matter in the plane |
| Time | t | second (s) | flight time, RPM base |
| Force | F | newton (N) | push or pull; $1$ N pushes $1$ kg at $1$ m/s² |
| Pressure | P | pascal (Pa) | force on each square metre; $1$ Pa $= 1$ N/m² |
| Energy / work | E, W | joule (J) | $1$ J $= 1$ N pushed over $1$ m |
| Power | P | watt (W) | joules per second; $1$ W $= 1$ J/s |
| Speed | v | m/s | how fast (no direction) |
| RPM | — | rev/min | propeller/motor rounds per minute |

Conversions the test assumes: $1$ km $= 1000$ m, $1$ h $= 3600$ s, $1$ kW $= 1000$ W, $g ≈ 10$ m/s² (they always say 10 to keep maths clean).

**Unlocks:** every numerical — you must spot whether the answer wants N, Pa, J, or W.

## 2. Scalars vs vectors — number vs arrow

- **Scalar** = only a number: mass (4 kg), speed (20 m/s), temperature, time.
- **Vector** = number PLUS direction: velocity (20 m/s north), force (30 N forward), displacement.

Forces add like arrows, not plain numbers. Two pushes at right angles combine with Pythagoras:

$$R = \sqrt{A^2 + B^2}$$

Worked (A4/C-paper favourite): thrust $30$ N forward + crosswind $40$ N sideways → $R = \sqrt{900 + 1600} = \sqrt{2500} = 50$ N. Remember 3-4-5 triangles: 30-40-50 is just 3-4-5 × 10. Direction: tilted $\arctan(40/30) ≈ 53°$ off the nose.

**Unlocks:** resultant-force questions; why lift (up) and drag (back) never simply add.

## 3. Newton's three laws — in one breath each

1. **Still stays still, moving keeps moving** unless a force acts (inertia). A cruising plane needs NO extra thrust to keep moving — only to fight drag.
2. **$F = ma$** — bigger force = bigger acceleration; heavier plane = harder to accelerate. Weight itself is $W = mg$: a $4$ kg model weighs $4 × 10 = 40$ N.
3. **Push back pushes you** — wing shoves air down (downwash), air shoves wing up (lift). Rocket, balloon, walking — same law.

Worked: $2$ kg plane, motor pushes with net $6$ N → $a = F/m = 3$ m/s². Double the mass, half the acceleration.

**Unlocks:** weight↔lift balance (A10), downwash→lift (C-theory Qs), why level flight needs zero net force.

## 4. Pressure — $P = F/A$

Pressure is how crowded a push is: same force on a smaller area = more pressure (needle vs palm).

$$P = \frac{F}{A} \qquad 1\ \text{Pa} = 1\ \text{N/m}^2$$

Air around us already presses ~101,325 Pa (1 atmosphere) from all sides — wings care only about DIFFERENCES from this background. If bottom pressure exceeds top by $1200$ Pa, each square metre of wing gets $1200$ N of upward push.

**Unlocks:** reading $\Delta P$ answers (A3); "which side has higher pressure" traps.

## 5. Density — $\rho = m/V$

Density is heaviness-per-box: $$\rho = \frac{m}{V}$$ Air at sea level ≈ **$1.2$ kg/m³** (the number every aero numerical uses). Hot/high air is thinner (smaller $\rho$) → less lift — why planes struggle on hot days, one line the test may quote.

## 6. Continuity — narrow pipe, fast flow

Water in a garden pipe: squeeze the pipe (smaller area $A$), water shoots faster ($v$) so the same volume passes each second:

$$A_1 v_1 = A_2 v_2$$

Over a wing, the curved top squeezes streamlines together like a half-pipe → top air speeds up. That is the physical reason $v_{top} > v_{bottom}$ in every Bernoulli sum.

**Unlocks:** "why is air faster above the wing" options — answer: streamline squeezing / continuity.

## 7. Bernoulli — the full equation, term by term

$$P + \frac{1}{2}\rho v^2 + \rho g h = \text{constant}$$

Read left to right: **push-energy + speed-energy + height-energy never changes** along a smooth flow. Gain speed → must lose pressure.

- $P$ — static push of the air.
- $\frac{1}{2}\rho v^2$ — "wind energy" from motion (called dynamic pressure).
- $\rho g h$ — height energy; for a small model wing both sides are at nearly the same $h$, so it cancels.

Worked (the exact A3 sum): $\rho = 1.2$, $v_{top} = 60$, $v_{bot} = 40$:
$\Delta P = \frac{1}{2} × 1.2 × (60^2 − 40^2) = 0.6 × (3600 − 1600) = 0.6 × 2000 = \mathbf{1200}$ Pa, higher pressure on the **bottom** (slower side).

Steps to never fumble: (1) square both speeds, (2) subtract (fast² − slow²), (3) multiply by $\rho/2$, (4) higher pressure sits on the SLOWER side.

**Unlocks:** A3, every "low pressure is where" MCQ, sample-paper C-theory justifications.

## 8. Energy, work, power — three formulas

- Kinetic energy: $KE = \frac{1}{2}mv^2$ — doubling speed QUADRUPLES energy (test loves this).
- Work: $W = F × s$ (force × distance along the push).
- Power: $P = F × v$ for motion, or $P = V × I$ for electrics.

Worked pair: $2$ kg plane $10 → 20$ m/s: $\Delta KE = \frac{1}{2} × 2 × (400 − 100) = 300$ J (A8). Electrics: $11.1$ V $× 20$ A $= 222$ W (A9).

**Unlocks:** A8/A9, battery-endurance sums ($time = capacity ÷ current$).

## 9. Tiny trig — only sin matters here

For a wing tilted at angle $\theta$: vertical rise $= length × \sin\theta$. Memorize two: $\sin30° = 0.5$, $\sin90° = 1$.

Worked (A12): half-span $1$ m, dihedral $30°$ → tip rise $= 1 × 0.5 = \mathbf{0.5}$ m. Angle of attack itself is just this $\theta$ between chord line and airflow — see [[wings-controls#6-angle-of-attack-and-stall-flow-separation]].

## 10. Rearranging formulas — the $45$-second skill

Every aero formula appears solved for a different letter. Master moving one symbol:

- $AR = span^2 / area$ → $area = span^2 / AR$ → $span = \sqrt{AR × area}$.
- $RPM = kV × volts$ → $volts = RPM / kV$.
- $max\ current = capacity(A) × C$ → $C = current / capacity$.
- $t = \sqrt{2h/g}$ → $h = gt^2/2$.

Worked: $AR = 6$, span $12$ → area $= 144/6 = 24$ m². $19{,}980$ rpm motor at $1800$ kV → volts $= 19980/1800 = 11.1$ V (a 3S pack — full circle back to batteries).

## 11. Map: school topic → aero question

| If the MCQ asks… | Reach for | Page |
|---|---|---|
| climb / accelerate / level? | $F = ma$, balanced vs unbalanced forces | §3 |
| pressure high top or bottom? | Bernoulli + slow-side rule | §7 |
| resultant of two forces? | Pythagoras 3-4-5 | §2 |
| lift value for level flight? | $W = mg$ | §3 |
| flight time / range of drop? | $t = \sqrt{2h/g}$, range $= v×t$ | §10 |
| tip height / AoA geometry? | $\sin\theta$ | §9 |
| motor rpm / battery current? | multiplication rearrangements | §10 |
| power or energy number? | $\frac{1}{2}mv^2$, $VI$ | §8 |

Drill loop: attempt [[team-onyx-sample-paper-01]] Section A → miss a sum → come back to its row above → redo with pen.
