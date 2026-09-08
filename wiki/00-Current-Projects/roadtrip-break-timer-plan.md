---
date: 2026-09-09
description: "Roadtrip break-timer design: car pulls to the shoulder and refuels during breaks. Four implementation options (manual pull-over, Pomodoro auto-pairs, mid-route pit stops, fuel-gauge metaphor) with code anchor points, open questions for discussion."
tags: [builds, roadtrip, plan, break-timer, pomodoro, canvas, ux]
last_updated: "2026-09-09"
confidence: high
relations:
  depends_on: "[[roadtrip-focus]]"
  relates_to: "[[quote-pomodoro]]"
---

## For future agent
Design record for the roadside break timer (user request 2026-09-09, build NOT started). Holds 4 implementation options + code anchors + open questions. Discussion scheduled next session; do not implement until user picks an option after discussion.

# Roadtrip Break Timer — car pulls over & refuels (plan)

> **Status:** OPEN — discussion tomorrow. **North Star:** builds (roadtrip is the favourite build; breaks complete the Pomodoro loop).

## Concept

A break mode where the car eases onto the shoulder, the world stops scrolling, hazards blink, the engine hum fades, and a fuel bar fills 0→100 over the break countdown. Break over → back on the highway.

## Why it fits the existing code (anchors)

- `RoadtripCanvas.tsx` switches behavior off refs (`isRunningRef`/`isPausedRef`, pause freezes dash scroll at `canvas:138-140`, car drawn at `canvas:221-261`). A `parkedRef` follows the same pattern: freeze scroll, ease `carX` to the shoulder, kill the bob, blink hazards.
- Pause accounting (`pausedRef`/`pausedAt`, `RoadtripExperience.tsx:84,92`) already excludes paused time from trip duration — a frozen session clock during breaks keeps stats clean for free.
- Breaks stay **local-only**: never POST as `sessions` rows (no migration, no RLS touch), same as the reset-path precedent except even the reset path posts — breaks must not.

## Options (easiest → richest)

### A. Manual "Pull over" (recommended v1)
Button anytime (or post-finish): pick 2/5/10/15 min → car parks, countdown, "Back on road" resumes or starts next route. Smallest build, full user control.

### B. Pomodoro auto-pairs
Classic rhythm: 25→5, 50→10 (the Tk [[quote-pomodoro]] already had these pairs). Finishing a focus route auto-offers (or auto-starts) its paired refuel stop. Slightly more timer state.

### C. Mid-route pit stops
On 90/120-min hauls, a "Pit stop?" nudge midway; accepting freezes the session clock, parks the car; resume continues the **same** run. Best for long drives, most timer-state care (must not trip the one-fire guard or mint a second row).

### D. Fuel-gauge metaphor (v2)
Every route burns fuel (progress = fuel draining); breaks are refuel stops; gauge persists across trips in `rf_state`. Most gamified, most canvas work.

## Open questions for tomorrow

1. Manual-first (A) vs auto-cycle (B)? Default recorded: A first, B later.
2. Break presets: 2/5/10/15 or custom input like routes?
3. Auto-return when countdown ends vs manual "Back on road"? (Auto-return risks yanking attention; manual risks forgotten breaks.)
4. Sound: fade hum to silence, keep noise bed, or engine-off click? (Noise bed toggle already exists.)
5. Should breaks appear anywhere in Trip Log/stats, or fully invisible? (Default: invisible.)
6. Mid-route pit stops (C) in v1 scope or deferred?

## Definition of done (when built)

- [ ] Car visibly parked at shoulder + fuel bar fills over countdown
- [ ] Session clock frozen during break (trip duration/stats unchanged)
- [ ] Zero `sessions` rows created by breaks (verify table count delta = 0)
- [ ] `tsc` + webpack build green, Vercel deploy, live test
- [ ] Vault: log entry, commit + push

## Links

- Build home: [[roadtrip-focus]] · predecessor rhythm: [[quote-pomodoro]] · prod reference: [[pomodoro-web/overview]]
- Builds hub: [[00-Current-Projects/INDEX|Builds INDEX]]
