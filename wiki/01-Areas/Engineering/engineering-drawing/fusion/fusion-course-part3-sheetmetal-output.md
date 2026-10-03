---
course_code: "BTech-ED-CAD"
course_name: "Engineering Drawing — CAD self-study"
unit: "Fusion course dump 3 — sheet metal, render, drawings"
date: "2026-10-04"
last_updated: "2026-10-04"
description: "Part 3 of the PTS CAD EXPERT Fusion 360 dump — sheet metal rules and flanges, unfold-cut-refold, render local vs cloud, third-angle drawings with chain dimensions, PDF export, share links, contacts, section analysis."
tags: [cad, fusion, pts-cad-expert, course, sheet-metal, render, drawings, simulation]
confidence: medium
prerequisites: ["[[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part2-features-assembly|Fusion course part 2]]"]
sources: ["https://www.youtube.com/watch?v=gKGP1iFhd1s (Hindi audio, EN UI terms transliterated)"]
---

## For future agent
Part 3 of 3, covering 03:12–04:44: sheet metal module, render, drawings/detailing, share, contacts (brief), parametric edits, section analysis. Follows [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part2-features-assembly|part 2]]. Series: [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part1-setup-sketch|1]] · [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part2-features-assembly|2]]. Captions: `raw-sources/youtube-transcript-fusion-360-complete-pts-cad-expert.txt`. Paths `TBC` in-app.

# Fusion Course Dump 3/3 — Sheet Metal, Render, Drawings

## 1. Sheet metal: gauge thinking (03:12)

Sheet products = bend/punch/fold flat stock. Thickness is ordered in **gauge** (16/18 ga…) — Google a gauge table for exact mm; the shop speaks gauge, not mm.

**Rules first:** Sheet Metal Rules → per-material thickness + bend conditions. Build/edit custom rules once, call them per design — parameters (thickness, bend relief) then propagate everywhere.

## 2. Base flange + edge flange (03:13)

- Sketch profile → select → right-click → **Press-Pull as Flange / Base Edge Contour** (or Create-menu equivalent) → set thickness side (one/two/center) → OK: first sheet exists.
- **Edge Flange:** pick edge(s) — Ctrl-hold adds more, each with independent params — drag up, set **height, angle (90°/45°/30°…), position (inside/outside), flip direction, full-edge vs partial, symmetry**. Height 30→70 live-editable per edge; delete one edge's flange without touching others.
- **Bend:** sketch bend line → Create → **Bend** → select line → fix one side → flip direction → OK.
- **Fillet/chamfer** on sheet edges: same select-and-pull as solids.

## 3. Unfold → cut → refold (the sheet-metal superpower, 03:18)

Cuts near bends can't be made folded — **Modify → Unfold** (stationary face + bends to unfold, All optional) → sketch + press-pull the cutout → **Refold**. Flat-pattern thinking beats 3D hacking every time.

Showcase build (octagon box, 03:20): polygon 8 sides Ø50 → horizontal constraint → edge flanges all around → unfold-all → sketch TTR circles R20 on flat → press-pull cuts → **solid Create → Circular Pattern** (axis center, quantity 8) → back to sheet metal → **Refold**. Same recipe builds laptop stands and enclosures — bend here, modify there, nothing special anywhere else.

## 4. Render without surprises (03:43)

- **Save first** — render refuses unsaved files.
- **Local vs Cloud:** local = your GPU, free; cloud = credits required. Resolution presets up to print-grade — match purpose (screen vs print), don't max blindly.
- Materials/appearances assigned before render decide 90% of the look; lighting does the rest.

## 5. Drawings: third-angle detailing (03:50)

- Views: **Base (front) → projected Top/Side → Isometric** (SW/NE orientations). Third-angle = top view above front — state it, don't assume the reader knows.
- Per-view control: double-click → Visible vs Visible+Hidden edges, full-length vs smooth edges, **threaded features ON** so threads display.
- **Dimensioning:** `D` as usual; **Chain Dimension** strings consecutive lengths (select previous, click along, Enter). Lengths, angles, radii (R12), depths — any view may carry any dim, place where readable; arrow direction/position adjustable.
- **Labels:** Text tool → click → type (TOP/FRONT/SIDE/ISOMETRIC) → height in drawing units (watch mm-vs-inch unit setup!) → color/underline/center → **Ctrl+C/Ctrl+V** to duplicate across views, rename each.
- **Save + export:** save then **Export PDF** (free tier may hide it → fallback **Ctrl+P print**, current sheet, line-weights on, Desktop or Cloud save). **Detail view** (circle → enlarged elsewhere) and **Section view** for internals.

## 6. Share, contacts, parametric proof (04:02–04:31, gist)

- **Share:** file → Share latest-version link — anyone opens current rev; no STEP-email chains.
- **Contacts (04:11, TBC in-app):** pinned vs frictionless options per joint — pick per real behavior; verify labels in your build.
- **Parametric proof (04:21):** shell thickness 3→5 mm via Edit — whole model follows. Redo of the part-2 lesson at part level: drive numbers, never retype.
- **Section analysis (04:31)** + select/group edges for bulk fillets (04:40): inspect innards before printing, not after.

## 7. Tasks (graded)

1. **Tonight (30 min):** base flange + 4 edge flanges at mixed heights/angles + one bend line. Done = folded box screenshot + flat pattern screenshot.
2. **This week:** octagon build abridged — polygon → flanges → unfold → 4 TTR cutouts → circular pattern → refold. Done = before/after fold pair + `.f3d`.
3. **Portfolio:** full drawing sheet of your sensor bracket — front/top/side/iso, chain dims, R-callouts, labels, exported PDF. Done = PDF you'd hand a fabricator + `.f3d` feeding advanced-track project 1.

## 8. Drawings checklist (before any PDF leaves your machine)

Third-angle stated · base scale 1:1 · hidden edges only where needed · threads ON · chain dims continuous · radii prefixed R · text units match sheet (mm vs inch!) · labels copied, renamed, spelled right · detail + section views where internals hide · saved + PDF exported (or Ctrl+P fallback printed). A sheet missing any line gets returned by any fabricator — his words in spirit.

*Series complete: [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part1-setup-sketch|1 · Setup + Sketch]] · [[01-Areas/Engineering/engineering-drawing/fusion/fusion-course-part2-features-assembly|2 · Features + Assembly]] — next build from the [[01-Areas/Engineering/engineering-drawing/fusion/fusion-advanced-parametric-track|advanced track]] ladder.*
