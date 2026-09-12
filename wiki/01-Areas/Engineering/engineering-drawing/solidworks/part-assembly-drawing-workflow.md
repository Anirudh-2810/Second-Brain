---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - documents and pipeline"
tags: [btech, engineering-drawing, solidworks, cad, part, assembly, drawing, mates, workflow]
last_updated: "2026-09-12"
description: "The master SolidWorks pipeline for beginners: Part vs Assembly vs Drawing documents, mates, the sketch-feature-part-assembly-drawing flow, and in-context editing."
module: "engineering-drawing"
prerequisites: [["sketch-mastery"], ["INDEX"]]
confidence: high
---

# Part → Assembly → Drawing: The Master Workflow

## For future agent
Foundation page 3. Establishes the document pipeline every later page assumes: PL1 ≈ Part-level, PL2 ≈ Part + Assembly. Mates and in-context editing grounded in standard SolidWorks behavior (version-stable for a decade+). Links forward to machine-build pages.

> **The mental model:** Part = one manufactured piece. Assembly = how pieces fit and move. Drawing = the legal document the workshop builds from. A model without a drawing can't be manufactured; an assembly without mates is just overlapping solids.

---

## 1. The pipeline

```mermaid
flowchart TD
    A[Requirement:\nwhat must it DO?] --> B[Part: sketch → features\none .sldprt per component]
    B --> C{More than\none part?}
    C -->|Yes| D[Assembly: insert parts\n+ mates, .sldasm]
    C -->|No| E[Drawing: views +\ndimensions, .slddrw]
    D --> E
    E --> F[Manufacture:\nshop reads the drawing]
    F --> G{Design change?}
    G -->|Yes| B
```

**Real-world anchor:** in industry the **drawing is the contract** — machine shops quote and cut from it, not from your 3D file. Dimensions, tolerances, surface-finish marks, title block: that's what turns geometry into a purchasable part. Your ED theory ([[../overview]]) is exactly this language.

---

## 2. Part modeling order (the combo all builds share)

```
1. Base feature  — biggest shape first (extrude/revolve of the main profile)
2. Major form    — cuts and adds that change the silhouette (cut-extrude, loft)
3. Functional    — holes (Hole Wizard!), threads, mounting bosses
4. Dress-up LAST — fillets, chamfers, shells, drafts
5. Check         — mass properties, section view, interference (if multi-body)
```

**Why dress-up last:** fillets consume edges by identity — later features referencing filleted edges break constantly. Shell near the end (it hollows using existing faces). Every playlist build that "suddenly broke" violates this order (TBC per-video, but the pattern is universal).

**Multi-body vs assembly:** you can model several solid bodies inside one Part (great for weldments, mold halves, master-model technique). Split into an assembly when parts **move relative to each other** or are **manufactured separately** (gearbox: separate parts; mold core/cavity: multi-body then split).

---

## 3. Assemblies & mates (PL2 territory)

An assembly positions parts with **mates** (geometric constraints between faces/edges):

| Mate family | Examples | Used for |
|---|---|---|
| Standard | Coincident, Concentric, Parallel, Perpendicular, Tangent, Distance, Angle | 95% of static assemblies (gearbox housings, shafts, press frames) |
| Advanced | Symmetric, Width, Path, Linear/Linear-coupler | Symmetric mechanisms, sliding elements |
| Mechanical | **Gear mate** (ratio!), Rack-pinion, Screw, Hinge, Cam | Moving machines — PL2 gearboxes come alive here |

```mermaid
flowchart TD
    A[Insert first part] --> B[Fix it to origin]
    B --> C[Insert next part]
    C --> D[Mate: position + orientation\nConcentric shaft, Coincident faces...]
    D --> E{Fully defined?\nno -/+ in tree}
    E -->|Under-defined| D
    E -->|Yes| F{Should it MOVE?}
    F -->|Yes| G[Leave rotational DOF free\n+ mechanical mate, Motion study]
    F -->|No| H[Fully lock it]
```

**Rules that prevent assembly hell:**
- First part **fixed** at origin; build outward from it.
- Mate to **planes and origins** where possible, not decorative faces (faces disappear in redesigns; planes don't).
- **One mate at a time**, watch the part move, confirm before adding the next.
- Gear mate needs the ratio (teeth counts from [[gearbox-fundamentals]]) — wrong ratio = lying prototype.
- Large assemblies: **Lightweight mode**, SpeedPak, sub-assemblies — open only what you're working on.

---

## 4. In-context editing (top-down design)

Edit a part **inside** the assembly (right-click → Edit Part) so it references neighboring geometry — e.g., size the gearbox cover from the housing it closes. Power + danger: creates **external references** (part depends on assembly context). Rules: keep references to stable things (planes, major faces), never to fillets/edges; lock them (`List External Refs → Break All`) before sending files anywhere — a part that can't find its assembly won't open correctly on another machine (TBC: exact freeze behavior varies by version; the caution doesn't).

## 5. Drawings (manufacturing output)

Standard sheet flow: model views (Front/Top/Isometric) → dimensions pulled from the model (they **update** when the model changes — never fake with static text) → tolerances on mating features → notes (material, finish) → title block. **Section views** ([[../orthographic-projections]] theory, now one click) reveal interiors of housings and gearboxes. For PL2 machines, add an **exploded view + BOM (bill of materials)** — the assembly instruction sheet.

## 6. Verify-in-app checklist (per build)

- [ ] FeatureManager tree reads like a recipe (named features, sensible order)
- [ ] Mass properties sane (a steel bracket the size of your palm shouldn't weigh 40 kg — wrong units/material is the classic)
- [ ] Section view shows intended interiors, no accidental voids/overlaps
- [ ] Assembly: no `-` (under-defined) or errors; drag moving parts through full travel
- [ ] Drawing views + BOM update after a model edit (change one dimension, rebuild, confirm)

---

## 7. Worked example: spacer plate → 2-part assembly → drawing (one sitting)

**Part (spacer plate 100×60×8, 4× M5 holes, 2× Ø8 dowel holes):**
1. Front? No — plates lie flat: sketch on **Top Plane** → corner rectangle 100×60 anchored to origin (two edges coincident) → fully define → Extrude 8 Mid-Plane (symmetric about Top — design intent for a stacking part).
2. Hole Wizard: 4× M5 clearance on 90×50 pattern (10 from edges — pattern the FIRST hole with linear pattern, don't place four), 2× Ø8 dowels on centerline spaced 60. Rename all.
3. Fillet outer vertical edges 1 mm (deburr) — LAST. Mass check: steel ≈ 100×60×8 minus holes ≈ 370 g (TBC: read YOUR mass window — the habit is the lesson, not my arithmetic).

**Assembly (plate + standoff + second plate — a mini stack):**
1. New Assembly → insert plate → **Fix** (grounds it). Insert standoff (model quickly: revolve stepped cylinder Ø10/Ø6) → Concentric mate to a dowel hole + Coincident to plate top.
2. Insert second plate → Concentric to standoff + Coincident to standoff top. Tree shows no `-` anywhere.
3. Mate audit: drag the top plate — locked in all 6 DOF? It should be (concentric kills 4? precisely: concentric removes 4 DOF leaving axial slide+spin, coincident face kills slide, and a second coincident/parallel kills spin — count DOF per mate until this is instinct).

**Drawing (the contract):**
1. New Drawing → A4/ISO template (TBC: match your college standard) → Front + Top + Isometric views of the PLATE part.
2. Model Items → import dimensions (they arrive associative — change the model, drawing updates; demo this once and you'll never hand-type a dimension again).
3. Section view through the dowel holes; hole callouts via Hole Wizard data (M5 clearance + Ø8 H7? tolerance per fit intent — TBC: confirm fit tables, not this page); title block filled (material: C45/MS — TBC per stock).

## 8. Configurations + Pack and Go (file hygiene that scales)

- **Configurations:** one part file, multiple variants (Default: full detail; Simplified: holes suppressed for big assemblies; Flat: for drawings). Suppress (not delete) heavy features in working configs — rebuild speed is a feature.
- **Pack and Go** (File → Pack and Go): zips part + assembly + drawing + references for sending/sharing. Sending a lone .sldasm without its parts is the classic broken-delivery — Pack and Go makes it impossible.
- **External references audit** (for in-context parts): List External Refs → check nothing points at volatile geometry before sharing; Break/Lock what shouldn't travel (caution from §4 stands).

**Next:** solid features — [[extrude-revolve-sweep]].

---

## 10. Drawing detailing deep pass (the contract, filled out)

**View selection (the 3-view habit from [[../orthographic-projections]], applied):** front (most informative face) + top + side + ONE isometric (3D readability for the shop) + sections where interiors hide (housings, gearboxes, manifolds — if it has guts, it gets a section) + detail views for small features (threads, grooves, O-ring seats at 2:1 scale — TBC per complexity). Aligned views (projected, associative) over random placements — move the parent, children follow.

**Dimensioning discipline (manufacturing reads these, not your 3D):** dimension FUNCTION (mounting holes, mating diameters, thicknesses) not every edge — over-dimensioned drawings get ignored, and ignored drawings get misbuilt; hole callouts FROM Hole Wizard data (quantity + size + depth + thread in one leader — never hand-type what the feature knows); datums on mating faces (the A-B-C discipline is full GD&T territory — TBC depth; awareness: datums exist, flatness/position callouts follow in pro work, confirm with drafting standards NOT this page); general tolerance block in the title area (untoleranced dims default here — e.g., ISO 2768-m — TBC per shop standard) so the drawing is COMPLETE (a dimension without tolerance is a wish, not a spec).

**BOM + balloons (assembly drawings):** item-numbered balloons to every part (no orphans!) → BOM table (part no, description, qty, material) → revision column (REV A/B/C with change notes — the engineering-change habit; TBC per company process). Fasteners listed with full spec (M6×20 SHCS, not "screw") — purchasing buys from the BOM, and vague BOMs buy wrong parts.

---

## 9. Mates deep pass: DOF thinking (the 10-minute mastery)

Every rigid part has 6 degrees of freedom (3 translations + 3 rotations). Each mate REMOVES specific ones — count them and assemblies stop being trial-and-error:

| Mate | Removes | Leaves |
|---|---|---|
| Concentric (shaft in hole) | 4 (all but axial slide + spin) | Slide + spin |
| Coincident faces | 1 (axial) | — |
| Concentric + Coincident | 5 | Spin only |
| + Parallel/second Coincident | 6 | Fully fixed |
| Distance / Angle | 1 (parameterized!) | Restrained but adjustable |
| Gear mate | Couples rotations by ratio | Motion WITH relationship |

**Deliberate under-definition (advanced habit):** leave exactly the motion DOF free (a hinge keeps 1 rotation; a slider keeps 1 translation) and VERIFY by dragging — then lock with limit mates (Angle/Distance with min/max) so the mechanism can't travel past reality. Mechanisms modeled fully-fixed can't be tested; mechanisms left floppy fall apart. One free DOF + limits = testable truth.

**Mate errors decoded:** "over-defined assembly" = two mates fighting (e.g., two distance mates on the same axis) — suppress mates one-by-one from the bottom until it solves; the last unsuppressed is the conflict. "Flipped mate" after edits = reference face vanished — reattach to planes (the stability ladder from [[solidworks-basics-setup#9-rebuild-survival-guide]]).

## CROSS-REFERENCES
- [[INDEX]] · [[sketch-mastery]] · [[extrude-revolve-sweep]] · [[gearbox-fundamentals]] (assembly-heavy) · [[../overview]]
