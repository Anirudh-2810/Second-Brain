---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Workshop PPTs Merged"
date: 2026-09-23
description: "Build workflow taught properly in simple words from Workshop PPT (45 pp) + WORKSHOP PPT 2021 (67 pp): history, classifications, 5-step design process, wing numbers, avionics to first flight."
tags: [btech, aeromodelling, workshop, build-process, design, avionics, team-onyx]
last_updated: "2026-09-24"
confidence: medium
---

## For future agent
Full teaching ingest of `raw-sources/Workshop PPT.pdf` (45 pp, classic deck) and `raw-sources/WORKSHOP PPT 2021.pdf` (67 pp, expanded deck). Style contract (owner ask 2026-09-24): teach like [[aerodynamics-foundations]] — tables, daily-life examples, memory tricks, interview-trap lines, self-check. ~70% overlap by design; one build flow kept, 2021 deltas noted separately. Theory detail: [[aerodynamics-foundations]], [[wings-controls]]; chain detail: [[avionics-rc-stack]], [[esc-deep-dive]], [[propulsion-system-deep-dive]]; cheat sheet [[team-onyx-quick-revision]]; drill [[team-onyx-interview-mock-01]].

# Workshop PPTs — Merged Build Flow (simple words)

> Parent hub: [[INDEX]] · Theory: [[aerodynamics-foundations]] · Chain: [[avionics-rc-stack]] · Bench: [[esc-deep-dive]] + [[propulsion-system-deep-dive]] · Cheat sheet: [[team-onyx-quick-revision]] · Drill: [[team-onyx-interview-mock-01]]
> How to use this page: read each heading slowly. Every hard word has a daily-life example. Lines starting with **INTERVIEW:** are the exact traps interviewers love.

## 1. Which deck is which (30 seconds)

- **Classic `Workshop PPT.pdf` (45 pp):** the tight story — history, aircraft gallery, classifications, stability and control, parts, aero intro, and the 5-step design process in clean slide order. Read it for the BUILD order.
- **2021 deck (67 pp):** the same spine PLUS the modern era (alternative fuels, zero-carbon aim), fuller aero derivations, the camber family, constant-speed vs ground-adjustable props, and a full propeller/battery/ESC/Tx-Rx/servo chapter with diagrams. Read it for the AVIONICS chapter.

Same forces, same Bernoulli, same drag types in both — learn once, cite either.

## 2. History in 4 lines (enough colour for any interview)

1. **da Vinci** dreamed it — drew flying machines centuries early, never built one that flew.
2. **Cayley (1853)** built the first real glider — proved wings can carry a person.
3. **Lilienthal** jumped off hills in gliders — proved humans can control a wing, died trying.
4. **Wright brothers (17 Dec 1903)** flew the first powered, controlled flight — the birthday of aviation.

Gallery names to drop if shown pictures: An-225 (biggest ever), A380 (biggest passenger), B-2 (flying wing, stealth), F-35 (modern fighter), Concorde (supersonic passenger, with Tu-144 as its Soviet twin).

**Memory trick:** "Dream (da Vinci) → Glide (Cayley) → Jump (Lilienthal) → Fly (Wright)."

**INTERVIEW:** "First powered flight?" → Wright brothers, 17 December 1903. "First glider?" → Cayley, 1853.

## 3. Classifications — sort any plane in one breath

Planes are sorted on fixed axes. Learn the axes, not the list — then you can classify any plane they name:

| Sorted by | Buckets | Example |
|-----------|---------|---------|
| **Use** | passenger / cargo / military | A380 / An-225 / F-35 |
| **Weight vs air** | lighter-than-air (aerostats: balloons, airships) vs heavier-than-air (everything with wings) | hot-air balloon vs Cessna |
| **Wing count** | monoplane (1) / biplane (2) / multiplane (3+) | Cessna 172 / vintage stunt biplane |
| **Landing** | land / sea (floats) / amphibious (both) | normal / seaplane / amphibian |
| **Wing mount** | low / mid / shoulder / high / parasol (above body on struts) | racer / fighter / cargo / bush plane / parasol classic |
| **Stability tilt** | dihedral (up = stable, auto-levels) vs anhedral (down = agile, turns fast) | trainer vs fighter |
| **Speed** | subsonic (< Mach 1) / supersonic (> Mach 1) / hypersonic (> Mach 5) | airliner / Concorde / X-43 |
| **Wing motion (2021)** | fixed wing vs rotary wing (spinning blades) | Cessna 172 vs V-22 Osprey |

**Memory trick:** "Use-Weight-Wings-Landing-Mount-Speed" — six axes, pick any two and sound expert.

**INTERVIEW:** "Classify a seaplane fighter?" → military use, heavier-than-air, sea landing, pick mount/speed from the picture. They test the AXES, not memory.

## 4. The 5-step design process — memorise in order

This is the "walk me through a build" answer. Like cooking: recipe first, then ingredients, then taste-test. Never skip, never reorder:

1. **Problem statement** — write what the plane must do (payload, speed, flight time). Like writing the recipe name before cooking: "slow trainer that carries a camera for 10 minutes."
2. **Airfoil selection & analysis** — pick the wing's side-view shape and study it. Curved (cambered) for lift at low speed, mirror-flat (symmetrical) for tails that must not pull on their own. Like picking the right knife before chopping.
3. **Wing configuration & dimensions** — decide size and shape: span, area, rectangular vs tapered, low vs high mount. This fixes how much lift you get.
4. **Empennage configuration & dimensions** — empennage = the whole tail assembly (fin + elevators + their supports) sitting behind the body. Size it to keep the nose pointing where you want.
5. **Stability & control check** — verify it flies straight when you let go and turns when you ask. Dihedral for auto-level, decalage gap for pitch mood ([[airplanes-for-juniors-foundations]] §5), control surfaces sized to overpower gusts.

Wing numbers you must be able to name (one line each):

| Number | Meaning in plain words |
|--------|------------------------|
| Incidence / AoA | tilt between wing and incoming air; past ~16° it stalls |
| Aspect ratio | span² ÷ area — long-skinny = efficient |
| Taper ratio Ct/Cr | tip chord ÷ root chord — how much the wing narrows |
| Sweep | how far back the wing slants — for fast flight |
| MAC | mean aerodynamic chord — the "average" chord; on a rectangular wing it just equals the chord |
| Efficiency L/D | lift ÷ drag — higher glides farther |

**Memory trick:** "Problem, Profile (airfoil), Planform (wing), Posterior (tail, ha — empennage), Prove-it (stability)."

**INTERVIEW:** "Walk me through designing a trainer" → recite the 5 steps, then say: cambered airfoil, high wing with dihedral, generous tail, then stability check. Done in 60 seconds.

## 5. Aero recap — one paragraph per force (detail in [[aerodynamics-foundations]])

- **Lift** acts perpendicular to the airflow, through the centre of pressure. Amount = dynamic pressure × wing area — so it grows with air density, wing size, and velocity SQUARED (double speed → quadruple lift, same ×4 rule as [[airplanes-for-juniors-foundations]] §1).
- **Weight** = empty plane + payload + fuel/battery. Climb rule from the 2021 deck: thrust ÷ weight (F/W) > 1 accelerates you straight up.
- **Thrust** = propulsion reaction (air shoved back, plane pushed forward) — full story in [[propulsion-system-deep-dive]].
- **Drag** acts parallel, opposing motion: skin-friction (rubbing), induced (the price of making lift — wingtip vortices), interference (where parts meet), wave (shock waves at high speed).
- **Flaps:** same flap, two jobs — extra LIFT for take-off, extra DRAG for landing slowdown.

**INTERVIEW:** "F/W > 1 means what?" → the plane can accelerate vertically upward.

## 6. Avionics chain to first flight (the 2021 chapter)

Battery ladder — oldest to newest: lead-acid → NiCad → NiMH → Li-ion → **Li-poly**. LiPo wins on energy per gram, thinness, low resistance, free shape, long cycle life (brick phone → smartphone, same story as [[propulsion-system-deep-dive]] §5).

Then the chain you already know: battery → ESC (with BEC/UBEC/SBEC/LBEC family — [[esc-deep-dive]] §4) → motor → prop; sticks → transmitter → modulation → radio → receiver → servos + ESC. Servo = precise angle/velocity motor for flaps and gear.

The deck's last slide is the **final-connections checklist**: every plug seated, control directions correct (right stick = right roll), propeller tight, battery strapped, range check done — then first flight. In interview words: "I never skip the pre-flight: surfaces, screws, straps, signal."

**INTERVIEW:** "Walk final connections" → battery → ESC → motor + Rx; Rx → servos + ESC throttle lead; verify directions, straps, range — then fly.

## 7. 2021 deltas — three to cite if asked what changed

If they ask "what's new in the 2021 deck", name any three: zero-carbon future aim; ethanol/electric/solar prototype aircraft; MAC in integral form; camber family (low/deep/symmetrical/cambered); constant-speed vs ground-adjustable props; LiPo intercalation chemistry line; BEC family table; emoji Tx/Rx/servo walkthrough.

## Quick self-check (answers in [[team-onyx-quick-revision]])

1. Recite the 5-step design process without looking.
2. Classify a floatplane fighter on three axes.
3. First powered flight — who, when? First glider — who, when?
4. F/W > 1 means what, in one line?
5. Name the 6 wing numbers in one breath each.
6. Walk final connections: battery → ? → ? → ? → air.
7. Name three 2021-deck additions.
