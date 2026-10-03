---
course_code: "BTech-ED-CAD"
course_name: "Engineering Drawing — CAD self-study"
unit: "Fusion course dump 1 — setup, files, sketch mastery"
date: "2026-10-04"
last_updated: "2026-10-04"
description: "Part 1 of the PTS CAD EXPERT Fusion 360 complete tutorial dump — CAD/CAM/CAE, free licensing, file limits, timeline, units, sketch tools, geometric constraints, fully-defined discipline, parametric dimensioning, TTR circle, offset, patterns."
tags: [cad, fusion, pts-cad-expert, course, sketch, constraints, parametric, beginners]
confidence: medium
prerequisites: ["[[01-Areas/Engineering/engineering-drawing/fusion/INDEX]]", "AutoCAD 2D basics"]
sources: ["https://www.youtube.com/watch?v=gKGP1iFhd1s (Hindi audio, EN UI terms transliterated)"]
---

## For future agent
Part 1 of 3 distilling PTS CAD EXPERT's *Fusion 360 Complete Tutorial (2025)* (4h44m, Hindi/Hinglish audio — UI terms stay English, quoted here in English). Covers 00:00–01:30: positioning, setup, sketch mastery. Full captions: `raw-sources/youtube-transcript-fusion-360-complete-pts-cad-expert.txt` (7,332 lines). Timestamps like (46:33) point into the video. Interface paths `medium`/`TBC` — verify in-app. Continues in [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part2-features-assembly|part 2 (features + assembly)]] · [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part3-sheetmetal-output|part 3 (sheet metal + render + drawings)]].

# Fusion Course Dump 1/3 — Setup, Files, Sketch Mastery

> Hub: [[01-Areas/Engineering/engineering-drawing/fusion/INDEX]] · Advanced track: [[01-Areas/Engineering/engineering-drawing/fusion/fusion-advanced-parametric-track|advanced parametric track + 8 projects]]

## 1. Why Fusion, CAD/CAM/CAE in one line (00:00)

- **CAD** = Computer Aided Design, **CAM** = Manufacturing, **CAE** = Engineering (analysis). One model feeds all three — design it, machine it, test it.
- Market claim: Fusion 360 directly competes with SolidWorks/NX/CATIA/Creo; for product design the two most-used are SolidWorks + Fusion. Pitch: mechanical engineer wanting a design job right after college.
- Licensing (00:10): **personal use = free of cost** (video's words) — matches the vault's Education-plan route on the [[01-Areas/Engineering/engineering-drawing/fusion/fusion-setup-and-interface|setup page]]; confirm current terms in-app.

## 2. File and timeline discipline (00:19–00:37)

- **10 editable files limit** on free/personal: the 11th file refuses to activate until you make an old one read-only/uneditable. Plan accordingly — archive ruthlessly, don't hoard versions.
- **Timeline = history recorder** (bottom bar): every sketch and every feature lands as an entry. Double-click any entry to roll back and edit — the model rebuilds forward. Long timeline = hard future edits (he repeats this at 01:41: fewer commands, smaller tree, faster modifications).
- **Units check first:** default reads millimetre. Confirm mm before sketch one — silent inch scaling kills assemblies later. Sanity: sketch 100 mm line, measure it.

## 3. Constraints: geometry first (00:46)

Two families (same as AutoCAD): **geometrical** (relations) and **dimensional**. Fusion lives on geometrical:

- Horizontal, vertical, perpendicular, concentric/same-center, tangent, equal, collinear, coincident — the full set under the Constraints tools.
- **Dimension shortcut: `D`.** Select element → drag → type value (e.g. 12, 40, 75 mm). Two-point selection dimensions gaps.
- **Parametric calculator in the box:** drawings often give chained dims (40 + 20 + …). Don't hand-calc — type expressions directly: `45+25+(75)/2` + Enter. Any formula works; the software solves it (00:48). Radius→diameter: type `23.26*2`.
- **Equal kills double-dimensioning:** symmetric lengths? Select both → **Equal** (symbol appears). Change one, the other follows — one dimension drives both.

## 4. Fully defined or nothing (00:49–01:14)

- **Blue/light = free**, can be dragged. **Black = fully defined/constrained**, zero degrees of freedom, can't be pulled. Goal: everything black via relations + minimal dims.
- **Over-define is refused:** a fully-defined sketch rejects new dims (non-editable). That's parametric discipline, not a bug — every parametric tool does this.
- **Solver logic demo:** total 100, one leg 40, other leg Equal-related → solver auto-derives the remainder (100−80=20) with no explicit dim. Extra dims belong on the **drawing sheet** later (detailing allows repeats), never in the sketch.
- **Relationships over numbers:** "maximum relations, minimum dimensions" — his words at 01:04. Fully-defined sketch is the non-negotiable habit before any feature.

## 5. Line, circle, rectangle, offset (00:51–00:58)

- **Line (chain mode):** continuous clicks chain segments. Length + **Tab jumps to angle** (100 + Tab → 90°). Missed the angle? Dimension tool → select two lines → set degrees anytime.
- End a chain with the **green tick**. Reference-only lines: enable **Construction** (dashed/hidden) or **Centerline** before drawing; convert existing geometry by selecting → toggling Construction. Never leave Construction on globally.
- **Circle (`C`):** all AutoCAD methods present. Default dimension = **diameter** (most parametric tools do this) — radius known? Type `r*2`. **Tangent lines:** draw near-tangent, then apply Tangent constraint between them to snap true.
- **Trim (`T`):** click or drag across to cut.
- **2-tangent circle (TTR):** inside Circle options — click line 1, line 2, drag, type radius. AutoCAD's TTR, built in. He notes SolidWorks needs a workaround here — one genuine Fusion edge.
- **Rectangle (`R`):** many methods; **start at Origin or build symmetric about it** (left-right equal) — always. Size during draw or `D` after (120 × 75).
- **Offset (`O`, Modify):** Chain ON = whole profile, OFF = single element. Drag or Flip side; One-side / Two-side / Symmetric (±value both ways, or independent inside-outside values).

## 6. Circle/pattern extras (01:14–01:30, gist)

- Centerlines + horizontal relations tame drifting geometry; **circular pattern** multiplies holes/lugs around an axis (full drill in part 2's octagon build).
- Things to drill: equal-relation chains, TTR between two lines, offset-in-10-mm-again inner profile.

## 6b. Worked mini-example: mirrored hole plate (02:47 method)

Base 180×75, four Ø12 holes at 20×15 offsets: draw ONE hole + two construction centerlines → dimension → **Mirror** about first centerline (select hole, not the lines) → Ctrl-hold both → mirror about second → four holes, one dimension set. Finish → press-pull 5 mm. Lesson: model once, mirror twice — never draw four holes.

## 7. Tasks (graded)

1. **Tonight (25 min):** 120×75 rectangle from Origin, inner offset 10 mm, 4 Equal relations, all-black sketch. Done = drag-proof + dimension edits propagate.
2. **This week:** TTR circle tangent to two lines + dimension expression `(45+25+75)/2` typed raw in the box. Done = screenshot of expression + solved value.
3. **Portfolio:** fully-defined base sketch of the HC-SR04 bracket (60×40, 2×M3 at pitch 20) with Equal + symmetric relations only. Done = `.f3d` sketch + black-geometry screenshot for the advanced-track project 1.

Next: [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part2-features-assembly|Part 2 — sketch-based vs applied features, 3 modeling approaches, extrude/press-pull, sweep, bodies vs components, top-down assembly, joints]].
