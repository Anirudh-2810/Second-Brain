---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Propulsion System Deep Dive"
date: 2026-09-23
description: "Propulsion chain from Propulsion System PDF (18 pp): BLDC outrunner vs inrunner, prop diameter vs pitch, kV math, LiPo bands, ESC+BEC, Tx/Rx/servo links."
tags: [btech, aeromodelling, propulsion, bldc, propeller, lipo, esc, team-onyx]
last_updated: "2026-09-23"
confidence: high
---

## For future agent
Full ingest of `raw-sources/Propulsion System.pdf` (18 pages) for the Team Onyx interview. Chain order to memorise: motor → propeller → ESC → battery → servo → Tx → Rx. Numbers that get asked: BLDC 85–90% vs brushed 75–80%, kV × volts worked example, LiPo per-cell bands. Sibling: [[esc-deep-dive]] for component detail; chain recap: [[avionics-rc-stack]].

# Propulsion System Deep Dive

> Parent hub: [[INDEX]] · Sibling: [[esc-deep-dive]] · Chain: [[avionics-rc-stack]] · Mock: [[team-onyx-interview-mock-01]]
> Source: `raw-sources/Propulsion System.pdf`.

## 1. What propulsion means

Push forward: the engine accelerates a working fluid (air) and the reaction pushes the aircraft. RC electric chain: battery → ESC → BLDC motor → propeller → thrust; Rx/Tx command it, servos steer it.

## 2. Motors — BLDC is the standard

Brushed DC wears brushes, sparks, needs maintenance, 75–80% efficient. BLDC: no rubbing, coils switched electronically, 85–90% efficient, lighter, faster, quieter, easily controlled. Two layouts:

| Type | Stator / rotor | Character | Drive |
|---|---|---|---|
| Outrunner | stator middle, rotor outside | more torque, direct-drive prop, less friction | team default for props |
| Inrunner | stator outside, rotor middle | more RPM, needs gearbox for prop, more friction | EDF / high-speed use |

Working idea: stator coils energise in sequence, attract then repel rotor magnets; energising pairs (one pulls, one pushes) is faster than single-coil stepping.

## 3. Propeller — diameter vs pitch

A fan converting rotation into thrust. Two numbers in inches: diameter (tip-to-tip length) × pitch (forward advance per revolution, like a screw in wood). Small prop spinning fast → top speed; big prop spinning slow → punch/acceleration but needs a stronger motor. Fine/low pitch → take-off bite; coarse/high pitch → cruise. Stamp 8×5 = 8 inch diameter, 5 inch pitch; 8×5 needs a stronger motor than 8×4. Pusher props sit at the back and push.

## 4. ESC + battery + servo + radio (condensed)

- ESC: varies speed/direction, dynamic brake, smooth efficient control; takes PPM from the Rx throttle channel; built-in BEC extracts 5 V from the LiPo for Rx/servos.
- LiPo: lithium polymer, high discharge, high energy density, thin, customisable shape, long cycle life. Per-cell bands: 3.7 nominal, 4.21 full, 3.3 floor. 3S = 11.1 nominal, ~12.4–12.6 fresh, land by ~10.6.
- Servo: DC motor + closed-loop feedback for fixed-angle moves (flaps, gear, throttle arm), not continuous spin.
- Tx/Rx: Tx converts stick motion to radio signal (modulation); Rx pulls data from the waves and routes servo vs motor commands; the motor path always goes through the ESC.

## 5. Matching rules to recite

- Pick prop first, then motor strong enough, then ESC above motor amps.
- Outrunner + direct prop for torque; inrunner only with gearbox.
- kV means RPM per volt unloaded: max RPM = kV × volts. PDF example: 1800 kV × 12 V = 21,600 rpm.
- C-rating headroom: max amps = Ah × C (2.2 Ah × 25C = 55 A continuous).

## Quick self-check

1. Outrunner vs inrunner — which drives a prop directly and why?
2. 9×6 vs 9×4 — numbers mean what, which needs the stronger motor?
3. 2200 kV on 3S nominal — max rpm?
4. 3S pack at 9.9 V total — fly or land, and why?
