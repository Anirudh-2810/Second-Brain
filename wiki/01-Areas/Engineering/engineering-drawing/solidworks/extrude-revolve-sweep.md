---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - core solid features"
tags: [btech, engineering-drawing, solidworks, cad, extrude, revolve, sweep, beginner]
last_updated: "2026-09-12"
description: "The three solid workhorses for beginners: Extruded Boss/Cut, Revolved Boss/Cut, Swept Boss/Cut — when to use each, end conditions, and the failure modes to avoid."
module: "engineering-drawing"
prerequisites: [["sketch-mastery"], ["part-assembly-drawing-workflow"], ["INDEX"]]
confidence: high
---

# Extrude · Revolve · Sweep: The Three Workhorses

## For future agent
First solid-features page. Covers the three features behind most PL1 beginner exercises and PL2 prismatic/machined parts. Behavior described is version-stable SolidWorks core (a decade+). Dimensions in examples mirror playlist conventions (mm), not engineering requirements.

> **Why these three:** nearly every manufactured object is either pushed straight (extrude), spun round (revolve), or dragged along a path (sweep). Recognize which one a shape wants and modeling becomes classification, not struggle.

---

## 1. Which feature? (the only flowchart that matters at first)

```mermaid
flowchart TD
    A[Look at the shape] --> B{Constant cross-section\npushed straight?}
    B -->|Yes| C[EXTRUDE\nbrackets, plates, housings, keys]
    B -->|No| D{Round and symmetric\nabout an axis?}
    D -->|Yes| E[REVOLVE\nshafts, bottles, pulleys, washers]
    D -->|No| F{Follows a path?\nrails, tubes, springs}
    F -->|Yes| G[SWEEP\npipes, wires, coils, handles]
    F -->|No: morphs between\nDIFFERENT profiles| H[LOFT → lofted-boss-boundary]
```

## 2. Extrude (Boss = add, Cut = remove)

Sketch a closed profile → pull it straight. The **end condition** decides intelligence:

| End condition | Meaning | Use when |
|---|---|---|
| Blind (depth) | Fixed mm | Quick brackets, plates |
| Through All / Up To Surface | Adapts to geometry | Holes through housings — survives thickness changes (design intent!) |
| Mid-Plane | Symmetric both ways | Anything symmetric about its sketch plane — half the dims |
| Up To Vertex/Body | Associative | Features that must track neighbors |

**Real-world anchor:** machined parts (milled/EDM) are extrude-native — a mill cuts straight down, exactly like an extruded cut. If a part will be CNC-milled, bias toward extrudes: the model mirrors the manufacturing, quotes come back cheaper, and nobody has to reinterpret your geometry.

**Draft** (taper while extruding): mandatory for molded/cast parts so they eject from the mold — typically 1–3° (TBC exact shop standard; ask the molder). Add it in the extrude, not as a later feature.

## 3. Revolve (Boss/Cut)

Sketch the **half-profile** on one side of a **centerline** → spin 360° (or less: 180°/270° sectors). Rules: profile must not cross the centerline (else self-intersecting solid); keep the centerline a construction line in the same sketch.

Where it owns the playlist: bottles, jugs, vases, pulleys, shafts, washers, the SpaceX-Dragon-class axisymmetric bodies ([[bottles-containers]], [[complex-showcase]]). **Thin-feature revolve** makes hollow vessels (bottle walls) in one step — wall thickness as a parameter.

## 4. Sweep (Boss/Cut)

**Profile** (cross-section) + **Path** (curve it travels along) = tube/rail/coil. Constraints that bite beginners:

- Path should be smooth (tangent-continuous); kinks in the path become creases or failures.
- Profile plane ⊥ path start, or use **pierce relation** (profile point pierced to path) so it tracks.
- **Guide curves** (second rails) control twisting profiles — the bridge to [[lofted-boss-boundary]].
- Spring/coil = circle profile + helix path (Helix/Spiral curve tool).

Real-world: wiring harnesses, hydraulic tubes, springs, ergonomic rails — anything "long and following."

## 5. Cut versions & Hole Wizard

Every Boss has a Cut twin (same dialog, removes material). Prefer **Hole Wizard** over sketched circles + cut for real holes: it carries threads, counterbores, countersinks, and standard sizes (M3/M4/M6…) with cosmetic or modeled threads. A drilled-and-tapped hole modeled as a plain cut is a manufacturing lie — the shop needs the thread callout, which Hole Wizard puts on the drawing automatically.

## 6. Failure clinic

| Symptom | Cause → Fix |
|---|---|
| "Sketch is not closed" / zero-thickness | Gap/overlap at corners → magnify, Repair Sketch; extrude needs a watertight profile |
| Sweep twists or self-intersects | Path curvature tighter than profile size → shrink profile, smooth path, add guide curves |
| Revolve fails | Profile crosses centerline → keep profile one side only |
| Cut goes the wrong way / blind misses | Wrong direction or end condition → Flip Side, or switch to Up-To-Surface |
| Rebuild errors after edit | Child lost its reference face → re-attach sketch plane to a plane, not a face |

**Verify in-app:** model a bracket (extrude + cut + hole wizard), a shaft (revolve), a hook (sweep on an arc path) — change each driving dimension once and confirm clean rebuilds.

**Next:** [[lofted-boss-boundary]] for morphing shapes.

## CROSS-REFERENCES
- [[INDEX]] · [[sketch-mastery]] · [[lofted-boss-boundary]] · [[dressup-productivity]] · [[beginner-exercises]]
