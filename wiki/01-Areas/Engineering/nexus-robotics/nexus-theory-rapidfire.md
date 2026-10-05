---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Coding Interview Prep"
unit: "Theory Rapid-Fire"
date: 2026-10-05
description: "60-question embedded-systems theory bank for the Nexus Robotics coding interview - memory and C traps, MCU peripherals, comms buses, sensors, control loops, ROS2 - with a core-15 must-know list for last-hour drilling."
tags: [btech, kjsce, nexus-robotics, interview-prep, embedded, theory, robotics-club]
last_updated: "2026-10-05"
confidence: medium
---

## For future agent
Theory side of the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics prep pack]]. Authored from standard embedded-systems practice (generic club-round shape) — **not** sourced from a Nexus notice, because none exists in `raw-sources/`. Each answer is deliberately one or two sentences: the point is retrieval speed, not depth. Answer style follows [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01|Onyx Set A]] (one breath, concrete, no hedging). Depth lives elsewhere: memory layout in [[01-Areas/Engineering/SPM/module-1-spm-c-basics]], padding/pointers in [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers]], control/estimation in [[01-Areas/Engineering/robotics/robotics-fundamentals]], ROS2 commands in [[01-Areas/Engineering/robotics/ros2-cheatsheet]].

# Theory Rapid-Fire — Embedded & Robotics

## How to use

Read the whole bank once. Then **cover the column and answer out loud, one breath each**. Anything you stumble on twice goes on the drill list. Do not memorise sentences — memorize the *cue → answer* link.

---

## 1. Memory layout & C traps (the highest-yield cluster)

1. **Name the five regions of a process's memory and what goes where.** Text/code (read-only), data (initialised globals/statics), BSS (zero-init globals), heap (`malloc`/`new`), stack (locals, return addresses). Grows downward; managed by the runtime.
2. **`stack` vs `heap` — the two-word comparison.** Stack: automatic, LIFO, fast, small, freed on scope exit, no explicit free. Heap: manual, slow, large, survives function return, must be freed by you.
3. **Why does a microcontroller prefer `static` buffers over `malloc`?** Deterministic — no fragmentation, no unpredictable allocation latency that could blow a control-loop deadline. Fragments over long uptimes; a leak is a slow OOM.
4. **What does `volatile` actually do, and what does it NOT do?** Tells the compiler the object may change outside the flow of the program, so don't cache it in a register or elide reads/writes. It does **not** make an operation atomic and does **not** order memory accesses — for that you need barriers/atomics.
5. **Where is `volatile` mandatory in embedded code?** ISR-shared flags, memory-mapped I/O registers (`*(volatile uint32_t*)0x40021000`), and any variable the hardware changes behind your back.
6. **Why can't a `volatile` flag alone protect a shared value?** Because read-modify-write is three steps; an interrupt landing mid-sequence loses an update. You need to disable interrupts for the critical section (or use an atomic CAS).
7. **`static` on a local variable — what changes?** Storage duration becomes the whole program, scope stays the block. It's how you get a persistent counter without a global.
8. **`static` on a file-scope variable or function?** Internal linkage — invisible to other translation units. Gives you module-private state; also the standard way to keep a driver's state off the stack.
9. **`const` vs `const volatile` in embedded.** `const` = compiler may put it in flash/ROM, don't write. `const volatile` = read-only to you *and* the hardware changes it — exactly a status register or an input pin.
10. **Why does `sizeof` on an array parameter lie?** Array parameters decay to pointers, so `sizeof` gives pointer size (8 on 64-bit) not the array size. Pass `n` explicitly.
11. **Struct padding — why is `{char; int; char}` 12 bytes and not 6?** Each member is aligned to its natural boundary (int→4), so the compiler inserts 3 bytes after the first char and 3 of tail padding.
12. **How do you minimise padding?** Order members largest-alignment-first (descending size), or pack deliberately with `__attribute__((packed))` / `#pragma pack` at the cost of unaligned access.
13. **`const char *` vs `char *const` vs `const char *const`.** Pointer-to-const-char / const-pointer-to-char / both. Reads right-to-left.
14. **Why is `-1 >> 1` still `-1` but `1 << 31` is undefined behaviour?** Right-shift of a negative signed value is implementation-defined (arithmetic shift on real compilers → sign-extends). Left-shift that overflows the value range is UB in C.
15. **Unsigned underflow — the classic bug.** `unsigned x = 5; x -= 10;` wraps to a huge number, not `-5`. Always check before subtracting, or use a signed temp.
16. **Integer promotion — why is `char` compared against 200 the way it is?** `char` promotes to `int` before arithmetic, so 8-bit wraparound does not occur unless you assign back to a `char`.
17. **Why must a driver `init()` run once, not every loop call?** Peripherals and clocks are configured by write-once registers; reconfiguring resets the module and wastes cycles. Use a `static bool done` guard or an idempotent check.
18. **What is the difference between a `static` function and one declared in a header?** The former is private to its TU (no symbol clash, enables inlining); the latter is exported and needs the `static` keyword removed and prototype kept in sync.
19. **Why does `printf` with `%d` on a `float` fail?** Variadic calls promote floats to `double` and don't know the type; you must cast to `double` for `%f` or use `%f` with a double. Mismatched format specifiers are UB.
20. **What causes a hard fault in a Cortex-M?** Unaligned access, invalid address, executing from non-executable memory, or a bad function pointer.

## 2. MCU peripherals & interrupts

21. **What does an ISR (interrupt service routine) do and what must it NOT do?** Runs on interrupt with the main loop paused. Must be short, must not block, must not call heavy library code. Sets a flag; the main loop does the work.
22. **Name the standard GPIO modes.** Input floating, input pull-up, input pull-down, output push-pull, output open-drain. Pull-up inverts the logic — common source of off-by-one bugs.
23. **What is `millis()` and why replace `delay()` with it?** `millis()` returns elapsed milliseconds since boot. `delay()` blocks everything — no button reads, no other timing. Non-blocking loops check `now - last >= interval` instead.
24. **Why does `now - last` (unsigned subtraction) handle the millis rollover correctly?** Unsigned wraparound makes the subtraction correct modulo 2^32 even across the overflow instant — a signed comparison would break.
25. **ADC resolution → step size.** 10-bit → 1024 levels; with a 3.3 V reference, one LSB = 3.3/1023 ≈ 3.22 mV. Value = raw/1023 × Vref.
26. **What is a PWM duty cycle and how do you set brightness/motor speed from it?** Duty = on-time / period as a fraction. `analogWrite`/compare register takes 0–255 or 0–100%; speed ≈ proportional to duty (for DC motors, roughly).
27. **Why is an LED always driven through a resistor?** Current limiting. Without it the LED (a diode) draws unbounded current and destroys itself or the pin.
28. **Timer CTC mode — why do we compare to a register instead of counting up?** Compare-match clears the counter automatically → a reliable period with no interrupt overhead per tick.
29. **What is prescaler and why do you need it?** Divides the clock before counting so a fast CPU clock maps to a usable timer range (and widens the resolution of each tick).
30. **Watchdog timer — what is it for?** A timer that resets the MCU unless fed. Catches firmware hangs (infinite loop, blocked ISR). You must kick it in the main loop.
31. **Serial baud rate — what does 9600 8N1 actually mean?** 9600 symbols/s, 8 data bits, no parity, 1 stop bit → 10 bits on the wire per byte. Real throughput = 960 bytes/s, not 1200.
32. **I²C — how many wires, and why do they need pull-ups?** Two (SDA, SCL), open-drain, so external pull-ups define the high level and let arbitration/bus-release work.
33. **SPI vs I²C — the tradeoff in one line.** SPI: faster, full duplex, one pin per slave (CS), no addressing, more pins. I²C: two pins, many devices, addressed, slower, pull-ups needed.
34. **What is a UART's weakness vs SPI/I²C?** No clock line — both ends must agree on baud rate, and there's no acknowledgements or defined framing beyond start/stop bits.
35. **What does a debounce solve and what are the two approaches?** Mechanical switch contacts bounce for milliseconds. Software: fixed-time sampling, or state-change + timer confirmation (the better one).
36. **What is a watchdog-worthy bug vs a logic bug?** Watchdog catches the program-not-reaching-main-loop class (infinite loop, deadlock, blocked on a flag nobody sets). It never catches wrong-but-running logic.

## 3. Sensors & signal conditioning

37. **HC-SR04 ultrasonic: how do you compute distance?** Trigger 10 µs pulse → echo pulse width t µs → distance cm ≈ t / 58 (sound ≈ 343 m/s, round trip). Divide by 2 for the return leg.
38. **Why does the ultrasonic sensor need `delayMicroseconds` and not `millis`?** The µs resolution matters and the echo window is short; a millis-based blocking wait is far too coarse.
39. **What does an HC-SR04 return if nothing is in range?** Echo stays high (≈ no pulse within ~38 ms timeout) → read as 0 cm. So "0" means "out of range", not "touching".
40. **DHT11 vs DHT22 — the two differences.** DHT11: 0–50 °C, ±2 °C, 1 Hz. DHT22: −40–80 °C, ±0.5 °C, 0.2 Hz. Both use a single-wire protocol with a fixed 50 µs low-start pulse.
41. **What is sensor noise and the three standard fixes?** Physical/vibration, ADC quantisation, electrical. Fixes: averaging/filtering (software), shielding and decoupling caps (hardware), better supply.
42. **Moving average vs low-pass vs median filter — when each?** Moving average smooths random noise (and blurs sharp edges, adds group delay). Low-pass (single-pole) is cheaper and phase-friendly. Median kills outliers/spikes (e.g. a bad ultrasonic echo) without the blur.
43. **Why filter on the MCU vs in software later?** Filtering at the source keeps noise out of the control loop and reduces data you have to transmit/store. A PID loop acting on unfiltered ADC is a common beginner failure.
44. **What is sensor drift and how do you handle calibration?** Slow offset change (temperature, aging). Handle with periodic two-point calibration against a known reference and store the offset.
45. **Potentiometer → angle: the wiring and the formula.** 5 V across ends, wiper to ADC, ground the bottom. angle = raw/1023 × 270° (typical servo range).

## 4. Control

46. **State the PID equation from memory.** u(t) = Kp·e(t) + Ki·∫e dt + Kd·de/dt, where e = setpoint − measurement.
47. **What does each PID term actually fix?** P: reacts to present error. I: removes steady-state offset from constant disturbances. D: damps, anticipates, reduces overshoot/settling oscillation.
48. **Why does pure P control leave a steady-state offset?** Because a nonzero error is needed to produce any output at all — it settles where Kp·e balances the load.
49. **Integral windup — what is it and what fixes it?** The integrator keeps accumulating while the actuator is saturated, so the controller overshoots badly when it leaves saturation. Fixes: clamp the integral, conditional integration, anti-windup feedback.
50. **Why is a derivative term dangerous in real robot control?** Sensor noise differentiates into large spikes. Always low-pass the derivative, and note that D assumes smoothness that sensors don't deliver.
51. **What does a low-pass filter do to a control loop?** Adds phase lag. Too much filtering and the loop goes unstable (gain margin lost) — the reason "add more filtering" is not a free fix.
52. **Sampling rate rule of thumb for a control loop.** At least 10× the closed-loop bandwidth (often 10–20×). Nyquist says sample at >2×, but you need the 10× margin for usable phase margin.
53. **PWM frequency for a motor: too low vs too high.** Too low (<1 kHz) → audible whine, poor current smoothing. Too high (>25 kHz) → switching losses and beyond hearing so no benefit. 15–20 kHz is the common target.
54. **H-bridge: what does it do?** Four switches let you reverse polarity of a DC motor → forward/back and braking. Direction bits select the diagonal pair; freewhe diodes handle inductive kick.
55. **What is a control loop's "duty cycle of CPU" concern?** If your loop must run at 1 kHz but each iteration takes longer than 1 ms, you cannot keep up. Measure worst case, not average.

## 5. Robotics architecture & ROS2 (concept level)

56. **Differential-drive kinematics — the two equations.** v = (v_right + v_left)/2, ω = (v_right − v_left)/L where L is wheelbase. From ω you get heading.
57. **How do you get odometry from encoders?** Accumulate counts → distance (and for two wheels, the arc difference gives heading). Dead reckoning — it drifts, so fuse with IMU/GPS via a Kalman filter.
58. **What is sensor fusion and why?** Combine complementary sensors (encoder good short-term, IMU good mid-term) via a Kalman/EKF filter to get a better estimate than either. Gain K comes from covariance.
59. **ROS2: topic vs service vs action — when each?** Topic: continuous streams, many-to-many, fire-and-forget. Service: single request/reply. Action: long-running goal with feedback and cancelability.
60. **Name five `ros2` CLI commands from memory.** `ros2 node list`, `ros2 topic list`, `ros2 topic echo /odom`, `ros2 run`, `ros2 bag record` — full set in [[01-Areas/Engineering/robotics/ros2-cheatsheet]].

---

## Core 15 — drill these out loud before sleep

If you only memorise fifteen, memorise these. Each unlocks a cluster above.

| # | Cue | One-breath answer |
|---|------|-------------------|
| 1 | `volatile` | Stops the compiler caching/optimising away accesses to something changed outside program flow — ISR flags, memory-mapped registers. Not atomic, not a barrier. |
| 2 | ISR discipline | Short, non-blocking, sets a flag; main loop does the work. Never park in an ISR. |
| 3 | `delay()` → `millis()` | Non-blocking scheduling: check `now - last >= interval`, unsigned so rollover is safe. |
| 4 | 10-bit ADC LSB (3.3 V) | 3.3/1023 ≈ 3.22 mV per count. |
| 5 | Struct padding rule | Members align to natural boundaries; reorder largest-first to shrink `sizeof`. |
| 6 | Stack vs heap in firmware | Prefer `static` buffers: deterministic, no fragmentation, no unpredictable allocation latency. |
| 7 | HC-SR04 distance | Echo pulse width µs ÷ 58 = cm (round trip ÷ 2); 0 means out of range. |
| 8 | Debounce approaches | Timed-sample, or better: detect change then confirm after a stable interval. |
| 9 | PID terms | P present error, I removes steady-state offset, D damps/anticipates (needs filtered D). |
| 10 | Integral windup | Integrator saturates; clamp it or use conditional integration. |
| 11 | Control sampling rule | ≥10× closed-loop bandwidth, 10–20× typical. |
| 12 | Motor PWM band | ~15–20 kHz: above audible whine, below switching-loss wall. |
| 13 | H-bridge | Four switches reverse motor polarity → direction + braking; freewheel diodes for kick. |
| 14 | Diff-drive kinematics | v = (v_R+v_L)/2, ω = (v_R−v_L)/L. |
| 15 | ROS2 topic vs service vs action | Streams / single reply / long goal with feedback. |

## Fumble routing

Where to go when a cluster collapses:

| Missed cluster | Re-read |
|---|---|
| Memory layout, compilation, regions | [[01-Areas/Engineering/SPM/module-1-spm-c-basics]] |
| Structs, unions, pointers, padding | [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers]] |
| Arrays, strings, sorting | [[01-Areas/Engineering/SPM/module-3-arrays]] · [[01-Areas/Engineering/SPM/module-3-strings]] |
| C language depth beyond syllabus | [[01-Areas/Programming/c-programming/index]] |
| Control, estimation, SLAM, planning | [[01-Areas/Engineering/robotics/robotics-fundamentals]] |
| ROS2 commands and QoS | [[01-Areas/Engineering/robotics/ros2-cheatsheet]] |
| Hardware/electronics side (ESC, motor, LiPo) | [[01-Areas/Engineering/aeromodelling/avionics-rc-stack]] |

**Note on scope honesty:** bitwise operators were removed from the SPM Module 1.5 syllabus scope in AY 2026-27 (see [[01-Areas/Engineering/SPM/spm-module1-faculty-companion]] §6a) — so bit-level questions here are **outside** your coursework coverage. That's exactly why they're worth drilling tonight; don't apologise for them, just answer.

*Home: [[01-Areas/Engineering/nexus-robotics/INDEX]] · Drills: [[01-Areas/Engineering/nexus-robotics/nexus-embedded-coding-drills]] · Fallbacks: [[01-Areas/Engineering/nexus-robotics/nexus-interview-fallbacks]]*