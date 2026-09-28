---
date: 2026-09-28
description: "The operating half of 'Comparing the Wrong Number' — the 9 failure modes that make the opportunity-cost framework collapse, and the 7-step protocol (track units not hours; write one line: what did this cost me)."
tags: [self-dev, opportunity-cost, marginal-returns, protocol, failure-modes, metrics, vanity-metrics, comparison, productivity, youtube-distillation]
type: [youtube-distillation-practice]
source_url: "https://www.youtube.com/watch?v=SliceDfqcH8"
source_channel: "avishi mishra"
last_updated: "2026-09-28"
confidence: high
relations:
  relates_to: "[[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]]"
  relates_to: "[[01-Areas/Self-Dev/comparing-the-wrong-number-math|Comparing the Wrong Number — The Mathematics]]"
---

## For future agent
The runnable half of [[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]], split out because it is used differently from the argument. The parent page answers *"why does grade-guilt feel like a character flaw?"* — this one answers *"what do I actually do on Sunday, and how do I know the framework is lying to me?"* Two parts: **§1 failure modes** (consult when a drill produces a suspiciously comfortable result — most of them are the framework being misused as a defence rather than a mirror) and **§2 the protocol** (a 2-change week, 3 habits a month, 2 decisions a semester). Notation ($h$, $k$, $S$, $MP_h$, $c$) and derivations are on the companion math page. Staleness caveat: none. Use for: "how do I stop feeling behind", "what should I track", "why did the accounting make me feel better without changing anything".

# Comparing the Wrong Number — Practice & Failure Modes

Parent: [[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]] · Maths: [[01-Areas/Self-Dev/comparing-the-wrong-number-math|The Mathematics]] · Source: [youtube.com/watch?v=SliceDfqcH8](https://www.youtube.com/watch?v=SliceDfqcH8)

The framework has exactly one hard precondition, stated by the speaker himself: **"This framework only works if your alternative is actually worth something… The math is a mirror not a defense."** Almost every failure below is a violation of that one line.

---

## 1. Failure modes

| Failure mode | What it looks like | Why the framework fails | Fix |
|---|---|---|---|
| **Fictitious opportunity cost** | "My time is worth a lot because I'm building a brand" — while actually scrolling | $c_p$ prices nothing; the alternative is not a real output, so the mirror reflects an empty room | Name the *specific deliverable* you gave up. If you can't, $c_p = 0$ |
| **Escaping disguised as a build** | 3 "side-project" hours that produce nothing shippable | Highest-$c$ alternative is fake, so the trade is strictly worse than it looks | Judge the alternative by the same output standard you want from study |
| **Input metric relapse** | Back to counting hours, streak-days, focus minutes | $MP_h$ is unobserved, so hours get mistaken for progress | Convert to syllabus units *before* recording anything |
| **Objective standard as a new comparison** | "My units this week vs my units last week vs a study influencer's" | The standard became another human yardstick; the Festinger loop re-closes | Compare against **your own** prior value only |
| **Exempting the expensive hour** | "My opportunity cost is high, so I don't have to do the hard subject" | The framework prices a trade; it does not license abandoning output entirely | Price it, *then* decide. High $c$ is not a waiver |
| **Total-as-return** | "They did 3 more hours than me, so they're 3 units ahead" | Confuses $h$ with $S$ and ignores differing $f$ and $k$ | Compare $\partial S / \partial h$ at your own margin, never $\Delta h$ |
| **Guilt-laundering** | Doing the accounting, then feeling *better* without changing anything | The mirror was read as a defence | The output is the one written line. No line, no framework |
| **Comparison as the wrong target** | Treating "I feel behind" as the problem to fix | Comparison is the *symptom*; the missing standard is the *cause* | Supply the standard; the feeling usually resolves unassisted |
| **Strawman topper** | Assuming the comparison target's trade also costs them nothing | Their $c$ may be near zero, which is exactly why the asymmetry exists | Price *your own* $c$; theirs is irrelevant to your budget |

### The two that matter most

**Guilt-laundering** is the failure mode the framework is most likely to produce in this vault, because the vault rewards writing good notes. A beautifully written cost analysis that produces no changed behaviour is strictly worse than no analysis, because it discharges the feeling while leaving the drift. The one-line test: **did the week end with a written line?** If not, nothing happened.

**Fictitious opportunity cost** is the mirror's own failure. Once you have a vocabulary for "my time is valuable", it becomes available as a *story* — and stories are much cheaper than deliverables. The check is always the same: name the specific thing. A deliverable, a merged PR, a client brief. If the noun phrase does not exist, $c = 0$ and the accounting returns nothing.

---

## 2. The protocol

The speaker's own prescription is deliberately minimal: *"change the variable this week. Just try one thing: track units instead of hours. And at the end of this week, write one thing: what did this cost me?"* Everything below is that, scaled.

### This week — the entire intervention (2 changes)

1. **Switch the tracked variable.** Delete hours from your tracker. Track **syllabus units covered** per subject. Define "one unit" *before* you start (one lecture + its notes; one chapter; one problem set) — the anchor must be absolute, not a feeling. This is the load-bearing step: a unit defined by feeling is an input metric wearing an output metric's clothes.
2. **Write the one line every Sunday:** *"What did this cost me?"* Name the specific best-forgone alternative for the week. Not "I wasted time" — the actual deliverable, client, or build hour you traded away.

### This month

3. **Price your hours, explicitly.** For your three main time sinks (coursework, builds, content), write down what the marginal hour is actually buying. Any alternative you cannot name is a $c = 0$ hour — and those are the ones to cut, not the expensive ones.
4. **Find your bend point.** Which subject's $MP_h$ collapses earliest? (His answer: anything maths-y. Plausibly true here too — see the [[01-Areas/Engineering/INDEX|Engineering INDEX]] maths row and the [[01-Areas/Engineering/engineering-math/formula-sheet-am|engineering-math formula sheet]] backlog.) Put that subject's hardest units at the *start* of the week, when $k$ is highest — not at hour 6 of a day.
5. **Build the objective standard for your builds too.** "Units" transfers: merged PRs, deployed features, finished modules. A build measured in hours is as unmeasurable as a course measured in hours.

### This semester

6. **Own the line item.** Decide deliberately which side of the trade you are funding. There is no free version — you are buying coursework with build time, or vice versa. Write the choice down once a semester; re-deciding every week *is* the drift he is describing.
7. **Stop collecting toppers as data.** Their $c$ is not your $c$. Remove the comparison trigger that keeps re-supplying the nearest human; replace it with your own syllabus line.

---

## 3. Running the drill in this vault

- **Weekly ritual, 5 minutes, Sunday.** (1) count syllabus units per subject, (2) write the one line. That is the whole loop; anything more is over-engineering and will not survive a bad week.
- **The one-line test is the gate.** No line written ⇒ the week's accounting is void, regardless of how good the notes were.
- **Anti-drift check.** "I'm behind the topper" is the *symptom*. If a week ends with no written line, the framework was used as a mood regulator, not a decision tool.
- **Keep builds and coursework on the same scale.** Both get "units". Comparing a course in hours to a build in vibes is the original error in a new costume.
- **Named trade, concretely.** The question the framework forces each week: *for the hour I was going to spend on [[01-Areas/Business/quant-finance/quantitative-finance-foundations|quant foundations]], what was the actual best forgone alternative?* Not "scrolling" — name the thing. (Live context: [[00-Current-Projects/INDEX|current projects]] vs coursework vs the [[North Star]] goals.)

---

## Related

- [[01-Areas/Self-Dev/comparing-the-wrong-number|Comparing the Wrong Number]] — the argument, the disclaimer, the source registry, the quote bank.
- [[01-Areas/Self-Dev/comparing-the-wrong-number-math|The Mathematics]] — shadow price, production function, Cobb-Douglas/Euler, metric table, the $c = 0$ boundary case.
- [[01-Areas/Self-Dev/productivity/overview|Productivity Overview]] — $Productivity = Output/Input$ and Pillar 7 (Completion & Review), where the weekly ritual belongs.
- [[01-Areas/Self-Dev/productivity/deep-work-attention-economics|Deep Work]] — the $MP$ decay that step 4 is scheduling around.
- [[01-Areas/Self-Dev/digital-wellness|Digital Wellness]] — scrolling as the canonical $c = 0$ alternative behind failure modes 1 and 2.
- [[01-Areas/Self-Dev/self-mastery/temptation-mastery|Temptation Mastery]] — the fortress model for the same drift, in the self-mastery vocabulary.
