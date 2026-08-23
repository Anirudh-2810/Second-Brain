---
course_code: "PROJECT"
course_name: "Portfolio Projects"
unit: "handsens101"
tags: [project, github, python, opencv, mediapipe, computer-vision, hci, portfolio]
last_updated: "2026-08-23"
confidence: stated
relations:
  relates_to: "[[robotics/overview|Robotics Overview]]"
---

## For future agent
This note catalogs the owner's GitHub repo **handsens101**, a hand-gesture human-input device, extracted from README + source on 2026-08-23. Use it for questions about the project's CV pipeline and gesture mapping; the repo is small (single-file) so this note covers essentially all of it.

# handsens101 — Hand-Gesture Mouse Control

**Repo:** https://github.com/Anirudh-2810/handsens101 · Python · updated Apr 2026

Webcam-based controller that replaces the mouse with hand tracking. Gestures (per README):
1. **Pinch index + thumb** → click
2. **Index + middle finger together** → scroll
3. **Normal hand movement** → cursor control

## Pipeline (from `src/main.py`, class `JarvisUltimaPro`)
- **MediaPipe HandLandmarker** (tasks API, IMAGE mode, 1 hand, detection confidence raised to 0.85 for noise reduction); auto-downloads `hand_landmarker.task` model on first run
- **OpenCV** capture from webcam (index 0)
- **pyautogui** drives the real cursor (`PAUSE = 0` for latency, failsafe disabled)
- Landmark coordinates mapped to screen size; **exponential smoothing factor (`smooth = 5.0`)** on cursor position; drag state + scroll-y memory for gesture state machine

## Why it matters (my read)
Small but complete perception→action loop: detect → filter → map → actuate. That's literally a robotics stack in miniature (see [[robotics/overview|the robotics module]]) and a nice concrete example of sensor-noise handling via smoothing before actuation — same intuition as filtering in [[worked-example-odom-ekf]]. Good demo material; could be extended to ROS2 teleoperation later.
