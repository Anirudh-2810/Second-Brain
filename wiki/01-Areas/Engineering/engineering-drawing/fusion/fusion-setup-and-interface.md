---
course_code: "BTech-ED-CAD"
course_name: "Engineering Drawing — CAD self-study"
unit: "Fusion 1 — Setup, licence and interface orientation"
date: "2026-10-02"
last_updated: "2026-10-02"
description: "Day-0 setup for Autodesk Fusion — how to claim and renew the free 1-year Education licence, the browser vs desktop install choice, navigating the canvas, unit settings, and the interface differences from SolidWorks that will trip you up on day one."
tags: [cad, fusion, autodesk-fusion, setup, licensing, interface, self-study, hardware]
confidence: medium
prerequisites: ["[[01-Areas/Engineering/engineering-drawing/fusion/INDEX]]"]
sources: ["Autodesk education + subscription pages, verified 2026-10-02 via web search"]
---

## For future agent

Page 1 of the Fusion track, scoped as a **complement to SolidWorks** — see [[01-Areas/Engineering/engineering-drawing/fusion/INDEX]] for why both exist and why this must not become a second full CAD track.

**Confidence split matters here.** The **licensing and platform facts are `high`** — verified against Autodesk's own education and subscription pages on 2026-10-02. **Everything about the interface is `medium`/`TBC`** — Fusion's UI moves between releases and there is no source material in `raw-sources/` to check against. **Do not trust a menu path written here without confirming it in the installed app.** When you work through this page, correct the paths in place — that is the main value this page accrues over time.

**Not verified here, and you should check:** exact menu labels, the current default workspace layout, browser-feature parity with desktop, and whether any specific tutorial URL still resolves.

---

# Fusion 1 — Setup, Licence & Interface

> **Track hub:** [[01-Areas/Engineering/engineering-drawing/fusion/INDEX]]
> **You already have Fusion downloaded** (2026-10-02) — this page covers claiming the licence and getting oriented.

---

## 1. Claim the free Education licence first

You are a BTech student, so the **Education plan** is the right route. Do this **before** you start modelling — the app runs in a limited/viewer state without it, and you can lose work in that state.

| Route | Cost | Features | Catch |
|---|---|---|---|
| **Education** ✅ | **Free** | **Full** | **1 year, renewable annually**; school-email verification |
| Personal use | Free | **Reduced** | 3-year term; non-commercial; revenue cap |
| Commercial | $85/mo · $680/yr · $2,040/3yr | Full | **No perpetual licence** |

**Steps:**

1. Open the Autodesk Education products page, sign in with your **school email address**.
2. Complete student-status verification (documentation may be requested).
3. Choose **Autodesk Fusion**, download the installer, install, sign in.
4. Fusion detects the licence type automatically on first launch.

> ### 🔔 Set a renewal reminder now
> Autodesk emails **30 days before expiry**, but that notice is easy to miss. Education access **must be renewed every year** or access stops. Put a recurring calendar reminder in for ~1 month before your anniversary. Renewing is a few minutes; losing a licence mid-project is not.

**You do not need any paid extension.** Machining, Product Design, Simulation, Nesting & Fabrication, Additive Build and Generative Design are separate paid add-ons (~$495/user/year, 14-day trials). Base Fusion already covers modelling, rendering and **3D-print preparation** — which is all this track needs.

---

## 2. Desktop app or browser?

Fusion runs on **Windows, macOS and a browser**. For this thread, use the **desktop app** for modelling and treat the browser as the fallback.

| | Desktop app | Browser |
|---|---|---|
| Works | Windows · macOS | any device with a browser |
| Heavy parts | full performance | may be slower on complex assemblies |
| Good for | everything in this track | viewing, sharing, quick edits away from your machine |
| Installs | yes | nothing |

**The browser route is the genuine differentiator** — if you ever want to check a model from a machine that isn't your main one, you can, without installing anything.

---

## 3. First launch — orient before you model

Fusion's interface **looks** different from SolidWorks, but the underlying paradigm is identical. This mapping is the fastest way to transfer what the SolidWorks track taught you:

| SolidWorks habit | Fusion equivalent | Watch out for |
|---|---|---|
| FeatureManager design tree (left) | **Browser** (left) | Fusion folds operations into *components* in the tree — read it before assuming |
| Sketch → dimension | Sketch → **constraint dimensions** | Fusion is *more* constraint-driven; expect to be asked to fully-define |
| Boss-Extrude / Revolve / Sweep / Loft | **Extrude / Revolve / Sweep / Loft** (same names) | the truest part of the mapping |
| FilletChamfer dress-up | **Combine → Fillet / Chamfer** | Fusion often nests these under a *Combine* operation |
| Linear/circular pattern | Pattern (linear/circular) | similar |
| Configuration | **Configuration table** on a component | Excel-embeddable — powerful, learn later |
| Design table / equations | **Equations** (a real equation editor) | worth learning early, see §5 |
| Export STEP / STL | Export STEP / **3MF** / STL | **3MF is the one you want** for printing |

**Three things that will trip you on day one** (`TBC` — confirm against your build):

1. **The Browser tree groups by component, not a flat feature list.** A feature you expected at top level may be nested inside another component. Don't panic; expand and look.
2. **Constraining philosophy is stricter.** A sketch that is *visually* right but not *fully defined* will be flagged, and Fusion will often refuse to build the feature until it's constrained. That is deliberate — it catches the errors SolidWorks lets slide.
3. **Operation history is less visible.** If you need to see or roll back what a parameter did, look for the ability to suppress/roll back on the operation itself.

---

## 4. Units — set them deliberately

Fusion defaults to **millimetres**. Most 3D-printing workflows and every Arduino/robotics part in this track are metric, so **mm is usually right** — but confirm rather than assume, because a unit mismatch silently scales a whole assembly.

**Sanity check before your first real part:** draw a 10 mm cube and confirm it measures 10 mm, not 10 inches or 100 mm.

---

## 5. Set up one thing before your first part: equations

If you learn one non-obvious thing on day one, make it this. Fusion has a real **equation editor**, so dimensions can be *driven* rather than typed:

- Put `wall = 2.5` (mm) in as a named variable
- Reference `wall` in every thickness dimension
- Change `wall` once → the whole part updates

**Why it matters here:** your parts are *iterative* — a sensor mount gets redesigned three times as the sensor changes. Anything you typed as a literal number three times is three chances to forget to update it. Fusion lets **component count** be driven too (`floor(len / pitch)`), which is the trick the SolidWorks track uses repeatedly.

---

## 6. Verification checklist before project 1

Do these in order — each one catches a class of mistake that is expensive later:

- [ ] Education licence active, **renewal reminder set**
- [ ] Units confirmed (mm expected)
- [ ] Can navigate: orbit, pan, zoom, and select a face
- [ ] Can create a sketch on a plane and add a constrained dimension
- [ ] Can extrude that sketch into a solid
- [ ] Can fillet an edge
- [ ] Can export **3MF** and open it in your slicer
- [ ] Can run the model **Check** tool and read the result
- [ ] Can save to a local folder (not only the cloud) — **do not work only in-browser**

---

## Next

**Project 1 — the sensor-mount bracket.** It forces the fundamentals: fully-defined sketch, extrude, fillet, and a hole pattern. Start it once §6 is complete. Full project list in the track hub §5.

Then the pending pages: **sketch mastery → part workflow → 3D printing → project ladder.**

---

## Cross-References

- **Track hub (scoping, licensing, project ladder):** [[01-Areas/Engineering/engineering-drawing/fusion/INDEX]]
- **SolidWorks equivalent for the same habits:** [[01-Areas/Engineering/engineering-drawing/solidworks/sketch-mastery]] · [[01-Areas/Engineering/engineering-drawing/solidworks/part-assembly-drawing-workflow]]
- **Printing guidance already in the vault:** [[01-Areas/Engineering/engineering-drawing/solidworks/surfacing-methodology]] §1 and §10 (Check tool, orientation, support avoidance, hole coupons)
- **Course hub:** [[01-Areas/Engineering/engineering-drawing/overview]]

*Created 2026-10-02. Licensing and platform facts verified against Autodesk's own pages; interface details are `TBC` and should be corrected in place as you work through them.*