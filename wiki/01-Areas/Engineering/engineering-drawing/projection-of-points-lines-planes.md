---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "2 - Projection of points, lines and planes (TBC)"
tags: [btech, engineering-drawing, points, lines, planes, traces, true-length, projections]
last_updated: "2026-09-09"
description: "Exam-grade constructions for points in 4 quadrants, lines incl HT/VT traces and true-length with theta/phi, plus plane projection 3-stage method and rapid key points."
module: "engineering-drawing"
prerequisites: ["[[overview]]", "[[orthographic-projections]]"]
confidence: medium
---

# Projection of Points, Lines & Planes

## For future agent
This page holds the exam-heavy construction detail for Module 2 (sources cataloged by filename only: `Module 2_Projection of Lines_25-26_R1.pdf`, `key points for lines.pdf`, `key points for planes.pdf` — never opened). It assumes first-angle convention from [[orthographic-projections]]. If the PDFs get read in a later session, verify the θ/φ trapezoid steps and trace rules against them.

---

## 1. Points — the atom of everything

Notation: front view `a'` (above/below XY), top view `a` (below/above XY). Projector `a-a'` is always **perpendicular to XY**.

| Point position | Front view `a'` | Top view `a` |
|---|---|---|
| Above HP, in front of VP (Q1) | `h` above XY | `d` below XY |
| Above HP, behind VP (Q2) | `h` above XY | `d` above XY |
| Below HP, behind VP (Q3) | `h` below XY | `d` above XY |
| Below HP, in front of VP (Q4) | `h` below XY | `d` below XY |
| On HP | ON XY | `d` below/above XY |
| On VP | `h` above/below XY | ON XY |
| On both (on XY line) | ON XY | ON XY |

```
Q1 point (h=20 above HP, d=30 in front of VP), first angle:

        a' •          ← 20 above XY
  ───────XY───────────
               • a    ← 30 below XY
```

**Exam check:** projector length on sheet = `h + d`. If the question gives "20 above HP, 30 in front of VP" you must show exactly those two offsets from XY.

---

## 2. Lines — 9 standard positions

A line = two endpoints. Always project **both endpoints**, join front views (`a'b'` = elevation length) and top views (`ab` = plan length).

### 2a. Simple positions (parallel to a plane)

| # | Line position | Front view | Top view |
|---|---|---|---|
| 1 | Parallel to both HP and VP | True length (TL) | TL |
| 2 | Parallel to VP, perpendicular to HP (vertical) | TL (vertical) | Point |
| 3 | Parallel to HP, perpendicular to VP | Point | TL |
| 4 | Parallel to VP, inclined to HP by θ | TL, angle θ to XY | Foreshortened (length = TL·cosθ) |
| 5 | Parallel to HP, inclined to VP by φ | Foreshortened (TL·cosφ) | TL, angle φ to XY |
| 6 | Contained in HP | ON XY region, TL | TL on/below XY |
| 7 | Contained in VP | TL above/below XY | ON XY region, TL |

### 2b. Oblique line (inclined to BOTH planes) — the classic exam problem

Given: TL, θ (to HP), φ (to VP), position of one end. Both views foreshortened; apparent angles α (front) > θ, β (top) > φ.

**Rotating-line method (3 steps):**

```
Step 1 — assume line parallel to VP, inclined θ to HP:
  a'b1' = TL at angle θ        ab1 = foreshortened plan

Step 2 — assume line parallel to HP, inclined φ to VP:
  ab2 = TL at angle φ          a'b2' = foreshortened elevation

Step 3 — rotate to final position:
  • With centre a' and radius a'b2', swing arc → locus of b' (horizontal line)
  • With centre a and radius ab1, swing arc → locus of b (horizontal line)
  • b' = intersection of locus-from-step-1-plan with vertical projector from locus
  • Join a'b' (elevation), ab (plan). Measure α, β if asked.
```

**Trapezoid / TL-lookup shortcut (given plan + elevation, find TL + θ):**

1. Take plan length `ab`. At one end erect a perpendicular equal to the **difference of the two ends' heights** read from the elevation.
2. Hypotenuse = **TL**; angle at the plan end = **true θ**.
3. Mirror with elevation length + plan-end depth difference → TL (same value, check!) and true φ.

```
   TL │╲
      │ ╲   vertical side = (height of b' − height of a') from elevation
      │θ ╲
      └───╲
      plan length ab
```

### 2c. Traces — where the line pierces the planes

- **HT (Horizontal Trace):** line meets HP → its front view meets XY. Extend elevation to XY, drop projector to extended plan → HT (in top view).
- **VT (Vertical Trace):** line meets VP → its top view meets XY. Extend plan to XY, raise projector to extended elevation → VT (in front view).
- Line parallel to a plane has **no trace** on that plane. Line in a plane has its trace ON the line itself.

```
Elevation extended ──meets XY at v── projector down ──► VT... (wait, convention)
Memory hook: "H goes with plan, V goes with elevation."
  • HT found by extending ELEVATION to XY, projecting to PLAN side.
  • VT found by extending PLAN to XY, projecting to ELEVATION side.
```

**Exam traps:** (a) traces required even when the intersection falls off-sheet — extend the line; (b) no-trace cases must be stated ("no HT since parallel to HP"), not left blank; (c) label HT/VT with the correct view (HT in plan with `h`, VT in elevation with `v'`).

---

## 3. Planes — lamina projection

A plane figure (triangle, square, pentagon, circle). Rule: **face-on view = true shape; edge-on view = straight line.**

| Plane position | Front view | Top view |
|---|---|---|
| Parallel to HP | Line (edge) | True shape |
| Parallel to VP | True shape | Line (edge) |
| Perpendicular to HP, inclined φ to VP | Foreshortened | Line at φ to XY |
| Perpendicular to VP, inclined θ to HP | Line at θ to XY | Foreshortened |
| Perpendicular to both (edge to both) | Line | Line |
| Oblique to both | Foreshortened polygon | Foreshortened polygon (auxiliary needed for true shape) |

### 3-stage method for an inclined plane (exam standard)

```
Stage 1 — SIMPLE position: draw TRUE SHAPE in the view it is parallel to
  (e.g. pentagon parallel to HP → true pentagon in top view, edge-line in front)

Stage 2 — TILT to first inclination:
  • Redraw the edge-line view at angle θ (or φ), keeping one edge/point fixed per question
  • Project every corner back to the other view → foreshortened shape

Stage 3 — SWING to second inclination (oblique planes only):
  • Rotate the foreshortened view by the second angle about a vertical axis
  • Project across again → final front + top views
```

**Circle-in-plane note:** a circle inclined to HP projects as an **ellipse** (major axis = diameter, minor = diameter·cosθ). Never draw the foreshortened view as a smaller circle.

### Traces of planes
- **HT of plane:** line where the plane meets HP (seen in top view).
- **VT of plane:** line where the plane meets VP (seen in front view).
- A plane perpendicular to HP has its VT perpendicular to XY; perpendicular to VP → HT perpendicular to XY.

---

## 4. Key-points rapid revision (from `key points for lines/planes.pdf` titles)

1. Projector `a-a'` ⊥ XY, always.
2. TL appears only in a view **parallel** to the line.
3. Apparent inclinations α ≥ θ, β ≥ φ (equality only when parallel to the other plane).
4. θ + φ of a single line can never exceed 90° for a valid oblique line (TBC against Module 2 PDF).
5. HT ↔ plan side, VT ↔ elevation side.
6. Plane true shape ↔ face-on view; second view collapses to line when edge-on.
7. Incline in stages: simple → tilt → swing. Never draw the oblique position directly.
8. First angle throughout (India/BIS): top view **below** front view.

---

## 5. Exam checklist

- [ ] XY line drawn, labelled; Q1 layout (front above, plan below)?
- [ ] Both endpoints projected with ⊥ projectors; endpoints labelled `a',b'` / `a,b`?
- [ ] TL + θ + φ found by rotation/trapezoid, values boxed?
- [ ] HT/VT located (or "no trace" stated with reason)?
- [ ] Plane: true shape first, then tilt, then swing — stages visible as light construction?
- [ ] Dimensions/angles written above thin lines, arrows touching extension lines?

## CROSS-REFERENCES

- [[orthographic-projections]] (quadrants, first/third angle, solids summary) · [[overview]] (line types, dimensioning) · [[development-of-surfaces]] (solids + development) · [[isometric-and-sections]] (pictorial + sections) · [[autocad-lab-and-exam-prep]] (worksheets + MSE drill)
