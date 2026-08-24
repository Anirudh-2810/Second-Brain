---
module: "engineering-drawing"
topic: "Orthographic Projections — Beginner's Guide (1st & 3rd Angle, Views, Points→Solids)"
tags: [engineering-drawing, orthographic, projections, first-angle, third-angle, hp, vp, views, beginner]
last_updated: "2026-08-21"
prerequisites: ["[[overview]] — line types, drawing basics"]
---

# Orthographic Projections

> The **most important topic** in the subject. Idea in one line: a 3D object is described by drawing its **flat shadows** from different directions (front, top, side). Read carefully — this builds up step by step.

---

## 1. The big idea (glass box analogy)

Imagine your object inside a **glass box**:

- Look through the **front** glass → you see the **Front View**
- Look down through the **top** glass → you see the **Top View**
- Look through the **side** glass → you see the **Side View**

Then unfold the glass box onto a flat sheet. That flat sheet of views **is** the orthographic drawing.

```
              Top view
    ┌─────────────────────┐
    │       (plan)        │
    ├─────────────────────┤   ← fold line XY
    │       (elevation)   │
    │    Front view       │
    └─────────────────────┘
```

- **Front View (Elevation)** — what you see straight-on
- **Top View (Plan)** — what you see looking straight down
- **Side View (End elevation)** — what you see from the left/right

**Golden rule:** the Front and Top views are always **vertically aligned** (share the same width). The Front and Side views are **horizontally aligned** (share the same height). Project across!

---

## 2. The reference planes

- **Horizontal Plane (HP)** — the floor (horizontal)
- **Vertical Plane (VP)** — the wall in front of you (vertical)
- **Auxiliary Plane (AP)** — any extra plane (for inclined/side views)

The line where HP meets VP is called the **reference line** ($XY$ or $x$–$y$).

### The 4 quadrants — visualised

Imagine standing in a room:
- **HP = floor** (horizontal)
- **VP = front wall** (vertical)
- The **corner** where floor meets front wall = the $XY$ reference line

```
           ABOVE HP (height +)
                    ↑
                    │   Quadrant 2        Quadrant 1
                    │   (above HP,        (above HP,
                    │    behind VP)       in front of VP)
                    │
       BEHIND VP ◄──┼──► IN FRONT OF VP
      (distance -)  │   (distance +)
                    │
                    │   Quadrant 3        Quadrant 4
                    │   (below HP,        (below HP,
                    │    behind VP)       in front of VP)
                    │
           BELOW HP (height -)
```

| Quadrant | Position relative to HP | Position relative to VP | Used for projection? |
|---|---|---|---|
| **1st** | **Above** | **In front of** | ✅ **First Angle (India/ISO/BIS)** |
| 2nd | Above | Behind | ❌ Views overlap |
| **3rd** | **Below** | **Behind** | ✅ **Third Angle (USA/ANSI)** |
| 4th | Below | In front of | ❌ Views overlap |

### Why only Quadrants 1 & 3?

When you **fold HP down 90° clockwise** onto the drawing sheet:
- **Q1 & Q3**: Front view and Top view land on **opposite sides** of XY → clean separation
- **Q2 & Q4**: Both views land on the **same side** of XY → they **overlap** → confusing/unusable

> **India uses FIRST ANGLE projection (ISO/BIS).** Object sits in **Quadrant 1** (above HP, in front of VP). After folding HP down, the top view appears **below** the front view on the sheet.
>
> **USA uses THIRD ANGLE projection (ANSI).** Object sits in **Quadrant 3** (below HP, behind VP). After folding, the top view appears **above** the front view.

---

### 🧠 Mental model: "You're the projector"

Stand in the room corner (where floor meets front wall = XY line):

| Quadrant | Where is the object? | What you see |
|---|---|---|
| **Q1 (1st Angle)** | Floating **above floor**, **in front of you** | You look **up** → front view is **above** XY<br>You look **down** through floor → top view is **below** XY |
| Q2 | Above floor, **behind you** | Both views end up on same side when folded |
| **Q3 (3rd Angle)** | **Below floor** (in basement), **behind you** | You look **down** → front view is **below** XY<br>You look **up** through floor → top view is **above** XY |
| Q4 | Below floor, in front of you | Both views overlap when folded |

**Key insight:** In 1st angle, the **object is between you and the projection plane**. In 3rd angle, the **projection plane is between you and the object**. That's why views swap sides.

---

## 3. First angle vs Third angle — the confusion-killer

The ONLY difference is **where the views land after unfolding the box**.

| | First angle (India/UK) | Third angle (USA) |
|---|---|---|
| Object position | Q1 (above HP, before VP) | Q3 (below HP, behind VP) |
| Front view | at top of sheet | at top of sheet |
| Top view | **below** front view | **above** front view |
| Side view | to the **right** of front | to the **left** of front |
| Identifying symbol | frustum (cut cone) | two circles |

Symbols to draw in the title block:

```
First angle:               Third angle:
   ┌───┐                        ○
   │   │                      ┌─┴─┐
   └───┘   (frustum)          └───┘   (left circle, right small circle)
```

---

## 4. Projection of a POINT (the foundation)

A point has **no size** — just a dot. We locate it by its distances from HP and VP.

- A point **on HP**: its front view lies ON the reference line $XY$ (distance from HP = 0).
- A point **on VP**: its top view lies ON $XY$.
- A point **above HP** (height $h$) and **in front of VP** (distance $d$):
  - **Top view** (plan) at distance $d$ **below** $XY$
  - **Front view** (elevation) at distance $h$ **above** $XY$

```
        ↑ h (front view)
   •───────── XY
        ↓ d (top view)
        •
```

> Once you get a point right, lines are just **two points connected**, and planes/solids are just **many points connected**. Master the point → everything follows.

---

## 5. Projection of a LINE

A line = two points. Project both points, join them.

**True length (TL) rule:** a line appears in its **true length** only in a view **parallel to that plane**. Otherwise it's foreshortened.

| Line position | Front view | Top view |
|---|---|---|
| Parallel to both HP & VP | TL | TL |
| Parallel to VP, inclined to HP | TL | shorter (foreshortened) |
| Parallel to HP, inclined to VP | shorter | TL |
| Inclined to both | both foreshortened | both foreshortened |

**Finding true length & angle (the exam classic):**
Given a line's plan & elevation, to find its **true length (TL)** and true inclination:

1. Draw a **line of the same length as the plan** from one end, vertical up by the **difference in heights** of the two ends (from the elevation).
2. The hypotenuse = **TL**; the angle at the plan end = **true inclination to HP (θ)**.

Same trick horizontally with the elevation's length gives the inclination to VP (φ).

---

## 6. Projection of a PLANE

A plane = a flat surface (triangle, square, circle). Project its **corners** (or center + edge), join them.

- **Plane parallel to HP** → top view = **true shape**, front view = a line.
- **Plane parallel to VP** → front view = **true shape**, top view = a line.
- **Plane perpendicular to both** → both views are lines.
- **Inclined plane** → true shape appears only after an **auxiliary view** (project perpendicular to the plane's edge).

> **Shortcut:** whatever view shows the plane "face-on" is the true shape; the other view collapses to a straight line.

---

## 7. Projection of SOLIDS (the exam core)

Solids (cube, prism, pyramid, cylinder, cone, sphere). The plan is usually drawn first because the solid's base sits on HP.

**Key terms:**
- **Axis** — the line through the center (vertical for most problems).
- **Resting on HP** = base on the floor; **resting on VP** = base on the wall.
- **Sections** through a solid give shapes: cone cut by a plane parallel to base → circle; pyramid cut vertically → triangle; etc.

**General method for any solid:**
1. Draw the **plan** (top view) of the solid in its resting position.
2. Project **up** to get the front view (elevation).
3. If inclined, first draw in a simple position, then **rotate** using the axis — never try to draw the inclined position directly.

| Solid | Plan (base on HP) | Front view |
|---|---|---|
| Cube | square | square |
| Prism (triangular) | triangle | rectangle |
| Pyramid | polygon | triangle |
| Cylinder | circle | rectangle |
| Cone | circle | triangle |
| Sphere | circle | circle |

---

## 8. The 3-view orthographic drawing (freehand/reading)

Given a 3D pictorial, produce front/top/side views:

1. Choose the **direction of the front view** (usually the arrow shown, or the most informative side).
2. Draw the front view.
3. Project **vertically down** → top view.
4. Project **horizontally across** (with a 45° miter line) → side view.

```
        Front           Side
   ┌──────────┐      ┌───┐
   │          │      │   │   ← same height
   └──────────┘      └───┘
        │  (project down)  │ (project right via 45° line)
        ▼                  ▼
   ┌──────────┐      ┌──────────┐
   │ Top view │      │(same width)│
   └──────────┘      └──────────┘
```

**Reading a drawing (reverse):** hidden edges = **dashed**, visible = **solid**, center lines = **dash-dot**. Reconstruct the 3D shape mentally by matching the three views.

---

## 9. Common mistakes (check these in every attempt)

- ❌ Drawing top view **above** the front view — that's third angle; use **first angle** (top below front).
- ❌ Forgetting the **hidden (dashed)** edges in views.
- ❌ Not aligning views (project across properly).
- ❌ Confusing `TL` — a line is TL only in a view parallel to it.
- ❌ Drawing dimension lines touching the object (leave a gap; use extension lines).

---

## Quick formula recap

| Item | Rule |
|---|---|
| Point | two distances: from HP (→ front view height), from VP (→ top view distance) |
| Line | project 2 points; TL only in parallel view |
| Plane | true shape in face-on view; line in edge-on view |
| Solid | draw plan first, project up; incline via axis rotation |
| First angle | top view **below** front view |

## CROSS-REFERENCES

- [[overview]] (line types, scales) · [[isometric-and-sections]] (3D views & cutting)
- [[wiki/index#engineering-drawing-cross-cutting|Module catalog]]