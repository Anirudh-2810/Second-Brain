---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - guided project briefs"
tags: [btech, engineering-drawing, solidworks, cad, projects, simulation, testing, portfolio]
last_updated: "2026-09-12"
description: "Six guided SolidWorks project briefs (quadcopter, gearbox, gripper, bottle mold, enclosure, reverse-engineered mouse), each with roadmap, efficiency playbook, validation ladder, and simulation sandbox."
module: "engineering-drawing"
prerequisites: [["flowcharts-master"], ["solidworks-cheatsheet"], ["INDEX"]]
confidence: high
---

# SolidWorks Project Ideas (Six Guided Briefs)

## For future agent
Capstone practice spine. Six 1–2k-word briefs, each self-contained: goal, ordered feature roadmap, efficiency playbook, testing/validation ladder, simulation sandbox. Assumes the full module as background (links per brief). Simulation content covers built-in entry tools (SimulationXpress static, Motion kinematics, plus awareness-level pointers to full Simulation/Flow) — TBC: exact license availability varies (student/EDU vs commercial); everything here targets what's reachable on a student setup.

> **How to run these:** one brief at a time, in order — each reuses the previous brief's skills and adds one new discipline. Log hours, screenshots, and failures in your daily note; every brief ends shippable (files + drawing + render).

---

## The universal brief template (read once)

Every brief below follows: **Goal** (what + why it matters) → **Roadmap** (ordered features/parts) → **Efficiency** (design-intent + speed moves) → **Validation ladder** (tests in order — sketch → geometry → assembly → drawing) → **Simulation sandbox** (what to analyze + what the numbers mean) → **Ship checklist** (files, drawing, render, portfolio line).

**Efficiency rules shared by all six:**
1. Layout/master sketch FIRST — every mating dimension flows from one sketch.
2. Fully-defined sketches, symmetric halves mirrored, patterns over copies.
3. Feature order: big shapes → functional → dress-up last; rollback-bar test after each stage.
4. Configurations: working (simplified/fast) vs detailed (full) vs presentation.
5. Name everything; mass-properties window open during assemblies (weight/units truth).

---

## Brief 1 — Quadcopter frame + landing gear (~1.5k words of work)

**Goal:** a flyable 5-inch-class (TBC: size to your motors/props — confirm with flight references) X-frame with center stack, motor mounts, battery bay, landing gear, and camera mount. Why: your drone-team currency — every decision here transfers to team hardware.

**Roadmap:**
1. Layout sketch (top view): arm angles (X = 90° symmetric), motor-center distance from prop diameter + clearance rule (props must not overlap: center distance > prop diameter + margin — TBC exact margin per safety practice), stack hole pattern (30.5×30.5 mm standard — TBC: confirm current FC/ESC mounting standards).
2. Bottom + top center plates: extruded flats with pocketing (lightening cutouts that keep stiffness — ribs-by-subtraction thinking).
3. Arms (4×, one part patterned): tapered plates, motor-mount hole pattern at tips, wire-routing slots.
4. Standoffs (bought-out envelopes), battery pad + strap slots, landing gear (bent wire or printed legs — model envelopes + mounts), camera/gimbal plates (TBC per payload).
5. Fastener plan: M3 pattern library (screws + nuts + standoffs as envelope parts), assembly with concentric/coincident mates.
6. Drawing set: plate DXFs for cutting (carbon/FR4 — TBC: confirm cutter capability with your fab source), hardware BOM.

**Efficiency:** one arm part → circular pattern in assembly (not 4 modeled arms); plate pockets as one patterned cut; equations drive prop-clearance (change prop size → mounts move, not rebuild).

**Validation ladder:** sketch diagnostics → plate flat-pattern/DXF sanity → assembly interference (props vs arms vs battery through full tilt — rotate-check) → mass rollup vs thrust margin (target ≈ 2:1 thrust:weight for agility — TBC: confirm with flight references) → fastener count vs BOM → drawing review (hole callouts match bought hardware).

**Simulation sandbox:** SimulationXpress static on ONE arm (cantilevered at root, motor-thrust load at tip — TBC: use max thrust per motor datasheet): read max stress vs material yield + deflection at tip (deflection changes prop plane — stiffness matters more than strength here). Compare solid vs pocketed arm: weight saved vs deflection gained — the engineering tradeoff, quantified. Motion study (awareness): landing-gear impact is dynamic — hand-calc energy + static-equivalent load is the student-level approximation (TBC: flag as approximation, not analysis).

**Ship:** plates DXF + printed-mount STLs + assembly + BOM + hero render + one-line portfolio entry.

## Brief 2 — Single-stage spur gearbox, buildable (~1.5k words)

**Goal:** a 1:3 reduction box you could actually assemble on the bench (3D-printed gears + hardware-store shafts/bearings). Why: the PL2 template made physical — ratio math, fits, and assembly order stop being abstract.

**Roadmap:**
1. Ratio math on paper: teeth (e.g., 16 → 48), module from printability (≥ ~1 mm module prints reliably on FDM — TBC: confirm with your printer), center distance $a = m(z_1+z_2)/2$.
2. Gears: revolved blanks + circular-patterned tooth cuts + bore + keyway + hub/set-screw.
3. Shafts: stepped profiles, shoulders, circlip grooves (TBC: or shaft collars for printed builds — simpler, confirm per build).
4. Bearings: 608-class skate bearings as envelope parts (cheap, available — TBC per sourcing), seats modeled to slip fit (printed bores shrink — TBC: calibrate with test prints, typically +0.2–0.3 mm allowance, confirm per printer/filament).
5. Housing: two printed halves split at the shaft plane + feet + cover bolts + input/output windows; ribs at bearing seats.
6. Assembly: gear mate with ratio → hand-rotation check → exploded view + BOM + print list (orientation + supports plan per part — TBC per slicer).

**Efficiency:** layout sketch with center distance equation-driven (change teeth → shafts/housing follow); one gear-tooth cut patterned (never model 48 teeth); hardware as envelope library reused across briefs.

**Validation ladder:** ratio math → center-distance check → gear-mate rotation (output = input ÷ 3?) → interference through FULL rotation (teeth must clear!) → backlash eyeball (must not touch both flanks — TBC: printed gears need generous backlash, confirm by test) → bench test: input RPM vs output RPM counted by hand/mark.

**Simulation sandbox:** Motion study with the gear mate: plot output speed vs input (verify 1:3 on the graph, not by eye); contact-force awareness (full contact analysis is pro-Simulation territory — TBC depth). Torque thought-experiment: stall the output by hand-feel (qualitative), note which part flexes first — that flex location is your redesign target, and the habit of *looking for it* is the lesson.

**Ship:** STL pack + hardware list with sourcing links + assembly drawing + bench-test video/log.

## Brief 3 — Servo-driven 2-finger gripper (~1.2k words)

**Goal:** a linkage gripper (servo → linkage → parallel or angular jaws) for a robot arm or demo rig. Why: mechanisms — the first brief where parts MOVE relative to each other by design, and motion study becomes the test bench.

**Roadmap:**
1. Jaw-travel requirement (object size range → jaw stroke) → 4-bar/linkage sketch BLOCKS (layout sketch with movable links — solve the motion on paper/in-sketch first).
2. Base/palm plate, two jaw fingers (profiled tips — V-groove for round objects, flat with grip pads for boxes), linkage arms, servo mount + horn interface (servo spline/horn dimensions to your servo datasheet — TBC per model).
3. Pivots: shoulder screws/pins as envelope hardware + modeled bores with clearance (pivots must rotate freely — TBC: printed bores + screws need calibrated clearance, confirm by test fit).
4. Assembly with hinge/limit mates → drag through full travel → check jaw parallelism (if parallel-link design) and no link collisions.
5. Grip pads (TBC: TPU print or rubber sheet — confirm per sourcing) + mounting flange to arm.

**Efficiency:** sketch-block linkage FIRST (an afternoon of sketch iteration beats a week of remodeling); one finger + mirror; link lengths equation-linked to jaw stroke.

**Validation ladder:** sketch-block travel (does the math close?) → interference through full travel (links vs palm at extremes!) → pivot clearance (free rotation, no slop that ruins repeatability — TBC: judge per application) → grip test on real objects (round/square/soft) → stall drew vs servo rating (don't burn the servo — TBC: check servo stall current vs supply).

**Simulation sandbox:** Motion study: jaw tip trajectory plot (is the path what you intended? parallel-closure proof for parallel designs); velocity/force transmission check at extremes (linkages go force-weak near toggle positions — TBC: read the force curve, redesign link ratios if the grip force collapses mid-travel). This is the brief where Motion stops being a toy and becomes a design tool.

**Ship:** STL pack + servo + hardware BOM + travel video + force notes.

## Brief 4 — Bottle + cap + mold split (~1.2k words)

**Goal:** a small bottle with гибели? no — with cap, threads, and a 2-part mold split demonstrating mold-readiness. Why: packaging DFM + the mold toolset (parting lines, shutoffs, draft) that industrial CAD interviews probe.

**Roadmap:**
1. Vessel: 4-zone profile (base/body/shoulder/neck per [[bottles-containers]]) → revolve → shell/thin to wall thickness.
2. Neck finish to cap spec (TBC: pick a real finish standard like 28-400 from packaging references — model threads as cosmetic or modeled per [[bottles-containers#3-caps-closures-threads]]).
3. Cap as separate part (knurl cosmetic — TBC) + seal interface + assembly with section/interference check.
4. Draft analysis → add release taper to all vertical walls (TBC: 1–3° typical, confirm per molder).
5. Parting line + shutoff surfaces + mold halves (core/cavity split — awareness-level: full mold design with cooling/ejection is its own discipline, TBC depth): demonstrate Tooling Split on the bottle body, show core + cavity separating along the pull direction.

**Efficiency:** revolve-first (one profile drives everything); thread/cap dimensions from the neck (in-context), never independent; draft IN the base features where possible.

**Validation ladder:** profile fairness (combs) → wall uniformity (section) → cap fit (section + interference) → draft analysis all-green → parting line sensible (silhouette edge) → mold-half separation (no undercuts locking the pull — the pass/fail gate).

**Simulation sandbox:** drafts/undercut audit IS the analysis here (mold-release simulation-lite); wall-thickness analysis (sink-risk zones at thick-to-thin transitions — TBC: confirm sink rules with molding references); fill-pattern awareness (gate location thinking — pro Moldflow territory, TBC depth, but place a hypothetical gate and reason about weld-line positions).

**Ship:** bottle + cap + mold halves + section-view drawing + draft-analysis screenshots.

## Brief 5 — Sheet-metal electronics enclosure (~1.2k words)

**Goal:** a folded sheet-metal box for a single-board computer (mounting bosses? no — standoffs, ports, vents, lid). Why: sheet metal is the cheapest custom enclosure process on earth (laser/bend) — employable skill, same-week shippable.

**Roadmap:**
1. Board envelope + port positions (measure the real board — TBC per board) → box dimensions with clearance (TBC: ~2–3 mm typical internal clearance, confirm per assembly needs).
2. Base tub: base flange + edge flanges (Sheet Metal tools) → corner treatment (welded vs folded tabs — TBC per shop).
3. Lid: separate part with return flanges + fastener pattern (quarter-turn or M3 — TBC per look/cost).
4. Cutouts: port windows, vent slots (patterned), LED holes, cable glands — all BEFORE flat pattern, cut features only (never model vents as solids!).
5. PEM/standoff provisions (TBC: self-clinching hardware needs vendor specs — confirm datasheets, model pilot holes only).
6. Flat pattern check per part (must unfold cleanly — THE manufacturability gate) → DXF export → bend table/notes on drawing.

**Efficiency:** gauge table + bend parameters set once (TBC: K-factor/bend deduction to YOUR shop's tooling — ask them, don't guess); symmetric flanges mirrored; vent pattern once, mirrored.

**Validation ladder:** board fit (section + interference with ports aligned!) → flat-pattern unfolds with no distortion → bend radii ≥ shop minimum (TBC per shop) → lid closes with fastener alignment → drawing carries bend notes + finish (powder-coat — TBC per vendor).

**Simulation sandbox:** flat-pattern + bend-sequence review IS the analysis (can it be cut from one sheet? how many setups? — cost thinking); stiffness sanity: lid flex by hand-feel reasoning + rib/hem additions where it oil-cans (TBC: thin-sheet oil-canning is real — hems and beads fix it, confirm per build); thermal awareness: vent area vs heat load (rule-of-thumb stage — TBC: confirm with thermal references for real products).

**Ship:** DXFs + hardware list + assembly + BOM + flat-pattern drawing + cost quote from a laser shop (real number = real lesson).

## Brief 6 — Reverse-engineered mouse, surfacing capstone (~1.5k words)

**Goal:** your daily mouse, rebuilt as a two-shell surfacing model with buttons, wheel, and PCB standoffs. Why: the capstone — ergonomics, knit/thicken, parting lines, assembly, presentation. Portfolio hero.

**Roadmap:**
1. Caliper survey: length/width/height/crown position + photos front/side/top with ruler (reverse-engineering per [[artistic-organic]]).
2. Top shell: 3 profiles + center-ridge guide → lofted/boundary → trim at parting line → thicken inward.
3. Bottom shell + internal bosses (PCB + battery bays to measured positions — TBC per mouse) + ribs.
4. Buttons (separate parts, consistent gaps — TBC: ~0.3–0.5 mm typical) + wheel (revolve + axle + encoder envelope — TBC per part) + side grips (freeform tweaks).
5. Assembly + interference + section checks; appearances + studio render; zebra proof screenshots.

**Efficiency:** symmetric half + mirror for the base shell (asymmetric details after); parting-line curves defined ONCE and shared by both shells; wheel/button envelopes block out space before shell detailing (packaging-first, styling-second).

**Validation ladder:** caliper-vs-model spot checks (5+ dimensions within ~0.5 mm — TBC tolerance per goal) → knit/thicken clean → parting-line continuity (shells meet!) → buttons actuate without binding (travel + clearance) → wheel spins free → zebra smooth on top skin → render + fairness proof.

**Simulation sandbox:** drop-test thought experiment (awareness: real drop sim is explicit-dynamics territory — TBC depth): identify likely failure points by reasoning (thin button hinges, shell screw posts) + reinforce with ribs/fillets; wall-thickness audit (uniform 2-ish mm — TBC per process); assembly-tolerance stack review (worst-case gaps vs best-case — the DFM habit).

**Ship:** shells + internals + assembly + BOM + hero render + zebra proof + one-paragraph technique writeup ("lofted shell, mutual trim, inward thicken, split-line buttons" — skills, not tutorials).

---

## Ship standards (all briefs)

- Files: parts + assembly + drawing (+ DXF/STL where applicable), named, no dead features.
- Drawing: views + critical dims + notes a shop could quote from.
- Proof: one render + one analysis screenshot + rebuild test (change a driving dim, confirm clean).
- Log: daily-note entry with hours, failures, and fixes — failures documented are the portfolio's hidden value.

---

## Simulation reading guide (what the numbers MEAN — all briefs)

Beginners either worship or ignore FEA colors. Neither is engineering. How to read entry-level results:

**SimulationXpress static (Briefs 1, 3, 4-adjacent):**
1. Mesh first, sensibly coarse (converge LATER — first run answers "where," not "how much").
2. Read LOCATION first (red zone = redesign target), magnitude second.
3. Compare against yield with a factor of safety ≥3 for static student work (TBC: confirm with machine-design references — FoS covers your load-guesses, mesh coarseness, and material variation all at once).
4. Deflection often matters more than stress (drone arms, press beds, gripper jaws) — read displacement plots with the same seriousness.
5. Refine mesh once around the peak: if the number barely moves, trust it; if it jumps, your mesh was lying (convergence check — TBC depth, but the concept is non-negotiable).

**Motion kinematics (Briefs 2, 3):**
1. Plot FIRST (trajectories, speeds, ratios) — graphs over eyeballing, always.
2. Check extremes of travel (toggle/lock positions, interference at ends — the failures live at extremes, never mid-stroke).
3. Force curves: collapsing mechanical advantage near a toggle = redesign the link ratios, not a bigger servo/motor.
4. Qualitative + quantitative pair: hand-feel/bench test AND the plotted numbers must agree — disagreement means the model lies somewhere (find it; that's the lesson).

**What entry tools CANNOT tell you (awareness, not discouragement):** fatigue life, impact/crash, vibration resonance, fluid flow, heat — these need full Simulation/Flow/explicit-dynamics (pro territory, TBC license depth). The student move: name the limitation in your notes ("static-equivalent approximation — TBC with dynamic testing"), never present colors as proof of what they didn't analyze.

## CROSS-REFERENCES
- [[INDEX]] · [[flowcharts-master]] · [[solidworks-cheatsheet]] · [[consumer-electronics]] · [[gearbox-fundamentals]] · [[bottles-containers]] · [[artistic-organic]] · [[presses-forming-drone]] · [[../cad-design-interview-prep]]

---

## Brief 7 — Line-following + obstacle-avoiding bot chassis (bonus: autonomy-ready platform)

**Goal (the software-meets-CAD bridge):** a small tracked/wheeled rover chassis with sensor mounts, such that control code has somewhere to live. Why: your RAI degree in one brief — mechanical platform + electronics bays + sensor geometry, the full robotics stack bottom layer.

**Roadmap:** wheel/track choice (wheels: simple + fast on flat; tracks: grip + climb curbs — TBC per terrain; model BOTH configs? — the §-config habit: one chassis, swappable running gear!) → motor + gearbox envelopes (gear-motor units bought — TBC per torque/speed calc from §-gearbox pages!) → chassis tub (battery + controller + wiring volumes FIRST per §8-envelope discipline!) → sensor mast positions (ultrasonic/IR/camera heights + fields-of-view modeled as CONES — TBC per sensor datasheets; blind zones visualized, not discovered!) → bumper + drop-sensor mounts (stairs kill rovers — TBC per testing!) → CAD consequence: electronics FIRST, chassis around (the §8-PCB lesson at vehicle scale!).

**Validation ladder:** mass + CG vs tip-over angles (ramps + curbs modeled as test ramps in CAD? — TBC taste: tip analysis on paper + real-ramp testing!) → sensor FOV clash (cones vs chassis through full steering — the §7-drone-prop-clearance habit generalized!) → drop/kerb impact reasoning (the §-simulation sandbox: static-equivalent + physical drops, TBC!) → wiring service loops at every articulation (the §9-slew-cable lesson!) → field test log (terrain × outcome × breakage — the failure resume earning robotics entries!).

## Brief 8 — Parametric phone-stand + desk-organizer family (bonus: first sellable product)

**Goal (design-for-listing in one weekend):** a phone stand that actually holds phones (angle + cable + stability!) extended into a S/M/L + accessory family. Why: the §8-first-gig appendix made concrete — a portfolio piece that can ALSO list on Etsy/college fest stalls (TBC per marketplace practice!).

**Roadmap:** phone envelope set (sizes + case thicknesses + cable plugs — TBC per current models; design to ENVELOPES, not one phone!) → viewing-angle + stability geometry (tip-over moment vs base footprint — TBC per physics; test with the heaviest phone + cable tug!) → cable routing channel (strain relief per the §9-appliance lesson!) → S/M/L configs via design table (the §8-config habit as product line!) → accessory modules (pen cup? watch dock? — the §12-platform thinking at desk scale!) → CAD consequence: print-orientation features (no-support angles per the §8-printing appendix! — flat backs, 45° rules, TBC!) + finish note (layer lines vs sanding vs filler — TBC per craft!).

**Validation ladder:** heaviest-phone tip test (physical! — CAD predicts, gravity judges!) → cable plug/unplug cycles (retention + wear — TBC per testing!) → wobble audit on real desks (felt pads modeled? — TBC!) → print-cost math (filament + time per unit — the §8-pricing inputs!) → listing photos (the §8-publishing anatomy: hero + proof + technique + failure + files!).

---

## Toolchain appendix (software + data that multiplies CAD)

**PDM thinking at solo scale (awareness — TBC: confirm with PDM references for team depth):** revision discipline per §-execution-protocols (REV + notes + revalidation — solo PDM is HABIT, not software!) → where-used tracking (which assemblies use this part? — the §10-file-hygiene folder habit + a spreadsheet beats memory past ~50 parts!) → release states (WIP vs REVIEW vs RELEASED folders — TBC taste; released files are READ-ONLY by convention, edits branch new REVs!) → the team-readiness payoff (solo habits that scale ARE team habits — PDM onboarding takes days not months when discipline pre-exists!).

**Interoperability pack (files that travel — TBC per receiving-system practice):** STEP AP214 (assemblies + colors travel — the default exchange!) → Parasolid (kernel-native for Siemens-shop flows — TBC per toolchain) → STL/3MF refined (print/export per [[surfacing-methodology]] §8, NOT dumb defaults!) → DXF/DWG flat + 3D PDF for shops without CAD (TBC per shop capability!) → the exchange checklist (units confirmed? + origin sane? + bodies named? + revision marked? — the §-ship-standards extended to EVERY file format!).

**Render + documentation toolchain (TBC per tool availability):** studio renders in-CAD (the §8-publishing hero shots!) → exploded-line diagrams (assembly instructions that customers actually follow — TBC per technical-illustration practice!) → video turntables + assembly animations (Motion studies DOUBLE as instructions — the §-simulation sandbox doing documentation duty!) → the single-source rule (renders/animations REGENERATED from live CAD, never frozen exports — stale visuals lie about current design!).

---

## Execution protocols (run every brief like a pro)

**Session structure (the 2-hour block that ships):** 10-min plan review (which steps? what could fail? — the pre-mortem!) → 90-min modeling sprints (phone away, ONE feature set per sprint — the §2-exercise timing discipline generalized) → 15-min verify (rebuild test + section + mass per the brief's ladder — NEVER skip; verification debt compounds!) → 5-min log (daily note: done/next/blocked + ONE trick kept — the §6-log-template habit). Four blocks a week finish any brief in a month alongside coursework (TBC per YOUR pace — the rhythm, not the calendar!).

**Stuck escalation (the §8-stuck-protocol applied to projects):** 15-min rule per feature (then log + sidestep to an independent feature — parallel progress beats serial suffering!) → module-page lookup (exact section, not rereading!) → daily-note parking lot (stuck items age into easy items overnight — TBC: confirm against YOUR log hit-rate!) → peer trade (swap trees with a friend per [[beginner-exercises]] §8-review — foreign eyes spot your blind assumptions in minutes!) → NEVER restart from scratch before the §7-reorder-surgery pass (archaeology first, rebuild last — restated because it hurts the most to skip!).

**Definition of DONE per brief (no partial credit):** files named + ordered (the §10-hygiene audit passed!) → rebuild test green (one driving-dim change, clean rebuild — the universal proof!) → drawing quoted-shoppable (views + dims + tolerances + notes + BOM — the §10-drawing discipline!) → render + proof screenshots (beauty + evidence — the §8-publishing pair!) → failure resume updated (the appendix-matrix habit — losses converted to assets!) → daily log closed (hours + score + next — the loop shut cleanly!). Six checks, all green, or it ships next session — standards compound faster than speed.

---

## Appendix: brief-selection matrix + 90-day arc (how to run all six)

**Which brief first (honest ordering for a beginner):** Brief 4 bottle+mold (surfacing fundamentals, low part-count, fast wins) → Brief 5 enclosure (sheet metal + flat-pattern confidence) → Brief 6 mouse (surfacing capstone — now you have the vocabulary) → Brief 2 gearbox (first assemblies with motion) → Brief 3 gripper (mechanisms + Motion analysis) → Brief 1 quadcopter (everything combined + weight discipline). Easiest-first builds compounding skill; hardest-last cashes it out. Total scope ≈ one solid academic term alongside coursework (TBC per YOUR pace — the arc, not the calendar, is the commitment).

**The 90-day arc (scope + order, per vault plan rules — no dates-as-promises):** foundation pages + L-bracket + bottle-half (the basics-setup → sketch → bottles chain) → Briefs 4+5 (shipped: DXFs + drawings + renders) → Brief 6 (portfolio hero #1) → Briefs 2+3 (motion literacy + bench-tested hardware) → Brief 1 (flying capstone + weight-budget proof) → publish-all + GrabCAD + club demo (the §8-publishing habit executed). Each stage's OUTPUT feeds the next stage's INPUT (enclosure sheet skills → drone plates; gearbox mates → gripper linkages; mouse surfacing → quadcopter canopy?) — the compounding is designed, not accidental.

**Failure resume (keep one — it outperforms a grade sheet):** every brief's §-validation failures logged with cause + fix + prevention ( stripped threads → torque discipline; jammed mesh → backlash budgeting; overweight frame → budget-first redesign). Interviewers and clients probe failures harder than successes — a failure resume with fixes demonstrates seniority that certificates can't. Start it with Brief 4's first stripped thread.
