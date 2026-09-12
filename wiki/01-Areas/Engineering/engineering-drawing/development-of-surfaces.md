---
course_code: "216U06C105 (Module-3 slides; Section slides say 111U06C105 — confirm current code TBC)"
course_name: "Engineering Drawing"
unit: "Module-IV - Projection of solids (syllabus 4.1/4.2)"
tags: [btech, engineering-drawing, solids, sections, development, true-shape, prism, pyramid, cone, cylinder]
last_updated: "2026-09-12"
description: "Module-IV solids: classification, prism/pyramid vocab + point-naming, axis-position catalog Q1-Q19, change-of-position method, sections/true-shape, parallel/radial development with exam steps."
module: "engineering-drawing"
prerequisites: ["[[orthographic-projections]]", "[[projection-of-points-lines-planes]]"]
confidence: high
---

# Projection of Solids, Sections & Development of Surfaces

## For future agent
Module-IV exam core, now grounded in the actual sources (read 2026-09-12): `Module 3 - Projection of Solids.pdf` (36 slides, Parag Sarode, text-extracted — vocabulary pp 6-16, worked-position bank Q1-Q19 pp 17-34) and `Section and development of solids.pdf` (14 slides, figures-only — confirms parallel-line/radial-line methods + prism/cylinder/cone developments, no extractable text). Scope per syllabus 4.2: right regular solids (prism, pyramid, cylinder, cone) inclined to ONE reference plane only — spheres, hollow and composite solids EXCLUDED. Assumes first-angle views from [[orthographic-projections]] and tilt-then-swing from [[projection-of-points-lines-planes]]. Source skips Q7 numbering (Q6→Q8); figures in both PDFs still need visual verify in AutoCAD/sketch session.

---

## 0. Syllabus scope (source: Module-3 slides pp 1-2)

- **4.1** Introduction to projection of solids, classification of solids.
- **4.2** Projection of **right regular** solids (prism, pyramid, cylinder, cone) inclined to **one** reference plane only — **excluding spheres, hollow and composite solids**.
- Reference throughout: N. H. Dubey, *Engineering Drawing* (see [[autocad-lab-and-exam-prep]] for the 78 MB `EDrawing N.H DUBEY.pdf` file map).

### Classification (slide p 6)

- **Polyhedron** (bounded by plane surfaces): **prism, pyramid** (incl. cube/hexahedron, tetrahedron).
- **Solids of revolution**: **cylinder, cone** (sphere excluded from this syllabus).

---

## 1. Solids vocabulary (slides pp 7-16)

| Family | Examples | Base in plan | Side faces |
|---|---|---|---|
| Prism | triangular, square, hexagonal | polygon | rectangles |
| Pyramid | triangular, square, pentagonal | polygon + centre (apex) | triangles |
| Cylinder / Cone | — | circle | curved (rectangle / sector when developed) |
| Sphere | — | circle | none (gore/zone development only) |

- **Axis:** centre line (vertical when the solid stands on HP).
  - Prism: imaginary line through the **centres of both bases**. Pyramid/cone: through **apex + base centre**.
- **Resting on HP** = base flat on floor. **Axis inclined** = tilted by θ to HP or φ to VP.
- **Generator:** a straight line on a curved surface (cylinder/cone) — used for section + development point transfer.
- **Prism edges:** vertical (lateral/longer) edges where two rectangular faces meet vs **base edges** (shorter) where rectangular face meets base; corner = three faces meet. **Edges of a prism = 3n** (n = base sides). **Cube/hexahedron:** l=b=h, six square faces.
- **Pyramid edges:** **slant/lateral edges** (two triangular faces meet) vs **base edges** (triangle meets base). Pyramids named by base (triangular/square/pentagonal/hexagonal); tetrahedron = triangular pyramid with all-equilateral faces.
- **Right regular** = axis ⊥ base (rectangular faces / regular-triangle faces). **Oblique** = axis inclined to base (faces are parallelograms). **Truncated** = cut by a plane inclined to base, top removed. **Frustum** = truncated + the cut face capped parallel-ish (slides p 16).
- **Point-naming convention (slides p 13):** base corners `1,2,3…`, top base same numbers; vertical edges `1-1',2-2'…`; lateral faces `1-1'-2'-2…`; axis `O-O'`. Use it consistently — examiners track matching numbers across views.

---

## 1b. Axis-position catalog — what the question bank actually asks (slides pp 17-34)

Three families only (one-plane inclination max). Standard sizes reused: **40 mm base / 40 mm diameter, 60 mm axis** (70 mm + 65 mm in the VP-inclined set).

| Family | Slide Qs | Setup |
|---|---|---|
| Axis ⊥ HP, ∥ VP (base on HP) | Q1 prism (base edges equally inclined to VP), Q2 square pyramid (two base sides ⊥ VP), Q3 cylinder, Q4 cone | Simple position: true-shape plan first, project up |
| Axis ⊥ VP, ∥ HP (base in VP) | Q5 square prism (base side ∥ HP), Q6 square pyramid (base edges equally inclined to HP) | Mirror of above: true-shape elevation first |
| Axis inclined to HP, ∥ VP | Q8 prism on base **corner** (axis 30° HP), Q9 prism on base **edge** (axis 60° HP), Q10 pyramid base side in HP (axis 45° HP), Q11 cylinder base-circle point in HP (axis 45° HP), Q12 pyramid on triangular **face** (base edge ⊥ VP), Q13 cone on **generator** in HP, Q14 pentagonal prism on base corner (4 wordings: opposite side ∥ HP⊥VP / longer edge 40° / base 50° to HP / opposite rectangular face 40°) | **Direct** = angle given on the axis; **indirect** = resting condition given (corner/edge/face/generator) — first convert to axis angle, then tilt |
| Axis inclined to VP, ∥ HP | Q15 square prism corner in VP (axis 40° VP), Q16 pyramid base edge in VP (axis 30° VP), Q17 pyramid on triangular face in VP, Q18 pentagonal prism base edge in VP (face 30° VP), Q19 cube of **solid diagonal 80 mm** (diagonal ∥ HP, corner in HP) | Same tilt logic, views swapped |

> No Q7 in the source (numbering jumps Q6→Q8). Q14's four OR-wordings are the same solid — practice rephrasing, not four solids.

---

## 2. Change-of-position method (never draw the incline directly)

```
Stage 1 SIMPLE: base on HP, axis vertical (or otherwise parallel to a plane).
  → draw true-shape plan, project up to elevation.

Stage 2 TILT (axis inclined to HP by θ):
  → redraw ELEVATION tilted at θ (one base corner/edge on XY per question),
     project each corner DOWN + ACROSS to rebuild the plan.

Stage 3 SWING (axis inclined to VP by φ, oblique solids only):
  → rotate the Stage-2 PLAN by φ, project back up to rebuild elevation.
```

**Defaults examiners expect:** draw the plan first; keep the solid's base corner that touches HP/VP exactly on XY after tilting; show all construction projectors lightly; hidden base edges dashed.

| Solid, base on HP, axis vertical | Plan | Elevation |
|---|---|---|
| Cube / square prism | square | rectangle (height = side) |
| Hexagonal prism | hexagon | 3-rectangle elevation |
| Square pyramid | square + centre diagonals | triangle |
| Cylinder | circle | rectangle (h = height) |
| Cone | circle + centre | triangle (h = height) |
| Sphere | circle | circle |

---

## 3. Sections of solids

A **section plane** cuts the solid; the cut face hatched in the sectional view; its **true shape** found by auxiliary projection.

### 3a. Section-plane orientations (VT/HT notation)

| Section plane | Seen as | Yields |
|---|---|---|
| Perpendicular to VP, inclined θ to HP (VT inclined) | inclined line in elevation | sectional plan + true shape |
| Perpendicular to HP, inclined φ to VP (HT inclined) | inclined line in plan | sectional elevation + true shape |
| Parallel to HP (horizontal) | line in elevation | true shape directly in plan |
| Parallel to VP | line in plan | true shape directly in elevation |

### 3b. Construction steps (VT-inclined cut, the most asked)

1. Draw the solid's front + top views (change-of-position if inclined).
2. Draw the cutting plane as an inclined line (VT) at given θ, at given distance from apex/base.
3. Mark section points where VT crosses **each edge/generator** (`1',2',3'…`).
4. Drop projectors to the plan → `1,2,3…` on the matching edges.
5. Join in order → **sectional plan** (hatch the cut face at 45°).
6. **True shape:** draw auxiliary reference line `X1Y1` parallel to VT; project each section point perpendicular to VT; transfer widths from the plan → join → true shape.

```
Elevation:      VT line ╲ cutting cone
                 1' 2' 3' • section points on generators
                    │ │ │  projectors down
Plan:              1 2 3  • on matching generators → sectional plan (hatch)

True shape:  X1Y1 ∥ VT; transfer distances → ellipse/truncated polygon
```

### 3c. What shape to expect (sanity check)

| Solid + cut | Section / true shape |
|---|---|
| Cylinder, ∥ base | circle |
| Cylinder, inclined | ellipse |
| Cone, ∥ base | circle |
| Cone, inclined (across all generators) | ellipse |
| Cone, ∥ one generator | parabola (TBC) |
| Pyramid/prism, ∥ base | smaller similar polygon |
| Pyramid/prism, inclined | truncated polygon |

> If your "true shape of a cut cylinder" comes out a circle when the plane was inclined — wrong. Inclined cut on a cylinder/cone is an **ellipse**.

Hatching rules (from [[isometric-and-sections]]): hatch **only** the cut face, thin 45° lines, same part = same direction; ribs/webs unhatched by convention; label the view `SECTION A-A`.

---

## 4. Development of surfaces (flat patterns)

Unfold the solid's skin onto one sheet — sheet-metal, packaging, ducting work.

| Method | Used for | Idea |
|---|---|---|
| **Parallel-line** | prisms, cylinders | lateral faces unroll to rectangles; stretch-out length = base perimeter (πD for cylinder) — Section-slides pp 2-5 confirm prism + cylinder developments (figures-only) |
| **Radial-line** | pyramids, cones | faces swing about the apex; radius = slant height; cone = sector with angle 360·r/R — Section-slides p 2 methods list + p 8 cone figure (figures-only) |
| **Triangulation** (TBC — in neither PDF's text) | transition pieces, oblique solids | surface split into triangles, each drawn true-shape |
| Sphere | approximate only | gore or zone strips (true development impossible) |

### 4a. Prism / cylinder (parallel-line)

```
1. Stretch-out line = base perimeter (square prism side s: 4s; cylinder: πD).
2. Divide into one panel per base edge (prism) or 12 equal generator divisions (cylinder).
3. Height = solid height (or truncated heights transferred edge-by-edge).
4. Top + bottom bases drawn attached to one panel (true shape).
```

### 4b. Pyramid / cone (radial-line)

```
1. Centre = apex O. Radius = slant height L (pyramid: true slant-edge length; cone: R).
2. Lay off base edges in order along the arc (pyramid: true edge widths; cone: sector angle = 360·r/R).
3. Join to apex → lateral development. Base attached to one edge.
4. TRUNCATED solid: transfer each surviving edge height (from elevation, true-length-corrected for pyramids) onto its radial line; join the cut polygon smoothly (cone: smooth curve through 12 generator points).
```

### 4c. Development with a section cut (combined problem)

1. Develop the **full** solid first (light lines).
2. On each generator/edge of the development, mark the **remaining height** read from the sectional elevation.
3. Join cut points (straight segments for prism/pyramid, smooth curve for cylinder/cone).
4. Darken the surviving portion; keep the removed portion faint or omit; attach the true-shape section if asked.

---

## 5. Exam checklist

- [ ] Plan first, project up; tilt-then-swing stages visible, base contact point on XY?
- [ ] Section points numbered on EVERY edge/generator, matched across views?
- [ ] Sectional view hatched 45° on cut face only, labelled `SECTION A-A`?
- [ ] True shape via `X1Y1 ∥ VT`, widths transferred (not eyeballed)?
- [ ] Development: correct method (parallel vs radial), stretch-out = perimeter / sector angle computed?
- [ ] Truncation heights transferred per-edge; cylinder/cone cut curve smooth, not polygonal?

## CROSS-REFERENCES

- [[orthographic-projections]] (views, quadrants) · [[projection-of-points-lines-planes]] (tilt/swing, traces) · [[isometric-and-sections]] (hatching + section types) · [[overview]] (line types, dimensioning) · [[autocad-lab-and-exam-prep]] (MSE/worksheets drill)

## Sources

- [[raw-sources/drive-download-20260908T190927Z-1-001/Semester 1/Drawing/Module 3 - Projection of Solids.pdf]] — 36 slides, read 2026-09-12 (stated; figures unverified visually)
- [[raw-sources/drive-download-20260908T190927Z-1-001/Semester 1/Drawing/Section and development of solids.pdf]] — 14 slides, figures-only, methods + prism/cylinder/cone figures (visual verify pending)
- N. H. Dubey, *Engineering Drawing* — cited as [1] on every Module-3 slide; full text at `Semester 1/Drawing/EDrawing N.H DUBEY.pdf` (see [[autocad-lab-and-exam-prep]])
