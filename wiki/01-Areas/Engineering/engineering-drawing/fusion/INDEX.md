---
course_code: "BTech-ED-CAD"
course_name: "Engineering Drawing — CAD self-study"
unit: "Fusion track hub (complement to SolidWorks)"
date: "2026-10-02"
last_updated: "2026-10-02"
description: "Hub for the Autodesk Fusion track, scoped as a complement to the 27-page SolidWorks track - why Fusion exists alongside it, free Education-licence route, the browser-based workflow, and the project ladder aimed at the Arduino/hardware/3D-printing thread."
tags: [cad, fusion, autodesk-fusion, 3d-printing, hardware, engineering-drawing, self-study, hub, solidworks]
confidence: medium
prerequisites: ["[[01-Areas/Engineering/engineering-drawing/overview]]", "Basic engineering drawing"]
sources: ["Autodesk education + subscription pages, verified 2026-10-02 via web search"]
---

## For future agent

**Fusion is a COMPLEMENT to SolidWorks, not a replacement.** The user made this call explicitly on 2026-10-02. There is already a **27-page, ~490 KB SolidWorks track** at [[01-Areas/Engineering/engineering-drawing/solidworks/INDEX]] built from 154 ingested YouTube videos. **Do not build a second parallel full CAD track** — that splits effort and duplicates ~90% of the concepts.

**The scoping rationale (record this so a future agent doesn't undo it):**

| | SolidWorks | Fusion |
|---|---|---|
| Cost to this user | paid / edu licence | **free** (1-yr Education, renewable) |
| Platform | **Windows only** | Windows · **macOS** · **browser** |
| CAM (milling/turning) | separate product | **integrated** |
| 3D-print prep | add-on | **integrated** |
| 3MF export | add-on | built in |
| India industry recognition | **high** | moderate/growing |

**So:** SolidWorks stays the design/portfolio skill; **Fusion is the tool for the Arduino → robotics → 3D-printing hardware thread** (North Star: "build the hardware gap for RAI"). This page is the routing point; it is deliberately *thin*, because there is **no Fusion source material in `raw-sources/`** and no video transcripts to distil.

**Confidence is `medium` throughout.** This page was built from web research, not from ingested sources. Menu paths and feature names move between releases — **verify against the installed app** rather than trusting a path written here. That's why the SolidWorks track, which came from 154 real videos, is far richer. If the user later drops Fusion tutorial videos into `raw-sources/` (the way they did for SolidWorks), this page should be **replaced** with a distilled track, and this hub becomes the index for it.

---

# Autodesk Fusion — CAD Track (complement to SolidWorks)

> **Why you have both:** SolidWorks is the industry-standard design skill; Fusion is free, cross-platform, and has CAM + 3D-printing built in — which is what the hardware thread needs.
> **SolidWorks track:** [[01-Areas/Engineering/engineering-drawing/solidworks/INDEX]]

---

## 1. Getting the software (free)

**You are a BTech student at KJSCE → the Education plan is the route.**

| Route | Cost | What you get | Catch |
|---|---|---|---|
| **Education plan** ✅ | **Free** | **Full features** | 1 year, **renewable annually**; needs school-email verification |
| Personal use | Free | **Reduced** feature set | 3-year term; non-commercial only; under ~$1,000/yr revenue |
| Commercial | $85/mo · $680/yr · $2,040/3yr | Full | **No perpetual licences exist** |

**Getting the Education licence:**

1. Go to the Autodesk Education products page and sign in with your **school email**.
2. Verify your student status (may need documentation).
3. Select **Autodesk Fusion**, install, sign in — the licence type is detected automatically.
4. **Set a calendar reminder** — Autodesk emails 30 days before expiry, and the licence must be renewed annually or you lose access mid-project.

> **Do this first.** An expired licence mid-build is a nasty surprise, and renewal is a 5-minute job if you remember.

**Extensions are paid add-ons** — Machining, Product Design, Simulation, Nesting & Fabrication, Additive Build, Generative Design each start around $495/user/year with 14-day trials. The base product already covers modelling, rendering and 3D-print prep, so **you do not need any extension for this track.**

---

## 2. Why Fusion, specifically, for this thread

```
   NORTH STAR GOAL: close the hardware gap for FE Robotics & AI
                            |
                            v
   need parts you design yourself
                            |
        +-------------------+-------------------+
        |                                       |
        v                                       v
   3D PRINT IT                          MACHINE IT
   (enclosures, brackets,               (but only if you
    mounts, robot chassis,               have a mill/lathe —
    sensor mounts)                       you probably don't yet)
        |                                       |
        v                                       v
   Fusion's strength:                  NOT worth learning yet
   integrated slicer prep,              (Simulation extension is
   3MF export, colour,                  paid; hand-calc + Fusion
   free, browser access                 SimulationXpress equivalent
   from any machine                     is a later goal)
```

**The honest reason Fusion earns its place here:** you can go **sketch → part → 3MF export → slicer → print** without ever installing anything else, and you can do the first four steps from a **browser** — useful on a machine that isn't your main one.

---

## 3. The workflow (same skeleton as every parametric CAD tool)

This is deliberately the *shape*, not button-by-button. The concepts transfer to SolidWorks, which is the point.

```
   BRIEF  ->  SKETCH  ->  FEATURE  ->  FINISH  ->  EXPORT  ->  MAKE
              |          |           |           |          |
        fully-defined   extrude/    fillet,     STEP for   3MF for
        profiles,       revolve,    chamfer,    CAM,        slicer,
        constraints     sweep,      pattern,    OBJ/3MF,   DXF for
                       loft        shell       STL        laser cut
```

**Stage 1 — Sketch.** Draw a 2D profile with dimensions and constraints. The goal is a **fully-defined sketch**: every dimension either fixed or driven by an equation, so the profile is unambiguous. A sketch that only looks right but is not fully defined will surprise you later.

**Stage 2 — Feature.** Turn the profile into a solid. Learn these in this order:

| Feature | Use it for |
|---|---|
| **Extrude** | the workhorse — prismatic solid from a closed profile |
| **Revolve** | anything axisymmetric — wheels, pulleys, knobs, shafts |
| **Sweep** | solid along a path — brackets, handles, tubing |
| **Loft** | solid between two or more profiles — transitions, ergonomic shells |
| **Fillet / Chamfer** | edges and corners — **never skip these**, they are what make a part look right |

**Stage 3 — Finish.** Dress-up features: fillet, chamfer, patterns (linear/circular), mirror, shell, draft.

**Stage 4 — Export.** For this thread you need **3MF** (colours and units travel; preferred) or **binary STL**. Export **STEP** only if a CAM tool is ever involved. Always run the model's **Check / interference** tool before exporting — a slicer needs closed solids and will crash on naked edges.

**Stage 5 — Make.** Slice, orient, print. The design rules that matter: holes print undersized, so **print a hole-tower test coupon first** rather than trusting nominal dimensions; design **away** overhangs > 45° with chamfers instead of accepting forests of support.

---

## 4. Reading order

| # | Topic | Status |
|---|---|---|
| 1 | **[[fusion-setup-and-interface]]** — install, Education licence + renewal, browser access, navigation, units, the interface differences from SolidWorks | ✅ written |
| 2 | **[[fusion-advanced-parametric-track]]** — advanced track for AutoCAD users: parameters/equations, Body vs Component, joints, shell/ribs, Check + 3MF + hole-tower, 8 showable hardware projects | ✅ written |
| 3 | **[[fusion-course-part1-setup-sketch]]** — PTS CAD EXPERT 4h44m course dump 1/3: CAD/CAM/CAE, licensing, file limits, timeline, units, sketch tools, constraints, fully-defined discipline, TTR, offset | ✅ written |
| 4 | **[[fusion-course-part2-features-assembly]]** — dump 2/3: feature families, 3 approaches, extrude/press-pull/sweep, Body vs Component, top-down assembly, joints + quick-return | ✅ written |
| 5 | **[[fusion-course-part3-sheetmetal-output]]** — dump 3/3: sheet metal + unfold/refold, render, third-angle drawings, PDF export, share, contacts, section analysis | ✅ written |
| 2 | Sketch mastery — fully-defined sketches, constraints, relations, the under/over-constrained diagnostic | ⬜ pending — build when you reach it |
| 3 | Part workflow — extrude, revolve, sweep, loft, dress-up, assembly export | ⬜ pending |
| 4 | 3D printing — 3MF/STL export, Check tool, orientation, supports, tolerances, test coupons | ⬜ pending |
| 5 | Project ladder execution — build the 8 parts below, hardest skills first | ⬜ pending |

**Pages 2–5 are deliberately not created yet.** Writing empty placeholders would be structure without content, and the vault's own rule is that a note must earn its place. Each will be built when you reach it — ideally from the app itself, plus whatever source material exists by then.

---

## 5. Project ladder — robotics/hardware first

Ordered so every project teaches something the next needs. Each is a real part from the Arduino → RAI thread, not a tutorial exercise.

| # | Project | Skills it forces |
|---|---|---|
| 1 | **Sensor mount bracket** (ultrasonic / HC-SR04, M3 screws) | fully-defined sketch, extrude, fillet, hole pattern |
| 2 | **Enclosure for an Arduino + breadboard** | shell, draft, vent slots, lid with fastener pattern |
| 3 | **Robot wheel + tyre mount** | revolve for the hub, extrude/pattern for spokes |
| 4 | **Pan-tilt servo bracket (2-axis)** | assembly constraints, mates, interference check |
| 5 | **Line-follower chassis plate** | larger flat part, lightening pockets, cable channels |
| 6 | **Drone arm / motor-mount plate** | load paths, fillets at stress concentrations |
| 7 | **Cable clips / strain relief** | small batch, printing quantity, tolerance practice |
| 8 | **Enclosure with a printed-in breadboard grid** | grid patterns, embossed labels |

**Rule for every project:** print a **test coupon** (hole tower + a small feature) on the same printer and filament before committing to a full part. Ten minutes of testing beats three failed assemblies.

---

## 6. How this complements SolidWorks (not duplicates it)

| Keep in SolidWorks | Keep in Fusion |
|---|---|
| Portfolio-grade part and assembly modelling | Everything that ends up **printed** |
| Drawing creation and GD&T habits | Fast iteration — no install, browser-based |
| Surfacing depth (27 pages of it) | CAM export path when you get a machine |
| The design-intent discipline the 154-video track teaches | The **free** licence reality |

**If you ever switch your mind** and want Fusion to be the primary tool instead, that is a legitimate call — but then the honest move is to *retire* the SolidWorks track rather than run both. Flag it and it can be archived properly.

---

## Cross-References

- **SolidWorks track (the primary design skill):** [[01-Areas/Engineering/engineering-drawing/solidworks/INDEX]]
- **Course hub:** [[01-Areas/Engineering/engineering-drawing/overview]] · CAD interview prep: [[01-Areas/Engineering/engineering-drawing/cad-design-interview-prep]]
- **North Star:** [[01-Areas/Engineering/engineering-drawing/overview|Engineering Drawing]] · hardware thread in [[North Star]]
- **Arduino decision that motivates this track:** `daily/2026-10-02` and [[Wins]] (2026-09-30 career decision)
- **Source coverage:** [[01-Areas/Engineering/engineering-physics/source-map-physics-sem1]] documents the same pattern for physics — see it for how to record un-ingested material

*Created 2026-10-02. Software/licensing facts verified against Autodesk's education and subscription pages on that date. Feature paths and menu locations are **not** verified against the installed app — treat them as `TBC` and confirm as you go.*