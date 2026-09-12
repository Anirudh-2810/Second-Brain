---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - complex showcase builds"
tags: [btech, engineering-drawing, solidworks, cad, surfacing, helmet, advanced]
last_updated: "2026-09-12"
description: "Flagship complex builds from PL1: football helmet trilogy, marine propeller, SpaceX Dragon, washbasin, water taps, nozzles, lampshade, car door — multi-patch strategies and assembly thinking."
module: "engineering-drawing"
prerequisites: [["household-tools"], ["surfacing-methodology"], ["INDEX"]]
confidence: medium
---

# Complex Showcase Builds

## For future agent
PL1 flagship page: the hardest builds — helmet trilogy (#16–18), propeller (#15), SpaceX Dragon (#91), washbasin (#84), water taps (#39/#49), nozzles (#54/#55/#86), lampshade (#92), hair-dryer body (#93/#94), car door (#8), magician hat (#6), engraved text on sphere (#7), water tank + handle (#2/#26/#79), shower assemblies. Strategies inferred from titles + surfacing methodology (TBC per-video). This page teaches decomposition of scary models into patch plans.

> **The real lesson of this page:** no model is "advanced" — every showcase build is 5–10 beginner techniques sequenced well. Decompose first, model second. If a build intimidates you, you haven't decomposed it yet.

---

## 1. Decomposition method (applies to everything below)

```mermaid
flowchart TD
    A[Scary model] --> B[List regions of\nconsistent curvature]
    B --> C[Assign one technique\nper region]
    C --> D[Order: big shell →\nopenings → details]
    D --> E[Define seams on\nstyle/hidden lines]
    E --> F[Build → knit → thicken\n→ verify]
```

## 2. Flagship deconstructions

**Football helmet (#16–18, three parts) — the capstone of PL1:**
- Part 1: outer shell — boundary patches over crown/side zones, planned seams on ridge lines.
- Part 2: openings — visor + ear holes via trim with oversized patches first, edge roll (swept bead) around openings for stiffness + safety.
- Part 3: liner + details — offset-surface inner liner, chin strap mounts, vents. Multi-part thinking: shell/liner/hardware as separate bodies or parts.

**Marine propeller (#15):** one blade (lofted/boundary with twist from root to tip — pitch built into the profiles) → circular pattern → hub (revolve) → fillet blade roots (stress!). Blade pitch/rake/thickness distribution is naval architecture (TBC: this is CAD practice, not propeller design).

**SpaceX Dragon (#91):** capsule = revolve base + lofted shoulder + heat-shield base; SuperDraco pods as repeated lofted pods (pattern!). Symmetry + repetition turn a spacecraft into an exercise in planning.

**Washbasin (#84):** big sanitary ware — outer styling skin + inner bowl (offset!) + rim + drain hole + overflow (TBC if modeled). Ceramic reality: uniform walls, generous radii, no undercuts (mold/mandrel release).

**Water taps (#39/#49) + nozzles (#54/#55/#86):** spout sweeps + valve bodies + aerator threads; the plumbing lesson is standard interfaces (threads, seats) modeled to mate, not to look right solo.

**Lampshade (#92):** revolved/lofted shade + light-source clearance + heat awareness (incandescent vs LED changes everything — design context, not CAD).

**Car door (#8):** outer panel (large gentle curvature — boundary showcase) + window frame + handle recess + trim lines. Automotive panels demand C2 thinking ([[surfacing-methodology]]) — your zebra-stripe final exam.

**Magician hat (#6) + text on sphere (#7):** ruled/developable-ish surfaces (hat cone + brim) and text-wrapped-on-curved-face technique (split/project + emboss) — presentation-model skills.

**Water tanks (#2/#26/#79):** large vessels + handles + fittings (inlet/outlet bosses, lid threads) — the packaging-to-industrial bridge.

## 3. Multi-part discipline (showcase builds are assemblies in disguise)

- Separate bodies/parts per material and per manufacturing process (shell vs liner vs hardware).
- **Master-model technique (TBC depth):** drive multiple parts from one layout sketch/part so interfaces always agree — helmets and dragons stay consistent this way.
- Fasteners and bought-out parts (screws, vents, straps) as library components, not hand-modeled (model envelopes + mating features only).

## 4. Failure clinic (showcase scale)

| Symptom | Cause → Fix |
|---|---|
| 40-feature tree, afraid to touch anything | No decomposition plan → rebuild with region-per-feature-set order; name everything |
| Openings shatter the shell | Trimming across patch chaos → consolidate patches first, trim once, edge-roll after |
| Assembly interfaces mismatch | Parts modeled in isolation → master sketch or in-context references for every mating dimension |
| Zebra chaos on big panels | Too many sliver patches → rebuild zone with 2–3 large boundary patches |

---

## 5. Worked example: helmet shell patch plan (paper deliverable + build start)

Do the PAPER plan first (30 min) — regions, techniques, order, seams — then model Part 1 only. The plan is the graded deliverable.

**Paper plan (template — fill for YOUR helmet reference):**
| # | Region | Technique | Seams on |
|---|---|---|---|
| 1 | Crown center | Boundary (2 profiles × 2 guides) | Ridge style-lines L/R |
| 2 | Left/right sides | Boundary each, mirrored (model ONE side!) | Ridge lines + lower edge |
| 3 | Rear lower | Lofted transition to edge roll | Edge roll start |
| 4 | Visor opening | Trim (oversized shell first) | Opening curve + edge-roll bead |
| 5 | Ear recesses | Trim + small fill blends | Recess rims |
| 6 | Edge roll | Swept bead around full lower rim | Rim (functional seam, reads as design) |
| Order: 1→2→3 (knit as you go, staged) → 4→5 (trims) → 6 (bead) → zebra → thicken inward 3 (TBC: shell thickness per construction) |

**Propeller blade appendix (#15, numbers-first approach):**
1. Blade data: 3 blades, Ø300 (TBC illustrative), root chord 40 → tip chord 22, pitch angle 25° root → 12° tip (twist BUILT into profile orientations — TBC: real pitch follows hydrodynamic rules; this is CAD practice).
2. 4 sections (root/mid/tip + one intermediate) as rotated airfoil-ish profiles (flat-bottomed at this level — TBC) → Lofted surface with connectors aligned at leading edges (twist + connector discipline combined).
3. Circular pattern ×3 → hub revolve (Ø60 with shaft bore + keyway) → blade-root fillets 6 (stress! — the highest-loaded zone gets the biggest fair fillets).
4. Hand-rotation clearance vs a nozzle ring envelope (if ducted — TBC per design).

**Tap appendix (#39/#49, 10-step core):** base flange (revolve + bolt circle) → valve body (revolve) → spout centerline path → swept/lofted spout per §2 nozzle logic → aerator thread (modeled learning-grade) → handle lever (extrude + grip) → cartridge envelope inside body → assembly + section (water path visible? — the plumber's check) → chrome appearance + render.

---

## 6. Showcase support systems (what separates demos from products)

**Vents + grilles (hair dryer #93/#94-class, helmet #16–18):** intake zones need OPEN area (TBC: confirm airflow-area rules per device — illustrative starting point ~30–50% open) → patterned slots/holes (pattern a ZONE, cosmetic-rest per [[shredders-recycling-machines#5-failure-clinic]]) → recess the grille (impact protection + finger-safety: holes small enough to fail the finger probe — TBC: confirm safety standards for real products) → filter mesh envelope behind (serviceable? — model the access path, not just the mesh).

**Hinges + latches (any opening product):** living-hinge geometry (thin PP flex zone — TBC: confirm living-hinge design rules, NOT this page) vs mechanical hinge (pin + knuckles with clearance — TBC per size) vs snap latch (cantilever deflection math — TBC: confirm with snap-fit references). Pick per material and cycle count; model the pivot explicitly (assemblies that "just touch" separate in reality).

**Water/dust sealing (taps, shower #71/#82, outdoor housings):** O-ring grooves (rectangular groove to seal-cross-section rules — TBC: confirm with seal datasheets, e.g., standard O-ring groove tables) + squeeze verification in section view (groove fill ~75–85% — TBC per seal references) + drain paths for what gets past (seals delay water; drainage removes it — belt-and-suspenders is the professional stance).

**Fastener strategy (showcase assemblies):** ONE screw size per product where possible (service simplicity — TBC taste, confirm per cost analysis) → thread-forming screws into plastic bosses (pilot-hole per screw spec — TBC per datasheet) vs machine screws + inserts for serviceable joints (TBC per cycle count) → captive hardware where the user opens it (lost screws = support calls).

**Verify in-app:** produce the helmet paper plan for a real helmet photo set (front/side/top with ruler), then model regions 1–2 only + knit + zebra. Regions 1–2 done well beat all six done badly.

**Next:** [[artistic-organic]] → then PL2 machines from [[gearbox-fundamentals]].

---

## 14. Crowns, guards + machine-canopy appendix (covers that protect AND sell)

**Machine guarding as product design (the §9-conveyor + §10-press safety lessons merged — TBC: confirm with machinery-safety standards like ISO 14120/12100, NOT this page):** fixed vs movable vs adjustable guards (access frequency decides — daily-access points get interlocked doors, annual points get bolted panels! — TBC per risk assessment) → viewing windows (polycarbonate rated for impact/process — TBC per material; operators MUST see the process or they open guards!) → ventilation + noise integration (guarded machines cook and deafen — the §9-ventilation + §13-noise lessons inside the guard design!) → CAD consequence: guard MODULES with quick-release + interlock envelopes (the §11-top-down module habit: guards are modules with interfaces, not afterthought panels!).

**Aesthetic canopies (selling through sheet metal — TBC per industrial-design practice):** brand surfaces (color breaks, logo zones, lighting strips — the §13-appliance-trim language at machine scale!) → access choreography (which panels open for which tasks? — daily/weekly/annual access TIERS with distinct hardware: quarter-turns vs bolts vs interlocks — TBC per maintenance analysis!) → forklift/crane interfaces (lifting eyes + fork tubes rated — TBC per handling; machines move, plan the lift!) → CAD consequence: canopy SPLIT LINES follow access tiers (panel boundaries = service boundaries — form follows maintenance, and customers notice!).

**Retrofit + upgrade paths (machines live decades — TBC per lifecycle practice):** sensor/controls upgrade space (spare panel room + conduit capacity designed in — TBC per controls practice!) → guarding upgrades for regulation changes (mounting provisions for future interlocks — TBC per foresight!) → capacity creep interfaces (stronger motor mounts? bigger throat? — TBC per product family planning!) → CAD consequence: MARGIN modeled visibly (empty DIN rail space, spare I/O, oversize frames noted as intentional — the §11-margin habit restated: designed-in growth beats redesigned-later, 10:1 on cost!).

---

## 13. Magnetic + hinge + latch micro-mechanisms appendix (the details that delight)

**Magnetic closures (the premium feel — TBC: confirm with magnet-application references, NOT this page):** magnet + keeper sizing (pull force vs size/grade — TBC per magnet spec; N52 tiny vs ferrite chunky — TBC!) → steel shunt plates (flux concentration DOUBLES useful pull — TBC per magnetic-circuit practice!) → pockets + retention (press-fit? adhesive? overmolded? — TBC per assembly; LOOSE magnets in shipping = returns + bad reviews!) → polarity planning (multi-magnet arrays need mapped polarities — TBC per design; wrong polarity REPELS at the customer!) → CAD consequence: magnet pockets modeled with insertion draft + adhesive grooves (TBC per process) + polarity marks on the DRAWING (assembly instruction, not geometry!).

**Hinge micro-design (laptop/phone/tablet lid hinges and beyond — TBC: confirm with hinge references):** friction vs detent (free-stop positioning needs CONSTANT torque across angles — TBC per clutch design; cams + springs, not just tight pivots!) → cycle life (30k+ open-closes for laptops — TBC per spec; wear-tracked, not hope-tracked!) → cable routing THROUGH the hinge (display/data lines cross the pivot — service loop + bend-radius discipline, TBC per flex-circuit practice!) → CAD consequence: hinge modeled at 3 angles minimum (closed/90/open — interference + cable sweep checked at ALL THREE, not mid-travel complacency per §11-tripper lesson!).

**Latch + eject mechanisms (the click that satisfies):** push-push card slots (heart-cam track geometry — TBC depth: the track IS the mechanism, confirm with mechanism references!) → spring-loaded ejectors (battery/SIM trays — TBC per force) → snap-latch cantilever math (deflection + strain vs fatigue life — TBC: confirm with snap-fit references; the §4-enclosure lesson restated at precision scale!) → CAD consequence: latch states as configurations (latched/unlatched/ejecting — the §11-dispensing-states habit generalized: mechanisms get modeled in EVERY state!).

---

## 12. Appliance platform thinking (families, not one-offs)

**Platform strategy (how brands really build — TBC per business practice):** shared chassis/motor/pump across 5–10 SKUs (the expensive engineered core amortized!) → differentiated skins/trim/colors per SKU (surfacing variations on a common platform — YOUR surfacing skills applied to business logic!) → feature-ladder planning (base/mid/premium differ by ADDED modules, never redesigned cores — TBC per product management) → CAD consequence: platform parts in a SHARED library folder (never copied per SKU — the §10-file-hygiene habit at business scale!) + SKU assemblies differing ONLY in trim/feature configs (the [[dressup-productivity]] §8-config habit as product strategy!).

**Variant management in CAD (the mechanics of families):** design tables driving dimensions per SKU (TBC per version: Excel-linked tables — learn YOUR table UX once) → suppressed-feature ladders (premium gets the chrome trim + extra jet zones; base suppresses them — the [[dressup-productivity]] §8-ladder restated) → color/material configs (appearances per SKU — renders per config for marketing BEFORE tooling! — TBC per workflow) → the cardinal rule: platform changes propagate TO ALL SKUs (change the shared chassis = revalidate every SKU's interfaces — the layout-sketch discipline from [[sketch-mastery]] §12 at family scale!).

**Cost-down redesigns (the sequel every product gets — TBC per business practice):** part-count reduction drives (combine two parts? eliminate a fastener? — TBC per DFM analysis) → material substitution (validated by re-testing, never by hope — TBC per QA) → supplier-driven changes (second-source equivalence proofs — TBC per procurement) → CAD consequence: revision discipline per [[part-assembly-drawing-workflow]] §10 (REV letters + change notes + revalidation checklist PER SKU affected). Cost-down without revalidation is how recalls happen — the ethics note that belongs in an engineering page.

---

## 11. SpaceX-Dragon + water-tank appendix (big envelopes, modeled smart)

**Capsule bodies (#91-class method):** pressure-vessel base (revolved + domed ends — the vessel logic from [[bottles-containers]] §9-beverage generalized: pressure shapes are round for physics, not style) → heat-shield base (blunt ablative envelope + separation plane — TBC: confirm with aerospace references for anything beyond CAD practice; model the INTERFACE (bolt circle + separation springs envelope — TBC), not the chemistry) → SuperDraco/pod protrusions (repeated lofted pods per §2-pattern logic — model ONE pod, pattern + mirror!) → docking/berthing interface envelope (TBC per standard: androgynous vs probe-drogue is mission architecture — awareness, NOT this page) → TPS tile/panel breaks as split-line zones (TBC taste: maintenance access patterns read as design detail).

**Water tanks at scale (#2/#26/#79-class, industrial reading):** storage vs pressure duty (atmospheric storage = thin shell + stiffening rings; pressure = coded vessel — TBC: confirm with pressure-vessel standards, NOT this page; the CODE decides everything past atmospheric!) → level fittings (inlet/outlet/drain/overflow flanges + level gauge — TBC per installation; EVERY penetration is a modeled flange + reinforcement pad — TBC per vessel practice) → access + venting (manway for inspection + vent sized against pump rates — TBC: collapsed tanks come from undersized vents! — confirm with storage-tank references) → foundation + anchoring (wind/seismic overturning — TBC per code; anchor-chair envelopes on the drawing!) → CAD consequence: nozzles/reinforcements scheduled in a TABLE (tag every penetration — the vessel documentation habit).

**Scale-model discipline (both builds share it):** model at TRUE scale (1:1 units — scaling lies about clearances and fasteners; TBC taste: scaled display configs allowed, scaled MASTERS forbidden) → human/vehicle reference envelopes in-scene (doorway heights, truck beds, door widths — TBC per context: designs live in worlds, and worlds have standard sizes that constrain you) → transport split lines (ships in pieces? — flange pairs at split points modeled from the START, not retrofitted — TBC per logistics).

---

## 10. Water-tap + valve internals appendix (plumbing that seals)

**Cartridge systems (what's INSIDE the shiny body — TBC: confirm with plumbing references, NOT this page):** ceramic-disc cartridges (two lapped discs shearing flow ports — the modern standard; model the cartridge ENVELOPE + seat diameters, buy the cartridge — TBC per size) → compression stems (legacy rising-spindle with washer — TBC depth) → thermostatic mixers (wax element + sliding piston — TBC depth; awareness that temperature regulation lives INSIDE, not in the handle) → CAD consequence: bodies are SHELLS around cartridge envelopes (design the cavity FIRST from cartridge dims, style the outside second — inside-out discipline restated).

**Sealing + seats (where taps actually fail):** seat faces (replaceable seat rings vs machined-in — TBC per tier; modeled as separate ring parts when replaceable!) → O-ring grooves on spout/shower joints (swivel joints need DYNAMIC seals — TBC: confirm with seal references; static groove tables don't apply to rotating joints!) → aerator threads + flow straighteners (honeycomb insert envelope — TBC per part; limescale service access modeled — TBC per maintenance) → water-path section audit (the §5-plumber's check formalized: inlet → cartridge → spout outlet, no dead legs harboring stagnant water — TBC per hygiene practice for potable systems).

**Finish durability (chrome lives or dies here):** substrate (brass body — TBC per standard; zinc die-cast for budget with thicker plate — TBC) → nickel + chrome layer stack (TBC: confirm with plating references; CAD models the SUBSTRATE, drawings note the plate spec + thickness) → sharp edges plate thin and corrode first (generous radii aren't styling — they're corrosion engineering, TBC per finishing practice) → crevice corrosion at joints (seal + drain, never trap water against chrome — TBC).

---

## 9. Lampshade + small-appliance appendix (light, heat, and cords)

**Lampshade (#92-class):** shade profile (revolve/loft per silhouette — opaque vs diffuser zones SPLIT the design: opaque outer + translucent inner diffuser as separate bodies with an air gap? TBC per lighting practice) → bulb envelope + socket mount (E27/screw-shell dimensions — TBC per standard; model the socket, not just a hole — retention + electrical contact are real features) → heat chimney (hot air MUST exit top — vents sized per wattage, TBC: confirm with lighting-thermal references; trapped heat kills LEDs and yellows plastics) → cord grip + strain relief (cords pull — the grip takes the load, not the terminals — TBC per electrical-safety practice) → harp/finial mounts (the mechanical interface language of lamps — TBC per standard parts).

**Small-appliance patterns (generalizing hair dryer + shower + taps):** water + electricity NEVER share unsealed volumes (double-insulation or grounding + seals — TBC: confirm with appliance-safety standards, NOT this page; model the isolation barriers explicitly!) → service split lines (heating element / motor replaceable? — TBC per product tier; cheap appliances are sealed-for-life, premium ones open — the split-line placement differs!) → cord storage (wrap posts? retractable? — TBC per product) → feet/suction (vibration walk-off prevention — TBC).

**Glass + liquid done professionally (extending [[artistic-organic]] §6):** fill line at the NECK (ullage for expansion + pour control — TBC per packaging practice) → meniscus modeled (tiny fillet at the wall — the realism detail renders read) → bubbles/inclusions for styled liquids (TBC taste — cosmetic only) → condensation on cold servings (bump-appearance zones below the fill line — TBC per version) → the GLASS thickness gradient (base 3× wall — TBC illustrative; tumblers read quality through base mass).

---

## 8. Helmet trilogy: full 3-part build script (the deep dive)

Reference photos first: front + side + top with a ruler in frame (per [[artistic-organic]] §1) → Sketch Pictures scaled with head breadth + length (TBC: measure YOUR head or a real helmet — illustrative numbers below assume ~600 mm circumference class, confirm per shell size).

**PART 1 — outer shell (boundary zones, staged knits):**
1. Layout: 3 longitudinal guide rails (center ridge + 2 intermediate style lines per side — these double as patch seams AND styling) + 5 cross profiles (brow / temple / crown / rear / lower-rim), all derived from the reference pictures via traced splines (rebuild traces with ≤6 points each + tangent ends — fairness starts here).
2. Crown-center patch: Boundary with the ridge rail + adjacent style rails as Direction 2, cross profiles as Direction 1 → zebra immediately (fix the FIRST patch perfectly — every neighbor inherits its edges).
3. Side patches (ONE side, then mirror!): boundary between style rail and lower-rim rail → mirror about the center plane (asymmetric graphics come later as decals — structure stays symmetric).
4. Rear patch: lofted transition closing crown-to-rim → knit crown + sides + rear IN STAGES (crown+sides first, confirm, then rear) → staged-knit discipline from [[filled-knit-trim-thicken]].
5. Lower rim: edge-roll bead (swept tube Ø8–10 along the rim loop — TBC illustrative: stiffness + safe edge in one feature) → knit bead into shell if same material, or separate part if rubber trim (TBC per construction).

**PART 2 — openings, vents, visor (trim phase):**
6. Visor opening: sketch the aperture on a side-offset plane (TBC per helmet: aperture width ~240–260 illustrative) → project-trim onto shell (trim-with-sketch per [[filled-knit-trim-thicken]] §8) → visor recess ledge (offset-surface step 3 deep for the shield to sit flush — TBC illustrative) → shield as SEPARATE transparent part (revolve/loft to opening curvature + pivot bosses at both temples).
7. Ear recesses: trim circles/ovals (Ø70-ish speaker pockets — TBC per comms gear) + shallow fill-blend rims (no sharp edges near ears — comfort + safety).
8. Vents: brow intake (2 slots) + crown exhausts (3–4) + rear extractors — patterned trims with mesh envelopes behind (insect/debris screening — the forgotten function; model mesh as cosmetic + frame groove) → chin-bar vents if full-face (TBC per helmet type: half/open/full dictate the whole opening map — confirm per YOUR reference).

**PART 3 — liner, retention, hardware (assembly phase):**
9. Comfort liner: offset-surface inward (8–12 gap per §5-liner example in [[surfacing-utilities-troubleshooting]]) → trim to coverage (crown + cheeks, NOT visor/rim) → cheek pads as separate lofted pads (removable/washable in reality — model the snap envelopes, TBC depth).
10. Retention: chin strap (webbing sweep along drape path — TBC) + D-ring/micrometric buckle envelopes (bought-out — model envelopes + mount points, never hand-model buckles) → strap anchors riveted through shell+liner (rivet envelopes + pull-through reinforcement washers — TBC per standard; anchors are life-safety parts, confirm with helmet standards NOT this page).
11. Assembly: shell + liner + shield + pads + strap + vents → interference check (liner vs shell gap uniform? shield sweep vs opening through full pivot travel? — drag-test the shield!) → mass rollup (shell-heavy helmets fatigue necks — TBC: confirm weight targets per standard/size) → exploded view (assembly/service story) → hero render + zebra proof + section through vents (air path visible? — the ventilation check).

**Graduation bar:** paper plan (§5) + regions 1–2 modeled + knit + zebra was the checkpoint; THIS section is the full trilogy. Finish all three parts + assembly + checks = surfacing-capable, provably.

---

## 7. Car-door panel appendix (#8-class: large gentle curvature)

**Why doors are the zebra final exam:** acres of low-curvature skin where every ripple shows — C2-or-bust territory.

1. **Character lines FIRST:** the door's creases/style lines are patch BOUNDARIES (upper shoulder line, lower sculpt) — 3 patches (upper/mid/lower) meeting at designed creases beats one heroic patch spanning everything.
2. **Boundary with C2 on long edges:** profiles from orthographic sections every ~200 mm (TBC illustrative density) + Direction-2 rails along the character lines → continuity C2 to neighbors → zebra after EACH patch (not at the end — isolate defects while cheap).
3. **Openings:** window frame (trim + edge roll — the helmet edge-roll move at automotive scale), handle recess (trim + separate handle part + clearance for fingers — §7-handle clearance generalized), mirror mount reinforcement (doubler patch inside — TBC per construction).
4. **Inner structure (awareness):** real doors have intrusion beams + window regulators inside (TBC depth) — model the beam envelope so the skin never intersects it through slam-travel (the packaging check).

**Panel-gap discipline (the automotive read):** shut lines (door-to-fender gaps) are uniform ~3–4 mm (TBC: confirm with automotive references) — model adjacent panels (fender/rocker envelopes) to READ your gaps, never eyeball a door solo. Uniform gaps photograph as quality; wavy gaps as amateur — same CAD skill as button gaps in [[consumer-electronics]], scaled up.

## CROSS-REFERENCES
- [[INDEX]] · [[household-tools]] · [[artistic-organic]] · [[surfacing-methodology]] · [[gearbox-fundamentals]] · [[solidworks-project-ideas]]
