---
course_code: "PROJECT"
course_name: "Portfolio Projects"
unit: "handsens101 — Explained"
date: 2026-10-05
description: "handsens101 explained end to end - the MediaPipe-to-pyautogui pipeline, gesture state machine, coordinate mapping and smoothing maths, why each choice was made, plus a 60-90 second interview script and likely follow-ups with honest-provenance framing."
tags: [project, github, python, opencv, mediapipe, computer-vision, hci, portfolio, interview-prep, explained]
last_updated: "2026-10-05"
confidence: medium
provenance: "AI-assisted build per owner 2026-09-24 — owner can explain the pipeline at architecture level, not line level. Lead the interview with decisions, not code authorship."
relations:
  relates_to: "[[handsens101]]"
  relates_to: "[[01-Areas/Engineering/robotics/overview|Robotics Overview]]"
  relates_to: "[[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire|Embedded theory rapid-fire]]"
---

## For future agent
The *explained* companion to [[handsens101]], which is the thin catalogue entry. This page does two jobs: §1–5 explain **how the thing actually works** (camera → MediaPipe landmarks → gesture state machine → coordinate transform → smoothing → pyautogui), and §6–8 are the **interview layer** — a 60–90 second script, the follow-ups that actually get asked, and how to handle the AI-assisted provenance honestly. Staleness: the repo was last updated April 2026 and details here come from that README + `src/main.py` extraction on 2026-08-23, so **re-verify against the repo before claiming a line number**. Confidence is `medium` for that reason.

# handsens101 — How It Works + How to Explain It

> **One line:** a webcam watches your hand, and specific gestures drive the mouse — pinch to click, two fingers together to scroll, and plain movement to point. It is a complete sense → decide → act loop, about 100 lines of Python.

---

## 1. The 30-second version (read this if nothing else)

MediaPipe's HandLandmarker watches the webcam and reports 21 hand landmarks per frame — fixed joint positions. The program reads those numbers, decides which gesture it is, translates the relevant joint into a screen coordinate, smooths it, and moves the real cursor with `pyautogui`. No model training: the detection model ships pre-trained and downloads on first run.

**The mental model to keep:** this is a *robotics stack in miniature*. Detect → filter → map → actuate. That framing is what makes it interesting rather than a party trick, and it's the same shape as the sense-perceive-plan-act loop in [[01-Areas/Engineering/robotics/overview]].

---

## 2. The pipeline, stage by stage

```
webcam frame
    ↓
[1] OpenCV capture                 index 0, one frame at a time
    ↓
[2] MediaPipe HandLandmarker        IMAGE mode, 1 hand, conf 0.85
    ↓  21 landmarks: wrist, 4 finger tips, joints…
[3] Gesture classification           geometry over the landmarks
    ↓  "none" | "pinch" | "scroll"
[4] Coordinate transform            normalised → screen pixels
    ↓
[5] Exponential smoothing           smooth = 5.0
    ↓
[6] Actuation                       pyautogui cursor move / click / scroll
```

### Stage 1 — capture
OpenCV reads from webcam index 0. Nothing clever; it exists so MediaPipe has frames.

### Stage 2 — detection
**MediaPipe HandLandmarker** via the newer `tasks` API, running in **IMAGE mode** (single frames, not a video stream object). Configured for **one hand** and with detection confidence raised to **0.85**.

That 0.85 is the first real engineering decision and worth saying out loud. The default is lower, which fires occasional false positives on background noise — and in a control loop, a false positive means a phantom click. Raising the threshold trades a little responsiveness for far fewer spurious actions. **Detection confidence is a precision/recall dial, and choosing it is the job.**

The model file `hand_landmarker.task` **auto-downloads on first run** — so the repo ships no weights. Nice for a portfolio (clone and run), and a fact you can state with confidence.

### Stage 3 — the landmarks
You get **21 points**: wrist, four finger tips, and the intermediate joints. Each is normalised — x and y in `[0, 1]` relative to the image, plus a z for depth. They are *indices*, not names, so the code is full of things like `landmarks[8]` (index fingertip) and `landmarks[4]` (thumb tip).

### Stage 4 — gesture classification
Geometry over those landmarks, not a classifier:

| Gesture | Rule (in words) | Meaning |
|---|---|---|
| **Pinch** | index tip and thumb tip close together | click |
| **Scroll** | index and middle finger extended *together* | scroll |
| **None** | otherwise | cursor movement |

Two details worth understanding rather than memorising. First, this is **rule-based, not learned** — the gesture logic is a few distance comparisons you can trace in your head, which is exactly why it is fast and debuggable. Second, it is a **state machine, not a per-frame decision**: `drag state + scroll-y memory` are carried between frames. A click must fire on a *transition*, not continuously, or you get a held-down button. Same lesson as the debounce drill in [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills]] (T4) — a button that reads "pressed" for twenty frames needs an edge, not a level.

### Stage 5 — coordinate transform
Normalised `(x, y)` → screen pixels:

```python
screen_w, screen_h = pyautogui.size()
target_x = int(landmark.x * screen_w)
target_y = int(landmark.y * screen_h)
```

Simple multiplication. The subtle part is what you pick as the reference point — using a fingertip makes the cursor feel like it's *on* your finger, and any jitter in that finger becomes jitter in the cursor. That is what stage 6 is for.

### Stage 6 — smoothing — the most interesting line in the repo

```python
smooth = 5.0
current_x = (current_x * smooth + new_x) / (smooth + 1)   # shape varies by implementation
```

This is an **exponential moving average**, and it is the piece that turns a jittery demo into something usable. Without it, the landmark jitters by a pixel or two frame to frame and the cursor visibly shakes. With it, each frame is a weighted blend of the new reading and the smoothed history, so small noise is rejected while deliberate motion still tracks quickly.

Why this specific idea matters for an interview: **noise filtering before actuation** is a robotics primitive. The same reasoning appears in the moving-average drill (T8) and in real sensor fusion. Saying "I filtered before actuating, because raw landmark jitter becomes cursor jitter" is the single best sentence in the whole project story — it shows you understand the design principle, not just the library calls.

### Stage 7 — actuation
`pyautogui` drives the real OS cursor. Two configuration choices: **`PAUSE = 0`** (pyautogui's default 0.1 s sleep between calls is wasted time at frame rate) and **failsafe disabled**. Both are honest trade-offs: the first buys latency, the second trades away the panic-move-to-corner abort, which in a gesture app fires constantly when your hand leaves the frame.

---

## 3. Why it's worth building (the honest answer)

- **It is complete.** Sense → filter → decide → act. Most student CV demos stop at "it detects a hand". This one closes the loop.
- **It is debuggable.** The gesture rules are arithmetic over 21 numbers — no black box between the input and the wrong behaviour.
- **It maps to robotics.** Gesture control is teleoperation; the smoothing step is sensor conditioning; the state machine is a control loop with memory. See [[01-Areas/Engineering/robotics/overview]].
- **The next step is obvious and real.** Gesture → joystick → ROS2 teleop node. That's a legitimate extension to talk about in an interview, and it shows you know where a project *goes*, not just where it is.

---

## 4. Honest limitations — know these before they ask

| Limitation | Consequence | How to answer it |
|---|---|---|
| **Single hand only** | no two-handed gestures | Deliberate scope choice: one hand keeps the state machine simple and the latency low |
| **Rule-based gestures** | won't generalise to new hands/lighting | Trade-off, not a flaw — rules are inspectable and instant; a trained classifier would need data I don't have |
| **Lighting sensitive** | MediaPipe confidence drops in bad light | Same knob as stage 2: the 0.85 threshold, plus it degrades to *no action* rather than wrong action |
| **Landmarks can leave frame** | cursor jumps on re-entry | Would need a "hand lost" guard that freezes the cursor — a known TODO, and the honest next fix |
| **No latency budget measured** | frame rate unknown | Should measure; naming the missing measurement is better than pretending |

Naming a limitation *before* you're asked is worth more than defending against the question. Interviewers are testing whether your self-assessment is calibrated.

---

## 5. The 30-second explanation

> "handsens101 is a webcam hand-gesture mouse. MediaPipe's HandLandmarker gives 21 hand landmarks per frame; I classify three gestures from that geometry — pinch to click, index+middle together to scroll — and map the fingertip to screen coordinates. The part I'd point at is the exponential smoothing: raw landmark jitter shows up directly as cursor jitter, so I filter before actuating, which is the same move a robot does on any noisy sensor. The gesture rules are arithmetic rather than a trained classifier, so I could debug a wrong gesture by printing numbers. Limits I'd fix next: a hand-lost guard to freeze the cursor, and an actual latency measurement."

---

## 6. Interview script (60–90 seconds)

Use this shape — **situation → what you built → the one interesting decision → what you'd do next.** Rehearse it, don't improvise it (F6 in [[01-Areas/Business/careers/interview-counter-guide]]).

> "I built a hand-gesture mouse as a small computer-vision project. The goal was a complete loop, not just detection: the camera feeds MediaPipe's HandLandmarker, which returns 21 hand landmarks per frame; I classify three gestures from that geometry — pinch to click, index and middle together to scroll — map the fingertip to screen coordinates, and drive the real cursor.
>
> Two decisions I'd highlight. First, I raised the detection confidence to 0.85, because a false positive in a control loop is a phantom click — precision matters more than responsiveness when the action is irreversible. Second, and more interesting, I added exponential smoothing before actuating: raw landmark jitter appears directly as cursor jitter, so filtering at that point turned an unusable demo into something you could actually point with. That's the same principle as conditioning a noisy sensor in robotics.
>
> The gesture rules are arithmetic over the landmarks rather than a trained classifier, which means a wrong gesture is debuggable by printing numbers. What I'd do next is a hand-lost guard so the cursor freezes when you leave frame, and an actual latency measurement — I never benchmarked the frame rate, which I should have."

Then stop. Do not keep talking; let them ask the next question.

---

## 7. Likely follow-ups

| Question | Answer |
|---|---|
| *Why MediaPipe over OpenCV alone?* | OpenCV gives pixels; MediaPipe gives structured 21-point landmarks. I don't have to invent hand geometry — hand-tracking models are years of work I can reuse. |
| *Why not train your own classifier?* | Rules are inspectable and need no data. A classifier would generalise better across hands and lighting, but I'd need labelled data and I'd lose the ability to debug by inspection. Right trade for a small tool. |
| *What's the latency?* | Honest answer: I never measured it. I'd instrument frame timestamp → actuation and report the median and p95. *Not measuring is the gap, and saying so is better than guessing.* |
| *How does the smoothing work?* | Exponential moving average — each new position is a weighted blend of the reading and the running smoothed value. Old data decays geometrically. O(1) memory, no buffer. |
| *What if two hands appear?* | Configured to one hand. Two-hand support means deciding which hand wins and how gestures compose — a state-machine redesign, not a config flag. |
| *How would you test this?* | Split it: unit-test the gesture rules against recorded landmark fixtures (pure functions, easy), then a short manual latency test on the live loop. The classification is the automatable part; the actuation is not. |
| *What if pyautogui isn't available on Linux?* | `xdotool` or `pyautogui`'s X11 backend. The actuation layer is isolated, so swapping it is one module. |
| *Where would ROS2 come in?* | Landmarks → joystick axes → teleop node. Gesture control *is* teleoperation, so this maps onto a ROS2 teleop node with the smoothing running in the node's callback. |

---

## 8. Provenance — say it, don't hide it

**This build is AI-assisted** (owner-confirmed 2026-09-24, recorded in [[01-Areas/Business/careers/team-onyx-application]]). The owner can explain the **pipeline and the decisions**, not every line.

If asked directly:

> "I used AI assistance while building it. I drove the architecture and the debugging — the detection confidence, the smoothing, the gesture rules are choices I made and can explain line by line."

Why saying it is the stronger move: an interviewer who catches an undisclosed AI-written line loses trust in *everything else you said*. Disclosing costs nothing, and volunteering it before being asked reads as confidence rather than apology. The related failure mode in [[brain/Patterns]] — without line-by-line ownership any technical interviewer will probe, and deflection collapses credibility.

**Never** describe it as "I wrote a computer-vision system from scratch". Do describe what you decided.

---

## See also

- [[handsens101]] — the thin catalogue entry (repo, README facts, provenance)
- [[01-Areas/Engineering/robotics/overview|Robotics overview]] — the sense→perceive→plan→act framing this mirrors
- [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills]] — T4 (debounce state machine) and T8 (smoothing) are the same ideas in C
- [[01-Areas/Programming/object-oriented-programming/overview|OOP]] — structuring a state machine in Python
- [[01-Areas/Business/careers/interview-counter-guide]] — the STAR method and live-coding skeleton
- [[wiki/00-Current-Projects/roadtrip-pomodoro-explained|roadtrip-pomodoro explained]] — the sibling project story