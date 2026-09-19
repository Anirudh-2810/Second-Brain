---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Round 1"
unit: "Wings and Control Surfaces"
date: 2026-09-19
description: "Airfoil terms and types, five wing planforms, five mountings, dihedral effect, aspect ratio, angle of attack and stall, aileron-elevator-rudder axes."
tags: [btech, aeromodelling, airfoil, wing, aspect-ratio, stall, control-surfaces]
last_updated: "2026-09-19"
confidence: high
---

## For future agent
Distilled from `[[raw-sources/Aerodynamics_and_Avionics_Study_Material.pdf]]` §3–8 (wing basics → control surfaces). Highest MCQ density of the PDF — planform/mounting/control-surface identification questions come from here.

# Wings and Controls

> Parent hub: [[INDEX]] · Prev: [[aerodynamics-foundations]] · Next: [[avionics-rc-stack]]

## 1. Airfoil terminology and types

1. **Leading edge** — front point, maximum curvature.
2. **Trailing edge** — rear/end point.
3. **Chord line** — straight line joining leading to trailing edge.
4. **Mean camber line** — locus of midpoints between upper and lower surfaces.
5. **Thickness** — measured along chord, either vs mean camber line or vs chord line.

| Type | Camber vs chord line | Lift at zero AoA | Notes |
|------|----------------------|------------------|-------|
| **Symmetrical** | identical upper/lower; camber = chord | **none** | helicopter main rotors, vertical tails (no unwanted turning in straight flight) |
| **Asymmetrical (cambered)** | more curvature above chord | **useful lift at 0° AoA** | more lift per AoA, better lift-to-drag, better stall characteristics |

## 2. Wing planforms (top-view shape)

| Planform | Character | Trade-off |
|----------|-----------|-----------|
| **Rectangular** | straight, untapered | simplest to manufacture |
| **Tapered straight** | chord narrows toward tip, approximates elliptical lift distribution | compromise: manufacturability vs efficiency |
| **Elliptical** | elliptical outline | **lowest induced drag, most aerodynamically efficient** — but poor manufacturability |
| **Swept** | leading edges swept back | reduces drag at **transonic** speeds (normal-velocity component) |
| **Delta** | triangle, very low aspect ratio | efficient in **all regimes** (subsonic/transonic/supersonic); supersonic European designs |

Planform area = wing area + fuselage-projected centerline extension.

## 3. Wing mounting (monoplane, vs fuselage)

- **Low wing** — near/below fuselage bottom.
- **Mid wing** — halfway up the fuselage.
- **Shoulder wing** — upper "shoulder", slightly below top (sometimes classed as high-wing subtype).
- **High wing** — on top / cabin-roof projection above fuselage.
- **Parasol** — clear above fuselage on cabane struts / pylon / pedestal.

## 4. Dihedral, anhedral, dihedral effect

- **Dihedral angle** — upward angle of wings from horizontal. Multiple kinks along span = **polyhedral**.
- **Dihedral effect** — rolling moment from non-zero sideslip; **more dihedral ⇒ stronger effect ⇒ more spiral stability**.
- **Fighters**: near-zero or **anhedral** (downward) → less spiral stability → **more manoeuvrability**.
- **High-wing heavies** (An-124, Galaxy): wing above CG gives pendulum/keel-effect dihedral for free; designers **add anhedral** to cancel the excess so the plane stays manoeuvrable.

## 5. Aspect ratio (AR)

Skinny long wing (glider) = high AR; short fat wing = low AR.

- Square wing: $AR = span / chord$.
- General: $$AR = span^2 / wing\ area$$

## 6. Angle of attack, stall, flow separation

- **AoA ($\alpha$)** — angle between chord line and incoming airflow. Nose-up/climb ⇒ AoA rises; nose-down/dive ⇒ falls.
- More AoA ⇒ more lift, **until the critical angle** (~16° in the PDF diagram). Beyond it lift **drops** = **stall**.
- Cause chain: rising AoA → air flows against rising pressure → **flow separation** creeps forward on the wing top → separated region grows → turbulent wake grows → lift collapses, pressure drag spikes.
- Cambered airfoil still lifts at $\alpha = 0°$; symmetrical does not.

## 7. Primary control surfaces

| Surface | Location | Motion | Axis | Effect |
|---------|----------|--------|------|--------|
| **Ailerons** | wingtips, move **opposite** (one up / one down) | Roll / banking | **longitudinal** | raised aileron → less lift on that wing; dropped → more lift (camber + downwash) |
| **Elevators** | horizontal stabilizer, move **together** up/down | Pitch | **lateral** | up-elevator → more downward lift at tail → nose-up (climb); down → nose-down. Moment about CG |
| **Rudder** | vertical stabilizer | Yaw | **vertical** | deflect right → lift pushes tail left → nose turns right. Used **with roll** for turns |

Horizontal stabilizers are inverted airfoils; the vertical stabilizer is a symmetrical-airfoil section.

## Quick self-check

1. Which planform has lowest induced drag, and why isn't everything built that way?
2. Which mounting sits on struts above the fuselage?
3. Why do fighters use anhedral and heavy high-wings too?
4. $AR$ for span 12 m, area 24 m²?
5. Aileron up on the right wing → roll which way? Rudder alone turns nose about which axis?
