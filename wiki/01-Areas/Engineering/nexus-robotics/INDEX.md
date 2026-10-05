---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Coding Interview Prep"
unit: "Module Hub"
date: 2026-10-05
description: "Nexus Robotics club coding-interview prep hub (interview 2026-10-06): embedded C drills, Python telemetry tasks, theory rapid-fire, and a tiered fallback ladder if prep time collapses."
tags: [btech, kjsce, nexus-robotics, interview-prep, embedded, c-programming, python, robotics-club]
last_updated: "2026-10-05"
confidence: medium
---

## For future agent
Hub for the **Nexus Robotics** club coding interview scheduled **2026-10-06** (user-confirmed; time/venue/round-count `(TBC)`). Built as the Onyx sibling — [[01-Areas/Engineering/aeromodelling/INDEX|Team Onyx]] was a student robotics/aero club, so this reuses that proven shape (theory rapid-fire → live code → STAR → mock) but retargets the coding to **embedded C** (bit ops, ring buffers, ISR-safe patterns, fixed-point) plus **Python** telemetry/analysis tasks. No Nexus source material exists in `raw-sources/` — every question here is authored from standard embedded-systems practice and the user's own SPM C-course, so questions are **generic-club-shaped, not sourced from a Nexus notice**. If a Nexus notice/email/syllabus turns up later, re-ingest and correct the guesses marked `(TBC)`.

# Nexus Robotics — Coding Interview Prep

> **North Star alignment:** serves **FE RAI** (robotics club recruitment = the RAI hardware/robotics thread) and **builds**. Same target as Onyx — a club track that compounds into portfolio evidence, not a distraction from coursework.
> **Sibling pack:** [[01-Areas/Engineering/aeromodelling/INDEX|Team Onyx pack]] — reuse its mock structure and answer-key style.
> **Method:** [[01-Areas/Business/careers/interview-counter-guide]] (narrate while coding; honest IDK; live-coding skeleton).

## Page map

| Page | What it is | Time to use |
|------|-----------|--------------|
| [[nexus-theory-rapidfire]] | 60-question embedded/roboting theory bank in short answers, grouped (memory & C traps · MCU peripherals · comms buses · sensors · control · ROS2). Ends with a 15-question must-know core. | Read once tonight, then drill the core 15 before sleep |
| [[nexus-embedded-coding-drills]] | **Drill hub** — the 8-step live-coding narration loop, time boxes, priority order by time available, and per-task verification status. Read this before any drill. |
| [[nexus-c-embedded-drills]] | **8 C drills (T1–T8)** — bit-field macros, saturating clamp + Q8 fixed-point, SPSC ring buffer, non-blocking debounce, ISR→main-loop flag handoff, CRC-8, integer PID with anti-windup, O(1) moving average. Each has narration script, expected output, complexity, 2–3 follow-ups. | Do 3–6 under a timer tonight; the rest are the backup pool |
| [[nexus-python-drills]] | **4 Python drills (T9–T12)** — telemetry CSV parse, outlier rejection + rolling median, PID with filtered derivative, serial frame parser. All outputs executed and verified. | T9 reuses the Onyx CSV muscle — start here if the round is Python-leaning |
| [[nexus-interview-fallbacks]] | **The backup mechanism.** Three prep tiers (T-mini 45 min / T-core 2 h / T-full 3.5 h), each with an explicit cut line, plus device-failure logistics, the honest-IDK script bank, and the "prep ran out of time" triage. | Read this FIRST if you have less than 2 hours |
| [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] | Onyx's live-code mock (Python prop/CSV + Arduino talk) — closest thing in the vault to a real dry run; re-run its Set B/C with C versions of the same tasks | If time remains |
| [[01-Areas/Engineering/robotics/robotics-fundamentals]] | Derivation-level kinematics, PID, Kalman, SLAM, planning | Only for the "why" follow-ups, not cramming |

## Language revision (plain language, full coverage)

Written specifically for this interview — same **plain words → code → trap** structure, with the traps collected in one list at the end:

| Page | Covers |
|------|--------|
| [[01-Areas/Programming/c-interview-revision-plain-language]] | Every C construct in everyday words — types, the integer-division trap, `=` vs `==`, arrays and the `sizeof` length trick, strings and `'\0'`, pointers ("a piece of paper with an address on it"), structs and padding, storage classes, files — then §15 **embedded C**: `volatile`, ISR discipline, why firmware avoids `malloc`, fixed-point, the five memory regions |
| [[01-Areas/Programming/python-interview-revision-plain-language]] | Containers and when each is right, slicing, comprehensions, classes vs instance attributes, exceptions, `with`, generators, decorators — plus §18, a table of **C habits that will bite you** |

## Project stories (if they ask "tell me about something you've built")

| Page | The one thing it proves |
|------|-------------------------|
| [[01-Areas/Engineering/nexus-robotics/nexus-interview-fallbacks#5-star-story-skeletons-6-written-not-improvised|§5 of the fallback page]] | The six STAR skeletons, written once and reused |
| [[wiki/00-Current-Projects/projects/handsens101-explained\|handsens101 explained]] | Sense→filter→act in ~100 lines; the smoothing-before-actuation decision; honest AI-assisted provenance |
| [[wiki/00-Current-Projects/roadtrip-pomodoro-explained\|roadtrip-pomodoro explained]] | Single-threaded GUI + daemon-thread hand-off; 1 Hz timer vs 60 fps animation clocks; a whole world generated from a distance variable; a design where the vault *is* the database |

> Both builds are **AI-assisted** (owner-confirmed 2026-09-24). Neither explained page tells you to claim them as hand-written — §8 of each has the honest line to say instead, because a caught bluff discredits every other answer.

## Suggested tonight plan (if you have ~2 hours)

1. **[[nexus-theory-rapidfire]]** — read the whole bank once (35 min). Do not memorise; just build the retrieval path.
2. **Drill the "core 15"** at the bottom of that page out loud, one breath each (10 min).
3. **[[nexus-embedded-coding-drills]]** — do **T1, T2, T3, T7, T9** under a visible timer, narrating aloud (45 min). Skip the rest.
4. **[[nexus-interview-fallbacks]]** — §1 tier decision + §5 honest-IDK lines + §6 logistics (10 min).
5. Sleep. Per [[interview-counter-guide]] energy rules: interview day carries no other heavy cognitive work.

**If you'd rather refresh the languages first** (worth it if you haven't written C in a while), swap step 1 for a fast pass over [[01-Areas/Programming/c-interview-revision-plain-language]] §14–17 and [[01-Areas/Programming/python-interview-revision-plain-language]] §17 — the two trap lists, read out loud. That is a 20-minute substitute for re-reading a whole course, and it covers exactly what gets asked.

## What is NOT here (deliberate)

- **No fabricated Nexus specifics.** Round count, duration, syllabus, and interviewer names are `(TBC)` until the user supplies the notice.
- **No DSA grind.** This is an embedded-coding club round, not a DSA OA — the drills are systems-flavored. If the notice turns out to include DSA, go to [[01-Areas/Programming/dsa-interview-playbook]].
- **No ROS2 install or Gazebo work.** Concept questions only ([[01-Areas/Engineering/robotics/ros2-cheatsheet]] for command recall).

## If a Nexus notice arrives later

1. Drop the PDF/screenshot into `raw-sources/` (immutable).
2. Correct every `(TBC)` in these pages with the real specifics — the single-source-of-truth law applies.
3. Re-run `python .scripts/update-graph-colors.py` + `python .scripts/generate-index.py` if you add a page.
4. Append the correction to `wiki/log.md` and `brain/Gotchas.md` if it contradicts something already written.

## Cross-Domain Bridges

- C foundations → [[01-Areas/Engineering/SPM/syllabus-316U06C107|SPM C-course]] (structures/pointers/padding: [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers]]; memory layout: [[01-Areas/Engineering/SPM/module-1-spm-c-basics]])
- Deeper C practice → [[01-Areas/Programming/c-programming/index|C programming library]]
- Robotics theory → [[01-Areas/Engineering/robotics/index|Robotics & ROS2 hub]]
- Club-pack sibling → [[01-Areas/Engineering/aeromodelling/INDEX|Team Onyx]]
- Interview method → [[01-Areas/Business/careers/interview-counter-guide]] · [[01-Areas/Business/careers/example-question-bank]]
- Hardware thread context → [[01-Areas/Engineering/engineering-drawing/fusion/INDEX|Fusion track]] (the prints that these builds need)