---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "3 - Projection of solids, sections and development (TBC)"
tags: [btech, engineering-drawing, solids, sections, development, true-shape, prism, pyramid, cone, cylinder]
last_updated: "2026-09-09"
description: "Solids resting and inclined, section planes and true-shape construction, plus flat-pattern development of prisms, cylinders, pyramids and cones with exam steps."
module: "engineering-drawing"
prerequisites: ["[[orthographic-projections]]", "[[projection-of-points-lines-planes]]"]
confidence: medium
---

# Projection of Solids, Sections & Development of Surfaces

## For future agent
Exam core for Module 3 (sources cataloged by filename only: `Module 3 - Projection of Solids.pdf`, `Section and development of solids.pdf` — never opened). Assumes first-angle views from [[orthographic-projections]] and the tilt-then-swing method from [[projection-of-points-lines-planes]]. Verify solid-change-of-position conventions against the Module 3 PDF when it is eventually read.

---

## 1. Solids vocabulary

| Family | Examples | Base in plan | Side faces |
|---|---|---|---|
| Prism | triangular, square, hexagonal | polygon | rectangles |
| Pyramid | triangular, square, pentagonal | polygon + centre (apex) | triangles |
| Cylinder / Cone | — | circle | curved (rectangle / sector when developed) |
| Sphere | — | circle | none (gore/zone development only) |

- **Axis:** centre line (vertical when the solid stands on HP).
- **Resting on HP** = base flat on floor. **Axis inclined** = tilted by θ to HP or φ to VP.
- **Generator:** a straight line on a curved surface (cylinder/cone) — used for section + development point transfer.

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
| **Parallel-line** | prisms, cylinders | lateral faces unroll to rectangles; stretch-out length = base perimeter (πD for cylinder) |
| **Radial-line** | pyramids, cones | faces swing about the apex; radius = slant height; cone = sector with angle 360·r/R |
| **Triangulation** (TBC — needs PDF verify) | transition pieces, oblique solids | surface split into triangles, each drawn true-shape |
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
