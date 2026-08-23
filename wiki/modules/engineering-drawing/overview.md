---
module: "engineering-drawing"
topic: "Engineering Drawing — Module Overview & Beginner's Guide"
tags: [engineering-drawing, overview, drawing-basics, bis, sp46, lines, lettering, dimensioning, scales, beginner]
last_updated: "2026-08-21"
prerequisites: ["None — start here"]
---

# Engineering Drawing — Overview & Beginner's Guide

> Engineering Drawing is the **universal language of engineers** — the way we describe a 3D object on a flat sheet so anyone (anywhere, any language) can build it exactly. This module breaks it into small, visual chunks. Start here.

---

## What is Engineering Drawing, really?

Think of a **recipe** but for machines. A recipe says "flour, water, salt, bake at 200°C". A drawing says:

- **What** the part looks like (shape, size)
- **How** to make it (views, dimensions, tolerances)
- **Where** it fits (material, symbols, notes)

A drawing must be **complete** (nothing missing), **clear** (no guessing), **correct** (no errors), and follow **standards** (so it means the same thing everywhere).

**Golden rule:** a drawing is only useful if *any* engineer can read it without the person who drew it being there.

---

## The tools you'll use

| Tool | Purpose |
|---|---|
| Drawing board + T-square | Straight horizontal lines, parallel lines |
| Set squares (45° & 30°/60°) | Vertical lines and 45°/30°/60° angles |
| Compass | Circles and arcs |
| Protractor | Measuring angles |
| Scale (plain, diagonal, vernier) | Drawing to exact proportions |
| HB / H / 2H pencils | HB for sketching, H–2H for finished lines |
| Eraser, sharpener, cloth | Cleanup |
| French curves / flexi curve | Smooth non-circular curves |

> **Exam tip:** always draw light construction lines first (H pencil, thin), then darken the final object outline (2H/H, thick & dark). Clean sheet + sharp pencil = free marks.

---

## Line types — the "alphabet" of a drawing

Just like letters make words, **lines** make drawings. Every line type means something specific. Memorize these (BIS SP 46 / IS 10714):

```
THICK  CONTINUOUS  ━━━━━━━━━   Visible / object outlines (the actual edges you see)

THIN   CONTINUOUS  ─────────   Dimension lines, extension lines, hatching, leader lines

DASHED            ┄┄┄┄┄┄┄┄   Hidden / invisible edges (behind the object)

THIN DASH-DOT     ─·─·─·─·─   Center lines (axes of circles / symmetry)

THICK DASH-DOT    ─·━·─·━·─   Cutting plane lines (where a section is taken)

THIN DASH-DOT     ─·─·─·─·─   (ends in thick dashes) = cutting plane

THIN DASH         ┄┄┄┄┄┄┄    (with arrows) = projection / viewing direction

WAVY / FREEHAND   ﹏﹏﹏﹏      Break lines (short break in a part)
```

| Line | Used for |
|---|---|
| Thick continuous | Visible edges — the part's real outline |
| Thin continuous | Dimension & extension lines, section hatching |
| Dashed (thin) | Hidden edges — what you can't see from this view |
| Dash-dot (thin) | Center lines, symmetry axes |
| Dash-dot (thick) | Cutting-plane lines |
| Wavy/zig-zag | Break lines |

> **Why it matters:** two drawings can show the *same* outline but mean totally different things depending on whether the internal line is **dashed** (hole behind) or **continuous** (a real edge in front).

---

## Drawing sheet & title block

- Standard sheets (BIS): **A0 → A1 → A2 → A3 → A4** — each is half the previous. A4 is the exam standard.
- Margins & a **title block** (bottom-right) with: drawing title, scale, sheet number, name, roll number, date, material, drawing number.
- Title block is the "signature" — never leave it blank.

---

## Scales — fitting big/small things on paper

You can't draw a 100 m building on an A4 sheet, nor a watch gear at real size. So we **scale**.

$$\text{Scale} = \frac{\text{Drawing size}}{\text{Actual size}}$$

| Type | Scale | Example |
|---|---|---|
| Full size | 1 : 1 | drawing = object |
| Reduced (small objects→big drawings) | 1 : 2, 1 : 5, 1 : 100 | 1 cm on paper = 2 cm on object |
| Enlarged (tiny parts→visible drawings) | 2 : 1, 5 : 1, 10 : 1 | 2 cm on paper = 1 cm on object |

**Plain scale** = a simple ruler split into units & sub-units (e.g. metres + decimetres). **Diagonal scale** = measures to 2 decimal places (e.g. 2.47 cm) using diagonal lines. **Vernier scale** = precise sub-divisions with a sliding vernier.

> **Beginner trick:** read scale problems backwards — "1:4" means "draw one part, object is 4 parts". You always *divide* the actual size by the second number.

---

## Lettering — the words

- **Single-stroke** (one line per letter, no fancy fonts), **vertical or inclined (15°)**.
- Height standardised: **3.5 mm, 5 mm, 7 mm, 10 mm** (A4 exams usually want 5–7 mm).
- Uppercase for titles, lowercase for dimensions.
- Lettering is drawn with **light construction first**, then filled — never scribbled.

---

## Dimensioning — the "how big" part

Every dimension tells the maker a size. Rules (BIS 11669):

- Dimensions in **millimetres** (no unit symbol written).
- **Dimension line** (thin, with arrowheads at both ends) sits outside the object.
- **Extension lines** (thin) extend from the object to the dimension line.
- **Arrows** touch the extension lines; dimension value written **above** the dimension line, in the middle.
- **Leader lines** (thin, ending in an arrow/dot) point at a feature to label it.
- A circle is dimensioned by its **diameter (Ø)**; arcs by **radius (R)**.
- Dimensions from a common baseline = **chain/parallel** dimensioning; total must equal the sum of parts (never over-dimension!).

```
        ↑
   40   │
 ───────┼────────   ← dimension line (thin, arrows)
        │          ← extension lines (thin)
    ┌───┴────┐
    │ object │
    └────────┘
```

> **Rule of thumb:** every feature needs exactly the dimensions to define it — **neither missing nor repeated**.

---

## What's next (reading order)

1. **[[orthographic-projections]]** — the single most important topic: seeing a 3D object as 2D views (front, top, side). ~40% of the syllabus.
2. **[[isometric-and-sections]]** — drawing the 3D "picture" (isometric) and cutting objects open to see inside (sections).
3. Then practise: curves (ellipse, parabola), development of surfaces, intersections — all build on the same projection logic.

---

## Quick-start checklist for every problem

1. Read the question → identify the **shape** and the **view needed**.
2. Draw **light construction lines** for all views first.
3. Project lines **between views** (they always line up — project across).
4. Darken **only** the visible outlines; add dashed hidden lines.
5. Add center lines, dimensions, title block.
6. Check: is it complete, clear, correct, standard?

---

## Sources

- **N.D. Bhatt** — *Engineering Drawing (Plane & Solid Geometry)* — primary text
- **BIS SP 46:2003** — *Engineering Drawing Practice for Schools & Colleges* (line types, lettering, dimensioning standards)
- **K.L. Narayana & P. Kannaiah** — *Engineering Drawing*
- **Dhananjay A. Jolhe** — *Engineering Drawing*

## CROSS-REFERENCES

- [[orthographic-projections]] · [[isometric-and-sections]]
- Related: [[modules/engineering-physics/overview|Engineering Physics]] · [[modules/engineering-math/module-1-matrices|Engineering Math]]
- [[modules/index#engineering-drawing-cross-cutting|Module catalog entry]]