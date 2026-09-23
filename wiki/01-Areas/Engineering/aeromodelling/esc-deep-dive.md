---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "ESC Deep Dive"
date: 2026-09-23
description: "ESC taught properly in simple words from the ESCs PDF (5 pp): what it does, PPM signal, MOSFET switching vs old resistors, BEC family, buying and wiring rules for interview."
tags: [btech, aeromodelling, esc, bec, brushless, avionics, team-onyx]
last_updated: "2026-09-24"
confidence: high
---

## For future agent
Full teaching ingest of `raw-sources/ESCs (Electronic Speed Controllers).pdf` (5 pages) for the Team Onyx interview. Style contract (owner ask 2026-09-24): teach like [[aerodynamics-foundations]] — tables, daily-life examples, memory tricks, interview-trap lines, self-check. Complements `[[avionics-rc-stack]]` §4. Interview yield: BEC purpose, amp-headroom rule, opto vs BEC choice, PPM path.

# ESC Deep Dive (simple words)

> Parent hub: [[INDEX]] · Bench sibling: [[propulsion-system-deep-dive]] · Chain recap: [[avionics-rc-stack]] · Cheat sheet: [[team-onyx-quick-revision]] · Drill: [[team-onyx-interview-mock-01]]
> How to use this page: read each heading slowly. Every hard word has a daily-life example. Lines starting with **INTERVIEW:** are the exact traps interviewers love.

## 1. What the ESC does — the throttle guy

ESC = Electronic Speed Controller. It sits between your receiver and your motor and does two jobs: (a) converts your stick movement into motor power, (b) feeds safe low voltage back to the receiver and servos.

Think of it like the dimmer switch of a ceiling fan — your thumb says "faster", the ESC delivers more power. Except it also doubles as a phone charger for the receiver (more on that in §4).

Three wire sets leave every ESC. Memorise them like a train route:

| Wire set | Goes to | Simple meaning |
|----------|---------|----------------|
| **Main battery lead** | the LiPo pack | food pipe — brings all the power in |
| **Servo-style lead** | receiver throttle channel | ear — listens to your thumb via PPM signal |
| **Motor leads** | the motor | hands — delivers the spinning power out |

**Memory trick:** "Food in, orders in, work out." Battery feeds, receiver orders, motor works.

**INTERVIEW:** "Name the three ESC connections" → battery lead to pack, servo lead to Rx throttle channel, motor leads to motor. Say it in that order.

## 2. PPM — how the receiver talks to the ESC

PPM = Pulse Position Modulation. Big name, simple idea: the receiver sends a stream of tiny electric pulses down the servo lead, and the WIDTH of each pulse carries the order. Stick low = narrow pulses = slow motor. Stick high = wide pulses = fast motor.

Daily-life version: imagine tapping someone's shoulder to set fan speed — quick light taps mean slow, long hard presses mean fast. Same taps also drive servos, which is why the ESC and servos speak the same language.

The full signal path to recite in one breath:

**Stick → transmitter → 2.4 GHz radio → receiver → throttle channel → PPM → ESC → motor.**

**INTERVIEW:** "How does the Rx talk to the ESC?" → same PPM signal as a servo, down the throttle channel; wider pulses = more power.

## 3. MOSFET switching — why modern ESCs don't burn up

Old speed controllers used a resistor + wiper, like dragging your foot on the ground to slow a bicycle — the extra energy just burned off as heat. At half throttle they got HOT and wasted your battery.

Modern ESCs use a MOSFET switch that flicks ON and OFF about **2000 times per second** and changes the ON-share of each cycle:

- **ON moment:** current rises, the motor winding's magnetic field builds up.
- **OFF moment:** the winding's stored magnetic energy flows back safely through a **flyback diode** (a one-way valve for electricity) instead of turning into heat.

| Controller | Method | Result |
|------------|--------|--------|
| Old resistor type | burns extra as heat | hot, wasteful at part throttle |
| Modern MOSFET ESC | fast ON/OFF switching + flyback diode | cool, smooth, efficient |

Daily-life version: resistor control = riding the brake downhill (pads heat up); MOSFET control = tapping the brake in quick pulses (stays cool).

**INTERVIEW:** "Why did resistor controllers fail, and what replaced them?" → they burned excess as heat at part throttle; MOSFET switching (~2000/s) with a flyback diode replaced them.

## 4. BEC — the built-in phone charger

Long ago RC planes carried TWO batteries: one big pack for the motor, one small pack for the receiver. Heavy and silly.

The BEC (Battery Eliminator Circuit) **eliminates the second battery**. It steps the big LiPo voltage (11+ V) down to **5–6 V** for the receiver and servos, and sends it back up the same servo lead. Exactly like a phone charger stepping wall power down to 5 V.

The family (from the workshop deck — know the names):

| Type | Simple meaning |
|------|----------------|
| ESC with **BEC** | built-in charger, powers Rx over the throttle lead |
| **UBEC** (universal) | separate external charger unit, cleaner power |
| **SBEC** (switching) | efficient switching type, stays cool under load |
| **LBEC** (linear) | simple type, runs warmer, for small setups |
| **OPTO** ESC | **NO BEC inside** — light-isolated signal only, you MUST power the receiver separately |

**Memory trick:** "BEC = Battery Eliminates Clutter. OPTO = On your own for Power To Others (receiver)."

**INTERVIEW:** "What does OPTO imply?" → no built-in BEC, so the receiver needs its own separate power supply. "BEC voltage?" → 5–6 V.

## 5. Buying and wiring rules — the interview favourites

**Rule 1 — always buy bigger than the motor.** A 10 A motor gets a **15 or 18 A ESC**, never 10 A. An exactly-matched ESC runs at 100% all flight, overheats, and dies mid-air — like carrying a school bag loaded exactly to your weight limit. Headroom stays cool.

**Rule 2 — brushless motors need their ESC.** A brushless motor takes 3-wire drive that only an ESC can make. Brushed motors can run on plain 2-wire DC, but the team standard is brushless + ESC anyway.

**Rule 3 — walk the signal path, don't memorise parts.** Tx stick → 2.4 GHz → Rx throttle channel → PPM → ESC → motor; BEC 5 V flows back to Rx and servos. If you can walk it forward and backward, every wiring question answers itself.

**INTERVIEW rapid-fire:**
- "12 A motor — which ESC?" → 15 or 20 A (next standard size up, never 12).
- "ESC rating equals motor current — fine?" → never fine; runs hot, burns.
- "Brushed vs brushless for the team?" → brushless, 3-wire + ESC, 85–90% efficient.

## Quick self-check (answers in [[team-onyx-quick-revision]])

1. Name the three ESC wire sets and where each goes.
2. What is PPM, who sends it, who receives it?
3. Why did resistor controllers fail at part throttle, and what replaced them?
4. BEC does what, at what voltage, and what does OPTO imply?
5. 12 A motor — which ESC rating and why?
6. Walk the full signal path from thumb to propeller.
