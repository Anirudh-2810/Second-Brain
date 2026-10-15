---
course_code: "ARDUINO-REVISION-EP01-05"
course_name: "Arduino Tutorial Series — Revision & Test (Ep 01–05)"
unit: "Episodes 01–05"
tags: [engineering, arduino, microcontroller, embedded, revision, test, exam-prep]
last_updated: "2026-10-15"
confidence: high
description: "Condensed recall surface + self-test for Jeremy Blum Arduino Episodes 1–5: IDE/blink, buttons/PWM/functions, EE basics (Ohm's law, dividers, regulators), analog inputs (ADC, map()), motors/transistors/servos. Formula table, key functions, circuit values, 20-question test with answers."
---

## For future agent
This is a single recall-and-test surface for [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino module]] Episodes 1–5 (the series starts at Episode 01; "ep0-5" = everything through Episode 5). It condenses the five deep episode notes into facts you must recall cold (values, formulas, function signatures, circuit topologies) plus a 20-question self-test with an answer key. Use it to verify readiness before attempting Ep6+ or before hardware work; for full derivations and annotated code walkthroughs, open the linked episode notes. Confidence: high (all content distilled from the module notes, which are high-confidence). Last refreshed 2026-10-15.

# Arduino EP01–05 — Full Revision & Test

## 1. Episode Map (what each episode owns)

| Ep | Title | One-line core | Must-recall facts |
|----|-------|---------------|-------------------|
| 01 | Getting Acquainted | Board + IDE + Blink | `setup()` once / `loop()` forever; pin 13 has built-in LED (no resistor needed); `pinMode`, `digitalWrite`, `delay`; sketch = `.ino` in same-name folder; pick Board + Port or upload fails |
| 02 | Buttons, PWM, Functions | Digital input + debounce + dimming | `digitalRead`; floating pin = noise; 10 kΩ pull-down; switch bounce; `debounce()`; edge detect `last==LOW && current==HIGH`; `analogWrite` PWM 0–255 on `~` pins (3,5,6,9,10,11) |
| 03 | EE Basics | The theory backbone | $V=IR$; $P=VI$; LED resistor $R=(V_s-V_f)/I$ → 150 Ω (5 V, $V_f$=2 V, 20 mA); pull-up vs pull-down; divider $V_{out}=V_{in}\frac{R_2}{R_1+R_2}$; pot = variable divider; 7805 + decoupling caps |
| 04 | Analog Inputs | Sensors + ADC | `analogRead` = 10-bit, 0–1023, 0–5 V, 4.883 mV/step; LDR divider direction depends on which side sensor sits; threshold = calibration; `map(v,fL,fH,tL,tH)` (no clamp); Sharp IR analog out |
| 05 | Motors & Transistors | Power devices | Pin max ≈40 mA; motor = 100–1000 mA → transistor; BC547 NPN, 1 kΩ base resistor, low-side switch; 1N4004 flyback diode (cathode to +V); PWM speed via `analogWrite`; servo 0–180° via `Servo` library; separate 7805 rail + common ground; H-bridge concept |

## 2. Formula & Constants Sheet

| Quantity | Formula | Arduino-specific value |
|----------|---------|----------------------|
| Ohm's law | $V = I R$ | — |
| Power | $P = V I$ | 7805 heat = $(V_{in}-5)\times I$ |
| LED series resistor | $R = (V_{supply}-V_f)/I$ | $(5-2)/0.020 = 150\,\Omega$ (safe range 150–330 Ω) |
| Voltage divider | $V_{out} = V_{in}\cdot\frac{R_2}{R_1+R_2}$ | 10 kΩ/10 kΩ across 5 V → 2.5 V at wiper |
| ADC conversion | $V = \text{reading}\times 5.0/1023$ | 10-bit → 0–1023; ~4.883 mV per step; `analogRead` ~100 µs |
| PWM duty | 0–255 (8-bit) | 0 = off, 255 = full; effective average voltage |
| Pin current limit | ~20 mA comfortable, 40 mA abs max | Motor direct-drive = dead pin |
| Base current (Ep5) | set by 1 kΩ from 5 V pin | transistor saturates, low $V_{CE}$ |

## 3. Key Functions — Signature + Use

| Function | Signature | Episode | Gotcha |
|----------|-----------|---------|--------|
| `pinMode` | `pinMode(pin, INPUT\|OUTPUT)` | 01 | Forgot it → pin floats on INPUT, misbehaves on OUTPUT |
| `digitalWrite` | `digitalWrite(pin, HIGH\|LOW)` | 01 | HIGH = 5 V, LOW = 0 V |
| `digitalRead` | `digitalRead(pin)` → `HIGH`/`LOW` | 02 | Only meaningful after `pinMode(pin, INPUT)` |
| `delay` | `delay(ms)` | 01 | **Blocks** — no input processing during it |
| `analogWrite` | `analogWrite(pin, 0..255)` | 02, 05 | PWM only on `~` pins (3,5,6,9,10,11) |
| `analogRead` | `analogRead(pin)` → 0–1023 | 04 | Only A0–A5; returns count, not volts |
| `map` | `map(v, fromLow, fromHigh, toLow, toHigh)` | 04, 05 | **Does not clamp** — follow with `constrain` |
| `constrain` | `constrain(v, lo, hi)` | 05 | Servo safety clamp 0–180 |
| `Servo.attach/write` | `myServo.attach(pin)` / `myServo.write(deg)` | 05 | Angle 0–180, not speed |
| `debounce` (custom) | `boolean debounce(boolean last)` | 02 | Caller owns `lastButton = currentButton` update |

## 4. Circuit Topologies (recall cold)

**Blink (Ep1):** pin 13 → on-board LED + resistor → GND. No external parts.

**Button, pull-down (Ep2):**
```
+5V --[BUTTON]--+-- pin
                |
              [10k]
                |
               GND
```
Unpressed → LOW; pressed → HIGH. (Pull-up inverts: rests HIGH, pressed → LOW; Uno has built-in via `INPUT_PULLUP`.)

**LED (Ep3):** `pin --[150 Ω]--|>|-- GND` (anode to resistor, cathode to GND).

**LDR divider (Ep4):** `+5V --[LDR]--+--[R fixed]-- GND`, wiper → A0. Bright → LDR ↓ → voltage ↑ (if LDR on top). Direction flips if LDR swaps sides.

**DC motor (Ep5):**
```
+9V --[MOTOR]--+--(C)
                |      [1N4004]  (cathode to +9V, anode to (C))
pin9 --[1kΩ]--(B)  BC547
GND ----------(E)-------------+
```

**Servo rail (Ep5):** 9 V battery → 7805 → +5 V rail → servo V+; **Arduino GND tied to servo GND**; signal from pin 9.

## 5. The 10 Gotchas That Bite (exam-grade)

1. No LED without a current-limiting resistor — destroys LED and/or pin.
2. Motor never direct from a pin — use transistor/driver.
3. Flyback diode never omitted — inductive kick fries the transistor.
4. Missing common ground between logic and motor supplies — control signal meaningless.
5. Floating input without pull-up/pull-down — reads noise, random `if` firing.
6. Button without debounce — one press registers as many.
7. `analogWrite` on non-PWM pin — just on/off, no dimming.
8. Servo powered from Arduino 5 V pin — current spikes brown-out the board.
9. `map()` without `constrain()` — glitchy sensor can command servo past 0–180.
10. Thresholds set without calibration — light/temperature differ per environment; watch Serial first.

---

## 6. Self-Test (20 questions)

Answer from memory before checking the key (§7).

**Episode 01**
1. What does `setup()` do vs `loop()`?
2. Why can pin 13 blink with no external resistor?
3. Two upload-failure causes in the IDE, and the exact menu path to fix each.
4. What mode must pin 13 be in before `digitalWrite(13, HIGH)` lights the LED?
5. True/false: the board can read a button during `delay(1000)`.

**Episode 02**
6. What does an `INPUT` pin with nothing connected read, and what is the fix?
7. What is switch bounce, and how many milliseconds does the episode's debounce wait?
8. In `if (lastButton == LOW && currentButton == HIGH)`, what event does this detect?
9. What range does `analogWrite` take, and which Uno pins support it?
10. What happens if you forget `lastButton = currentButton;` in the toggle sketch?

**Episode 03**
11. Compute the series resistor for a blue LED, $V_f = 3.2$ V, target 15 mA.
12. State the voltage-divider formula. For $R_1 = R_2 = 10$ kΩ across 5 V, what is $V_{out}$?
13. Pull-down: pin rests at ___ and pressing the button connects pin to ___. Pull-up: the reverse.
14. What does a 7805 do, and why two capacitors?
15. What does $P = VI$ tell you about a 7805 stepping 9 V → 5 V at 250 mA?

**Episode 04**
16. What range does `analogRead(A0)` return, and what voltage range does it represent? mV per step?
17. Your night light turns on in bright light and off in dark. Name two possible causes.
18. `map(700, 0, 1023, 0, 180)` ≈ ? What prevents a glitchy value from sending a servo to 200°?

**Episode 05 (integration)**
19. Why can't a DC motor connect directly to a pin, and what three components fix it?
20. A servo jitters/resets when it moves. Which two wiring rules from Ep5 does this violate?

---

## 7. Answer Key

1. `setup()` runs **once** at power-on/reset (configuration). `loop()` runs **repeatedly forever** (main behavior).
2. The Uno has a resistor soldered in series with the on-board LED next to pin 13.
3. Wrong board: `Tools → Board → Arduino Uno`. Wrong/missing port: `Tools → Port → COM…` (install the USB driver from the IDE `drivers` folder first if the port never appears).
4. `OUTPUT` — `pinMode(ledPin, OUTPUT)` in `setup()`.
5. **False.** `delay()` blocks; nothing else runs during it.
6. It **floats** — reads noise (random HIGH/LOW) because it acts as an antenna. Fix: give it a defined resting state — pull-down resistor to GND (Ep2) or pull-up to +5 V / `INPUT_PULLUP`.
7. The metal contacts of a mechanical switch make/break several times in the first few ms after a press, so the MCU sees many false transitions. The sketch waits **5 ms** then re-reads.
8. A **rising edge** — a fresh press (transition from unpressed to pressed). This is what makes one press = one toggle instead of flicker while held.
9. **0–255** (0 = always off, 255 = always on). PWM-capable pins on the Uno: **3, 5, 6, 9, 10, 11** (marked `~`).
10. `lastButton` never changes, the edge condition never becomes true — the button seems dead.
11. $R = (5 - 3.2)/0.015 = 1.8/0.015 = \mathbf{120\,\Omega}$ (use the next standard value up, e.g. 120–150 Ω; power $P = I^2R = 0.015^2\times120 \approx 27$ mW, fine for 250 mW).
12. $V_{out} = V_{in}\cdot\frac{R_2}{R_1+R_2}$. With $R_1 = R_2$: $5\times\frac{10k}{20k} = \mathbf{2.5\,V}$.
13. Pull-down: rests **LOW**; pressed connects pin to **+5 V** (→ HIGH). Pull-up: rests **HIGH**; pressed connects pin to **GND** (→ LOW).
14. It regulates a higher, noisy input (≈7–35 V) down to a clean **5 V**. The ceramic (input) and electrolytic (output) **decoupling capacitors** absorb ripple and prevent oscillation.
15. $P = (9-5)\times0.250 = \mathbf{1\,W}$ wasted as heat — it will run hot; a heatsink may be needed at that current.
16. **0–1023** (10-bit ADC), representing **0–5 V**. $5.0/1024 \approx$ **4.883 mV per step**.
17. (a) LDR on the wrong side of the divider — reading moves opposite to brightness; (b) threshold set without calibration (outside the observed light/dark range). Fix by swapping sensor/fixed-resistor positions **or** flipping the comparison operator — understand why first.
18. $700\times180/1023 \approx 123°$. Use **`constrain(angle, 0, 180)`** after `map()` — `map()` does not clamp.
19. A motor draws 100–1000+ mA; a pin sources ≈40 mA max — direct drive destroys the pin (and the motor's coil resistance is far too low). Fix: **NPN transistor (BC547) as a low-side switch** driven through a **1 kΩ base resistor**, motor on its own supply, plus a **1N4004 flyback diode** across the motor.
20. (a) Servo powered from the Arduino 5 V pin — current spikes brown out the board (fix: separate regulated 5 V rail via 7805); (b) missing **common ground** between Arduino and servo supply (fix: tie GNDs together).

**Scoring:** 18–20 solid · 14–17 review the missed episode note · <14 re-read §2–§5 and retake.

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]] — episode map, quick answers, full scope
- [[01-Areas/Engineering/arduino-microcontrollers/ep01-getting-acquainted|Ep01 — Getting Acquainted]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep02-buttons-pwm-functions|Ep02 — Buttons, PWM, Functions]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep03-electrical-basics|Ep03 — EE Basics]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep04-analog-inputs|Ep04 — Analog Inputs]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep05-motors-transistors|Ep05 — Motors & Transistors]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Ep06 — Serial & Processing]] — next: serial (needed for calibration printing)
- [[01-Areas/Engineering/BEE/INDEX|BEE]] — formal circuit theory behind Ep03
- [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills|Nexus embedded drills]] — debounce state machine + PID in embedded C
