---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - bottles and containers"
tags: [btech, engineering-drawing, solidworks, cad, surfacing, revolve, bottles, packaging]
last_updated: "2026-09-12"
description: "Bottle, jug, vase and container builds from PL1: revolve-first vessel workflow, shoulders and necks, caps and assemblies, and packaging DFM notes for beginners."
module: "engineering-drawing"
prerequisites: [["beginner-exercises"], ["extrude-revolve-sweep"], ["INDEX"]]
confidence: medium
---

# Bottles, Jugs, Vases & Containers

## For future agent
PL1 product-family page. Vessel builds recur across the playlist (#20/#33/#40/#41 bottle variants, #21/#58 jugs, #69 vase, #80 perfume, #95 angle-neck, #27 bottle assembly, #52 bottle+cap). Recipes below follow the revolve-first vessel pattern standard to this genre (TBC per-video against bulk transcripts). Manufacturing notes are general packaging-CAD knowledge, flagged where shop-specific.

> **Why vessels first:** bottles are the kindest surfacing teacher — mostly axisymmetric (revolve does the heavy lifting), one hard part (the shoulder transition), and instant real-world feedback (you've held a thousand bottles; your eye already knows what's wrong).

---

## 1. The vessel workflow (memorize this)

```mermaid
flowchart TD
    A[Half-profile sketch:\nbase → body → shoulder → neck] --> B[Revolve 360°]
    B --> C{Shoulder smooth?}
    C -->|No: crease| D[Rebuild shoulder spline\nwith tangent ends]
    C -->|Yes| E[Thin-feature or Shell\nfor wall thickness]
    E --> F[Neck threads/cap\nseparate features]
    F --> G[Handle? → swept/lofted\n+ mutual trim — #58 jug]
    G --> H[Fillets, labels via\nSplit Line + Decal/TBC]
    H --> I[Cap as separate PART\n+ assembly]
```

**Profile anatomy (the four zones):** base (punt/dome for stability + mold release) → body (straight or gently curved — label panel flats go here) → shoulder (the money curve: tangent-continuous spline, never an arc-arc kink) → neck/finish (the standardized mouth the cap grips — model to cap spec, not by eye).

## 2. Playlist build map

| Build | Key technique (TBC per-video) | Lesson |
|---|---|---|
| #20 Bottle, #33/#40 Bottle variants | Revolve + shell + neck | Axisymmetric basics; compare variants to see design range from one workflow |
| #21 Jug, #41 Jug, #58 Jug (Revolved+Swept+Trim) | Body revolve + swept handle + mutual trim | Intersecting bodies: overshoot handle into body, mutual-trim, fillet the joint |
| #69 Vase, #100 Art vase (sketch picture) | Lofted/revolved organic profile; image-trace for art vase | Shoulder freedom; reverse-engineering via [[sketch-mastery#6-sketch-picture-reverse-engineering-on-ramp]] |
| #80 Perfume bottle | Small-scale precision + cap | Luxury packaging: tight tolerances, thick glass walls |
| #85 Plastic bottle, #95 Angle-neck bottle | Non-vertical necks, molded features | Angled axes: sketch planes at angles; draft for molding |
| #27 Bottle Assembly, #52 Bottle + Cap | Multi-part: vessel + cap + label | First assemblies: concentric + coincident mates, thread representation |

## 3. Caps, closures & threads (the assembly half)

- Model the cap as a **separate part** (it IS manufactured separately) — knurled grip via patterned cuts or cosmetic texture (TBC: knurl modeling varies; cosmetic appearance often suffices).
- Threads: **modeled threads** (helix + sweep-cut) for close-ups and 3D prints; **cosmetic threads** (Thread feature/decal callout) for drawings and performance. A bottle mouth with no thread callout is an unmanufacturable model — the drawing needs the spec (e.g., 28-400 finish — TBC: confirm standard with packaging references, not this page).
- Cap–neck fit: clearance for the seal + engagement length; verify with section view + interference detection in the assembly.

## 4. Packaging DFM (why factories will love/hate your model)

- **Draft:** all vertical walls need mold-release taper (1–3° typical, TBC per molder) — straight-walled bottle bodies without draft don't eject.
- **Uniform walls:** hollow vessels via thin-revolve or shell at even thickness; thick-to-thin transitions sink and warp in cooling.
- **Parting line placement:** put it where the mold halves meet sensibly (usually the silhouette edge) — split-line control from [[dressup-productivity]].
- **Label panels:** flat-ish zones dimensioned for the label size; recess them slightly (TBC: ~0.2–0.5 mm typical) so labels sit flush.

## 5. Failure clinic

| Symptom | Cause → Fix |
|---|---|
| Shoulder crease visible | Arc joints without tangency → single spline with tangent ends, curvature-comb it |
| Shell/thin-feature fails at shoulder | Wall thicker than local curvature → fair the curve or thin the wall |
| Handle joint looks glued-on | No mutual trim + fillet → intersect, trim, tangent-constrain, fillet the seam |
| Cap won't assemble | Thread/mouth mismatch → model cap FROM the neck dimensions (in-context), section-check |

**Verify in-app:** revolve one bottle from a 4-zone profile → shell → model its cap → assemble → section view + interference check. Then angle the neck 15° (angle-neck variant) and watch what breaks — that's the lesson.

**Next:** [[consumer-electronics]].

## CROSS-REFERENCES
- [[INDEX]] · [[beginner-exercises]] · [[consumer-electronics]] · [[extrude-revolve-sweep]] · [[filled-knit-trim-thicken]]
