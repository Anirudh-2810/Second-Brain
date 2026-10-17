---
course_code: "ARDUINO-VIVA-RECAP"
course_name: "Arduino Viva Recap — Ep01–05 (concepts, full-forms, oral Q&A)"
unit: "Episodes 01–05"
tags: [engineering, arduino, microcontroller, embedded, beginner, viva, exam-prep, glossary]
last_updated: "2026-10-17"
confidence: high
description: "Beginner-depth viva recap for Jeremy Blum Arduino Episodes 1–5: every acronym expanded, a plain-language episode-by-episode recap, formula/constants sheet, circuit topologies, and a 30-question oral Q&A with model answers. Pairs with the companion all-programs note."
---

## For future agent
This is the **concept half** of the Arduino Ep01–05 viva pack (2026-10-17, prep for a Monday viva covering the first five videos). It gives a full-forms glossary, an ELI5 recap of each episode, the formula/constants sheet, the five circuit topologies, and an oral Q&A. The **code half** (all 9 programs + demo checklists + write-it-live drills) is [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep01-ep05|viva-programs-ep01-ep05]]. Deep per-episode theory: [[01-Areas/Engineering/arduino-microcontrollers/ep01-getting-acquainted|Ep1]]–[[01-Areas/Engineering/arduino-microcontrollers/ep05-motors-transistors|Ep5]]. "ep0-5" = series start through Episode 5; there is no Ep00. Manual-verification: values/formulas are exam-grade and stable; IDE menus drift by version.

# Arduino Ep01–05 — Viva Recap (concepts, full forms, oral answers)

## How to use this pack

Two notes for Monday's viva:
- **This note** — understand + *say* the concepts (glossary, recap, formulas, oral Q&A).
- **[[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep01-ep05|All programs note]]** — *write* and *demonstrate* the code.

If asked "what did the first five videos cover?", the one-line answer: **1) get the board + IDE working and blink an LED, 2) read a button, debounce it, and dim an LED with PWM, 3) the electrical theory (Ohm's law, resistors, dividers, regulators), 4) read analog sensors (ADC, `map()`), 5) drive motors and servos safely with transistors.**

---

## 1. Full-Forms Glossary (every acronym expanded)

| Short form | Full form | Plain meaning | First seen |
|-----------|-----------|---------------|-----------|
| **Arduino** | (a brand/open-source platform, not an acronym) | Board + IDE + simplified C/C++ language for microcontrollers | Ep1 |
| **MCU** | Microcontroller Unit | Tiny single-purpose computer on one chip (the ATmega328P) | Ep1 |
| **IDE** | Integrated Development Environment | The Arduino app where you write, compile, and upload code | Ep1 |
| **USB** | Universal Serial Bus | The cable that both powers the board and uploads code | Ep1 |
| **COM** | Communications port | The Windows serial port (`COM3`, `COM4`…) the board gets assigned | Ep1 |
| **I/O** | Input/Output | Pins that either read the world (input) or drive it (output) | Ep1 |
| **GPIO** | General-Purpose Input/Output | A pin you can configure as input or output (Arduino's digital pins) | Ep1 |
| **HIGH / LOW** | — | Digital levels: HIGH = 5 V ("on"), LOW = 0 V ("off") | Ep1 |
| **LED** | Light-Emitting Diode | A diode that emits light when current flows through it | Ep1 |
| **ms / µs** | millisecond / microsecond | 1/1000 s / 1/1,000,000 s (used by `delay`, ADC timing) | Ep1 |
| **`.ino`** | (Arduino sketch extension) | The file type an Arduino program is saved as | Ep1 |
| **PWM** | Pulse Width Modulation | Fast on/off switching that averages to a variable brightness/speed | Ep2 |
| **ADC** | Analog-to-Digital Converter | Turns a 0–5 V analog voltage into a 0–1023 number | Ep4 |
| **DC** | Direct Current | Current that flows one way (batteries, Arduino supplies) | Ep3 |
| **AC** | Alternating Current | Current that reverses direction (mains) — mentioned for contrast | Ep3 |
| **V** | Volt | Unit of electrical "pressure" | Ep3 |
| **I** | Current (ampere, A) | Rate of flow of charge; mA = milliampere = 1/1000 A | Ep3 |
| **R / Ω** | Resistance / ohm | How much a component opposes current; kΩ = 1000 Ω | Ep3 |
| **P / W** | Power / watt | Energy per second a component uses/dissipates; mW = 1/1000 W | Ep3 |
| **Vf** | Forward Voltage | The voltage an LED "uses up" before it lights (≈2 V red, ≈3.2 V blue) | Ep3 |
| **LDR** | Light-Dependent Resistor | Resistor whose resistance falls as light increases (photoresistor) | Ep4 |
| **IR** | Infrared | The Sharp sensor measures distance with infrared light | Ep4 |
| **BJT** | Bipolar Junction Transistor | The 3-leg transistor used as an electronic switch | Ep5 |
| **NPN** | (junction order: N-P-N) | Transistor type used here (BC547); current into Base controls C→E | Ep5 |
| **PNP** | (junction order: P-N-P) | The complementary transistor type (mentioned for context) | Ep5 |
| **B / C / E** | Base / Collector / Emitter | The three transistor legs: control / output-high / output-to-ground | Ep5 |
| **VCE** | Collector–Emitter Voltage | The voltage across a transistor when on; low = fully "on"/saturated | Ep5 |
| **VCC / VDD** | (common supply-rail labels) | The positive supply voltage (here +5 V or +9 V) | Ep5 |
| **GND** | Ground | The 0 V reference; all supplies must share it ("common ground") | Ep1/Ep5 |
| **EMF** | Electromotive Force | The voltage a motor's coil kicks back when switched off ("back-EMF") | Ep5 |
| **PCB** | Printed Circuit Board | The board a circuit is soldered onto (context for the Arduino board) | Ep1 |
| **IC** | Integrated Circuit | A chip; the ATmega and 7805 are ICs | Ep1/Ep3 |
| **7805** | (part number, "78" = fixed +5 V series) | Voltage regulator: higher/noisy input → clean 5 V output | Ep3 |
| **baud** | (Baudot, from Émile Baudot) | Serial speed; here 9600 bits/second | Ep4 |
| **TX / RX** | Transmit / Receive | The two serial data lines (the board's and the PC's) | Ep6 (preview) |

> When you name an acronym in the viva, immediately give the full form — it signals you understand, not memorised.

---

## 2. Episode-by-episode plain-language recap

### Episode 1 — Getting acquainted (board + IDE + Blink)
- A **microcontroller** is a tiny single-purpose computer that runs **one program forever** — no operating system, no screen. **Analogy:** a laptop is an office building of workers; a microcontroller is one dedicated employee doing one routine perfectly, forever.
- **Arduino** is not one chip — it is the board + the IDE + a simplified language over C++. Before it, you needed a datasheet and a separate programmer.
- A program is called a **sketch**, saved as `.ino`, and always has two functions: **`setup()` runs once** at power-on/reset (configuration), **`loop()` runs over and over forever** (behavior).
- Digital pins are switches: **HIGH = 5 V, LOW = 0 V**. **Pin 13 has a built-in LED + resistor**, so Blink needs no external parts.
- **Toolchain:** write sketch → IDE compiles (checks syntax, turns C++ into machine code) → USB uploads to the ATmega → board runs. Pick the right **Board** and **Port** or upload fails.
- Functions used: `pinMode(pin, OUTPUT)`, `digitalWrite(pin, HIGH/LOW)`, `delay(ms)` (blocks).

### Episode 2 — Buttons, PWM, functions
- **`digitalRead(pin)`** is the input half: it *asks* a pin "HIGH or LOW?" (must be `pinMode(pin, INPUT)`).
- **Floating-pin problem:** an input with **nothing connected** does not read zero — it acts like an antenna and reads **noise**. **Analogy:** asking "is the door open?" of a room with no door. **Fix:** a **pull-down** resistor (pin→GND, 10 kΩ) gives a definite resting LOW; pressing connects +5 V, which "wins."
- **Switch bounce:** a button's metal contacts make/break several times in a few ms, so one press looks like many. **Debouncing** cleans it (software here: `delay(5)` + re-read; hardware in Ep10).
- **Functions:** you write your own — `boolean debounce(boolean last) { ... return current; }` — to avoid copy-paste.
- **PWM / `analogWrite(pin, 0..255)`:** a digital pin only does on/off, but switching fast gives *average* brightness. 0 = off, 255 = full. Only **`~` pins (3,5,6,9,10,11)**.
- **Edge detection:** act only on the *transition* (`last==LOW && current==HIGH`) so one press = one toggle. Must update `lastButton = currentButton;` each loop.

### Episode 3 — Electrical engineering basics (the theory backbone)
- **Ohm's law `V = I·R`** with the **water-pipe model**: V = pressure, I = flow rate, R = pipe narrowness. **Power `P = V·I`** (how much heat a part makes).
- **LEDs need a current-limiting resistor** because an LED is not a resistor — past its forward voltage it conducts almost freely and would burn out. **Worked example:** 5 V supply, Vf ≈ 2 V → 3 V across the resistor → `R = 3 / 0.020 = 150 Ω`.
- **Pull-down** (pin→GND): rests LOW; button to +5 V makes HIGH. **Pull-up** (pin→+5 V, or `INPUT_PULLUP`): rests HIGH; button to GND makes LOW.
- **Voltage divider `V_out = V_in·R₂/(R₁+R₂)`:** two resistors in series; the junction gives a fraction of the input. This is how a *resistance change* (sensor) becomes a *voltage* the ADC can read.
- **Potentiometer** = a resistor with a **wiper**; wired across +5 V/GND it is a **variable voltage divider** (a perfect analog "knob").
- **7805 regulator** makes clean 5 V from 7–35 V in (the rest is heat). It needs **decoupling capacitors** (ceramic in, electrolytic out) to stay stable.
- **Multimeter:** voltage measured **across** (parallel), current measured **through** (series).

### Episode 4 — Analog inputs (sensors + ADC)
- **Analog vs digital:** digital = on/off; analog = any value in a range (dimmer, not switch). The Arduino is digital, so it uses an **ADC** to sample analog.
- **10-bit ADC:** splits 0–5 V into 2¹⁰ = **1024 steps**, returning **0–1023**. Step size = 5.0/1024 ≈ **4.883 mV**. Convert back: `V = count × 5.0 / 1023`. Only pins **A0–A5**.
- **LDR voltage divider:** bright → LDR resistance ↓. **Which way the reading moves depends on which side of the divider the LDR sits** (the classic "my night light is backwards" bug).
- **Thresholds:** turn a number into a decision (`if (light < 200) LED on`). The threshold is **calibrated** — watch the Serial Monitor in light and dark, then pick a value between.
- **`map(value, fromLow, fromHigh, toLow, toHigh)`:** linearly rescales a range (e.g. 0–1023 → 0–255). Pure arithmetic; **does not clamp** — add `constrain()` if needed.
- **Serial Monitor:** `Serial.begin(9600)` then `Serial.println(x)`; match the baud or you see garbage.

### Episode 5 — Motors and transistors
- **A pin cannot drive a motor:** a pin sources ≈40 mA (20 mA comfortable); a motor wants 100–1000+ mA. Direct drive = dead pin. The pin is the *decision-maker*, not the *power source*.
- **Transistor as an electronic switch:** an **NPN (BC547)** has Base/Collector/Emitter. A small **base current** (through a **1 kΩ** resistor) lets a large current flow **C→E**. Motor between +9 V and Collector, Emitter to GND = a **low-side switch**.
- **Flyback diode (1N4004):** a motor is an inductor; cutting current generates a big reverse voltage spike that can kill the transistor. The diode placed **across the motor, reversed (cathode to +V)** gives the spike a safe path. **Never omit it.**
- **PWM speed control:** feeding the base a PWM signal makes the motor's *average* voltage (speed) vary — Ep2's PWM applied to a power device.
- **Servo:** a geared DC motor with feedback that holds an **angle 0–180°** (not continuous spin). Use the **`Servo` library**: `myServo.attach(pin)`, `myServo.write(deg)`.
- **7805 servo rail + common ground:** power the servo (and motor) from its **own** regulated 5 V rail, tie **GND common** with the Arduino; only the *signal* comes from the Arduino.
- **H-bridge (concept):** four switches to reverse polarity → forward/backward/brake. Direction is to a DC motor what angle is to a servo.

---

## 3. Formula & constants sheet

| Quantity | Formula | Value here |
|----------|---------|-----------|
| Ohm's law | $V = I R$ | — |
| Power | $P = V I$ | 7805 heat = $(V_{in}-5)\times I$ |
| LED series resistor | $R = (V_{supply}-V_f)/I$ | $(5-2)/0.020 = 150\,\Omega$ (safe 150–330 Ω) |
| Voltage divider | $V_{out} = V_{in}\cdot\frac{R_2}{R_1+R_2}$ | 10 kΩ/10 kΩ on 5 V → 2.5 V |
| ADC conversion | $V = \text{count}\times5.0/1023$ | 10-bit, 0–1023, ≈4.883 mV/step |
| PWM duty | 0–255 (8-bit) | 0 = off, 255 = full |
| Pin current | ~20 mA comfortable, 40 mA abs max | motor directly = dead pin |
| Base current | set by 1 kΩ from 5 V pin | saturates transistor, low $V_{CE}$ |

**Constants:** Arduino pin HIGH = 5 V; PWM pins = 3,5,6,9,10,11; analog pins = A0–A5; serial baud = 9600; debounce wait = 5 ms; LED resistor = 150 Ω; base resistor = 1 kΩ; flyback = 1N4004; transistor = BC547; regulator = 7805.

---

## 4. Five circuit topologies (be able to draw + explain)

1. **Blink (Ep1):** pin 13 → on-board LED + resistor → GND. No external parts.
2. **Button, pull-down (Ep2):** +5 V → button → pin; pin → 10 kΩ → GND. Rests LOW, pressed HIGH.
3. **LED (Ep3):** pin → 150 Ω → LED anode; LED cathode → GND.
4. **LDR divider (Ep4):** +5 V → LDR → junction (→ A0) → fixed resistor → GND. Direction flips if LDR swaps sides.
5. **DC motor, low-side NPN (Ep5):** +9 V → motor → Collector; pin → 1 kΩ → Base; Emitter → GND; **1N4004 across the motor, cathode to +9 V**.

---

## 5. Top gotchas (the ones an examiner likes to probe)

1. LED without a series resistor → destroyed LED/pin.
2. Motor driven directly from a pin → dead pin.
3. Flyback diode omitted → inductive kick fries the transistor.
4. No **common ground** between logic and motor supplies → control signal meaningless.
5. Floating input with no pull-up/pull-down → noise, random `if` firing.
6. Button with no debounce → one press registers many times.
7. `analogWrite` on a non-`~` pin → only on/off, no dimming.
8. Servo powered from the Arduino 5 V pin → brown-out/resets.
9. `map()` without `constrain()` → glitchy sensor commands out-of-range values.
10. Threshold set without calibration → works in one room, fails in another.

---

## 6. Oral viva Q&A (30 questions with model answers)

**Episode 1**
1. **What is a microcontroller?** A tiny single-purpose computer on a chip that runs one program forever — no OS, no screen.
2. **Difference between `setup()` and `loop()`?** `setup()` runs once at power-on/reset for configuration; `loop()` runs repeatedly forever for behavior.
3. **Why does pin 13 Blink without an external resistor?** The Uno has a resistor soldered in series with the on-board LED on pin 13.
4. **What does `pinMode(pin, OUTPUT)` do?** Configures the pin to *drive* voltage out (push 5 V/0 V). `INPUT` makes it listen.
5. **Two causes of an upload failure?** Wrong board (`Tools → Board`) or wrong/missing port (`Tools → Port`, possibly missing USB driver).
6. **Does anything run during `delay(1000)`?** No — `delay()` blocks; the board reads nothing.

**Episode 2**
7. **What does `digitalRead` return?** `HIGH` or `LOW` for an input pin.
8. **What is a floating input, and the fix?** An unconnected input reads noise; fix with a pull-down (or pull-up / `INPUT_PULLUP`).
9. **What is switch bounce?** Mechanical contacts make/break several times in the first few ms, so one press looks like many.
10. **How does the debounce work?** If the reading changed, wait 5 ms, then re-read; return the stable value.
11. **Why detect a rising edge rather than the level?** So one press = one toggle, instead of flickering while held.
12. **What breaks if you drop `lastButton = currentButton;`?** The edge never fires and the button seems dead.
13. **Range of `analogWrite`, and which pins?** 0–255; PWM pins 3,5,6,9,10,11 (marked `~`).
14. **Is `analogWrite` real analog?** No — it is PWM (fast on/off) that averages out.

**Episode 3**
15. **State Ohm's law and the water-pipe analogy.** `V = I·R`; V = pressure, I = flow, R = pipe narrowness.
16. **Compute a 150 Ω LED resistor.** Supply 5 V, Vf ≈ 2 V → 3 V across resistor; `R = 3/0.020 = 150 Ω`.
17. **Pull-up vs pull-down?** Pull-down (to GND) rests LOW, button to +5 V; pull-up (to +5 V) rests HIGH, button to GND.
18. **State the voltage-divider formula.** `V_out = V_in·R₂/(R₁+R₂)`; equal 10 kΩ on 5 V → 2.5 V.
19. **What is a potentiometer electrically?** A resistor with a sliding wiper — a variable voltage divider.
20. **What does a 7805 do, and why the capacitors?** Regulates a higher/noisy input to clean 5 V; the decoupling caps stop ripple/oscillation.
21. **How do you measure current with a multimeter?** In series (through the component), never across the supply.

**Episode 4**
22. **What does `analogRead` return, and what does it represent?** 0–1023 (10-bit ADC) representing 0–5 V; ≈4.883 mV per step.
23. **Convert reading 512 to volts.** `512×5/1023 ≈ 2.5 V`.
24. **What does `map()` do, and its danger?** Linearly rescales a range; it does **not** clamp, so add `constrain()`.
25. **Why does my night light work backwards?** The LDR is on the wrong side of the divider (or the comparison is reversed).
26. **Why calibrate a threshold?** Sensor readings differ with light/supply/environment; you pick the value from live readings.

**Episode 5**
27. **Why can't a motor connect straight to a pin?** A pin sources ~40 mA max; a motor needs 100–1000+ mA — it would destroy the pin.
28. **Name the three components around the transistor and their jobs.** 1 kΩ base resistor (safe base current), 1N4004 flyback diode (kills the inductive spike), BC547 NPN (the switch).
29. **Why the flyback diode, and which way?** The motor coil kicks back a reverse voltage on switch-off; the diode placed across the motor, reversed (cathode to +V), gives it a safe path.
30. **Why a separate 5 V rail for the servo, and what must be shared?** Servo current spikes would brown out the board; the GND must be **common** so the signal has a reference.

---

## 7. Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep01-ep05|All programs (write + demonstrate) — companion note]]
- [[01-Areas/Engineering/arduino-microcontrollers/revision-ep01-ep05-test|Ep01–05 revision + 20-question self-test]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep01-getting-acquainted|Ep1]] · [[01-Areas/Engineering/arduino-microcontrollers/ep02-buttons-pwm-functions|Ep2]] · [[01-Areas/Engineering/arduino-microcontrollers/ep03-electrical-basics|Ep3]] · [[01-Areas/Engineering/arduino-microcontrollers/ep04-analog-inputs|Ep4]] · [[01-Areas/Engineering/arduino-microcontrollers/ep05-motors-transistors|Ep5]]
- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
- [[01-Areas/Engineering/BEE/INDEX|Basic Electrical Engineering]] — the formal circuit theory behind Ep3.
