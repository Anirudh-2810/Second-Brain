---
course_code: "ARDUINO-VIVA-PROGRAMS"
course_name: "Arduino Viva — All Programs Ep01–05 (write + demonstrate)"
unit: "Episodes 01–05"
tags: [engineering, arduino, microcontroller, embedded, beginner, viva, exam-prep, code, programs]
last_updated: "2026-10-17"
confidence: high
description: "Every Arduino program from Jeremy Blum Episodes 1–5, in full, with beginner line-by-line commentary, wiring diagrams, live-demo checklists, and 'write it on the spot' model answers. Companion to the viva-recap hub for Monday's practical viva."
---

## For future agent
This note is the **code half** of the Arduino Ep01–05 viva pack: all 9 programs from the five episodes reproduced in full with plain-language line-by-line commentary, plus wiring, per-program demo checklists, and model answers for live "write this now" prompts. It pairs with [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep01-ep05|viva-recap-ep01-ep05]] (the concept/glossary/question half). The deep theory lives in the per-episode notes [[01-Areas/Engineering/arduino-microcontrollers/ep01-getting-acquainted|Ep1]]–[[01-Areas/Engineering/arduino-microcontrollers/ep05-motors-transistors|Ep5]]. Code is stable Arduino C; confidence high. Manual-verification: exact IDE menu names drift across IDE versions — the *code* is version-stable.

# Arduino Ep01–05 — All Programs (write + demonstrate)

## How to use this note

- The **viva will ask you to demonstrate a circuit and/or write code live.** For each program below: read the *What it does*, be able to *draw the wiring*, and be able to *retype the code from memory*.
- **9 programs total.** Ep3 has **no code** — but expect a **calculation** ("size the LED resistor"), so read §Ep3.
- Every program uses the same skeleton: `setup()` runs once, `loop()` runs forever. Say that first if asked "explain the structure."

## Program index

| # | Ep | Program | Pins | Extra parts |
|---|----|---------|------|-------------|
| 1 | 01 | Blink built-in LED | 13 | none (on-board LED) |
| 2 | 02 | Button mirrors LED | 2 in, 13 out | push button, 10 kΩ |
| 3 | 02 | Debounced toggle | 2 in, 13 out | push button, 10 kΩ |
| 4 | 02 | PWM brightness steps | 2 in, 9 out | push button, 10 kΩ, LED + 150 Ω |
| 5 | 04 | Read + print photoresistor | A0, (Serial) | LDR + 10 kΩ divider |
| 6 | 04 | Automatic night light | A0, 9 out | LDR + 10 kΩ, LED + 150 Ω |
| 7 | 04 | Brightness follows light | A0, 9 out | LDR + 10 kΩ, LED + 150 Ω |
| 8 | 05 | DC motor ramp | 9 out | BC547, 1 kΩ, 1N4004, motor, 9 V |
| 9 | 05 | Servo follows distance | 9 out, A0 in | servo, 7805, Sharp IR |

---

## Program 1 — Blink (Episode 1)

**What it does:** Turns the LED already built into the board (on pin 13) on for 1 s, off for 1 s, forever.

**Wiring:** none. Pin 13's LED and its resistor are already on the board — that is the whole reason this is the first program.

```cpp
/*
  Jeremy Blum's first Arduino program.
  Blinks the built-in LED on pin 13 once per second.
*/

int ledPin = 13;   // the built-in LED is wired to digital pin 13

void setup() {
  pinMode(ledPin, OUTPUT);   // we want to drive the LED, so it's an OUTPUT
}

void loop() {
  digitalWrite(ledPin, HIGH);  // turn the LED ON  (5 volts)
  delay(1000);                 // wait 1000 milliseconds = 1 second
  digitalWrite(ledPin, LOW);   // turn the LED OFF (0 volts)
  delay(1000);                 // wait another second
}
```

**Line-by-line (beginner):**
- `/* ... */` — a **multi-line comment**; the compiler ignores it. `//` comments out the rest of one line.
- `int ledPin = 13;` — makes a **variable** named `ledPin` holding the integer `13`. Outside any function = **global**, visible everywhere below. Using a name instead of the bare number `13` documents *why* it is 13.
- `void setup() { ... }` — `void` = "returns nothing". `setup()` runs **once** at power-on/reset. Curly braces `{ }` are the **body**; round brackets `( )` hold arguments (here none).
- `pinMode(ledPin, OUTPUT);` — tells the board pin 13 is an **output** (allowed to push voltage out). Forgetting this makes the pin misbehave.
- `void loop() { ... }` — runs **over and over forever**; the program never exits.
- `digitalWrite(ledPin, HIGH);` — drives the pin to **5 V** (HIGH = on). `LOW` = 0 V = off.
- `delay(1000);` — **blocks** (does nothing else) for 1000 ms = 1 s. Remember: this blocking is a limitation fixed later.
- Every statement ends with `;`.

**If the examiner asks:**
- *Why no resistor?* The board has one soldered next to pin 13's LED.
- *What if you remove `pinMode`?* Pin floats on input, LED behaves unpredictably.
- *Can the board read a button during `delay(1000)`?* No — `delay()` blocks everything.

**Demo checklist:** pick `Tools → Board → Arduino Uno` → pick `Tools → Port → COM…` → click **Upload** → LED on pin 13 blinks once per second. If upload fails: wrong board, wrong port, or (old boards) missing USB driver.

---

## Program 2 — Button mirrors the LED (Episode 2)

**What it does:** While the button is held, the LED is on; released, it is off. The LED follows the button in real time.

**Wiring (pull-down):**
```
        +5V
         |
        [BUTTON]   (open = not pressed)
         |
   pin2 -+----[10k]--- GND
```
Unpressed → pin pulled to GND through 10 kΩ → reads LOW. Pressed → pin connects straight to +5 V → reads HIGH (the 5 V "wins" over the weak pull-down).

```cpp
int switchPin = 2;    // button is on digital pin 2
int ledPin = 13;      // LED is on pin 13

void setup() {
  pinMode(switchPin, INPUT);    // we READ this pin
  pinMode(ledPin, OUTPUT);      // we DRIVE this pin
}

void loop() {
  if (digitalRead(switchPin) == HIGH) {   // button pressed?
    digitalWrite(ledPin, HIGH);           // LED on
  } else {
    digitalWrite(ledPin, LOW);            // LED off
  }
}
```

**Line-by-line (beginner):**
- `pinMode(switchPin, INPUT);` — pin 2 is now an **input**: the board *listens* instead of *driving*.
- `digitalRead(switchPin)` — **asks** the pin "are you HIGH (5 V) or LOW (0 V)?"; returns `HIGH` or `LOW`.
- `if (...) { } else { }` — run one block or the other. Note `==` compares; `=` assigns — a classic exam trap.
- The **pull-down resistor** is what makes unpressed read a clean LOW. Without it the pin **floats** (acts like an antenna) and fires randomly.

**If the examiner asks:**
- *What does a floating input read?* Noise — random HIGH/LOW.
- *Why does the LED flicker slightly?* Switch **bounce**; fixed in Program 3.

**Demo checklist:** wire button + 10 kΩ as above, LED on 13. Upload. Holding the button lights the LED; releasing turns it off.

---

## Program 3 — Debounced toggle (Episode 2) ★ key program

**What it does:** Each **press** toggles the LED and it *stays* toggled. Needs **edge detection** (act only on the moment the button changes) plus **debouncing**.

**Wiring:** same as Program 2.

```cpp
int switchPin = 2;
int ledPin = 13;

boolean lastButton = LOW;      // previous stable reading
boolean currentButton = LOW;   // current cleaned reading
boolean ledOn = false;         // LED state we are toggling

void setup() {
  pinMode(switchPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

// Our own debounce function
boolean debounce(boolean last) {
  boolean current = digitalRead(switchPin);
  if (last != current) {          // a change was detected...
    delay(5);                     // ...wait for the bounce to settle
    current = digitalRead(switchPin);  // re-read
  }
  return current;                 // hand the stable value back
}

void loop() {
  currentButton = debounce(lastButton);

  // Detect a RISING edge: was LOW, now HIGH --> a fresh press
  if (lastButton == LOW && currentButton == HIGH) {
    ledOn = !ledOn;               // toggle the state
  }

  lastButton = currentButton;     // remember for next iteration
  digitalWrite(ledPin, ledOn);    // apply the state
}
```

**Line-by-line (beginner):**
- `boolean` holds `true`/`false` (interchangeable with `HIGH`/`LOW`).
- `boolean debounce(boolean last)` — our **own function**: return type `boolean`, one parameter `last`. `last` is the **parameter** (declared inside the brackets); the caller supplies its value.
- Inside: read the raw state into a **local** variable `current`. If it changed, `delay(5)` to let the metal contacts stop bouncing, then re-read. `return current;` hands the clean value back.
- `if (lastButton == LOW && currentButton == HIGH)` — **rising-edge detection**: only true on the transition from unpressed→pressed. That makes one press = one toggle instead of flickering while held.
- `lastButton = currentButton;` — update the memory. **Without this line the button seems dead** (the edge never fires).
- `digitalWrite(ledPin, ledOn);` — `ledOn` is a boolean; `digitalWrite` accepts `true`/`false`.

**If the examiner asks:**
- *What is switch bounce?* The metal contacts make/break several times in the first few ms, so one press looks like many.
- *Why 5 ms?* Long enough for bounce to settle, short enough to feel instant.
- *Why edge, not level?* So the LED toggles once per press rather than flickering the whole time you hold it.

**Demo checklist:** upload, press once → LED toggles and holds; press again → toggles back. Ask them to cover/uncover nothing — just demonstrate clean single toggles.

---

## Program 4 — PWM brightness steps with a button (Episode 2)

**What it does:** Each press raises brightness by one step (0→51→102→153→204→255), then wraps back to off.

**Wiring:** button on pin 2 (pull-down, same as before); LED + 150 Ω on **pin 9** (a PWM `~` pin).

```cpp
int switchPin = 2;
int ledPin = 9;               // MUST be a PWM (~) pin for analogWrite

boolean lastButton = LOW;
boolean currentButton = LOW;
int ledLevel = 0;             // running brightness 0..255

void setup() {
  pinMode(switchPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

boolean debounce(boolean last) {
  boolean current = digitalRead(switchPin);
  if (last != current) {
    delay(5);
    current = digitalRead(switchPin);
  }
  return current;
}

void loop() {
  currentButton = debounce(lastButton);
  if (lastButton == LOW && currentButton == HIGH) {  // one press
    ledLevel += 51;             // 0,51,102,153,204,255
    if (ledLevel > 255) ledLevel = 0;   // wrap back to off
  }
  lastButton = currentButton;
  analogWrite(ledPin, ledLevel);        // PWM out
}
```

**Line-by-line (beginner):**
- `analogWrite(pin, 0..255)` is **PWM** (not true analog). 0 = always off, 255 = always on, 128 ≈ half brightness. Only works on `~` pins: **3, 5, 6, 9, 10, 11**.
- `ledLevel += 51;` adds 51 each press. **Why 51?** 255 ÷ 5 ≈ 51, so five presses reach full.
- `if (ledLevel > 255) ledLevel = 0;` — wrap-around when full.
- Reuses the exact `debounce()` and edge-detect pattern from Program 3.

**If the examiner asks:**
- *Why pin 9 and not pin 13?* Pin 13 is not PWM-capable; `analogWrite` there behaves like on/off.
- *Is `analogWrite` real analog?* No — it is fast on/off PWM that *averages* to a brightness.

**Demo checklist:** wire LED + 150 Ω on pin 9, button on pin 2. Upload; each press brightens, sixth press restarts from off.

---

## Ep3 — no code, but expect this calculation

Episode 3 is theory. In the viva you may be asked to **size a resistor**. Do it out loud in 4 steps:

1. LED forward voltage `Vf` (red ≈ 2 V, blue/white ≈ 3.2 V) — the LED "uses up" this much.
2. Voltage across the resistor = supply − Vf. For 5 V, 2 V LED → **3 V**.
3. Pick a target current, e.g. 20 mA = 0.020 A.
4. `R = V / I = 3 / 0.020 = **150 Ω**`. Then check power `P = V·I = 3×0.02 = 60 mW` (safe for a 250 mW resistor).

Also be ready with: `V = I·R` (Ohm's law), `P = V·I` (power), voltage divider `V_out = V_in · R₂/(R₁+R₂)`, pull-up vs pull-down, and "7805 regulates 7–35 V in → clean 5 V out, with decoupling caps."

---

## Program 5 — Read and print a photoresistor (Episode 4)

**What it does:** Prints the raw analog reading (0–1023) from an LDR voltage divider to the Serial Monitor, 10 times per second. This is the *calibration* program.

**Wiring (LDR divider):**
```
   +5V --[LDR]--+--[10kΩ]-- GND
                |
                +--> A0
```
Bright light → LDR resistance falls → if LDR is the top resistor, the A0 voltage rises.

```cpp
int sensorPin = 0;     // analog input A0
int sensorValue = 0;   // will hold the ADC reading

void setup() {
  Serial.begin(9600);  // open the serial link to the computer
}

void loop() {
  sensorValue = analogRead(sensorPin);  // 0..1023
  Serial.println(sensorValue);          // print it, one per line
  delay(100);                           // 10 readings per second
}
```

**Line-by-line (beginner):**
- `Serial.begin(9600);` — opens the serial link at 9600 baud. Must match the Monitor's baud, or you see garbage.
- `analogRead(sensorPin)` — 10-bit **ADC**: samples the 0–5 V on A0 and returns **0–1023** (a *count*, not volts). 5 V/1024 ≈ 4.883 mV per step.
- `Serial.println(sensorValue)` — prints the number then a newline (use `print` for no newline).
- `delay(100)` — 10 readings/second, easy to watch.

**If the examiner asks:**
- *Convert the reading to volts:* `V = count × 5.0 / 1023`.
- *Why 1023 and not 1024?* 1024 steps (0–1023 inclusive).

**Demo checklist:** wire LDR divider → A0, upload, open **Serial Monitor** (magnifying-glass icon), set baud **9600**. Cover the LDR → number changes; note the light and dark values.

---

## Program 6 — Automatic night light (Episode 4)

**What it does:** Turns an LED **on when the room is dark** (reading below a threshold).

**Wiring:** LDR divider → A0; LED + 150 Ω on pin 9.

```cpp
int sensorPin = 0;        // photoresistor on A0
int ledPin = 9;           // LED on a PWM pin (or 13)
int threshold = 200;      // calibrated "dark" boundary

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int lightLevel = analogRead(sensorPin);

  if (lightLevel < threshold) {   // dark?
    digitalWrite(ledPin, HIGH);   // turn the light on
  } else {
    digitalWrite(ledPin, LOW);    // bright enough, keep off
  }

  Serial.println(lightLevel);     // watch calibration live
  delay(100);
}
```

**Line-by-line (beginner):**
- `lightLevel` is a **local** int holding this pass's reading.
- `if (lightLevel < threshold)` turns a raw number into a **decision**. The threshold value is **calibrated** — you watch Program 5's output in light and dark and pick a number in between.
- `Serial.println` stays in so you can prove the logic live.

**If the examiner asks:**
- *"Mine works backwards"* — the LDR is on the wrong side of the divider (or reverse the `<`/`>`); understand why: swap the sensor and fixed resistor positions flips the direction.
- *What is a threshold?* The decision boundary between "dark" and "bright."

**Demo checklist:** upload, cover LDR → LED on; uncover → LED off. Show the printed number crossing the threshold.

---

## Program 7 — Brightness follows light, using `map()` (Episode 4)

**What it does:** LED brightness smoothly tracks the light level (analog → PWM bridge).

**Wiring:** same as Program 6.

```cpp
int sensorPin = 0;
int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int lightLevel = analogRead(sensorPin);          // 0..1023
  int brightness = map(lightLevel, 0, 1023, 0, 255); // scale to PWM
  analogWrite(ledPin, brightness);                 // dim accordingly
  delay(50);
}
```

**Line-by-line (beginner):**
- `map(value, fromLow, fromHigh, toLow, toHigh)` — **linearly rescales** one range to another. Here 0–1023 → 0–255 so an ADC reading can drive `analogWrite`.
- `map()` is pure arithmetic (a straight-line fit). **It does NOT clamp** — out-of-range input can produce out-of-range output. Add `constrain()` if the sensor can glitch.

**If the examiner asks:**
- *Does `map()` limit the result?* No — follow with `constrain(v, lo, hi)` when needed (Jeremy does this in Ep5).
- *To make it brighter as it gets darker,* invert: `map(lightLevel, 0, 1023, 255, 0)`.

**Demo checklist:** upload; cover/uncover the LDR and watch the LED fade smoothly.

---

## Program 8 — DC motor ramp (Episode 5)

**What it does:** A DC motor accelerates from off to full speed and back, smoothly, via PWM through a transistor.

**Wiring (the transistor low-side switch):**
```
   +9V ---[ MOTOR ]---+-----------------------+
                      |                       |
                     (C)                   [DIODE]  (1N4004, reverse;
        Base drive    |                       |        cathode to +9V)
  pin9 --[1kΩ]--(B)  [NPN]                    (A)
                      |                       |
   GND ---------------(E)---------------------+
```
Motor sits between +9 V and the transistor **collector**; the transistor **emitter** goes to ground; the pin drives the **base** through **1 kΩ**. The **flyback diode** goes across the motor, reversed.

```cpp
// Episode 5 - DC motor speed ramp
int motorPin = 9;   // PWM pin -> transistor base (through 1k)

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  // Ramp from off to full speed
  for (int i = 0; i <= 255; i += 5) {
    analogWrite(motorPin, i);
    delay(30);
  }
  delay(500);              // hold at full speed briefly
  // Ramp back down
  for (int i = 255; i >= 0; i -= 5) {
    analogWrite(motorPin, i);
    delay(30);
  }
  delay(500);
}
```

**Line-by-line (beginner):**
- `for (int i = 0; i <= 255; i += 5) { ... }` — a **loop** that starts `i` at 0, keeps going while `i ≤ 255`, and adds 5 each pass. Inside, `analogWrite` sets the PWM duty = speed.
- `delay(30)` sets the ramp step time; `delay(500)` holds at the extremes.
- The **Arduino only sets the base drive** (tiny current); the **transistor switches the motor's own 9 V supply** (big current). This is why a 40 mA pin controls a motor drawing hundreds of mA.

**If the examiner asks:**
- *Why a transistor?* A pin sources ~40 mA max; a motor wants 100–1000+ mA. The pin is the decision-maker, not the power source.
- *Why the 1 kΩ base resistor?* Sets a safe, sufficient base current. Too big → transistor never fully turns on (gets hot); too small → excessive base current.
- *Why the flyback diode?* The motor is an inductor; cutting current makes a large reverse voltage spike. The diode (cathode to + V) gives the spike a safe path, protecting the transistor. **Never omit it.**
- *Why separate 9 V?* So the motor's current doesn't drag down the Arduino's supply; **grounds must be common.**

**Demo checklist:** build wiring, upload, watch the motor spin up then down. Point out the diode orientation and the common ground.

---

## Program 9 — Servo follows distance (Episode 5)

**What it does:** Reads the analog value from a distance sensor and maps it to a servo angle (0–180°). A full **sense → compute → actuate** loop.

**Wiring:**
```
  Sharp IR:  V+ --> +5V   GND --> GND   OUT --> A0
  Servo:     signal <-- Arduino pin 9
             V+ <-- separate 5V rail (9V battery -> 7805)
             GND <-- common ground with Arduino!
```

```cpp
#include <Servo.h>

Servo myServo;

int servoPin = 9;
int distPin = 0;    // Sharp IR analog output on A0
int dist = 0;
int angle = 0;

void setup() {
  myServo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  dist = analogRead(distPin);                    // 0..1023
  angle = map(dist, 0, 1023, 0, 180);            // to servo degrees
  angle = constrain(angle, 0, 180);              // safety clamp
  myServo.write(angle);                          // command the servo
  Serial.println(angle);
  delay(50);
}
```

**Line-by-line (beginner):**
- `#include <Servo.h>` pulls in the **Servo library**; `Servo myServo;` creates a servo object.
- `myServo.attach(9);` binds the servo's **signal** wire to pin 9.
- `map(dist, 0, 1023, 0, 180)` converts the sensor range to an angle; `constrain(angle, 0, 180)` **clamps** it so a glitch can't command past the mechanical limit.
- `myServo.write(angle)` commands the **angle** (0–180°), not a speed.
- The servo's **power comes from a separate 5 V rail** (9 V → 7805) so its current spikes don't brown out the Arduino; **GND is tied common.**

**If the examiner asks:**
- *Why not `analogWrite` the servo?* A servo needs a specific pulse train; the Servo library generates it.
- *Why separate power + common ground?* Current spikes brown out the board if powered from it; without common ground the control signal has no reference.
- *What does `constrain` prevent?* Angles outside 0–180° that make the servo strain.

**Demo checklist:** wire sensor on A0, servo signal on 9, servo power on the 7805 rail with common ground. Upload; move your hand nearer/farther — the servo sweeps.

---

## "Write it on the spot" — model prompts

Be able to produce these quickly from memory (all are shortened forms of the programs above).

**A. Blink an LED on pin 13, once per second.**
```cpp
void setup() { pinMode(13, OUTPUT); }
void loop() {
  digitalWrite(13, HIGH); delay(1000);
  digitalWrite(13, LOW);  delay(1000);
}
```

**B. Read a button on pin 2 (pull-down) and light the LED on pin 13 while pressed.**
```cpp
void setup() { pinMode(2, INPUT); pinMode(13, OUTPUT); }
void loop() {
  if (digitalRead(2) == HIGH) digitalWrite(13, HIGH);
  else                        digitalWrite(13, LOW);
}
```

**C. Turn on a night light (LED on pin 9) when an LDR reading on A0 falls below 200.**
```cpp
void setup() { pinMode(9, OUTPUT); }
void loop() {
  if (analogRead(A0) < 200) digitalWrite(9, HIGH);
  else                      digitalWrite(9, LOW);
}
```

**D. Fade an LED on pin 9 up and down with PWM.**
```cpp
void setup() { pinMode(9, OUTPUT); }
void loop() {
  for (int i = 0; i <= 255; i += 5) { analogWrite(9, i); delay(20); }
  for (int i = 255; i >= 0; i -= 5) { analogWrite(9, i); delay(20); }
}
```

**E. Map an analog reading on A0 (0–1023) to LED brightness on pin 9.**
```cpp
void setup() { pinMode(9, OUTPUT); }
void loop() { analogWrite(9, map(analogRead(A0), 0, 1023, 0, 255)); delay(20); }
```

**F. Sweep a servo on pin 9 from 0° to 180° and back.**
```cpp
#include <Servo.h>
Servo s;
void setup() { s.attach(9); }
void loop() {
  for (int a = 0; a <= 180; a++) { s.write(a); delay(15); }
  for (int a = 180; a >= 0; a--) { s.write(a); delay(15); }
}
```

**G. Drive a DC motor (base on pin 9) at half speed, then full.**
```cpp
void setup() { pinMode(9, OUTPUT); }
void loop() { analogWrite(9, 128); delay(1000); analogWrite(9, 255); delay(1000); }
```

---

## Code-mistake checklist (self-audit before you hand it in)

- Function bodies use **`{ }`**, arguments use **`( )`** — never `void setup() ( ... )`.
- Every statement ends in **`;`**.
- `if` tests use **`==`**; assignments use **`=`**.
- `pinMode` set for every pin you read (`INPUT`) or drive (`OUTPUT`).
- `analogWrite` only on **`~` pins** (3,5,6,9,10,11); `analogRead` only on **A0–A5**.
- `map()` followed by `constrain()` when the source can go out of range.
- In the debounce pattern, **update `lastButton = currentButton;`** every loop.
- `Serial.begin(...)` baud must match the Serial Monitor.

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep01-ep05|Viva recap hub (glossary, concepts, oral Q&A)]] — the other half of this pack
- [[01-Areas/Engineering/arduino-microcontrollers/revision-ep01-ep05-test|Ep01–05 revision + 20-question self-test]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep01-getting-acquainted|Ep1 — Getting Acquainted]] · [[01-Areas/Engineering/arduino-microcontrollers/ep02-buttons-pwm-functions|Ep2 — Buttons/PWM/Functions]] · [[01-Areas/Engineering/arduino-microcontrollers/ep03-electrical-basics|Ep3 — EE Basics]] · [[01-Areas/Engineering/arduino-microcontrollers/ep04-analog-inputs|Ep4 — Analog Inputs]] · [[01-Areas/Engineering/arduino-microcontrollers/ep05-motors-transistors|Ep5 — Motors/Transistors]]
- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
