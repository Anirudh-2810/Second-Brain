---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Coding Interview Prep"
unit: "Fallback Ladder & Logistics"
date: 2026-10-05
description: "The backup mechanism for the Nexus Robotics interview prep — three time-boxed prep tiers with explicit cut lines, a stuck-mid-question rescue script bank, device and power failure logistics, and post-interview debrief capture."
tags: [btech, kjsce, nexus-robotics, interview-prep, fallback, contingency, logistics, failure-mode]
last_updated: "2026-10-05"
confidence: medium
---

## For future agent
This is the **backup mechanism** the user asked for: a way to prepare that degrades gracefully when time, energy, or hardware runs out, instead of collapsing. Built for the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics interview]] on **2026-10-06**, but the tier structure is reusable for any club or technical round. Method comes from the failure-mode taxonomy in [[01-Areas/Business/careers/interview-counter-guide]] and [[01-Areas/Programming/dsa-interview-playbook]] — every fallback here maps to a named failure mode rather than being invented. **Read §1 first if you have under two hours**; it is the routing decision and everything after it is only reached by choosing a tier.

# The Backup Mechanism

## Why this page exists

The failure mode being defended against is not "I didn't study enough." It's **"I had three hours, spent them badly, and went in with nothing loadable."** Prep that only works at full capacity is a single point of failure. A backup mechanism has tiers: each one is a *complete, shippable* prep state, and dropping a tier loses polish, never viability.

Governing rules:
- **Never trade sleep for tier 3.** A tired candidate loses working memory — precisely the resource the interview consumes (F3 in the DSA playbook). Sleep is part of the prep.
- **No new material in tier 3.** Retrieval only. Reading something new the night before is the classic failure of confusing consumption with preparation.
- **Stop the moment a tier completes.** Do not drift into tier 4 and start burning hours on polish.

---

## 1. Tier decision — pick before you start, not during

| Time genuinely available | Tier | You are walking in with |
|---|---|---|
| Under 45 min | **Tier 0 — Survival** | Core-15 theory recited + the honest-IDK script + logistics verified. Enough to not freeze. |
| ~2 hours | **Tier 1 — Standard** | Full theory bank read once + 5 timed coding tasks + STAR stories written + logistics. **This is the expected case.** |
| ~3.5 hours | **Tier 2 — Thorough** | Everything in Tier 1 + the remaining 7 coding tasks + one full mock run + the log re-read. |
| Interrupted / low energy | **Tier 0.5 — Fragmented** | 3 × 25-minute blocks, each one self-contained (below). |

**Anti-drift rule:** if you are a robot club applicant, this serves the **FE RAI** North Star thread. But if prep would eat the whole evening and you have coursework due, coursework wins — the club will recur, the submission deadline won't.

---

## 2. The tiers

### Tier 0 — Survival (45 min)

| Time | Do | Source |
|---|---|---|
| 15 min | Recite the **core-15** table out loud. Twice. No reading — retrieval only. | [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]] §Core 15 |
| 15 min | Write **3 STAR stories** from memory. Four beats each: situation, task, action, result. | §5 story skeletons below |
| 10 min | Memorise the honest-IDK sentence and the stuck-script. | §4 |
| 5 min | Verify the tech rig. | §6 |

**This tier is genuinely sufficient to not freeze.** It is not the ideal — it's the floor that still clears a bar. Ship it and stop.

### Tier 0.5 — Fragmented (3 × 25 min)

For a broken evening — 25 min here, dinner, 25 min there. Each block stands alone; there's no "continue where I left off".

- **Block 1 (theory):** questions 1–20 of the rapid-fire bank (memory layout + C traps). Read the question, answer aloud, check.
- **Block 2 (code):** do **T1** and **T9** from [[01-Areas/Engineering/nexus-robotics/nexus-embedded-coding-drills]] with the timer visible.
- **Block 3 (control + rig):** theory questions 46–55 (the PID/control cluster), then §6 logistics.

### Tier 1 — Standard (2 h) — the expected case

1. Read the full [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]] bank once, 35 min. Build the retrieval path; don't memorise.
2. Drill the core-15 out loud, 10 min.
3. Coding tasks **T1, T2, T3, T7, T9** with a visible timer, narrating aloud, 45 min.
4. Write the 6 STAR stories, 20 min.
5. §4 rescue scripts + §6 logistics, 10 min.
6. Sleep.

**Cut line:** if you're 20 minutes into step 3 and haven't finished T1, drop T2 and T7 and do T1, T3, T9 only. Three solid tasks beat five rushed ones — the interviewer sees one attempt, not your prep list.

### Tier 2 — Thorough (3.5 h)

Everything in Tier 1, then: all remaining coding tasks (T4, T5, T6, T8, T10, T11, T12), one full mock run from [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] with the Set C Arduino talk answered in **C** rather than Python, and a re-read of `wiki/log.md` for prior fixes.

**Cut line:** if the mock reveals a fumble, drill *only* that one area for 20 minutes and stop. Do not spiral into re-preparing everything.

---

## 3. What to skip at every tier

- **New tool installs.** No Arduino IDE, no toolchain, no ROS2 setup the night before. Installing a tool is not prep; it is procrastination with a plausible costume.
- **Full DSA practice sets.** This is an embedded club round, not a DSA OA. If a notice later says otherwise, that becomes [[01-Areas/Programming/dsa-interview-playbook]]'s problem, not tonight's.
- **Re-reading your own vault notes from scratch.** Retrieval from existing notes, not fresh study. Reading feels productive and is not (F4 — solution-reading addiction).
- **Solo deep-dives into SLAM, Kalman filters, or MPC.** Deep background is for T3-quality follow-up depth on one question, not a night-long session.

---

## 4. Stuck mid-question — the rescue scripts

This is the highest-value section. Silence is the only losing move (F2, silent coding).

### The stuck ladder

```
1. STOP talking for at most 10 seconds. Say: "Let me think out loud."
2. Brute force it aloud. Partial credit starts here — always.
3. Solve a TINY version by hand on paper. The pattern usually surfaces in the trace.
4. Restate what you know for certain: "the input is sorted, so I can binary-search…"
5. Name the related problem you DO know: "this looks like two-sum with a hash map — "
6. Honest + structured: "I'm torn between a hash map and sorting. I'd start with the
   hash map because n is unbounded, and here's how I'd benchmark it."
7. Never exceed ~90 seconds of silence before returning to step 2.
```

### The honest-IDK script — pre-commit it, don't improvise

F4 is *bluffing under follow-up*, and the defence is a sentence rehearsed in advance:

> **"I don't know the specifics of that. Here's how I'd find out: I'd check the datasheet register map first, then search for an example driver."**

Variants for different flavours of not-knowing:

| Situation | Sentence |
|---|---|
| Don't know the exact value | "I don't remember the exact figure — I'd look it up in the datasheet. What I do remember is that it's roughly in this range because…" |
| Never used it | "I haven't used that. Given the docs I'd read the reference example first, then run the smallest version that works before touching the real target." |
| Don't understand the question | "Can I restate what I'm hearing you ask? I want to make sure I build the right thing." *(buys you time and is always safe)* |
| Genuinely out of your depth | "That's beyond what I've worked with. I'd want to understand it properly before claiming otherwise — could you tell me how it's used here?" |

**Why these score:** interviewers are pattern-matching for future colleague behaviour. An honest IDK with a *method* attached reads as reliable. A bluff that collapses under one follow-up reads as noise, and it costs you every other answer too.

### Narration, not keystrokes

Comment the decision, not the character:

- ❌ "so I'm typing a for loop now and incrementing i"
- ✅ "I'm looping over the array because the input is unsorted — I'd rather do one pass with a hash map, which is O(n), than sort first"

---

## 5. STAR story skeletons (6, written not improvised)

F6 is improvising behavioural answers per interview, which produces inconsistent stories. Write these six **today**, in full sentences, then read them aloud once. Vault mines already in your dailies: the second-brain build, the stock-agent bug hunts, guitar-repair persistence, the ₹250-gig refusal, the DataZen/Onyx post-mortem.

| Story type | Situation you already have | What "result with a number" looks like |
|---|---|---|
| **Failure** | stock-agent bug hunt, or a vault link/metadata miss | "Found it in X minutes by checking Y, changed my process to Z" |
| **Conflict** | peer debug sessions in a group project | what *you* contributed to the mess, then the resolution |
| **Initiative** | the second-brain vault itself — built a system nobody asked for | "it now has N notes across M modules" |
| **Deadline pressure** | the SPM submission batch, or the fusion/editing ingest stretch | what you cut, and what you refused to cut |
| **Learning fast** | Arduino/embedded from a C base, this week | concrete: what you read, what you built, what broke |
| **Disagreement → commit** | the Fusion-vs-SolidWorks scoping decision | the trade-off you reasoned about, then committed |

Rehearsed-written beats written beats improvised. Six stories, 90 seconds each, is the whole requirement.

**Weakness question:** real, non-disqualifying, with active mitigation. "Beginner at embedded hardware — I've closed it with C from the SPM course plus a deliberate Arduino build plan." Never the "perfectionist" cliché.

---

## 6. Logistics — the boring part that actually fails

Per [[01-Areas/Business/careers/team-datazen-interview-prep]] and your own history: **the Vivobook K3405VF built-in mic is not working out of the box** ([[Profile]]), and the laptop battery health is already 49%. These are not hypotheticals — they have bitten a previous round.

### Rig checklist (Tier 0 step 5, 5 minutes)

- [ ] **Audio:** earphones + phone mic, tested on an actual call *before* the interview. Not "should work" — a 30-second test call.
- [ ] **Power:** charger plugged in; the 49% battery means treat a 1-hour interview as if it could be the last thing on battery.
- [ ] **Video:** camera angle tested, background checked, second person not walking behind you.
- [ ] **Editor:** the compiler/editor open with the empty file already there. Tab indentation on. **Font size up** — a strained reader codes worse.
- [ ] **Network:** know the backup. Phone hotspot, and the hotspot password written down where you'll find it.
- [ ] **Water, pen, paper** — for tracing by hand. The tiny-version-by-hand rescue in §4 needs a surface.

### If the tech fails mid-interview

Say it plainly and keep going. This is a logistics problem, not a competence signal.

> "My audio dropped — can you hear me now? While we sort that, let me keep talking through my approach so we're not losing time."

Then narrate the design aloud and write it once audio returns. An interviewer who sees you handle a failure calmly scores it *positively* — it's the same trait as debugging a flaky sensor.

### Offline contingency

Interview location `(TBC)`. If it's offline/paper: the C and Python answers in [[01-Areas/Engineering/nexus-robotics/nexus-embedded-coding-drills]] are written as real code you can transcribe. Pseudocode acceptable for the sketch parts — write the function signature, the loop, and the comment explaining the invariant. That scores; a blank page does not.

---

## 7. Post-interview — do this within 2 hours, while it's warm

The debrief is how the next round improves. Bank it per the energy rules in [[01-Areas/Business/careers/interview-counter-guide]].

Capture, in a `daily/` note:
1. Every question asked, verbatim if you can recall it.
2. Where you stumbled — the specific drill to fix it (map via the "Fumble routing" table in [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]]).
3. What the interviewer *pushed* on — that tells you what the club actually cares about, which is worth more than the questions themselves.
4. What you'd automate, given this team — the "what would you do in week one" answer is a strong closer.

Then append the outcome to `brain/Wins.md` or `brain/Patterns.md` depending on the result, per the routing table in [[Home]]. Even a rejection carries a reusable lesson; a loss with no write-back is a repeat.

---

## 8. Anti-patterns — what a backup mechanism must not become

| Trap | Why it fails |
|---|---|
| Re-preparing everything after one fumble | Perfectionism before shipping — an explicit anti-goal in [[North Star]] |
| Prepping until 3am to "use the time" | Sleep loss costs the working memory the interview needs; guaranteed net-negative |
| Rehearsing answers to imagined specific questions | F6 — builds scripts, not the person who can improvise |
| Silently coding to seem fast | F2 — the interviewer disengages and you have no partial credit |
| Bluffing a follow-up to protect ego | F4 — one collapsed bluff discredits every other answer |
| Treating Tier 3 as mandatory | Interpreting the ladder as a quota converts a fallback into a source of guilt |

**The one-line version:** ship the highest tier that fits the time you have, then stop and sleep.

---

*Home: [[01-Areas/Engineering/nexus-robotics/INDEX]] · Theory: [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]] · Drills: [[01-Areas/Engineering/nexus-robotics/nexus-embedded-coding-drills]] · Method: [[01-Areas/Business/careers/interview-counter-guide]]*