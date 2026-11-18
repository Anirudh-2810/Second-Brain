---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Robocon Viva"
unit: "ABU Robocon 2027 Rulebook V1.1"
date: 2026-11-19
tags: [btech, kjsce, nexus-robotics, abu-robocon, rulebook, viva, robotics-club]
last_updated: "2026-11-19"
confidence: stated
description: "Viva Q&A over the ABU Robocon 2027 rulebook V1.1 (The Pursuit of Mustika Nusantara): field and objects, TR/BR roles, scoring, retries, violations, robot specs, safety, teams, and the V1.0→V1.1 redline changes."
relations: {source: "raw-sources/ABU_Robocon_2027_Rulebook_V1.1_Redline-1.pdf"}
---

## For future agent

Viva bank over **ABU Robocon 2027 Rulebook V1.1 (Redline)**, ingested from `raw-sources/ABU_Robocon_2027_Rulebook_V1.1_Redline-1.pdf` (extracted with PyMuPDF — this model cannot read PDFs directly, so text was dumped to a temp file first). Every answer below is **stated** in the rulebook; rule numbers are quoted where useful. Companion pages: [[nexus-components-viva-level1]] (hardware), [[nexus-components-viva-level2]], [[nexus-theory-rapidfire]]. If V1.2+ arrives, re-ingest and correct — redline deltas are marked in the source.

# Robocon 2027 Rulebook Viva

## 1. Contest basics

| Q | A |
|---|---|
| Theme? | "The Pursuit of Mustika Nusantara" — Solo, Indonesia; contest day **29/8/2027**, venue Edutorium UMS. |
| Match format? | Red vs Blue, **exactly 3 minutes**, winner = higher total score (§3.1). |
| Early win after Mustika? | No — match continues to full 3 min (§4.2.3). |
| Two robots? | **TR** (Transporter: manual or auto) + **BR** (Builder: **must be fully autonomous**, §11.3). |
| Team size? | 3 students + 1 instructor (same institution), + up to 3 **Pit Crew** (undergrad/diploma only; postgrads banned) (§10). |

## 2. Field & objects (dimensions they can ask cold)

| Item | Spec |
|---|---|
| Game Field | 11000 × 11000 mm |
| Start/Retry Zone | 700 × 700 mm each; teams choose which box suits TR/BR |
| Storage Area | 1000 × 2000 mm — holds **20 Earth Blocks** per team |
| Ground Shared Area | 1200 × 1200 mm — **12 Sky Blocks**, alternating pattern on 5×5 grid, center empty (Fig 4, mirror-symmetric) |
| Mustika Pillar | ∅270 mm, 500 mm high, receptacle ∅180 × 100 mm |
| Level 1 | 600 mm high, 6000 × 6000 mm; reached by ramp (3500 mm) or stairs (300×1000×150 mm steps) |
| Level 2 | +300 mm above L1 (900 mm total), 3000 × 3000 mm; **no stairs L1→L2 — BR may climb from any L1 position** (V1.1 change) |
| Transfer Area | 1000 × 1000 mm at L1 boundary — TR↔BR exchange point |
| Building Spot | 500 × 500 mm green target square (with tolerance) |
| Central Pillar | ∅270 mm, 800 mm high — Mustika enshrinement |
| Earth Block | 350 mm cube (±5%), 3-layer cardboard, ~600 g (±20%), 20 per team |
| Sky Block | 200 mm cube (±5%), red one side / blue other, ~220 g (±20%), 12 shared |
| Mustika | Mikasa V300W volleyball, ∅210 mm, 260–280 g — **250 points** |

## 3. Game flow

1. **Setup:** 1 minute; robots fully inside Start/Retry Zones, nothing overhanging vertically; team stacks Storage (max 2 blocks high per column) (§4.1).
2. **TR job:** harvest Earth Blocks (Storage) + Sky Blocks (Ground Shared) → carry to Transfer Area. Max **3 blocks** carried (§3.4.3).
3. **BR job:** receive at Transfer → build **Complete Towers** on Building Spots on L1/L2. Max **2 blocks** (§3.4.4).
4. **Complete Tower** = exactly 2 Earth Blocks stacked + 1 Sky Block on top, in order, on a Building Spot (§2 terms).
5. **Sanctuary Mandate:** ≥2 Complete Towers standing **simultaneously**, ≥1 in a Shared Area (L1 or L2) → unlocks Mustika retrieval. Once fulfilled, **permanently fulfilled** even if opponent breaks the towers (§3.6.2).
6. **Mustika chain:** TR takes it from Mustika Pillar (only after mandate) → **direct handover to BR in Transfer Area, must not touch floor** (§3.4.5) → BR carries to L2 → enshrines on Central Pillar. Robot with Mustika carries **no blocks** (§3.4.6); only **first** enshrined Mustika counts (§3.6.8).

**Viva traps:**
- *Can BR receive blocks placed on the floor?* → yes for Earth/Sky Blocks (within Transfer boundary); **Mustika: direct handover only**.
- *Who builds towers?* → BR only (§3.5.1); TR is Ground-Area-only (can't enter L1 beyond Transfer, §4.3.1).
- *Push blocks?* → **no** — lift/carry only (§4.4.1). Pushing/dragging = violation.
- *Can you steal a tower?* → flip the Sky Block so your color faces up — lifted **only to flip, must return to same tower**; moving it to another tower = Forced Retry (§3.5.8).

## 4. Scoring

| Action | Points |
|---|---|
| Block delivered to Transfer Area (TR) | **5 each**, once per block, permanent (§8.1) |
| Earth Block bottom layer | L1: **10** · L2: **20** |
| Earth Block middle layer | L1: **20** · L2: **40** |
| Sky Block top layer | L1: **40** · L2: **80** |
| Mustika enshrined | **250** (§8.5.1) |

- **Ownership:** Earth-block points lock to the team that *placed* them (even if opponent stacks on top) (§8.3.1). Sky Block points follow **color facing up at buzzer** (§8.3.2). Flipping a Sky Block never transfers the Earth blocks beneath (§8.3.3).
- **Multi-team towers** score individually per placed block (§8.4).
- **Zero points if:** object still touched/gripped/supported by robot at buzzer (§8.6.1); out of sequence (must be Earth→Earth→Sky); pushed/dragged to spot (§8.6.4).

**Tie-break order (§9.3):** Mustika enshrined → more Sky Blocks of own color up → more blocks on L2 → more blocks on L1 → judges' decision (technical merit + sportsmanship).

## 5. Retry, Failure, Violation, Disqualification — the four-tier ladder

| Tier | Trigger | Consequence |
|---|---|---|
| **Retry (requested)** | Team calls it any time (malfunction, stuck, strategy reset); leader raises hand + shouts "Retry!" | Robot returns to its Retry Zone (TR→Start; BR→Start **or** L1 Retry Zone if it fully entered L1 at least once); held blocks **retained**; Mustika (if held) removed → pillar refilled (§5) |
| **Failure (new, V1.1)** | Earth Block touches floor outside Storage/Transfer/Building Spot, or placed out of sequence — released *or still held* | Block becomes invalid, removed when safe; **no Forced Retry**; transfer points already earned stay (§5.1.4) |
| **Violation → Forced Retry** | Area violation, carry-limit, dropped Sky Block, blocking in Shared Areas, tower collapse (Tower Protection), dropped Mustika | Offending robot retries; specific objects invalidated/restored per rule (§6) |
| **Disqualification** | Intentional damage; intentional displacement of opponent's placed blocks; safety violations; unsportsmanlike conduct (incl. intentional Sky-Block invalidation); unauthorized touching (procedure per Participation Guideline) | **Score = 0, lose match** (§7) |

**Key V1.1 restructures:** No-Pushing (old 6.1) → absorbed into 5.1.4 Failure; Handover Violation + Out of Bounds deleted (→ Failure/invalid object); Zone Violation renamed **Area Violation** (6.1); new **Invalidation of Sky Blocks** (6.3), **Carry Limit** (6.4), **Tower Protection** (6.6); Unauthorized Touching moved to DQ (7.4).

**Trap questions:**
- *Earth Block dropped → forced retry?* → **No** — that's a *Failure* (V1.1): just the block dies, no retry.
- *Sky Block dropped?* → Forced Retry **and** block invalid (§6.3); several at once → only one invalid, rest restored.
- *Carry 4 blocks as TR?* → Forced Retry; the 4th (last-picked) becomes invalid; restart with 3 (§6.4 example).
- *You knock over your own tower?* → Forced Retry **regardless of intent** (Tower Protection §6.6.1); tower restored to pre-incident state; both teams touching → both retry.
- *Both robots cause collapse?* → both retry.
- *Mustika dropped?* → removed from field; pillar refilled (§6.2).
- *Interfere with opponent in Shared Area?* → Forced Retry (§6.5); blocking their path is a violation.

## 6. Robot rules (§11) — the numbers to memorize

| Q | A |
|---|---|
| Starting size? | Each TR & BR within **700 × 700 × 700 mm** (§11.5) |
| Extended size? | **1400 × 1000 × 1200 mm** (L × W × H) each (§11.6/11.7) |
| Weight? | **60 kg total for both robots** incl. batteries, manual devices, match cables (V1.1 change from 50 kg/robot); setup-only devices excluded (§11.8) |
| Power sources? | Batteries, compressed air, elastic force **only** (§11.12) |
| Battery voltage? | Nominal **≤ 24 V** (series stack included) (§11.13) |
| Max circuit voltage? | **42 V** actual max, per isolated system (§11.14) |
| Pneumatic pressure? | **≤ 600 kPa**; purpose-built container or pristine plastic bottle (§11.15) |
| Banned? | Lead-acid / adhesive-sealed batteries, explosive/high-temp sources, unsafe lasers (Class 1 or 2 only, IEC 60825-1), flying mechanisms/drones (§11.16, 12.6) |
| Radio allowed? | Wi-Fi (802.11), Zigbee (**802.15.4** — V1.1 corrected), Bluetooth — for TR manual control, BR start switch, Freeze/Resume (§11.9) |
| TR↔BR communication? | **Absolutely prohibited** — no signals, no encoded info; BR may only *sense* the field itself; nobody may send info to BR except start switch + Freeze/Resume (§11.11) |
| BR start? | Team member operates a start switch at the signal; no manual intervention after (§11.19) |
| Freeze/Resume (new)? | **Remote pause of all actuators** on referee instruction; resume only with referee permission; not counted as manual intervention/communication (§11.4) |
| Emergency stop? | **Hardwired physical red STOP button on the robot, clearly visible/accessible — remote e-stop NOT permitted** (§12.2, V1.1 correction) |
| Suction allowed? | Yes, if no residue/damage to field or objects (§11.18) |
| Transport box? | 1 box: ≤ 1500 × 800 × 900 mm, gross ≤ 180 kg (§11.17) |

**Viva-style reasoning Qs:**
- *Why does BR need Freeze/Resume if it's autonomous?* → lets referees safely send someone into a Shared Area (e.g., retry) without the robot moving — safety interlock, not control.
- *Can you use a Raspberry Pi camera on TR to tell BR where blocks are?* → No — that's conveying encoded TR→BR information (§11.11(b)); BR must decide from its own sensors.
- *12 V battery × 3 in series?* → 36 V nominal > 24 V — **illegal**; 2 × 12 V = 24 V OK, and actual max still ≤ 42 V.
- *Which rule kills a 48 V motor?* → §11.13 (24 V nominal) — even though 48 V < 42 V circuit cap? → No: nominal battery ≤24 V AND circuit ≤42 V both must hold; 48 V exceeds the 42 V cap too.
- *Why is Zigbee attractive for TR control?* → allowed band, mesh, low power — but §11.10: organizer guarantees **nothing** about RF quality at the venue (2.4 GHz congestion is your problem).

## 7. Safety (§12) & misc (§13)

- Safety is the **highest priority**; mandatory organizer safety gear during matches/practice/setup (§12.4).
- No dangerous power sources/materials/mechanisms; no flying parts — battery smoke/fire = DQ-grade safety violation (§7.2 old / §7.3).
- ±5% tolerance on field/object dimensions unless stated (§13.2); unlisted situations → Panel of Judges decides (§13.1); rules updates published on aburobocon2027.id (§13.4).
- Field colors/materials (§14): plywood + water paint; Building Spot RGB 40-100-50; Transfer Red 245-170-60 / Blue 60-170-245; Mustika = original Mikasa V300W (Pantone 1235C/3591C), **no paint/coating allowed**.

## 8. V1.0 → V1.1 redline changes (favorite viva question: "what changed?")

1. **Sanctuary Mandate** now requires **two** Complete Towers simultaneously (was looser) — one must be in a Shared Area.
2. **No stairs L1→L2** — BR climbs onto L2 from any L1 position (field drawings → separate Appendix).
3. **Failure** is a new category: Earth Block out-of-place = invalid block, **no** Forced Retry.
4. **Carry limits** codified: TR 3, BR 2; Mustika-carrier carries no blocks.
5. **Mustika:** direct TR→BR handover without floor contact; pillar auto-refilled; one in possession at a time; only first enshrinement valid; dropped Mustika removed.
6. **Sky Block scoring:** must rest flat, one team color fully up; flip-only rule; out-of-sequence/leak = invalid + Forced Retry (6.3).
7. **Tower Protection (6.6):** any collapse/displacement → Forced Retry *regardless of intent*, tower restored (replaces old 7.2).
8. **Weight:** 60 kg combined (both robots + batteries + remotes + cables), not 50 kg each.
9. **Zigbee standard corrected** to IEEE 802.15.4; **BR Freeze/Resume added** (11.4); **BR start method added** (11.19); **e-stop must be hardwired** (12.2).
10. Unauthorized Touching → **Disqualification** (procedure in Participation Guideline).
11. Transfer points awarded **once per block** (8.1); final tie-break → judges (9.3.5); Sky Block initial layout figure made mirror-symmetric.

## 9. Rapid-fire round (answer, then stop)

1. Match length? → 3 min, no early win.
2. TR max blocks? BR max? → 3 / 2.
3. Complete Tower? → 2 Earth + 1 Sky in order on a Building Spot.
4. Sanctuary Mandate? → 2 towers up at once, 1 in a Shared Area.
5. Mustika points? → 250, first one only.
6. Earth dropped — retry? → No, Failure; block invalid only.
7. Both robots total weight? → ≤ 60 kg.
8. Battery nominal max? → 24 V.
9. E-stop? → hardwired red button on robot; remote not permitted.
10. Can TR talk to BR? → Never — sensors only; start switch + Freeze/Resume are the only exceptions.
11. Who's fully autonomous? → BR; TR may be manual.
12. Sky Block flip legal? → Yes, same tower only; moving it = Forced Retry.

## See also

- Hardware viva: [[nexus-components-viva-level1]] · [[nexus-components-viva-level2]]
- Theory bank: [[nexus-theory-rapidfire]] · INDEX: [[01-Areas/Engineering/nexus-robotics/INDEX]]
- Source: `raw-sources/ABU_Robocon_2027_Rulebook_V1.1_Redline-1.pdf` (immutable) — field drawings live in a **separate Appendix document** (rule 13.6), not yet in the vault `(TBC)`
