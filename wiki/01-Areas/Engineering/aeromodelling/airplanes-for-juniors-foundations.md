---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Juniors Book Foundations"
date: 2026-09-23
description: "Interview-grade ideas taught properly in simple words from Understanding Airplanes for Juniors (135 pp): dynamic pressure, vortices, drag ladder, turn balance, decalage, tube structures."
tags: [btech, aeromodelling, aerodynamics, drag, stability, structures, team-onyx]
last_updated: "2026-09-24"
confidence: medium
---

## For future agent
Teaching extract of `raw-sources/Understanding Airplanes for Juniors.pdf` (135 pages, Bernardo Malfitano 2018, image-heavy). Style contract (owner ask 2026-09-24): teach like [[aerodynamics-foundations]] — full explanations, daily-life examples, worked numbers, memory tricks, interview-trap lines, self-check. NOT a transcription — keeps the interview-grade extras the book adds beyond the Round-1 pages. Parts map: P1 lift & wings → [[aerodynamics-foundations]]; P2 drag → [[wings-controls]] + §3 below; P3 balance/stability/controls → [[wings-controls]] + §§4–5 below; P4 weight & structures → §6 below. Cheat sheet [[team-onyx-quick-revision]]; drill [[team-onyx-interview-mock-01]].

# Juniors Book — Foundations, Taught Properly (simple words)

> Parent hub: [[INDEX]] · Core theory: [[aerodynamics-foundations]] · Controls: [[wings-controls]] · Cheat sheet: [[team-onyx-quick-revision]] · Drill: [[team-onyx-interview-mock-01]]
> How to use this page: read each heading slowly. Every idea has a worked number or a daily-life example. Lines starting with **INTERVIEW:** are one-breath answers for "explain simply" probes.

## 1. Dynamic pressure — why speed matters SQUARED

Dynamic pressure (call it q) is the punch the moving air carries. Formula: q = ½ × density × velocity². The ² is the whole lesson: **double the speed → QUADRUPLE the push.**

Worked numbers (density and ½ stay same, so just square the speed):

| Speed | Speed² (proportional push) |
|-------|---------------------------|
| 10 m/s | 100 units of push |
| 20 m/s (×2) | 400 units (×4) |
| 30 m/s (×3) | 900 units (×9) |

Daily-life version: walking in rain barely wets your shirt; cycling in the same rain stings your face. Same rain, squared pain. That is why take-off and landing speeds are the whole game, and why lift, drag, and control authority all "explode" with small speed changes.

Since lift = q × wing area, this one rule explains half of aeroplane behaviour. Quote it whenever small speed changes come up.

**INTERVIEW:** "Why do small speed changes matter so much?" → dynamic pressure grows with velocity squared — double speed, quadruple lift AND drag.

## 2. Vortices — where wingtip swirls come from

Hold a flat plate edge-on to the wind: air flows clean past both sides, no drama. Now tilt it: the bottom side has high pressure, the top has low pressure, and at the EDGES the high-pressure air spills over to the low side and rolls into a spinning tube — a **vortex** (plural: vortices).

Daily-life version: water spilling over the edge of a dam curls into swirls below. Same spill, same curl, in air.

On a real wing this happens at the WINGTIPS: high-pressure air under the wing leaks around the tip to the low-pressure top and trails behind as two long swirls. Those swirls carry energy away — and that lost energy IS **induced drag** (the price of making lift). Long skinny wings (high aspect ratio) leak less per unit lift, which is exactly why gliders look like they do.

**Memory trick:** "Tilt it → spill it → swirl it → pay for it (induced drag)."

**INTERVIEW:** "What is induced drag, in one breath?" → wingtip vortices: high-pressure air spilling over the tips, the unavoidable price of making lift.

## 3. The drag-reduction ladder — three fixes in order

Every drag fix in the book climbs one ladder. Say it in order — "clean it, stretch it, thin it":

| Step | Fixes which drag | What you do | Example from the book |
|------|-----------------|-------------|----------------------|
| 1. **Clean the shape** | separation drag (air peeling off, messy wake) | streamline everything, delay separation | the 737-to-F-104 comparison set — smooth bodies stay attached |
| 2. **Stretch the wing** | angle-of-attack drag (cost of lift at tilt) | raise aspect ratio: span ÷ average chord, long and skinny | gliders — huge span, tiny chord, sips drag |
| 3. **Thin the section** | wave drag (shock waves near sound speed) | thin wings first, then sweep and area-ruling as speed climbs | P-80 → F-104 lineage — thinner, sharper, swept |

Daily-life version: a cyclist tucks low (clean), uses deep aero wheels (stretch the idea), and wears a sharp aero helmet for speed runs (thin). Same ladder, on a bicycle.

Note how step 2 reuses your aspect-ratio knowledge from [[wings-controls]] — the book is just showing you WHY long wings pay less for the same lift.

**INTERVIEW:** "How do you cut drag?" → ladder order: streamline the shape, stretch the aspect ratio, thin and sweep for speed. Never answer with just one.

## 4. Turn balance — why we bank

Fly straight: lift points straight up, balancing weight. Now you want to turn. If you just push the rudder, the plane skids sideways like a car on ice — nose points one way, body slides another. That sideways slide is a **skid** (or slip, other direction).

Instead, BANK: tilt the whole lift vector sideways. Part of lift still holds you up, part pulls you around the turn. Tighter turn → more bank needed, so that gravity + the turning push still combine into one arrow pointing straight down through your seat. When that arrow lines up with the plane's floor, the turn is **coordinated** — no skid, no slip, passengers feel "down" as normal.

Daily-life version: cycling around a corner you lean in — same lean, same reason. Lean too little and you slide wide; the book's rule just puts numbers on your bicycle instinct.

**Memory trick:** "Bank it to turn it; line up the seat-arrow to clean it."

**INTERVIEW:** "Why do planes bank to turn?" → tilting lift sideways pulls the plane around; coordinated when the combined force points straight through the seat — rudder-only turns skid.

## 5. Decalage — the wing-tail angle gap that sets the mood

Decalage = the difference in tilt (incidence) between the main wing and the tailplane. This small gap decides the plane's whole pitch personality:

| Gap | Personality | Simple meaning |
|-----|-------------|----------------|
| Too small | twitchy, nervous | sneezes at every gust, needs constant correction |
| Just right | stable, hands-off | flies straight when you let go — the trainer feel |
| Too big | over-stable, sluggish | refuses to pitch, mushy nose, fights your elevator |

Daily-life version: like the gap between bicycle handlebar looseness settings — too loose wobbles, just right steers itself straight, too tight won't turn.

Name this rule when asked what makes a model hands-off vs twitchy — it connects straight to the stability step of the design process ([[workshop-ppts-merged]] §4).

**INTERVIEW:** "What makes a model stable vs twitchy in pitch?" → the decalage gap between wing and tail incidence: right gap = stable, too close = twitchy, too much = sluggish.

## 6. Tube structures — cheap stiffness before composites

Problem: a fuselage or tail boom must be stiff but light, and carbon fibre costs money. The book's answer: the **welded steel tube truss** — a skeleton of thin tubes joined in triangles.

Why triangles? A triangle cannot squash without stretching a side; a square folds flat with a push. So a truss of triangles gives huge stiffness per gram of steel. Lots of height and length, very little material, cheap to weld in a workshop.

Daily-life version: bamboo scaffolding around Mumbai buildings — thin poles, triangle joints, holds workers many floors up. Same engineering, different material.

Cite this when asked how to build light AND stiff on a student budget — it shows you think in structures, not just parts.

**INTERVIEW:** "Light but stiff fuselage on a budget?" → triangulated steel-tube truss: maximum stiffness per gram before composites.

## Quick self-check (answers in [[team-onyx-quick-revision]])

1. Speed ×2 → dynamic pressure ×? Speed ×3 → ×? Show with numbers.
2. Where do vortices come from, in one sentence? What drag do they cause?
3. Name the three drag fixes in ladder order, with one example each.
4. Why bank instead of rudder-only? What is a coordinated turn?
5. What does the decalage gap control? Describe all three moods.
6. Why triangles in a tube truss?
