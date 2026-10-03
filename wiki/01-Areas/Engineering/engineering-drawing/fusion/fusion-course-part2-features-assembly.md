---
course_code: "BTech-ED-CAD"
course_name: "Engineering Drawing — CAD self-study"
unit: "Fusion course dump 2 — features and assembly"
date: "2026-10-04"
last_updated: "2026-10-04"
description: "Part 2 of the PTS CAD EXPERT Fusion 360 dump — sketch-based vs applied features, cake-slice/potter-wheel/manufacturing approaches, extrude and press-pull, sweep, Body vs Component, top-down assembly, joints and mechanisms."
tags: [cad, fusion, pts-cad-expert, course, extrude, assembly, joints, parametric]
confidence: medium
prerequisites: ["[[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part1-setup-sketch|Fusion course part 1]]"]
sources: ["https://www.youtube.com/watch?v=gKGP1iFhd1s (Hindi audio, EN UI terms transliterated)"]
---

## For future agent
Part 2 of 3, covering 01:31–03:11: features taxonomy, modeling approaches, extrude/press-pull/sweep, bodies vs components, top-down assembly with live references, joints and a quick-return mechanism demo. Follows [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part1-setup-sketch|part 1]]; ends with [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part3-sheetmetal-output|part 3]]. Captions: `raw-sources/youtube-transcript-fusion-360-complete-pts-cad-expert.txt`. Paths `TBC` in-app.

# Fusion Course Dump 2/3 — Features, Assembly, Joints

## 1. Two feature families (01:31)

- **Sketch-based** (needs 2D first): Extrude, Revolve, Sweep, Rib. Flow: plane → profile → feature.
- **Applied** (modifies existing solid): Fillet, Chamfer, Shell, Draft, Pattern. Flow: solid → select → apply.
- Every model is a mix; knowing which family a tool belongs to predicts where it lives in the UI.

## 2. Three modeling approaches — pick deliberately (01:32)

| Approach | How | When |
|---|---|---|
| **Cake-and-slice** | Layer-by-layer additive extrudes (section 1, then 2, then 3…) | General prismatic parts; his default demo |
| **Potter's wheel** | One full profile + **Revolve** about an axis | Axisymmetric parts (pulleys); one shot, not everywhere |
| **Manufacturing** | Start from stock block, **cut away** (extrude-cut diameters/depths) | Lathe/mill-mindset parts; mirrors how it'd be machined |

Same object can mix all three — requirement decides. His demo builds one part all three ways so the contrast sticks.

## 3. Extrude complete (01:34)

- Sketch profile → Finish Sketch → **Extrude (`E`)** or pre-select profile then `E`. Drag arrow or type thickness (10/15 mm) in dialog.
- **Direction:** positive above plane, negative below — flip by typing minus or dragging through. **Symmetric about plane:** change One-Side → **Symmetric**; **Whole Length** = total split half/half, Half Length = value each side (check which the dialog shows).
- **Timeline shows Sketch then Extrude** as separate entries — rollback point for life.
- **Two edit doors:** profile wrong? Right-click sketch → **Edit Sketch**. Thickness/direction wrong? Right-click feature → **Edit Feature** (e.g. 15→20 mm, done).
- **Cutting:** partial-depth cut (5 mm out of 20) = new sketch on face (circle Ø25 at 20 mm offsets) → select → right-click → **Press-Pull** → drag into solid → `-10`. Full-depth holes belong in the *first* profile (draw circle in base sketch, press-pull through) — fewer features, shorter tree.

## 4. Press-Pull > Extrude (his doctrine, 01:39)

Press-Pull on a face region adds *or* removes material with one gesture — same tool for boss and hole. Doctrine: **prefer Press-Pull; count features jealously.** Long tree = slow edits + wasted time. Full-depth removal? One profile + one pull, no extra cut feature.

## 5. Sweep essentials (02:12)

Profile + path: cross-section orientation choices — **parallel or perpendicular** to path faces. Circular sections allowed — pipes, handles, springs. Keep path tangent-continuous or the sweep kinks.

## 6. Bodies, components, combine (02:32–02:43)

- Every feature births a **Body**. Two overlapping bodies stay separate solids until **Combine** (join/cut/intersect) merges them.
- **Bodies can't take joints; Components can.** One Component holds unlimited bodies. Convert anytime: Body → Create Component, or start **New Component** (named: Base, Flange…) and model inside it.
- Why it matters: same-space bodies merge and cross-contaminate — a cut on one eats its neighbor. Components isolate. His demo: press-pull cut leaking into the adjacent body, then the Component version staying clean.
- **Display Component Colors ON** — instant visual split of who owns what.

## 7. Top-down vs bottom-up (02:46)

- **Top-down:** model every part inside one assembly file (his 99% choice — live references between parts).
- **Bottom-up:** separate files per part → Insert into Current Design → joint together. Universal across SolidWorks/Creo/CATIA/Fusion.
- Top-down killer demo: Base 180×75 with holes → Flange sketched with **Project** references + **To-Object / Two-Side** extrude to Base faces → change Base 75→65 → Flange follows automatically. Reference-driven design propagates; isolated files don't.
- Tricks used: wireframe visual style to grab hidden circles, Project edges as references, mirror about planes, **Capture Position** after moves, **To-Object** ends instead of blind depths.

## 8. Joints: ground, rigid, revolute, slider, tangent (03:00–03:11)

Setup order: insert/import parts → right-click first part → **Ground** (fixed) → joint the rest.

| Joint | Motion | Demo |
|---|---|---|
| **Rigid / Rigid Group** | None — fused | Bracket + flange + mirrored copy rigid-grouped; multi-select → Assemble → Rigid Group |
| **Align / Concentric** | Positioning only | Face-to-face, concentric shaft seating (Ctrl-hold for exact snaps) |
| **Revolute** | Spins in place | Pulley on shaft (Between-Two-Faces placement); spin proven with a witness nub modeled on the pulley |
| **Slider** | Slides along edge | Block on rail edge |
| **Tangent** | Rolling contact | Quick-return mechanism flanks |

Quick-return showcase: two revolutes + one slider + two tangents composed live, relationships deleted and rebuilt on camera. Takeaway: mechanisms are just joint vocabulary stacked — learn five types, build anything.

## 9. Worked example: pulley assembly end to end (02:47–03:07)

Base component (180×75 plate, Ø12 holes mirrored) → Flange component (50×75 + 5 mm chain offset, closed profile) → To-Object/two-side press-pull between Base faces → wireframe-project base circles for holes → press-pull cuts → third component mirrored with Capture Position → activate assembly → Display Component Colors → Ground Base → Align faces concentric → Rigid-group statics → Revolute on pulley (between-two-faces placement) → witness nub → spin check → quick-return variant (revolute + revolute + slider + 2 tangents, delete-and-rebuild drill). Follow this order verbatim once; it exercises every joint type in 30 minutes.

## 10. Tasks (graded)

1. **Tonight (30 min):** one profile, three builds — cake-slice extrude stack, single revolve, stock-block + cuts. Done = 3 timelines compared, shortest wins.
2. **This week:** Base (180×75) + Flange with projected references + To-Object ends; change Base to 65, screenshot Flange following. Done = proof of top-down propagation.
3. **Portfolio:** pulley + bracket + shaft assembly, pulley on revolute, rest rigid-grouped, spin video. Done = 10-s rotation clip + `.f3d` for the advanced-track project 3/4.

Next: [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part3-sheetmetal-output|Part 3 — sheet metal, render, drawings, share, contacts, section analysis]].
