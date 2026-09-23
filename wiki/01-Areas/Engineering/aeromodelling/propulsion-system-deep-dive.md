---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Propulsion System Deep Dive"
date: 2026-09-23
description: "Propulsion chain taught properly in simple words from the Propulsion PDF (18 pp): BLDC motors, propeller numbers, kV math with worked examples, LiPo bands, matching rules."
tags: [btech, aeromodelling, propulsion, bldc, propeller, lipo, esc, team-onyx]
last_updated: "2026-09-24"
confidence: high
---

## For future agent
Full teaching ingest of `raw-sources/Propulsion System.pdf` (18 pages) for the Team Onyx interview. Style contract (owner ask 2026-09-24): teach like [[aerodynamics-foundations]] — tables, daily-life examples, worked-number examples, memory tricks, interview-trap lines, self-check. Component detail lives in [[esc-deep-dive]]; chain recap in [[avionics-rc-stack]]; cheat sheet [[team-onyx-quick-revision]]; drill [[team-onyx-interview-mock-01]].

# Propulsion System Deep Dive (simple words)

> Parent hub: [[INDEX]] · Sibling: [[esc-deep-dive]] · Chain: [[avionics-rc-stack]] · Cheat sheet: [[team-onyx-quick-revision]] · Drill: [[team-onyx-interview-mock-01]]
> How to use this page: read each heading slowly. Every hard word has a daily-life example. Numbers are worked out step by step — copy the method, not just the answer. Lines starting with **INTERVIEW:** are the exact traps interviewers love.

## 1. What propulsion means — pushing air backwards

Propulsion = pushing forward by shoving air backward. A swimmer pushes water back and glides forward; a plane's propeller pushes air back and the plane moves forward. That push-back is Newton's Third Law again (same law as lift in [[aerodynamics-foundations]]).

The RC electric chain, in order:

**battery → ESC → motor → propeller → thrust.** Radio commands it, servos steer it.

**Memory trick:** "B-E-M-P — Big Elephants Make Peanuts." Say it as one breath and the order sticks.

## 2. Motors — BLDC is the team standard

Two kinds of electric motors exist. The table decides for you:

| Feature | Brushed DC (old) | BLDC — brushless DC (team standard) |
|---------|------------------|--------------------------------------|
| Wires | 2 (plain + and −) | 3 (needs its ESC to make the drive) |
| Inside | physical brushes rub and wear out, spark, need service | no rubbing parts — coils switch electronically |
| Efficiency | 75–80% | 85–90% |
| Feel | heavier, noisier, slower to respond | lighter, quieter, faster response |

Daily-life version: brushed = old drill machine that sparks and wears its brushes down; BLDC = modern ceiling fan motor that just runs for years.

Inside a BLDC, fixed coils (stator) switch on in sequence and pull-then-push the magnets (rotor) around. Firing them in pull+push pairs is faster than stepping one coil at a time — like rowing with both oars instead of one.

Two layouts — this is the favourite interview question of the whole PDF:

| Type | What spins | Character | Use |
|------|-----------|-----------|-----|
| **Outrunner** | outer shell spins around a fixed middle | big torque at low speed, drives the prop DIRECTLY, less friction | **team default for propellers** |
| **Inrunner** | inner shaft spins inside a fixed outer case | very high RPM, but NEEDS a gearbox to drive a prop, more friction | EDF jets / high-speed use |

Daily-life version: outrunner = ceiling fan (wide blades bolted to the spinning outer body, direct drive); inrunner = mixer-grinder motor (tiny shaft screaming fast, needs gears to do real work).

**Memory trick:** "OUTrunner pushes OUTside air directly. INrunner screams INside and needs gears."

**INTERVIEW:** "Outrunner vs inrunner — which drives a prop directly and why?" → outrunner: torque-rich, direct drive, no gearbox; inrunner needs a gearbox.

## 3. Propeller — two numbers that decide everything

A propeller is a fan that converts spinning into thrust. Its stamp has two numbers in inches: **diameter × pitch**.

- **Diameter** = tip-to-tip length (how big the disc of air is).
- **Pitch** = how far forward it would screw in one full turn if air were solid — like the gap between threads on a screw going into wood.

Stamp **8×5** = 8 inch diameter, 5 inch pitch. And 8×5 needs a STRONGER motor than 8×4 — bigger bite per turn, more muscle needed. Same logic as cycling: high gear (big pitch) needs stronger legs.

| Choice | Gets you | Costs you |
|--------|----------|-----------|
| Small prop, spinning fast | top speed | weak punch at start |
| Big prop, spinning slow | strong acceleration/punch | needs a stronger motor, slower top end |
| Fine (low) pitch | take-off bite | poor cruise |
| Coarse (high) pitch | cruise efficiency | hard take-off |

Pusher props sit at the BACK and push instead of pull — same physics, reversed seat.

**INTERVIEW:** "9×6 vs 9×4 — which needs the stronger motor?" → 9×6: same disc, bigger bite per turn. "Small vs big prop?" → small = speed, big = punch.

## 4. kV — rpm PER volt, with worked examples

**kV means RPM per 1 volt, measured with no load.** It is NOT kilovolt — this mix-up is the PDF's most-set trap.

Max rpm = kV × volts. Just multiply. Worked examples (do these yourself once):

- PDF example: 1800 kV × 12 V = **21,600 rpm**. (1800 × 12: 18 × 12 = 216, add two zeros.)
- Mock favourite: 2200 kV on 3S nominal 11.1 V → 2200 × 11.1 = **24,420 rpm**. (22 × 111 = 2442, add two zeros... check: 2200 × 11 = 24,200, plus 2200 × 0.1 = 220, total 24,420. Correct.)
- Reverse drill: you want ~20,000 rpm from a 3S pack (11.1 V) → kV ≈ 20,000 ÷ 11.1 ≈ **1800 kV**. Division is fair game too.

**Memory trick:** "kV = how thirsty-fast the motor spins per volt you feed it."

**INTERVIEW:** "1800 kV on 12 V?" → 21,600 rpm, and say "rpm per volt, not kilovolt" before they ask.

## 5. LiPo battery — the number bands

LiPo = lithium-polymer. Why the team uses it: huge punch (high discharge), lots of energy per gram, thin flat shape you can fit anywhere, long life. Like upgrading from a brick-phone battery to a smartphone battery — same idea, better everything.

Per-cell bands — memorise as three numbers:

| State | Volts per cell | Simple meaning |
|-------|---------------|----------------|
| **Nominal** (printed) | **3.7 V** | the name-plate number |
| **Full** (fresh charger) | **4.21 V** | just off the charger, hottest |
| **Floor** (land NOW) | **3.3 V** | below this the cell gets damaged |

Cells stack in series, marked S: 1S = 1 cell, 2S = 2 cells, 3S = 3 cells. Worked 3S pack:

- Nominal: 3 × 3.7 = **11.1 V**.
- Fresh: 3 × ~4.2 = **~12.4–12.6 V**.
- Land-by: 3 × 3.5ish ≈ **~10.6 V total** (the mock's line: below ~10.6 on 3S → land).

Capacity + punch: **2200 mAh** = fuel-tank size (2.2 amp-hours). **25C** = how fast you may drain it (25 × capacity per hour). Max continuous amps = Ah × C = 2.2 × 25 = **55 A**. Work it: 2.2 × 25 = 2 × 25 + 0.2 × 25 = 50 + 5 = 55. Show this working out loud — interviewers promote people who show working.

**INTERVIEW:** "3S pack reads 9.9 V total — fly or land?" → land: 9.9 ÷ 3 = 3.3 V per cell, sitting exactly on the damage floor. "2200 mAh 25C max amps?" → 55 A, with the 2.2 × 25 working.

## 6. ESC + servo + radio — condensed (detail in [[esc-deep-dive]])

- **ESC:** varies speed and direction, acts as a dynamic brake, makes the 3-wire drive for brushless, takes PPM from the Rx throttle channel, and its built-in BEC steals 5 V off the LiPo for the receiver and servos.
- **Servo:** a small DC motor with position feedback that moves to an exact angle and HOLDS it (flaps, landing gear, throttle arm) — an angle-holder, not a spinner. Speed = time to swing 60° at full load.
- **Tx/Rx:** transmitter turns stick motion into radio waves (modulation) on 2.4 GHz; receiver pulls the orders out of the waves and routes them — servo orders go straight to servos, motor orders always go THROUGH the ESC. One receiver binds to one protocol only, no mixing brands.

## 7. Matching rules — the one-line system answer

Build in this order, never backwards:

1. **Pick the prop first** (job decides: speed vs punch).
2. **Pick a motor strong enough** to spin that prop (outrunner, direct drive).
3. **Pick an ESC above the motor's amps** (10 A motor → 15/18 A — [[esc-deep-dive]] Rule 1).
4. **Pick a battery** whose voltage suits the kV (rpm = kV × V) and whose C-rating covers the amps (55 A example above).

**INTERVIEW:** "How do you size a power system?" → prop → motor → ESC above motor → battery to match. One line, in order, done.

## Quick self-check (answers in [[team-onyx-quick-revision]])

1. Recite the chain battery → thrust in one breath.
2. Outrunner vs inrunner — which drives a prop directly and why?
3. 9×6 vs 9×4 — numbers mean what, which needs the stronger motor?
4. 2200 kV on 3S nominal — max rpm? Show working.
5. 3S pack at 9.9 V total — fly or land, and why?
6. 2200 mAh 25C — max continuous amps? Show working.
7. State the 4 matching rules in order.
