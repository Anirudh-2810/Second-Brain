---
date: 2026-09-24
description: "ED textbook map: N.D. Bhatt (738 pp) and N.H. Dubey (563 pp, image-only scan) chapter-to-wiki index for Sem-1 Engineering Drawing — which book chapter feeds which concept page."
tags: [btech, engineering-drawing, textbook, nd-bhatt, nh-dubey, reference, index]
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "Reference map"
last_updated: "2026-09-24"
confidence: medium
---

## For future agent

Reference-index for the two ED textbooks in `raw-sources/`. Bhatt chapter numbers below are **stated** (extracted from the Bhatt PDF TOC via text layer); Dubey structure is **medium-confidence** (Dubey PDF is an image-only CamScanner scan, no text layer — mapping is by standard Dubey topic order, TBC against the physical TOC). Never re-OCR these books wholesale; distill single topics on demand into the linked concept pages.

# ED Reference Books — Chapter Map

> Sources (immutable, never edit): `[[raw-sources/ENGINEERING DRAWING BY N.D BHATT]]` (738 pp, text layer, noisy OCR) · `[[raw-sources/NH Dubey Engineering-Drawing]]` (563 pp, image-only scan)
> Module hub: [[overview]] · Practice: [[autocad-lab-and-exam-prep]]

## N.D. Bhatt → wiki pages

| Bhatt ch (per PDF TOC) | Topic | Study in wiki |
|---|---|---|
| Ch 1 — instruments, pencils, pins, drafting machine | Tools, sheet setup | [[overview#The tools you'll use]] |
| Ch 3 — types of lines (§3-1-1), dimensioning terms/rules | BIS lines + dimensioning | [[overview]] (line alphabet + dimensioning sections) |
| Ch 7 — loci, slider-crank, four-bar | Loci / mechanisms | (TBC — no wiki page yet; distill on demand) |
| Ch 10 — projections of straight lines (p195) | Lines: parallel/contained/perpendicular cases | [[projection-of-points-lines-planes]] |
| Ch 11 — projections of points | Points | [[projection-of-points-lines-planes]] |
| Ch 12 — traces, planes parallel/oblique | Planes | [[projection-of-points-lines-planes]] |
| Ch 13 — solids: types, simple positions, inclined axes (§13-3), spheres | Solids | [[isometric-and-sections]] + [[projection-of-points-lines-planes]] |
| Ch 14 — sections of solids | Sections | [[isometric-and-sections]] |
| Ch 15 — development: parallel/radial/triangulation, cube→cone, transition pieces, spheres | Development | [[development-of-surfaces]] |
| Ch 20 — orthographic reading, missing views/lines, pictorial→orthographic conversion | First/third angle, conversion | [[orthographic-projections]] |
| Ch 21 — centres of gravity (p540) | CG of areas | (TBC — distill on demand) |
| Ch 24 — threads, nuts, washers (p575–590) | Fasteners | [[cad-design-interview-prep]] (interview angle) |

Unconfirmed Bhatt chapters (standard edition order, TBC): Ch 2 lettering → [[overview]]; Ch 4 scales → [[overview]]; Ch 5 geometrical construction; Ch 6 engineering curves; Ch 8 orthographic theory → [[orthographic-projections]]; Ch 16 intersection of surfaces; Ch 17 isometric → [[isometric-and-sections]].

## N.H. Dubey → wiki pages (topic map, TBC)

Standard Dubey order; confirm against the book's printed TOC before citing chapter numbers:

| Dubey topic | Study in wiki |
|---|---|
| Instruments, lettering, dimensioning, scales | [[overview]] |
| Orthographic projections (1st/3rd angle) | [[orthographic-projections]] |
| Points, lines, planes | [[projection-of-points-lines-planes]] |
| Solids + sections + development | [[isometric-and-sections]] + [[development-of-surfaces]] |
| Isometric + AutoCAD | [[isometric-and-sections]] + [[autocad-lab-and-exam-prep]] |

## How to use these books

1. **Daily study:** wiki concept page first (distilled + exam-filtered).
2. **Stuck on a construction:** open the mapped Bhatt chapter for the full step-by-step figure sequence.
3. **Before ESE:** [[autocad-lab-and-exam-prep]] + Bhatt Ch 20 exercises (blueprint reading).

## See also

- [[overview]] — module entry point + reading order
- [[solidworks/INDEX]] — SolidWorks self-study track (linked from domain INDEX)
