---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "Interview prep - CAD & Design (Odyssey drone team)"
tags: [btech, engineering-drawing, autocad, blender, interview-prep, drone, cad-design]
last_updated: "2026-09-10"
description: "CAD & Design interview prep for the Odyssey (Somaiya drone team) technical round: AutoCAD 2D rapid-fire, Blender essentials, drone structures, tolerances, UCS/EXTRUDE, likely tasks and pitch script."
module: "engineering-drawing"
prerequisites: ["[[overview]]", "[[autocad-lab-and-exam-prep]]"]
confidence: medium
---

# CAD & Design Interview Prep — Odyssey Drone Team

## For future agent
Interview brief built 2026-09-10 for the Odyssey (Somaiya student drone-making team) CAD & Design technical round. Team identity user-stated, not verified against official Somaiya listings (the famous aero club is Team Onyx). Emphasis per posting: AutoCAD 2D, 3D modeling, structures, Blender. Pair with [[01-Areas/Business/careers/interview-counter-guide]] for behavioral meta-strategy (STAR, no-bluff rule).

---

## 1. AutoCAD 2D rapid-fire

- **Commands cold:** `LINE CIRCLE ARC RECTANGLE POLYGON TRIM EXTEND OFFSET MIRROR ARRAY HATCH LAYER DIMLINEAR DIMSTYLE PLOT`
- **Likely live task:** motor-mount plate — `RECTANGLE → CIRCLE → TRIM → OFFSET → ARRAY` (bolt holes) → `HATCH` → `DIMLINEAR`
- **`BLOCK`** for repeated parts (standoffs, holes); freeze vs off for layers
- **Plot:** 100mm part at 1:2 on A4 — scale factor + Layout viewport
- **Layers:** object / hidden / centre / hatch / dimension; BIS linetypes (thick = visible, dashed = hidden, dash-dot = centre)
- **Dimensioning:** mm, no unit symbol; Ø circles, R arcs; never over-dimension; chain vs parallel
- **Views:** first-angle (India standard — top view *below* front); dashed hidden lines; 45° section hatching

## 2. UCS + EXTRUDE (2D → 3D bridge)

- **UCS = where zero is and which way is up, right now.** `UCS → Face/Object/3Point` pins the working plane onto any surface (e.g. a vertical arm face) so 2D commands draw flat on it. Wrong UCS = geometry floating at wrong Z — check the icon first.
- **EXTRUDE:** closed 2D profile → solid (height + taper). Drone pipeline: sketch arm plate on right UCS → `EXTRUDE` 4mm → `SUBTRACT` bolt-hole cylinders → manufacturable part.
- **Name-drops:** `PRESSPULL`, `REVOLVE` (spinner cones), `UNION/SUBTRACT/INTERSECT`, `FILLET` internal corners (stress cracks start at sharp corners).

## 3. Blender essentials

- **Mesh vs parametric:** Blender = mesh (renders, concept shells, camera mounts); Fusion/SolidWorks = dimension-driven parts. State when you'd use which.
- **Modifiers:** Mirror, Subdivision Surface, Boolean, Solidify.
- **Print-ready:** manifold/watertight, STL export, walls ≥ 1.2mm, holes **+0.2mm** oversize (FDM ≈ ±0.2mm), flat face down.

## 4. Tolerances (one-line mastery)

- **Definition:** allowable variation in a dimension — the margin of error a part can have and still assemble and function.
- **Fits:** clearance (hole bigger — spins free, prop on shaft) / interference (pressed, never moves) / transition.
- **Golden line:** tight tolerances cost money — specify them only where function demands it.
- **Drone call:** generous on mounting plates (±0.1mm stacks fine on M3), tight only where motion/vibration lives (motor shaft holes).

## 5. Drone structures cheat sheet

- **Anatomy:** frame + 4 arms, motors + ESCs, props, FC, PDB, LiPo. X-quad standard (symmetric CG, simple mixing).
- **Numbers:** thrust-to-weight **≥ 2:1**; CG at geometric center; prop clearance drives wheelbase (5" props ≈ 220mm class).
- **Materials:** carbon plates for arms (laser-cut 2D profiles — AutoCAD skill applies directly), TPU soft mounts (vibration damping), PLA/PETG printed brackets.
- **Vibration:** prop imbalance → gyro noise → jello/unstable flight. Fix: balance props + soft-mount FC, never add mass.
- **Weight budget:** every gram costs flight time — lightening holes and pocketed arms, never across load paths.

## 6. Rehearsal questions

1. Design a 2205 motor mount on a 4mm carbon arm (M3 pattern, clamp vs through-bolt, print orientation, hole oversize).
2. X-frame vs H-frame? (symmetry, CG, yaw authority.)
3. Printed arm cracks along layer lines — why + fix? (load across layers; reorient or flat carbon plate.)
4. Read a drawing — what's missing? (dimensions, hidden lines, title block, tolerances.)
5. Carbon vs aluminium arms? (stiffness-to-weight vs cost/crash-replacement/tooling.)
6. Keeping the FC/ESC stack alive in a crash? (soft mounts, standoffs, guards, battery ejection path.)

## 7. "Have you made any projects?" script

> *"Most of my shipped projects are software — [roadtrip-pomodoro: full-stack timer, Next.js + Supabase, live on Vercel] and [stock-agent]. For CAD, my project work is my Sem-1 ED portfolio — AutoCAD lab sheets, orthographic sets, dimensioned parts — plus Blender modeling. That's why I want this role: drafting fundamentals plus a shipping habit, converting into real drone hardware from mounts and plates up."*

Rules: never bluff a CAD project (follow-ups kill); bridge don't apologize; carry 2 printed sheets + Blender screenshots and offer a walkthrough. Power move (2+ days out): model + dimension one quad arm plate / motor mount, print the drawing, walk in with your name in the title block.

## CROSS-REFERENCES

- [[overview]] · [[autocad-lab-and-exam-prep]] · [[orthographic-projections]] · [[isometric-and-sections]]
- [[01-Areas/Business/careers/interview-counter-guide]] (STAR, trap answers, no-bluff rule)
