---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - master decision trees"
tags: [btech, engineering-drawing, solidworks, cad, flowcharts, decision-trees, combos]
last_updated: "2026-09-12"
description: "Every SolidWorks decision tree in one place: feature choice, solid-vs-surface, loft repair, knit-to-thicken, gearbox selection, build decomposition, and troubleshooting flows."
module: "engineering-drawing"
prerequisites: [["INDEX"]]
confidence: high
---

# Flowcharts Master (Every Decision Tree, One Page)

## For future agent
Capstone reference page. Collects and extends the decision trees scattered across the module so any modeling question starts here. Trees link back to their home pages for depth. Mermaid diagrams render in Obsidian; ASCII fallbacks omitted for brevity — if Mermaid fails to render, each tree's home page explains the same logic in prose.

---

## 1. What feature makes this shape?

```mermaid
flowchart TD
    A[Look at the shape] --> B{Constant section,\nstraight push?}
    B -->|Yes| C[Extrude → extrude-revolve-sweep]
    B -->|No| D{Round about an axis?}
    D -->|Yes| E[Revolve → extrude-revolve-sweep]
    D -->|No| F{Follows a path?}
    F -->|Yes| G[Sweep → extrude-revolve-sweep]
    F -->|No: morphs between\nDIFFERENT profiles| H{Need solid or skin?}
    H -->|Solid| I[Loft/Boundary Boss → lofted-boss-boundary]
    H -->|Skin| J[Loft/Boundary Surface → lofted-boundary-surfaces]
```

## 2. Solid or surface?

```mermaid
flowchart TD
    A[New shape] --> B{Freeform skin or\nchanging curvature?}
    B -->|No| C[Stay SOLID — simpler,\nrobust, faster]
    B -->|Yes| D[Surface patches →\nsurfacing-methodology]
    D --> E[Knit → thicken →\nfilled-knit-trim-thicken]
```

## 3. Loft is twisted — fix order

```mermaid
flowchart TD
    A[Twisted loft] --> B[Drag connectors to\nmatching corners]
    B --> C{Fixed?}
    C -->|No| D[Equalize profile segments\n+ add guide curves]
    D --> E{Fixed?}
    E -->|No| F[Rebuild as Boundary\nwith explicit Direction 2]
    F --> G{Fixed?}
    G -->|No| H[Rebuild worst profile\nsketch — combs don't lie]
    C -->|Yes| I[Set tangency → zebra-check]
    E -->|Yes| I
    G -->|Yes| I
```

## 4. Knit/thicken failure — repair order

```mermaid
flowchart TD
    A[Knit or thicken fails] --> B[Find naked edges\nwireframe scan]
    B --> C[Extend + re-trim\nthe guilty patch]
    C --> D[Fill slivers]
    D --> E[Re-knit in stages,\nTIGHT tolerance]
    E --> F{Passes?}
    F -->|No| G[Check parent sketches:\ncombs + repair]
    G --> E
    F -->|Yes| H[Thicken-test → solid]
```

## 5. Which gearbox?

```mermaid
flowchart TD
    A[Power transfer need] --> B{Shaft layout?}
    B -->|Parallel, roomy| C[Spur/helical → helical-spur-gearboxes]
    B -->|Right angle| D[Bevel → bevel-planetary-gearboxes §1]
    B -->|Coaxial + compact| E[Planetary → bevel-planetary-gearboxes §2]
    B -->|Quiet + loaded| F[Herringbone → bevel-planetary-gearboxes §3]
```

## 6. Decompose a scary model

```mermaid
flowchart TD
    A[Scary model] --> B[Regions of consistent\ncurvature — list them]
    B --> C[One technique per region\n— assign from tree #1]
    C --> D[Order: big shell →\nopenings → details]
    D --> E[Seams on style lines\nor hidden faces]
    E --> F[Build → verify\n→ complex-showcase]
```

## 7. Finish-order combos

```mermaid
flowchart TD
    A[Symmetric?] -->|Yes| B[Model HALF → Mirror]
    A -->|No| C[Model full]
    B --> D{Repeated detail?}
    C --> D
    D -->|Regular| E[Pattern]
    D -->|One-off| F[Sketch-driven/manual]
    E --> G{Region-specific?}
    F --> G
    G -->|Yes| H[Split Line → finish zone]
    G -->|No| I[Fillet/chamfer/shell/rib]
```

## 8. Debug any failed feature (universal)

```mermaid
flowchart TD
    A[Feature fails] --> B[Read the error:\nWHAT entity is guilty?]
    B --> C[Roll back: does the\nparent geometry exist?]
    C -->|Dangling ref| D[Re-attach to planes/\nstable faces]
    C -->|Exists| E[Simplify: suppress\nlater features, retry]
    E --> F{Works now?}
    F -->|Yes| G[Reintroduce features\none by one — find the conflict]
    F -->|No| H[Rebuild the sketch:\nrepair + fully define]
```

## CROSS-REFERENCES
- [[INDEX]] · [[surfacing-methodology]] · [[lofted-boundary-surfaces]] · [[filled-knit-trim-thicken]] · [[gearbox-fundamentals]] · [[dressup-productivity]] · [[solidworks-cheatsheet]]
