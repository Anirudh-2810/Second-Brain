---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Workshop PPTs Merged"
date: 2026-09-23
description: "Merged build workflow from Workshop PPT (45 pp) + WORKSHOP PPT 2021 (67 pp): history, classifications, aero recap, design process, full avionics chain to first flight."
tags: [btech, aeromodelling, workshop, build-process, design, avionics, team-onyx]
last_updated: "2026-09-23"
confidence: medium
---

## For future agent
Merged ingest of `raw-sources/Workshop PPT.pdf` (45 pp, classic deck) and `raw-sources/WORKSHOP PPT 2021.pdf` (67 pp, expanded deck with future-of-aviation + battery/ESC/servo detail). ~70% overlap by design; this page keeps one build flow and notes 2021 deltas instead of two duplicate pages. Use for STAR build stories and pre-flight checklist generation. Theory detail lives in [[aerodynamics-foundations]], [[wings-controls]], [[avionics-rc-stack]].

# Workshop PPTs — Merged Build Flow

> Parent hub: [[INDEX]] · Theory: [[aerodynamics-foundations]] · Chain: [[avionics-rc-stack]] · Bench: [[esc-deep-dive]] + [[propulsion-system-deep-dive]] · Mock: [[team-onyx-interview-mock-01]]

## 1. Which deck is which

- Classic `Workshop PPT.pdf`: history (da Vinci → Cayley 1853 glider → Lilienthal → Wright 1903-12-17), aircraft gallery (An-225, A380, B-2, F-35, Concorde), classifications, stability/control, parts, aero intro, design process through empennage.
- 2021 deck: same spine plus modern era (alternative fuels, zero-carbon aim), fuller aero derivations (F/W climb math, downwash/lift story, MAC integral, efficiency = L/D), airfoil camber family, propeller/battery/ESC/Tx-Rx/servo chapter with emoji diagrams, final-connections → first flight close.
- Overlap: forces, Bernoulli, drag types, airfoil geometry, wing parameters, tail. Read 2021 for the avionics chapter; read classic for the tighter design-process slide order.

## 2. Classification rapid-fire (both decks ask this)

- By usage: passenger / cargo / military. By weight: lighter-than-air (aerostats) vs heavier-than-air. By wing count: monoplane / biplane / multiplane. By landing: land / sea / amphibious. By wing mount: low / mid / high / parasol; dihedral (lateral stability) vs anhedral (combat agility, unstable). By speed: subsonic < Mach 1, supersonic > Mach 1 (Tu-144, Concorde as civil examples), hypersonic > Mach 5 (X-43).
- 2021 adds rotary vs fixed wing (Cessna 172 vs V-22 Osprey) and morphable/wingless/lighter-than-air framing from the aviation definition.

## 3. Aero recap (one paragraph per force)

Lift (perpendicular to flow, via centre of pressure), weight (empty + payload + fuel), thrust (propulsion reaction), drag (parallel, opposing motion: skin-friction, induced as lift by-product, interference at junctions, wave from shocks). Lift = dynamic pressure × wing area; depends on density, velocity squared, area. 2021 climb line: F/W = a/g, F/W > 1 accelerates vertically. Flaps: extra lift on take-off, extra drag on landing for slowdown.

## 4. Design process (classic order, memorise)

Problem statement → airfoil selection & analysis → wing configuration and dimensions → empennage configuration and dimensions → stability and control. Wing parameters to name: incidence/AoA, aspect ratio, taper ratio Ct/Cr, sweep, MAC (rectangular wing MAC = chord), efficiency = L/D. Tail: full assembly aft of fuselage — fin + elevators + attachment structure.

## 5. Avionics chain to first flight (2021 chapter)

Battery types ladder (lead-acid → NiCad → NiMH → Li-ion → Li-poly → Li-metal); LiPo wins on energy density, thinness, low resistance, shape, cycle life. ESC chapter: controls/regulates BLDC speed; miniature RC units; brushed/brushless/BEC/UBEC/SBEC/LBEC family. Tx/Rx: sticks → modulation → radio → Rx → servos/ESC; receiver connections diagram; servo = precise angle/velocity/acceleration motor; final-connections slide = now ready to fly.

## 6. 2021 deltas to cite in interview

Zero-carbon future aim, ethanol/electric/solar prototypes, MAC integral form, camber family (low/deep/symmetrical/cambered), constant-speed vs ground-adjustable props, LiPo intercalation line, BEC family table, Tx/Rx/servo emoji walkthrough. If asked what changed between decks, name any three.

## Quick self-check

1. Recite the 5-step design process without looking.
2. Classify by mount: low vs high wing trade, dihedral vs anhedral use.
3. F/W > 1 means what, in one line?
4. Walk final connections: battery → ? → ? → ? → air.
