---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Round 1"
unit: "Avionics and RC Stack"
date: 2026-09-19
description: "RC plane electronics chain: propeller sizing and pitch, brushed vs brushless motors and kV, LiPo voltage and C-rating, ESC, Tx/Rx, servo torque and speed."
tags: [btech, aeromodelling, avionics, propeller, brushless, lipo, esc, transmitter, receiver, servo]
last_updated: "2026-09-19"
confidence: high
---

## For future agent
Distilled from `[[raw-sources/Aerodynamics_and_Avionics_Study_Material.pdf]]` §9–15 (Propellers → Servos). Numbers here (voltages, kV example, C-rating example, 60° servo-speed definition) are favourite MCQ targets.

# Avionics — RC Stack (simple words)

> Parent hub: [[INDEX]] · Prev: [[wings-controls]] · Revision: [[team-onyx-round1-revision]]
> The full chain in one line: your hands move the **Transmitter →** radio waves fly to the **Receiver →** receiver tells the **ESC** how fast → ESC powers the **Motor →** motor spins the **Propeller**. Separately, the ESC gives 5 V power to the receiver, and the receiver moves the **Servos**.

## 1. Propeller — "a spinning wing that pulls the plane forward"

A propeller blade is just a small wing going in circles. Like a wing makes upward lift, the spinning blade makes forward pull. We call that forward pull **thrust**.

**Big vs small — the opposite of what you expect:**

- Want a FAST plane (jet fighter, passenger jet look)? Use a **small propeller that spins very fast**.
- Want a SLOW, punchy plane (stunt / aerobatic)? Use a **big propeller that spins slowly**.

Why? A big prop scoops lots of air each turn, but that air fights back (resistance). So it needs a very strong motor. A small prop sips air, so even a weaker but faster-spinning motor can pull it quickly.

Think of bicycle gears: big gear = strong push, slow spin (climbing). Small gear = fast spin (racing downhill).

- Motor in FRONT → normal propeller. Motor at BACK → special **pusher** propeller (pushes instead of pulls).
- **Smaller prop → higher top speed. Bigger prop → quicker acceleration** (reaches speed faster, but lower max speed).

**Reading the size stamp (always in inches, two numbers):**

Stamp **8×5** means: **8 inch diameter** (tip to tip length) × **5 inch pitch** (steepness, explained below). An 8×5 needs a STRONGER motor than an 8×4 because the second number is bigger.

**What is pitch?** Imagine the propeller is a screw going into soft wood. Pitch = how far forward the screw would move in ONE full turn. A flat blade (pitch 0) would go nowhere. Steeper blades (higher pitch) bite more air each turn — more pull, but needs more muscle.

- **Fine / low pitch** (flat-ish blades) → good for **take-off** (quick bite, easy spin).
- **Coarse / high pitch** (steep blades) → good for **cruise** (fast forward flight).

**MCQ:** "8×5 means?" → 8″ diameter, 5″ pitch. "Which needs stronger motor, 8×5 or 8×4?" → 8×5.

## 2. Motors — brushed (old) vs brushless (standard)

First pick the propeller, THEN pick the motor strong enough to spin it.

| | Brushed (old) | Brushless (modern standard) |
|---|---|---|
| Power wires | DC battery power, **2 wires**, connects straight to battery | Needs AC-type pulses, **3 wires**, MUST go through an ESC |
| Inside | A wire coil spins inside a can lined with magnets. Tiny carbon **brushes** rub and keep flipping the current so the coil keeps turning. Rubbing = wasted heat. | Coils stay still, magnets spin around them (out-runner type). Electronics flip the current in microseconds — no rubbing, very efficient. |
| Personality | Heavy, wasteful, mostly dead in RC hobby. More pulling force (torque), less speed. | Light, fast, efficient. **Almost every RC plane uses this.** |
| Seen in daily life | Electric drills, grinders, toys | RC planes, drones, e-bikes |

Two motors can have the SAME power but different character: one is a wrestler (**strong + slow**, for big props), the other is a sprinter (**weak + fast**, for small props).

**Motor size code** like **28-36** = can is **28 mm wide (diameter)** × **36 mm tall (height)**.

**kV rating — the most asked MCQ in this section.** kV does NOT mean kilovolt. It means **how many RPM (rounds per minute) the motor spins for each 1 volt**, with no propeller attached.

Formula: max RPM = kV number × battery volts.

Worked example from the PDF: **1800 kV motor + 12 V battery** → $1800 × 12$ = **21,600 rpm**.

**MCQ:** "kV stands for?" → RPM per volt. "1800 kV on 12 V?" → 21,600 rpm.

## 3. Battery — LiPo (the RC standard)

RC planes use **LiPo (Lithium Polymer)** batteries. Three things printed on them: voltage (S number), capacity (mAh), and power punch (C rating).

**Voltage — count the cells.** Each cell gives **3.7 V** normally.

- **2S** = 2 cells joined = $2 × 3.7$ = **7.4 V** (the blue pack photo in the PDF).
- **3S** = 3 cells = $3 × 3.7$ = **11.1 V** normally.

Safety limits per cell (never cross these or the battery puffs / dies):

- Full charge: max **4.21 V** per cell. So fresh 3S = about **12.4–12.6 V**.
- Empty: never below **3.3 V** per cell. So 3S must land by about **10.6 V**.
- Golden rule: **drain less = battery lives longer.** Land early.

**Capacity (mAh)** = fuel tank size. **2200 mAh** = can give 2200 milliamps for 1 full hour (or 4400 mA for half an hour, etc.).

**C-rating** = how fast you may drain the tank without damage. Multiply C × capacity (in amps) to get max safe continuous current.

Worked example from the PDF: **2.2 amp battery × 25C** = $2.2 × 25$ = **55 amps** continuous. So that pack can feed up to 55 A from full (~12.6 V) down to empty (~10.6 V). Higher C = more punch for aggressive flying.

**MCQ:** "2S means?" → 2 cells. "3.7 V is?" → one cell nominal. "2200 mAh 25C gives?" → 55 A.

## 4. ESC — Electronic Speed Controller (the middleman)

The ESC does two jobs:

1. **Power supply:** steps the big battery voltage DOWN to **5 V** for the receiver (this 5 V line is called **BEC — Battery Eliminator Circuit**, because you don't need a separate receiver battery). Note: NOT every ESC has a BEC — the PDF warns about this.
2. **Translator:** converts battery **DC into motor-style AC pulses** that a brushless motor needs. It also sets the speed based on your throttle stick.

**Buying rule (MCQ favourite):** ALWAYS buy an ESC rated HIGHER than your motor's draw. Motor pulls 10 A → buy a **15 or 18 A** ESC, never exactly 10 A.

Why? An exactly-matched ESC runs hot, overheats, and can burn out mid-flight. A bigger ESC stays cool and lives long ("radiates less heat").

## 5. Transmitter — the radio in your hands

The box with two sticks you hold. Modern ones use **2.4 GHz** frequency (like Wi-Fi). Advantages over old FM radios: short antenna, and many pilots can fly together without signal fights.

**Channels** = how many separate things you can control. A 3-channel radio controls 3 things (say: motor + 2 servos). Each extra function needs one more channel.

Standard RC plane radio = **6 channels**: (1) rudder, (2) elevator, (3) ailerons, (4) motor throttle, (5) Aux 1, (6) Aux 2. Aux = extras like bomb drop, lights, camera — worked by spare switches/knobs on the radio.

## 6. Receiver — the radio inside the plane

Small box inside the aircraft that listens to your transmitter on the same **2.4 GHz** link. The PDF photo is a 6-channel receiver (the SBUS port doesn't count as a channel).

- Runs on **5 V** coming from the ESC's BEC through the throttle cable.
- Sends position signals to each **servo**, and a speed signal to the **ESC** (which drives the motor).
- **Binding rule:** a receiver pairs with only ONE brand/type of transmitter (protocol must match). You cannot mix any Tx with any Rx.

## 7. Servos — the "muscles" that move everything

Servos are tiny motors-with-brains that move the flaps, throttle arm, landing gear, smoke system — anything that must move mid-air. Most run on **3–5 V**. Big planes use high-voltage servos on **7.4 V (2S LiPo)**.

Air constantly tries to push the flaps around (like wind slapping a door). The servo must FIGHT that wind and hold position. Bigger plane = bigger flaps = stronger wind = needs **more torque**.

**Torque** = strength = force × arm length (how far from the servo's centre the push acts). Like opening a door — pushing far from the hinge is easier. Servo torque is measured the same way.

**Speed** = how fast the servo arm sweeps **60 degrees, while pushing its maximum rated load**. Example: "0.12 sec/60°" means it takes 0.12 seconds to swing 60° at full strength.

- Control surfaces → want **fast** servos (instant response).
- Landing gear → want **slower** servos (gentle, scale-like motion).
- Warning from the PDF: don't trust "top speed" alone — it doesn't tell how quickly the servo OBEYS your stick (response delay matters too).

## Quick self-check

1. 9×6 vs 9×4 — which needs the stronger motor, and what do the numbers mean?
2. 2200 kV on 11.1 V (3S) — max rpm?
3. 3S LiPo: nominal, fresh, and minimum voltages?
4. 10 A motor — which ESC rating and why?
5. Servo speed is defined over how many degrees, under what load?
