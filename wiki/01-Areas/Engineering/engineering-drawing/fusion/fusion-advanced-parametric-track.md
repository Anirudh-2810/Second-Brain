---
course_code: "BTech-ED-CAD"
course_name: "Engineering Drawing — CAD self-study"
unit: "Fusion 2 — Advanced parametric track (for AutoCAD users)"
date: "2026-10-03"
last_updated: "2026-10-03"
description: "Advanced Fusion track for someone who already knows AutoCAD basics — parameters and equations, fully-defined sketches, Body vs Component, joints, shell and ribs, pattern discipline, Check plus 3MF export with hole-tower tolerance, and 8 showable hardware projects."
tags: [cad, fusion, parametric, autocad, 3d-printing, hardware, engineering-drawing, projects, showable]
confidence: medium
prerequisites: ["[[01-Areas/Engineering/engineering-drawing/fusion/INDEX]]", "[[01-Areas/Engineering/engineering-drawing/fusion/fusion-setup-and-interface]]", "AutoCAD 2D basics"]
sources: ["Fusion track hub + installed-app verification pending by user"]
---

## For future agent
Advanced Fusion page for a user who knows AutoCAD 2D and wants beyond cubes. Scoped as the **print-side complement to SolidWorks** per [[01-Areas/Engineering/engineering-drawing/fusion/INDEX]] — never a second full CAD track. Interface paths are `medium`/`TBC`: Fusion moves between releases, so the user confirms paths in-app. Use for parametric discipline, enclosure/wheel/bracket builds, and portfolio-ready hardware parts.

# Fusion Advanced — Parametric Track (AutoCAD → Fusion)

> Hub: [[01-Areas/Engineering/engineering-drawing/fusion/INDEX]] · Setup: [[01-Areas/Engineering/engineering-drawing/fusion/fusion-setup-and-interface]] · Sketch habits transfer from [[01-Areas/Engineering/engineering-drawing/solidworks/sketch-mastery|SolidWorks sketch-mastery]] · Workflow: [[01-Areas/Engineering/engineering-drawing/solidworks/part-assembly-drawing-workflow|part-assembly workflow]]

## 1. AutoCAD → Fusion bridge (what changes)

| AutoCAD habit | Fusion equivalent | Trap |
|---|---|---|
| Lines + trims, exact coords | Sketch + **constraints + dimensions** | A sketch that *looks* right but is blue (under-defined) will break later — constrain till black |
| Blocks | **Components** (not Bodies) | Bodies merge silently; Components stay separable in the Browser — lid and box must be Components |
| Layers | Browser tree + visibility | Features nest inside Components — expand before assuming missing |
| DIMSCALE / printing | **Parameters + 3MF export** | Literals typed 3x = 3 chances to forget — drive with `wall`, `pitch`, `n` |
| XREF assemblies | **Joints** (rigid/revolute) | Mates are motion definitions, not just placement — pan-tilt needs revolute joints to prove movement |

## 2. Parametric discipline (the one skill that shows)

Set once in Modify → Change Parameters:

- `wall = 2.5` (mm), `hole_dia = 3.2` (M3 clearance), `pitch = 20`, `n = 2`
- Hole row length = `pitch * (n-1)` — never type 20/40 manually
- Extrude depth = `wall * 2`, fillet = `wall * 0.8`

**Test:** change `n` 2→3. If the part updates clean, it is parametric. If holes detach, the sketch was under-constrained. This test is the portfolio story: *"one parameter drives the family."*

## 3. Feature order that prints well

1. **Sketch** — one closed profile per feature, fully-defined, origin-anchored
2. **Extrude / Revolve / Sweep / Loft** — extrude for brackets, revolve for wheels/pulleys, sweep for handles, loft for transitions
3. **Pattern + Mirror** — never copy holes by hand; rectangular/circular pattern, mirror bosses
4. **Shell + Ribs** — enclosures: shell `wall` inward, ribs 0.6×wall, vent slots via pattern
5. **Fillet / Chamfer last** — fillets at stress roots, chamfers on >45° overhangs instead of supports
6. **Check → 3MF** — Inspect → Check/Interference, export **3MF** (units + colour travel), open in slicer before calling done

**Tolerance truth:** holes print ~0.2–0.3 mm undersized. Print a hole-tower (3.0 / 3.2 / 3.4) on the same printer + filament first, pick the fit, then print the part.

## 4. Showable projects (in order — each teaches the next)

| # | Build | Forces | Show as |
|---|---|---|---|
| 1 | **HC-SR04 sensor bracket** 60×40, 2×M3 | sketch, extrude, fillet, pattern | photo of sensor mounted + screenshot of `n=2→3` update |
| 2 | **Arduino + breadboard enclosure** with lid, vents, 4 bosses | shell, ribs, mirror, Component split | open/closed + lid-fit video (5 s) |
| 3 | **Robot wheel + tyre** | revolve hub, spoke pattern | rolling clip |
| 4 | **Pan-tilt servo bracket** 2-axis | rigid + revolute joints, interference check | sweep video proving motion |
| 5 | **Line-follower chassis** | pockets, cable channels | top-down with electronics seated |
| 6 | **Drone arm / motor plate** | fillets at stress roots | close-up of fillet + mounted motor |
| 7 | **Cable clips ×6** | batch tolerance, print orientation | set of 6 fitted on cable |
| 8 | **Breadboard-grid enclosure** | grid pattern, embossed labels | grid with components placed |

**Done per project:** `.f3d` + `.3mf` + 1 photo or ≤10 s clip + 1-line parameter story. No essay.

## 5. Portfolio shots (what recruiters actually open)

- Before/after parameter change (`n=2` vs `n=3`) side by side
- Slicer preview showing orientation + no-support chamfers
- Fitted assembly, not CAD render alone — render lies, fit proves

## 6. Anti-drift

SolidWorks stays the design/portfolio skill ([[01-Areas/Engineering/engineering-drawing/solidworks/INDEX]]). If Fusion starts absorbing surfacing/drawings/GD&T study, that is drift — archive one track rather than running both. North Star hardware thread owns this page.

## Next

- Pending vault builds when reached: sketch-mastery → part-workflow → 3D-printing deep pages (hub §4)
- Course hub: [[01-Areas/Engineering/engineering-drawing/overview]] · Interview: [[01-Areas/Engineering/engineering-drawing/cad-design-interview-prep]]
