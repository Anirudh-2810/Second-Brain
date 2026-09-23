---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Interview"
unit: "Interview Mock 01"
date: 2026-09-23
description: "Oral + live-code mock for the Team Onyx coding interview: theory rapid-fire, Python prop/CSV tasks, Arduino delay-vs-millis talk, STAR stories with answer key."
tags: [btech, aeromodelling, team-onyx, interview, mock, python, arduino]
last_updated: "2026-09-23"
confidence: high
---

## For future agent
Mock built for Anirudh after Round-1 clear (2026-09-23), coding-first software-only pitch, no hardware beyond one ASL LED lab. Candidate is comfortable live-coding Python on screen. Run out loud with visible timer per [[01-Areas/Business/careers/example-question-bank]] drilling laws. Sources: [[esc-deep-dive]], [[propulsion-system-deep-dive]], [[workshop-ppts-merged]], [[airplanes-for-juniors-foundations]], [[avionics-rc-stack]], [[01-Areas/Business/careers/interview-counter-guide]].

# Team Onyx Interview Mock 01

> Hub: [[INDEX]] · Application: [[01-Areas/Business/careers/team-onyx-application]] · Method: [[01-Areas/Business/careers/interview-counter-guide]] (narrate while coding; silence is the only losing move; honest "I don't know, here is how I would find out").

## How to run

Answer out loud, one pass, no pauses to read. Misses become Anki cards in your phrasing. Score each set pass / partial / fail; weakest set decides the next drill page.

## Set A — rapid-fire theory (say in one breath each)

1. ESC three wire sets — where does each go?
2. PPM signal — what is it, who sends it, who receives it?
3. BEC — purpose, voltage, what does OPTO imply?
4. 10 A motor — which ESC rating and why?
5. 8×5 prop — numbers mean what, and 8×5 vs 8×4?
6. kV — definition; 1800 kV on 12 V?
7. 2200 kV on 3S nominal — max rpm?
8. 3S LiPo — nominal, fresh, land-by voltages?
9. 2200 mAh 25C — max continuous amps?
10. Brushed vs brushless — wires, efficiency, team default?
11. Outrunner vs inrunner — which drives a prop directly?
12. Tx 2.4 GHz 6 channels — name the six.
13. Rx binding rule + what powers the Rx?
14. Servo speed defined over how many degrees, under what load?
15. Lift vs drag directions; flap effect on take-off vs landing.

## Set B — live Python (code on screen, narrate decisions)

Narrate per the live-coding skeleton: restate, brute force, bottleneck, nod, code, dry-run, complexity, offer follow-up.

### Task 1 — prop matcher

```python
def max_rpm(kv: int, volts: float) -> float:
    return kv * volts

def safe_esc(motor_amps: float) -> float:
    # headroom rule: next standard size up, never exact match
    for size in (12, 15, 18, 20, 30, 40):
        if size > motor_amps:
            return size
    return motor_amps * 1.5
```

Checks: `max_rpm(1800, 12) == 21600`; `round(max_rpm(2200, 11.1)) == 24420` (float dust — round it); `safe_esc(10)` in (15, 18); `safe_esc(12)` > 12. State complexity unprompted: O(1) time, O(1) space.

### Task 2 — thrust CSV parser (fake data, runs with zero hardware)

```csv
test,volts,amps,thrust_g
t1,12.4,8.5,620
t2,11.8,10.2,690
t3,10.4,11.0,640
t4,11.1,9.0,660
```

```python
import csv

def analyse(path: str) -> dict:
    rows = list(csv.DictReader(open(path)))
    for r in rows:
        r["volts"] = float(r["volts"]); r["amps"] = float(r["amps"]); r["thrust_g"] = float(r["thrust_g"])
    best = max(rows, key=lambda r: r["thrust_g"])
    mean_amps = sum(r["amps"] for r in rows) / len(rows)
    low = [r["test"] for r in rows if r["volts"] < 10.6]
    return {"best": best["test"], "best_thrust": best["thrust_g"],
            "mean_amps": round(mean_amps, 2), "undervoltage": low}
```

Expected on the fake file: best t2 at 690 g, mean amps ~9.68, undervoltage `[t3]`. Dry-run t3 by hand: 10.4 < 10.6 → flagged, land. Offer follow-up: plot thrust vs amps with matplotlib.

## Set C — Arduino talk (no parts, whiteboard only)

1. Write LED blink with `delay()` from memory (ASL lab pattern). Name the three calls: `pinMode`, `digitalWrite`, `delay`.
2. Explain the block: during `delay()` nothing else runs — button reads and second LEDs freeze.
3. Sketch the `millis()` version: record `last`, compare `now - last >= interval`, toggle, update `last`. Map to ESC idea in words: the same non-blocking loop could keep reading Rx PPM while pulsing output, which is why flight code never parks on `delay()`.

## Set D — behavioural STAR (90 seconds each)

1. 60-second intro ending in "code where it flies."
2. Why Onyx (Q1) without reciting — one vault proof per sentence.
3. Contribution (Q4) as three owned tools: prop-matcher, CSV parser, checklist generator.
4. Failure story ending in changed behaviour (use a stock-agent bug or a vault miss).
5. Weakness: real, non-disqualifying, with active mitigation (beginner hardware → software-first contribution + fast bench learning).
6. "What would you automate first week?" — answer: thrust-test CSV → parser → one chart the team actually checks.

## Answer key (Set A, short)

1. Battery lead → pack; servo lead → Rx throttle channel; motor leads → motor. 2. Pulse position modulation from Rx, same type as servo control, sets ESC power. 3. Steps LiPo to 5–6 V for Rx/servos; OPTO = no BEC, separate Rx supply. 4. 15 or 18 A — headroom stays cool, exact match burns. 5. 8 inch diameter, 5 inch pitch; 8×5 needs stronger motor. 6. RPM per volt unloaded; 21,600 rpm. 7. 24,420 rpm. 8. 11.1 / ~12.6 / 10.6. 9. 55 A. 10. Brushed 2-wire DC 75–80% vs brushless 3-wire + ESC 85–90%; team uses brushless. 11. Outrunner, direct-drive torque. 12. Rudder, elevator, ailerons, throttle, Aux1, Aux2. 13. One protocol only, no mixing; powered at 5 V from ESC BEC over throttle lead. 14. 60 degrees at max rated load. 15. Lift perpendicular via centre of pressure; drag parallel opposing motion; flaps add lift for take-off, add drag for landing slowdown.

## Fumble cards + scoring

- Card every fumble in your own phrasing; drill weakest set's source page next: ESC misses → [[esc-deep-dive]]; prop/motor/battery → [[propulsion-system-deep-dive]]; build flow → [[workshop-ppts-merged]]; lift/drag/stability → [[airplanes-for-juniors-foundations]] + [[aerodynamics-foundations]].
- Green bar: Set A ≥ 12/15 clean out loud, Set B both tasks run + dry-run stated, Set C `millis()` sketch without prompts, Set D every story under 90 seconds with a number or lesson.
