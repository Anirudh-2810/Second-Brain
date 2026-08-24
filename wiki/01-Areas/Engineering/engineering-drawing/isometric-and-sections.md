---
module: "engineering-drawing"
topic: "Isometric Views & Sectional Views — Beginner's Guide"
tags: [engineering-drawing, isometric, isometric-projection, sections, sectional-views, hatching, cutting-plane, dimensioning, beginner]
last_updated: "2026-08-21"
prerequisites: ["[[overview]]", "[[orthographic-projections]]"]
---

# Isometric & Sectional Views

> Two skills that make your drawings come alive: **Isometric** shows the object as a 3D "picture"; **Sections** show what's *inside* by cutting the object open. Both are exam favourites and easier than they look.

---

## Part A — Isometric Drawing / Projection

### A1. What it is

**Orthographic** = flat views (front/top/side). **Isometric** = one single **3D-looking** view. The word means **"equal measure"** — the three principal edges are drawn at equal angles, so all measurements keep their true ratios.

Why isometric? A 2D drawing needs 3 views to describe a part; an isometric shows the whole part **at a glance** — like a photo.

### A2. The 3 isometric axes

```
           Top axis
              ↖
               ╲
        Left    ╲    Right
        axis 30°╲   axis 30°
              ╲  ╲
          ──────── ────
        (horizontal base)
```

- **Vertical axis** — straight up (90°).
- **Left axis** — at **30°** to the horizontal.
- **Right axis** — at **30°** to the horizontal (mirror).
- All lines **parallel to these three** are isometric lines.

### A3. The golden rule: measure ALONG the axes only

- Lines **parallel to an axis** are drawn at **true length** (1:1).
- Lines **NOT parallel** to an axis (e.g. a square's diagonal) are **NOT** drawn at their true size — you must **locate their end points** by moving along isometric axes and joining.
- **Non-isometric lines** (like inclined edges) are found by the **box method**: draw the enclosing isometric box, then mark points along its edges.

### A4. The box method (how to draw any object)

1. Draw the smallest **isometric box** that fits the object.
2. Mark the box dimensions along the three axes (true lengths).
3. Plot the object's corners **on the box edges**.
4. Join the points with object lines; erase the construction box.

> **Circles in isometric** = ellipses. To draw a circle (e.g. a cylinder's end), inscribe it in an isometric **square**, then draw the ellipse that touches the square's midpoints (or use the 4-centre approximate ellipse method).

### A5. Isometric projection vs isometric drawing

| | Isometric Drawing | Isometric Projection |
|---|---|---|
| Scale | Full (1:1) lengths along axes | Foreshortened (≈0.816) |
| Axes | True lengths on axes | All dims reduced by ~18% |
| When | Freehand/pictorial practice | When true size must be preserved after projection |

> **Exam tip:** most undergraduate questions ask for the **isometric drawing** from given orthographic views. Draw the box, measure true lengths along the 3 axes, done.

---

## Part B — Sectional Views

### B1. What & why

A section **cuts the object open** to reveal interior details that hidden (dashed) lines would make confusing. Like slicing a fruit to see the seeds.

- The imaginary cut is the **cutting plane**.
- The surface actually cut is **hatched** (diagonal thin lines).
- Everything behind the cut (visible after slicing) is drawn normally.

### B2. The cutting plane line

Thick **dash-dot** line with arrows at the ends, labelled like **A–A** or **X–X**. The arrows show the **direction of viewing** the section.

```
       A ──►│◄───────────│── A        ← cutting plane A-A
            └────────────┘
              section A-A  (drawn separately)
```

### B3. Hatching (section lines)

- **Thin parallel lines at 45°** over the cut surfaces only.
- Same part, same hatch direction; adjacent parts → opposite directions.
- **Thin sections** (less than ~2 mm thick) may be **blackened** instead of hatched.

```
   ╱╱╱╱╱╱╱   ← hatched (this is the cut face)
   ─────────
```

### B4. Types of sections

| Type | What it is | Used for |
|---|---|---|
| **Full section** | One straight cut through the whole part | Simple interiors |
| **Half section** | Cut half the part, keep the other half as an outside view | Symmetric parts (half inside + half outside) |
| **Offset section** | Cut plane steps through several features | Parts with holes/ribs not in one line |
| **Revolved section** | Cross-section drawn at the cut, rotated into the plane | Long bars, spokes, arms |
| **Removed section** | Same as revolved but drawn beside the part | When space is tight |
| **Broken-out section** | Just a small patch cut out | Local interior detail |

### B5. Section rules to remember

- Hatched only where the plane **actually cuts** material.
- **Ribs, webs, spokes** — convention says they are **not** hatched even if cut (they read better as outlines).
- Hidden lines in section views are usually **omitted** (the section already shows inside).
- The section view's label matches the cutting-plane label (A–A → "Section A–A").

---

## Part C — Dimensioning quick recap (BIS)

- mm only, no symbol. Thin lines, arrowheads, value above the line.
- **Ø** before diameters, **R** before radii.
- Never let a dimension line pass through another line.
- Total = sum of parts; don't repeat dimensions.

```
     Ø30 (diameter)         R15 (radius)
   ┌────────┐               ╭───╮
   │   ─30─ │               R15
   └────────┘
```

---

## Common mistakes

- ❌ Measuring **non-isometric** lines at true length (measure along axes only!).
- ❌ Drawing ellipses for circles as flattened circles — use the box/4-centre method.
- ❌ Hatching the whole part instead of only the cut face.
- ❌ Mixing hatch directions on the same part.
- ❌ Forgetting arrows + label on the cutting plane.

---

## Quick checklist

- [ ] Isometric: is the box correct? Are only axis-parallel lines true length?
- [ ] Isometric circles drawn as proper ellipses?
- [ ] Section: cutting plane labelled with arrows?
- [ ] Hatching at 45°, only on cut faces, same part = same direction?
- [ ] Hidden lines cleaned up in section views?

## CROSS-REFERENCES

- [[overview]] (line types for cutting planes, lettering) · [[orthographic-projections]] (reading views to build isometric from)
- [[wiki/index#engineering-drawing-cross-cutting|Module catalog]]