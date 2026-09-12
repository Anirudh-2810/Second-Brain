---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - shredder and recycling machines"
tags: [btech, engineering-drawing, solidworks, cad, shredder, machines, welding, frames]
last_updated: "2026-09-12"
description: "PL2 shredder and recycling machine builds: plastic/paper/agri shredders, wood chipper, cutting chamber anatomy, blades, frames, and drive integration."
module: "engineering-drawing"
prerequisites: [["bevel-planetary-gearboxes"], ["gearbox-fundamentals"], ["INDEX"]]
confidence: medium
---

# Shredders & Recycling Machines

## For future agent
PL2 build page. Videos: #1 36-blade plastic shredder #329 · #4 heavy-duty prototype #341 · #7 mini plastic #328 · #10 single-shaft paper #330 · #27 industrial paper shredder · #5 mini agri #297 · #24 tree-chipper #327 · #26 wood chipper prototype #326 · #34 link-index (skip). Per-video specifics TBC vs bulk transcripts. Teaches: cutting chambers, blade stacks, weldment frames, and gearbox-to-machine integration (these machines ARE gearboxes with teeth on the outside).

> **Why shredders teach machine design:** one machine forces every subsystem — cutting chamber (precision), blades (wear parts), drive (gearbox + motor), frame (weldment), hopper (sheet metal), safety (guards + e-stop thinking). Model a shredder completely and no machine architecture surprises you again.

---

## 1. Cutting-chamber anatomy (the heart)

```
HOPPER (sheet metal, guides material in)
   ↓
BLADE STACK on hexagonal/octagonal SHAFTS (2 shafts counter-rotating typical)
   ↓ blades interleave with SPACERS + COMBS (clear jams, strip material)
SCREEN below (sized holes = output particle size)
   ↓
COLLECTION bin / conveyor out
```

- **Blades:** hooked/clawed discs, stacked with spacers; 36-blade count in #329 sets the patterning exercise (circular/linear patterns of blade instances + angular offsets between adjacent blades — TBC exact video method).
- **Shafts:** hex profiles so blades can't spin loose (flats drive the stack — elegant, no keys needed per blade); stepped ends for bearings.
- **Combs/stripers:** static fingers interleaving the blade stack that peel material off — the part beginners omit; without strippers the chamber packs solid.
- **Screen:** perforated arc under the chamber; hole size = product spec. Model as patterned cuts (keep counts sane for rebuild speed).

## 2. Playlist build map

| Build | Focus (TBC per-video) |
|---|---|
| #329 36-blade plastic shredder (#1) | Full chamber: blade stack patterning + spacers + screen |
| #341 heavy-duty prototype (#4) | Heavier shafts/bearings, frame upsizing — compare with #1 for duty scaling |
| #328 mini plastic (#7) | Compact variant — same architecture, smaller envelope |
| #330 single-shaft paper (#10), #27 industrial paper | Single-rotor + fixed-bed-knife cutting (different physics: shear vs tear) |
| #297 mini agri (#5), #327 tree chipper (#24), #326 wood chipper (#26) | Infeed hoppers, flywheels/anvils for wood, discharge chutes |
| Drive side (all) | Gearbox + motor coupling to blade shafts — torque math from [[gearbox-fundamentals]] |

## 3. Frames & weldments (the skeleton)

Shredder frames are **weldments**: structural members (square tube/angle/channel) cut and welded. SolidWorks Weldments module: sketch the skeleton lines → assign profiles → automatic miters/trims + cut list. Model weld beads only where the drawing must call them (cosmetic); the **cut list + weld table** on the drawing is the deliverable. Guards (sheet-metal covers over drives/blades) are safety AND legal — model them closed, with fasteners, no "guard removed for clarity" in final assemblies (awareness: real machines need interlocked guards — TBC regulatory depth out of scope).

## 4. Sheet-metal hoppers (the funnel)

Hoppers = tapered boxes from sheet: model with Sheet Metal tools (base flange + miter flanges or lofted bends where supported — TBC per version), check **flat pattern** (it must unfold without distortion — the manufacturability test), bend radii to shop capability (TBC: confirm with fabricator), hem raw edges (safety).

## 5. Failure clinic

| Symptom | Cause → Fix |
|---|---|
| Blade stack binds in assembly | Spacing math off (blade + spacer widths ≠ chamber width) → drive stack width from chamber via equations |
| Shafts can't be inserted in CAD | Assembly order ignored → plan insertion (shafts before side plates? side plates split?) like the gearbox split-plane habit |
| Screen holes kill rebuild | Thousands of patterned cuts → pattern a small zone + cosmetic rest, or suppress for working config (configurations!) |
| No stripper combs | Chamber packs in reality → add interleaving combs (lesson, not just geometry) |

**Verify in-app:** model a 6-blade mini chamber (2 shafts, spacers, screen arc, side plates), assemble, rotate shafts by hand checking blade interleave clearance. Scale the recipe toward #329's 36 blades only after the mini works.

**Next:** [[conveyors-material-handling]].

## CROSS-REFERENCES
- [[INDEX]] · [[gearbox-fundamentals]] · [[conveyors-material-handling]] · [[presses-forming-drone]] · [[dressup-productivity]] (patterns) · [[part-assembly-drawing-workflow]]
