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

# Avionics — RC Stack

> Parent hub: [[INDEX]] · Prev: [[wings-controls]] · Revision: [[team-onyx-round1-revision]]
> Signal chain: **Tx → (2.4 GHz) → Rx → ESC → motor → propeller** · **ESC-BEC (5 V) → Rx → servos**.

## 1. Propeller — "lifts the airplane forward"

- Spinning wing: rotary motion creates front/back pressure difference → **thrust**.
- **Fast plane** (jet/fighter) → **small prop, spins fast**. **Slow/acrobatic plane** → **large prop, spins slow**. (Big props move more air per turn but resist more → need a stronger motor.)
- Front motor = normal prop; rear motor = **pusher** prop.
- Size stamp in inches: **diameter × pitch**, e.g. **8×5** = 8″ diameter, 5″ pitch. Needs a stronger motor than 8×4.
- **Pitch** = distance the prop would screw forward in one revolution through a soft solid. Pitch 0 = flat. Higher pitch = steeper blades = more air per turn = stronger motor needed.
- Fine (low) pitch → take-off; coarse (high) pitch → cruise.
- Rule of thumb: **smaller prop → faster top speed; larger prop → faster acceleration.**

## 2. Motors

| | Brushed | Brushless |
|---|---|---|
| Power | DC, 2 wires, direct to battery | AC, 3 wires, needs ESC |
| Inside | wire coil spins inside permanent-magnet can; **brushes** commutate | stationary coils, magnet spins around (out-runner); coils pull magnets in microseconds |
| Character | heavy, inefficient, extinct in RC hobby; more torque, less rpm | **standard in RC**: faster, more efficient |
| Everyday analog | drills, grinders | RC planes/drones |

- Same power can be wound **strong+slow** (big props) or **weak+fast** (small props).
- Frame code e.g. **28-36** = 28 mm can diameter × 36 mm height.
- **kV rating = RPM per volt** (not kilovolt). Example: **1800 kV × 12 V = 21,600 rpm** max.

## 3. Battery (LiPo standard)

- Nominal **3.7 V/cell**. Example: **2S = 2 cells = 7.4 V**.
- Safety window per cell: never below **3.3 V** discharged, never above **4.21 V** charged. Fresh 3S ≈ 12.4 V; drain limit ≈ 10.6 V. **Drain less = longer life.**
- **Capacity**: 2200 mAh = delivers 2200 mA for 1 hour.
- **C-rating** = max continuous current multiplier. Example: 2.2 A × **25C = 55 A** continuous (from ~12.6 V down to 10.6 V). Higher C ⇒ more power.

## 4. ESC (Electronic Speed Controller)

1. Steps battery voltage down to **5 V** for the receiver (BEC — not present on every ESC).
2. Converts battery **DC → AC** for the brushless motor.
3. **Amperage headroom rule**: 10 A motor → buy **15–18 A** ESC, never exactly 10 A. Oversized ESC runs cooler; undersized overheats and can burn out.

## 5. Transmitter

- Pilot's radio; modern = **2.4 GHz** (many pilots at once, short antenna; older FM obsolete).
- **Channels** = number of things controlled. 3-channel = 3 servos/motors/accessories.
- Standard RC plane = **6 channels**: rudder, elevator, ailerons, motor, **Aux 1, Aux 2** (bomb drops, lights — extra switches/knobs).

## 6. Receiver

- Lives in the aircraft; 6-channel example (SBUS slot doesn't count as a channel). Binds on the same **2.4 GHz**.
- Runs on **5 V** from the ESC's **BEC (battery eliminator circuit)**; signals servos + tells ESC the throttle.
- **Binding caveat**: each Rx binds only to a specific Tx brand/type (protocol-dependent).

## 7. Servos — the "muscles"

Drive control surfaces, throttle, gear, smoke — anything needing in-air input. Most run **3–5 V**; big-plane high-voltage servos run **7.4 V / 2S LiPo**.

- **Torque** = force × distance from servo centre. Must fight air load trying to back-drive the surface — **bigger plane ⇒ more torque**.
- **Speed** = minimum time to rotate **60° at max rated torque**. Control surfaces want **fast**; landing gear wants slower. "Top speed" alone doesn't measure stick-response latency.

## Quick self-check

1. 9×6 vs 9×4 — which needs the stronger motor, and what do the numbers mean?
2. 2200 kV on 11.1 V (3S) — max rpm?
3. 3S LiPo: nominal, fresh, and minimum voltages?
4. 10 A motor — which ESC rating and why?
5. Servo speed is defined over how many degrees, under what load?
