---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "ESC Deep Dive"
date: 2026-09-23
description: "ESC distilled from ESCs PDF (5 pp): PPM input, MOSFET switching, BEC 5-6V, opto vs BEC types, amp-headroom buying rule for interview."
tags: [btech, aeromodelling, esc, bec, brushless, avionics, team-onyx]
last_updated: "2026-09-23"
confidence: high
---

## For future agent
Full ingest of `raw-sources/ESCs (Electronic Speed Controllers).pdf` (5 pages) for the Team Onyx interview. Complements `[[avionics-rc-stack]]` §4 with component-level detail (MOSFET switching ~2000/s, flyback diode, PPM, BEC family). Interview yield: BEC purpose, amp-headroom rule, opto vs BEC choice.

# ESC Deep Dive

> Parent hub: [[INDEX]] · Bench sibling: [[propulsion-system-deep-dive]] · Chain recap: [[avionics-rc-stack]] · Mock: [[team-onyx-interview-mock-01]]
> Source: `raw-sources/ESCs (Electronic Speed Controllers).pdf`.

## 1. What the ESC does

Interface between receiver and power plant. Three wire sets: (1) main battery lead, (2) servo-style lead into the receiver throttle channel, (3) motor leads. Jobs: vary speed/direction, act as dynamic brake, generate 3-phase drive for brushless, step battery voltage down for the receiver.

## 2. Input signal — PPM

Both brushed and brushless ESCs take the same PPM (pulse position modulation) signal as a servo, straight from the throttle channel. More throttle stick → wider pulses → more average power to the motor. Say this verbatim if asked how Rx talks to ESC.

## 3. How speed control works — MOSFET switching

Old resistor/wiper controllers burned excess as heat at part throttle. Modern ESCs switch a MOSFET ON/OFF ~2000 times per second and vary the ON share of each cycle. ON: current rises as winding magnetic field builds. OFF: stored magnetic energy is absorbed and returned through a flyback diode across the motor. Result: smooth, efficient speed control instead of resistor heat.

## 4. BEC — battery eliminator circuit

Early RC needed two packs (receiver + motor). The BEC removes the receiver pack by stepping LiPo voltage down to 5–6 V for receiver and servos. An ESC with built-in BEC powers Rx over the throttle lead; an OPTO ESC has no BEC and needs a separate receiver supply. Family from the workshop deck: brushless/brushed ESC, ESC with BEC, UBEC (universal), SBEC (switching), LBEC (linear).

## 5. Buying and wiring rules (interview favourites)

- ALWAYS rate ESC above motor draw: 10 A motor → 15 or 18 A ESC. Matched ratings run hot and burn mid-flight; headroom stays cool.
- Brushless motor needs its ESC (3-wire AC-style drive); brushed can take 2-wire DC but the team standard is brushless + ESC.
- Signal path to recite: Tx stick → 2.4 GHz → Rx throttle channel → PPM → ESC → motor; BEC 5 V back-feeds Rx and servos.

## Quick self-check

1. Why did resistor controllers fail at part throttle, and what replaced them?
2. What three wire sets leave an ESC, and where does each go?
3. BEC does what, at what voltage, and what does OPTO imply?
4. 12 A motor — which ESC rating and why?
