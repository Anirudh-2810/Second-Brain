---
course_code: "BTech-Sem1-ED (TBC)"
course_name: "Engineering Drawing"
unit: "SolidWorks - shredder and recycling machines"
tags: [btech, engineering-drawing, solidworks, cad, shredder, machines, welding, frames]
last_updated: "2026-09-12"
description: "PL2 shredder and recycling machine builds: plastic/paper/agri shredders, wood chipper, cutting chamber anatomy, blades, frames, and drive integration."
module: "engineering-drawing"
prerequisites: [["bevel-planetary-gearboxes"], ["gearbox-fundamentals"], ["INDEX"]]
confidence: medium
---

# Shredders & Recycling Machines

## For future agent
PL2 build page. Videos: #1 36-blade plastic shredder #329 · #4 heavy-duty prototype #341 · #7 mini plastic #328 · #10 single-shaft paper #330 · #27 industrial paper shredder · #5 mini agri #297 · #24 tree-chipper #327 · #26 wood chipper prototype #326 · #34 link-index (skip). Per-video specifics TBC vs bulk transcripts. Teaches: cutting chambers, blade stacks, weldment frames, and gearbox-to-machine integration (these machines ARE gearboxes with teeth on the outside).

> **Why shredders teach machine design:** one machine forces every subsystem — cutting chamber (precision), blades (wear parts), drive (gearbox + motor), frame (weldment), hopper (sheet metal), safety (guards + e-stop thinking). Model a shredder completely and no machine architecture surprises you again.

---

## 1. Cutting-chamber anatomy (the heart)

```
HOPPER (sheet metal, guides material in)
   ↓
BLADE STACK on hexagonal/octagonal SHAFTS (2 shafts counter-rotating typical)
   ↓ blades interleave with SPACERS + COMBS (clear jams, strip material)
SCREEN below (sized holes = output particle size)
   ↓
COLLECTION bin / conveyor out
```

- **Blades:** hooked/clawed discs, stacked with spacers; 36-blade count in #329 sets the patterning exercise (circular/linear patterns of blade instances + angular offsets between adjacent blades — TBC exact video method).
- **Shafts:** hex profiles so blades can't spin loose (flats drive the stack — elegant, no keys needed per blade); stepped ends for bearings.
- **Combs/stripers:** static fingers interleaving the blade stack that peel material off — the part beginners omit; without strippers the chamber packs solid.
- **Screen:** perforated arc under the chamber; hole size = product spec. Model as patterned cuts (keep counts sane for rebuild speed).

## 2. Playlist build map

| Build | Focus (TBC per-video) |
|---|---|
| #329 36-blade plastic shredder (#1) | Full chamber: blade stack patterning + spacers + screen |
| #341 heavy-duty prototype (#4) | Heavier shafts/bearings, frame upsizing — compare with #1 for duty scaling |
| #328 mini plastic (#7) | Compact variant — same architecture, smaller envelope |
| #330 single-shaft paper (#10), #27 industrial paper | Single-rotor + fixed-bed-knife cutting (different physics: shear vs tear) |
| #297 mini agri (#5), #327 tree chipper (#24), #326 wood chipper (#26) | Infeed hoppers, flywheels/anvils for wood, discharge chutes |
| Drive side (all) | Gearbox + motor coupling to blade shafts — torque math from [[gearbox-fundamentals]] |

## 3. Frames & weldments (the skeleton)

Shredder frames are **weldments**: structural members (square tube/angle/channel) cut and welded. SolidWorks Weldments module: sketch the skeleton lines → assign profiles → automatic miters/trims + cut list. Model weld beads only where the drawing must call them (cosmetic); the **cut list + weld table** on the drawing is the deliverable. Guards (sheet-metal covers over drives/blades) are safety AND legal — model them closed, with fasteners, no "guard removed for clarity" in final assemblies (awareness: real machines need interlocked guards — TBC regulatory depth out of scope).

## 4. Sheet-metal hoppers (the funnel)

Hoppers = tapered boxes from sheet: model with Sheet Metal tools (base flange + miter flanges or lofted bends where supported — TBC per version), check **flat pattern** (it must unfold without distortion — the manufacturability test), bend radii to shop capability (TBC: confirm with fabricator), hem raw edges (safety).

## 5. Failure clinic

| Symptom | Cause → Fix |
|---|---|
| Blade stack binds in assembly | Spacing math off (blade + spacer widths ≠ chamber width) → drive stack width from chamber via equations |
| Shafts can't be inserted in CAD | Assembly order ignored → plan insertion (shafts before side plates? side plates split?) like the gearbox split-plane habit |
| Screen holes kill rebuild | Thousands of patterned cuts → pattern a small zone + cosmetic rest, or suppress for working config (configurations!) |
| No stripper combs | Chamber packs in reality → add interleaving combs (lesson, not just geometry) |

---

## 6. Worked example: 6-blade mini chamber (dimensions + equations)

Scale-model of #329's 36-blade architecture — all numbers illustrative (TBC: confirm cutting geometry with shredder references for real builds).

**Chamber:** inner width 120 (fits 6 blades × 12 + 5 spacers × 8 + 2 end discs × 4 = 72+40+8 = 120 ✓ — the width equation; make it an actual equation so blade-count changes propagate).
**Shafts:** 2× hex 24 A/F (hex drives blades — no keys!), centers 90 apart vertically-staggered? No — side-by-side horizontal, center distance set by blade overlap: blade Ø100 → centers ≈ 75 (interleave depth 25 — TBC: confirm overlap practice; too deep = clash, too shallow = unshredded strips slip through).
**Blades:** Ø100 discs, 12 thick, 3 claw hooks each (sketch ONE hook profile → circular pattern ×3 per blade → blade pattern ×6 along shaft with 60° stagger between adjacent blades — the stagger is the cutting action; aligned blades = one wide knife, staggered = continuous shear).
**Spacers:** Ø60 × 8 (smaller than blade root so they don't touch material — TBC: confirm; spacers set cut WIDTH).
**Combs:** static stripper fingers between adjacent blades on both shafts (interleave! — 5 combs per shaft from the side plates; TBC exact mounting per video).
**Side plates:** 10 MS plate with bearing seats (pillow-block envelopes — bought out at this scale? TBC per build) + screen arc below (Ø-matched arc, Ø6 holes on 10 grid over the bottom 120° — pattern a ZONE then cosmetic-rest per §5).
**Hopper:** 4-sided sheet-metal taper (inlet 300×200 → throat 130×110 — TBC illustrative) with 60°+ wall angles (material mustSLIDE, not bridge — TBC: confirm flow angles per material; steep is safe).
**Drive:** motor → 1:2 chain/belt (TBC per video) → gearbox per [[helical-spur-gearboxes]] → hex shafts. Torque check: shredding torque is violent and spiky (flywheel effect helps — TBC: confirm with shredder references; awareness that steady-state math underestimates).

**Single-shaft appendix (#330-class):** one rotor + fixed bed knife (adjustable gap! — slotted mounts, TBC: knife gap sets cut quality, confirm per material) + screen — simpler, louder, hungrier for sharp knives. Model the knife adjustment explicitly (it's a maintenance feature, not a detail).

**Verify in-app:** model the 6-blade mini chamber, assemble, rotate shafts by hand checking blade interleave clearance. Scale the recipe toward #329's 36 blades only after the mini works.

**Next:** [[conveyors-material-handling]].

---

## 13. Mobile + plant-scale appendix (shredders that travel or anchor plants — TBC per mobile-plant references)

**Mobile shredders (tracked/wheeled units — TBC: confirm with mobile-equipment references):** transport envelope (road-legal width/height/weight PER JURISDICTION — TBC per regulation; design folds/telescopes to legal!) → self-propulsion vs towable (tracks for sites, wheels for roads — TBC per mobility need!) → onboard power (diesel-hydraulic vs genset-electric — TBC per emissions/noise site rules!) → setup/teardown time (outriggers + feed arrangement under an hour? — TBC per operations!) → CAD consequence: TRANSPORT configuration modeled (folded boom, pinned feeders, locked drums — the §12-storage-states habit for machines that commute!).

**Fixed-plant integration (the shredder as one organ — TBC: confirm with plant-design references):** feed metering upstream (starve vs choke scenarios designed — TBC per process control!) → dust + noise + fire systems shared across the line (the §10-appendix at plant scale — TBC per facility design!) → maintenance crane coverage (every heavy lift reachable — TBC per layout; unmaintainable corners get neglected per §9!) → CAD consequence: plant LAYOUT model with ALL disciplines (civil + mechanical + electrical envelopes — the §11-large-assembly habit: modules with interfaces at factory scale!).

**Permitting + community envelope (awareness — TBC: confirm with environmental/land-use regulation, NOT this page):** emissions + noise + traffic + hours-of-operation constraints SHAPE the plant (enclosed buildings, curfews, wheel-washes — TBC per permit!) → CAD consequence: permit drawings FROM the model (site plans, elevations, screening renders — the §8-publishing habit doing legal duty!).

---

## 12. E-waste + tire + white-goods appendix (hard streams — TBC per recycling references)

**E-waste (hazard-dense shredding — TBC: confirm with e-waste standards, NOT this page):** battery REMOVAL upstream (lithium in shredders = fires that make news — TBC per procedure; detection + manual pull BEFORE the chamber, no exceptions!) → refrigerants captured (CFC/HFC recovery by certified techs — TBC per regulation!) → mercury switches + backlight tubes diverted (TBC per hazmat stream!) → CAD consequence: pre-sort STATION layout (conveyor + pull stations + detector gates modeled as a SYSTEM with the shredder — the §11-flowsheet habit: the shredder is step 3, not step 1!).

**Tires (tough + steel-belted — TBC: confirm with tire-recycling references):** debeader FIRST (steel bead rings removed whole — TBC per process; beads destroy general shredders!) → rough shred → granulate → steel + fiber separation (magnetic + air per §11!) → crumb sizing to spec (sports turf vs asphalt vs molded goods differ — TBC per product!) → CAD consequence: debeader + staged chambers + separation in ONE line layout (footprint + height + access modeled together — plants, not machines, per §11!).

**White goods (fridges/washers — TBC per appliance-recycling practice):** degassing station (refrigerant + oil recovery FIRST — TBC per regulation!) → depollution pull (capacitors? mercury? batteries? PCBs? — the hazardous manifest per unit, TBC!) → shred whole AFTER depollution (hammers over knives for mixed scrap — TBC per process!) → foam blowing-agents captured (old CFC foams — TBC per regulation!) → CAD consequence: depollution LINE (stations + tools + extraction) modeled with equal care as the shredder (compliance hardware IS process hardware!).

---

## 11. Sorting + separation appendix (shredding is step one — TBC per recycling references)

**Downstream chain awareness (shredders FEED processes — TBC: confirm with recycling-plant references, NOT this page):** magnetic separation (ferrous out FIRST — protects downstream crushers/mills! — TBC per flowsheet) → eddy-current (non-ferrous ejected — TBC per physics) → air classification (light/heavy split by airflow — TBC per density cut-points) → optical/sensor sorting (color/material/NIR ejection — TBC per technology!) → CAD consequence: shredder DISCHARGE interfaces to conveyors at documented rates/heights (the §9-conveyor handoff: flange positions + flow rates ON the drawing, or integration fails on site!).

**Size-reduction stages (coarse → fine cascade):** primary shred (100–300 mm output — TBC per duty) → secondary shred/granulate (10–50 mm — TBC) → fine grind/pulverize (<10 mm — TBC per product spec!) → each stage SMALLER + FASTER + TIGHTER-toleranced than the last (the design progression!) → CAD consequence: common shaft/frame ARCHITECTURE across stages (platform thinking per [[complex-showcase]] §12: one proven chamber family, scaled!) → liner/screen interchangeability (wear parts shared across stages where possible — the spares-table economics from §8!).

**Contamination control (recyclate quality = money — TBC per market specs):** tramp removal upstream (magnets + manual picking BEFORE the chamber — the §10-wrench lesson generalized: protection pays!) → wash lines after granulation (labels/glue/dirt removal — TBC per process; water + drying envelopes in the layout!) → metal detection post-shred (missed tramp destroys granulator knives in seconds — TBC per practice!) → CAD consequence: detector + diverter-gate envelopes at discharge (rejected-stream chute modeled! — quality hardware needs space designed in, per the §10-safety-hardware rule!).

---

## 10. Dust, noise + fire appendix (shredders are hazardous by nature)

**Dust control (shredding MAKES dust — design for it):** enclosed chamber + discharge (open machines dust the building — TBC per industrial-hygiene practice) → extraction stubs at transfers (per §9-conveyor dust thinking generalized: every drop point gets a stub!) → filter maintenance access (blinded filters = no extraction = dust event — TBC per practice; model the filter door + differential-pressure tap! — TBC per monitoring) → combustible-dust awareness (organic/metal dusts EXPLODE — TBC: confirm with safety standards like NFPA 652/654, NOT this page; venting + isolation + housekeeping designed, not hoped!).

**Noise control (shredders are LOUD — TBC: confirm with occupational-noise references, NOT this page):** source level audit (impact + drive + discharge each contribute — TBC per measurement) → enclosure panels with mass + absorption (TBC per acoustic practice: mass blocks, foam absorbs — different jobs!) → operator distance + duty (exposure math decides PPE + rotation — TBC per regulation) → CAD consequence: acoustic covers modeled WITH access (the §8-guard lesson restated: covers that block maintenance get removed permanently — design covers that MAINTAIN through!).

**Fire triangle in one machine (awareness — TBC: confirm with fire-protection references, NOT this page):** fuel (shredded product + dust + lube oil!) + ignition (bearing failure heat, tramp metal sparks, electrical faults!) + oxygen (dust extraction MOVES air through the hazard!) → suppression (detection + deluge/gas zones — TBC per system design) → isolation (dampers stopping propagation to dust collectors — TBC) → CAD consequence: detector + suppression + damper MOUNTS modeled (retrofits never fit — the §9-controls lesson restated for safety hardware!) + tramp-metal protection upstream (magnets/belts BEFORE the chamber — TBC per installation; one wrench in the chamber totals blades AND shafts!).

---

## 9. Drive sizing + controls appendix (power and brains)

**Motor selection (the torque-speed envelope — TBC: confirm with motor references, NOT this page):** steady torque (process mean — §6-spikes restated: size for SPIKES via service factor, not means) → starting torque (loaded restarts! — across-the-line vs VFD starting capability differs 2–3×, TBC per motor type) → duty cycle (S1 continuous vs S3 intermittent — TBC per IEC duty; undersized-duty motors cook slowly, then suddenly) → frame + mounting (foot/B-flange/C-face per layout — TBC per catalog; model the FRAME, buy the motor — the envelope discipline from §6 restated) → efficiency class (IE3/IE4 premium vs purchase price — TBC per energy economics; motors run for decades, efficiency pays).

**VFD + controls (modern drives think):** soft-start (current + mechanical shock reduction — TBC per drive practice) → speed trimming (throughput tuning without sheaves/belts — the process-flexibility move) → jam response (current-limit + auto-reverse routines — TBC per program; the §8-unjam designed in SOFTWARE too) → interlocks (hopper-open inhibit, e-stop category, guard switches — TBC: confirm with machinery-safety standards, NOT this page) → CAD consequence: panel + conduit + sensor envelopes (VFD cabinet, pull-cord switches, level sensors — model the MOUNTS and cable routes, not just the machine!).

**Transmission choice matrix (motor→rotor power path):** direct-coupled (aligned, efficient, unforgiving of shock — TBC) → belt/chain (slip/clatter absorb spikes + ratio flexibility via sheaves — TBC per practice; belt dust + tension maintenance are the taxes) → gearbox (the [[gearbox-fundamentals]] decision tree applied: ratio + duty + space) → hydraulic (stall-safe + variable speed at low efficiency — TBC per mobile-equipment practice) → SELECT per shock profile (shredders shock → belt or hydraulic cushion; conveyors cruise → direct or gearbox). The transmission is a FUSE and a MATCHMAKER, not just a connector — size it like one.

---

## 8. Wear-part economics + jam recovery (the operator's design review)

**Wear hierarchy (design spares FIRST, not after):** knives/blades (sharpen 2–3× then replace — TBC per steel/duty) → screens (holes peen shut + abrade oversize — reversible? flip 180° for double life — TBC per screen design) → bearings near the chamber (dust ingress despite seals — TBC: confirm with maintenance references; purgeable seals where washdown happens) → belts/chains (tension-checked weekly — TBC per schedule) → gearbox oil (contamination-tracked, not calendar-tracked — TBC per practice). Model EVERY wear part as a separately-sourced part number (purchasing replaces numbers, not geometry) + flag them on the drawing with a spares table (the aftermarket thinking from §7 restated as deliverable).

**Jam-recovery design (shredders WILL jam — design the un-jam):** reversing function (drive reverses to spit the jam — motor/VFD spec, TBC per drive) → quick-access covers (tool-free latches, NOT 20 bolts — downtime is money; TBC per operation) → chamber cleanout position (rotate/shift for access — model the SERVICE configuration, not just running config!) → shear-pin/coupling fuse (mechanical overload protection that fails CHEAP — TBC: confirm with machine references; the fuse protects the gearbox, which costs 10× the pin) → e-stop + lockout points modeled (awareness: confirm with machinery-safety standards, NOT this page — unjam procedures kill when lockout is skipped).

**Throughput math (awareness — TBC: confirm with shredder-application references, NOT this page):** capacity ≈ chamber volume × bulk density × rotor speed × fill factor (fill ~30–50% illustrative) → power spikes 3–5× steady running on infeed gulps (size drives for SPIKES: motors thermally, gearboxes mechanically — TBC per duty) → screen hole size gates output (smaller holes = finer product = LOWER throughput + HIGHER power — the triangle every recycling quote balances). CAD consequence: screen as a CONFIGURATION (swap hole sizes per job — the product-flexibility move).

---

## 7. Single-shaft + paper machines + maintenance appendix

**Single-rotor + bed-knife physics (#330/#27-class):** one spinning rotor with cutting teeth passing a FIXED bed knife with a small adjustable gap (TBC: knife gap ~0.1–0.3 mm illustrative — confirm with shredder references; gap sets cut quality AND power draw). Rotor teeth (patterned cutters on a drum — fewer, chunkier than twin-shaft blades) shear material against the knife edge. Design consequences: knife adjustment slots are MANDATORY (knives dull → advance the gap, don't replace the rotor) → knife steel specified separately (hardened tool steel vs mild rotor body — TBC per build; model as separate part with its own material!) → screen wraps more of the rotor (particle sizing happens here, same patterned-cut discipline as §1).

**Paper-shredder specifics (#330/#27):** strip-cut (parallel shafts, interleaved discs — the twin-shaft pattern at fine pitch) vs cross-cut (added perpendicular shear — particle spec drives the mechanism choice; TBC per security level) → paper dust management (sealed bearings! paper dust kills open bearings — TBC: confirm with maintenance references) → bin-full interlock envelope (awareness: safety/compliance feature, model the sensor mount).

**Agri/wood appendix (#297/#327/#326-class):** infeed hopper STEEP + long (branches self-feed by gravity + vibration — TBC: confirm feed angles per material; shallow hoppers need push sticks = injury vector) → flywheel/anvil option for wood (inertia smooths the cut spikes from §6 — TBC: confirm flywheel sizing with machine references) → discharge chute aimed DOWN into collection (dust + chip throw direction is a safety feature — TBC per guarding practice) → PTO/drive interface for tractor-driven units (TBC per build: spline + shear-bolt overload protection — the shear bolt is the mechanical fuse, confirm with agri references).

**Maintenance-as-design (the industrial lesson):** every wear part needs a 10-minute replacement path — blades/knives/screens accessed through bolted (not welded!) covers with lifting points (TBC: confirm weights vs manual-handling limits) → grease points reachable without disassembly (model the nipples!) → spare-parts BOM flagged on the drawing (which parts to stock: knives, screens, belts, bearings — the aftermarket thinking that separates machine builders from modelers).

## CROSS-REFERENCES
- [[INDEX]] · [[gearbox-fundamentals]] · [[conveyors-material-handling]] · [[presses-forming-drone]] · [[dressup-productivity]] (patterns) · [[part-assembly-drawing-workflow]]
