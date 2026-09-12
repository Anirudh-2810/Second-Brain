---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - one-page reference"
tags: [btech, engineering-drawing, solidworks, cad, cheatsheet, reference]
last_updated: "2026-09-12"
description: "One-page SolidWorks command reference: mouse controls, sketch states, feature picker, surfacing pipeline, mates, diagnostics, and keyboard shortcuts."
module: "engineering-drawing"
prerequisites: [["INDEX"]]
confidence: high
---

# SolidWorks Cheatsheet (One Page)

## For future agent
Capstone quick-reference. Condenses the module's command vocabulary onto one scannable page — no new concepts, pointers to home pages for depth. Menu paths 2021–2026-era; press `S` to search any moved command.

---

## Mouse + view

| Action | Input |
|---|---|
| Rotate | Middle-mouse drag |
| Zoom | Wheel |
| Pan | Right-drag (or Ctrl + middle-drag) |
| Normal-to a face/plane | Select + click Normal To |
| Standard views | Set per [[solidworks-basics-setup]] §2; Spacebar view menu |
| Section view | Right-click plane → Section View |

## Sketch states

| Color/status | Meaning | Action |
|---|---|---|
| Blue / Under Defined | Floppy — NOT done | Drag-test → add missing relation/dim |
| Black / Fully Defined | Locked — the goal | Proceed to feature |
| Red / Over-defined | Conflicting dims | Delete newest, use a relation |
| Brown / Dangling | Reference deleted | Re-attach or delete |

## Feature picker (60 seconds)

- Constant section pushed straight → **Extruded Boss/Cut** (+ draft for molded)
- Round about axis → **Revolved Boss/Cut** (half-profile + centerline)
- Along a path → **Swept Boss/Cut** (profile + smooth path, pierce relation)
- Morphing profiles, solid → **Lofted/Boundary Boss**
- Morphing profiles, skin → **Lofted/Boundary Surface** (fix connectors first!)
- Holes with standards → **Hole Wizard** (not plain cuts)
- Rounds/edges → **Fillet** (molded/stress) / **Chamfer** (machined/deburr)
- Hollow → **Shell** (late in tree) · Taper → **Draft** · Strength → **Rib**
- Half the work → **Mirror** · Many copies → **Pattern** (linear/circular/curve)
- Region control → **Split Line** · Posts → **Mounting Boss**

## Surfacing pipeline (7 words)

**Patches → Trim → Fill → Knit (tight) → Thicken → Dress-up.** Full version: [[surfacing-methodology]].

## Mates (assembly)

- Static 95%: Coincident, Concentric, Parallel, Perpendicular, Tangent, Distance, Angle
- Motion: Gear (set RATIO), Rack-pinion, Screw, Hinge, Cam
- Habits: fix first part at origin, mate to planes, one mate at a time, drag-test travel

## Diagnostics (run on every skin)

Zebra stripes (smoothness) → Curvature combs (sketch fairness) → Deviation/naked-edge scan → Draft analysis (molded) → Section view → Interference detection (assemblies) → Mass properties (units sanity).

## Shortcuts worth muscle memory

`S` search commands · `D` confirm sketch/feature (TBC per version — rebind if needed) · `Tab` flip 3D-sketch plane · `Ctrl+drag` copy feature/part · `Spacebar` orientation menu · `F` zoom-to-fit · mouse gestures (right-drag flick — customize once, keep forever; TBC exact defaults per version).

## Order of operations (tattoo version)

**Plane → fully-defined sketch → base feature → form → function → dress-up LAST → mate → drawing.** Details: [[part-assembly-drawing-workflow]].

## CROSS-REFERENCES
- [[INDEX]] · [[flowcharts-master]] · [[solidworks-basics-setup]] · [[sketch-mastery]] · [[surfacing-methodology]]
