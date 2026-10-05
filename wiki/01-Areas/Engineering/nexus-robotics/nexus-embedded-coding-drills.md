---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Coding Interview Prep"
unit: "Live Coding Drill Hub"
date: 2026-10-05
description: "Hub and method page for the Nexus Robotics live-coding drills - the eight-step narration loop, time boxes, task index across the C and Python spokes, priority order by time available, and per-task verification status."
tags: [btech, kjsce, nexus-robotics, interview-prep, embedded, live-coding, method]
last_updated: "2026-10-05"
confidence: medium
---

## For future agent
Hub for the live-coding half of the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics prep pack]]. The 12 tasks were split across two spokes because the combined page crossed the 25 KB structure signal: [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills|C drills T1–T8]] and [[01-Areas/Engineering/nexus-robotics/nexus-python-drills|Python drills T9–T12]]. **The method on this page matters more than any individual task** — the failure being defended against is silence under a clock, not lack of syntax. Verification status is tracked per task in §4; read it before trusting any expected output.

# Live Coding Drills — Hub

## 1. The loop (this matters more than the tasks)

Per [[01-Areas/Business/careers/interview-counter-guide]] live-coding skeleton — rehearse until it's automatic:

```
1. Restate the problem. Confirm I/O with ONE example.        (30 s)
2. Brute force out loud + its complexity.                    (60 s)
3. Name the constraint that matters (O(1)? fixed memory?).   (30 s)
4. "Better approach before I code — does this work?"          (get the nod)
5. Code while narrating decisions, not keystrokes.
6. Dry-run ONE case + ONE edge case by hand.                 (60 s)
7. State final time/space complexity unprompted.
8. Offer a follow-up.  ("Want me to handle overflow / make it ISR-safe?")
```

**Time boxes:** C tasks 12–18 min each. Python 10–15 min. Never exceed the box — an unfinished task with a spoken approach scores higher than a finished task at minute 40 (the interviewer already knows you can finish).

**The silence rule:** if you have no idea, say the brute force out loud anyway. Partial credit starts at the first sentence.

**Narrate decisions, not keystrokes.** "I'm looping over the array because the input is unsorted" scores. "Now I'm typing a for loop" does not.

---

## 2. Task index

### [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills|Embedded C (T1–T8)]]

| # | Task | Time | Cluster |
|---|------|------|---------|
| T1 | Bit-field set/clear/test macros | 12 min | bitwise · start here |
| T2 | Saturating clamp + Q8 fixed-point | 15 min | overflow · integer-only math |
| T3 | Single-producer single-consumer ring buffer | 18 min | **the signature embedded task** — FIFO, `volatile`, ISR handoff |
| T4 | Non-blocking button debounce | 15 min | `millis` timing · state machine |
| T5 | ISR → main-loop flag handoff | 15 min | interrupts · critical sections |
| T6 | CRC-8 for a sensor frame | 15 min | bitwise · data integrity |
| T7 | Integer PID step with anti-windup | 18 min | **the control-loop task** |
| T8 | Fixed-window moving average, O(1) | 15 min | streaming · filter warm-up |

### [[01-Areas/Engineering/nexus-robotics/nexus-python-drills|Python (T9–T12)]]

| # | Task | Time | Cluster |
|---|------|------|---------|
| T9 | Telemetry CSV analysis | 12 min | closest to a real club task · reuses the Onyx muscle |
| T10 | Outlier rejection + rolling median | 12 min | sensor conditioning · **output is shorter than input** |
| T11 | PID with filtered derivative + windup guard | 12 min | control · the tuning harness |
| T12 | Serial frame parser | 15 min | protocols · incomplete-is-not-an-error |

---

## 3. Priority order by time available

| Time | Do | Why |
|---|---|---|
| **45 min** | T1 → T3 → T9 | bit ops, the embedded data structure, and the CSV muscle — the three highest-yield |
| **2 hours** | add T2 → T7 → T4 | now you also have fixed-point, the control loop, and non-blocking timing |
| **3.5 hours** | everything, then re-run the Onyx mock's Set C with C answers | one full simulation |

**Do not** drill T5–T6, T8, T10–T12 under time pressure. They are the backup pool in [[01-Areas/Engineering/nexus-robotics/nexus-interview-fallbacks]] §3 — read them *fast* (skeleton + narration beats only), don't solve them.

**Cut line:** if you're 20 minutes into the list and haven't finished T1, drop T2 and T7 and do T1, T3, T9 only. Three solid tasks beat five rushed ones — the interviewer sees one attempt, not your prep list.

---

## 4. Verification status — read before trusting an output

There is **no C toolchain on this machine** (`gcc`, `clang`, `cl`, `tcc` all absent), so **nothing has been compiled**. What was actually done:

| Task | Status | How |
|---|---|---|
| T1, T2, T3 | logic confirmed | re-implemented identically in Python and executed |
| T6 | logic confirmed | `crc8("123456789") == 0xF4` reproduced by running the algorithm |
| T8 | logic confirmed | the `2, 7, 15, 25…` warm-up sequence reproduced by simulation |
| T9, T10, T11, T12 | **exact** | executed directly on CPython 3.13 |
| T4, T5, T7 | **hand-checked only** | logic reviewed, not executed |

**Why this section exists:** the first draft of these pages asserted expected outputs from reading the code, and three of them were wrong (T8's warm-up, T10's output length, T11's saturation trace). All three are now corrected to the executed values, with *why* each surprise happens kept in the task text as teaching content. This is the argument for running code rather than trusting a plausible claim — logged as a durable lesson in [[Gotchas]].

If you compile the C, correct any drift here rather than letting the page and the compiler disagree.

---

## 5. Cross-links

- **Method:** [[01-Areas/Business/careers/interview-counter-guide]] (live-coding skeleton, F2 silent-coding, F4 bluffing) · [[01-Areas/Programming/dsa-interview-playbook]] (F3 timed-freeze)
- **Rescue mid-question:** [[01-Areas/Engineering/nexus-robotics/nexus-interview-fallbacks#4-stuck-mid-question--the-rescue-scripts]]
- **Theory for the non-coding questions:** [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]]
- **Sibling pack:** [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] (Onyx's mock — Set B is the Python CSV task, Set C is the Arduino talk)
- **C foundations:** [[01-Areas/Engineering/SPM/module-1-spm-c-basics]] (memory regions, compilation) · [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers]] (structs, padding, pointers) · [[01-Areas/Engineering/SPM/module-3-arrays]] (contiguity, sliding windows) · [[01-Areas/Programming/c-programming/index]]

*Home: [[01-Areas/Engineering/nexus-robotics/INDEX]]*