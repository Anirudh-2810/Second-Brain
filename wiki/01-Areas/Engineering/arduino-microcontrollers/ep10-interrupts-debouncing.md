---
course_code: "ARDUINO-EP10"
course_name: "Arduino Tutorial Series — Episode 10"
unit: "Episode 10"
episode_url: "https://www.youtube.com/watch?v=3Zf6tPBr3n4"
blog_url: "https://www.jeremyblum.com/2011/03/07/arduino-tutorial-10-interrupts-and-hardware-debouncing/"
parts_list_url: "https://www.jeremyblum.com/wp-content/uploads/2011/01/Episode-10-Parts-List.pdf"
schematics_url: "https://www.jeremyblum.com/wp-content/uploads/2011/01/Episode-10-Schematics.zip"
tags: [engineering, arduino, embedded, beginner, interrupts, debouncing, volatile, millis, rc-filter, schmitt-trigger, tutorial]
last_updated: "2026-10-14"
confidence: high
description: "Episode 10 of Jeremy Blum's Arduino series: interrupts vs polling — attachInterrupt, interrupt modes (RISING/FALLING/CHANGE/LOW), the volatile keyword and ISR rules, hardware debouncing with an RC filter and Schmitt trigger (74HC14), software debouncing with millis(), and timer interrupts; a beam-break counter project."
---

## For future agent
This note covers Episode 10 (season finale) of Jeremy Blum's Arduino Tutorial Series — interrupts and hardware debouncing. Key facts: interrupts let hardware events (pin changes, timers) preempt the main loop. Use `attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)` with modes **RISING, FALLING, CHANGE, LOW**; on the Uno only **pins 2 and 3** support external interrupts. Variables shared with an ISR must be declared **volatile**; ISRs must be **fast** — no `delay()`, no `Serial`, no long work. **Debouncing** removes the multiple spurious edges from a mechanical contact: *hardware* uses an **RC low-pass filter + Schmitt trigger (74HC14)**; *software* records `millis()` of the last change and ignores edges within a window. Also covers **`millis()`-based timing** (non-blocking, vs `delay()`) and **timer interrupts**. Confidence: high. Note: `attachInterrupt` signature is the Arduino 1.0+ form.

# Episode 10 — Interrupts and Hardware Debouncing

## Episode Overview

The main loop is a cooperative single task: it does one thing at a time, in order. That is fine until an event must be caught the instant it happens — a beam break, a button pulse, an encoder tick — *while the program is busy with something else*. **Interrupts** solve this: the hardware taps the processor on the shoulder, the processor pauses the main loop, runs a small function (the **ISR**), then resumes exactly where it left off.

The second half addresses a physical reality: a mechanical switch or button does not open and close cleanly once — its metal contacts **bounce** for a few milliseconds, producing a burst of on/off edges. If you count those edges, you get dozens of false counts. **Debouncing** — in hardware (RC + Schmitt) or software (`millis()`) — fixes it.

The episode's project combines both: a **beam-break counter** that uses an interrupt to count objects instantly and hardware debouncing to avoid miscounts.

Two big ideas, plus a third worth internalising:

1. **Interrupts beat polling** for time-critical, brief events.
2. **Debouncing** is mandatory for any mechanical input.
3. **`millis()` replaces `delay()`** when you need non-blocking timing.

### Learning objectives
- Contrast polling and interrupts.
- Attach an ISR with `attachInterrupt` and pick the right mode.
- Respect ISR rules: short, `volatile` variables, no blocking calls.
- Understand what hardware debouncing is and build an RC + Schmitt filter.
- Implement a software debounce with `millis()`.
- Use `millis()` for non-blocking timing instead of `delay()`.
- Know what a timer interrupt is.

---

## Core Concepts (ELI5)

### Polling vs interrupts
**Polling** is repeatedly checking the door to see if anyone is there — wasteful if visitors are rare, and easy to miss if they arrive between checks. **Interrupts** ring a doorbell: you keep working, and the instant someone arrives you stop, answer, and resume. For a beam break that lasts microseconds, polling will *miss* it unless it happens to be looking at that exact moment; an interrupt never misses it.

**Analogy:** polling is refreshing your email every minute; interrupts are a phone that rings the moment a message arrives. For rare-but-urgent events, the phone wins.

### attachInterrupt and the modes
```cpp
attachInterrupt(digitalPinToInterrupt(2), myISR, FALLING);
```

- Pin: use `digitalPinToInterrupt(pin)` (Arduino 1.0+). On an **Uno, only pins 2 and 3** can trigger external interrupts.
- ISR: the function to call (no arguments, no return).
- Mode:
  - **RISING** — trigger when the pin goes low→high.
  - **FALLING** — high→low (typical for a beam break going dark).
  - **CHANGE** — either direction.
  - **LOW** — continuously while the pin is low (rarely used; can re-enter repeatedly).

`detachInterrupt(pin)` disables it.

### The volatile keyword
The compiler loves to cache variables in registers for speed. But a variable changed **inside an ISR** may be read in the main loop without the compiler knowing it changed — so you must tell the compiler "this can change at any time": declare it **`volatile`**.

```cpp
volatile int count = 0;   // changed by myISR, read in loop()
```

Omitting `volatile` is a classic bug: the counter "does not update" because the loop reads a stale cached value.

### ISR rules (iron laws)
An ISR runs **between instructions** of your main code, with interrupts often globally disabled. Therefore:

1. **Be fast.** Long ISRs delay everything and can make the whole system feel frozen.
2. **No `delay()`.** Blocking inside an ISR is forbidden in spirit and broken in practice.
3. **No `Serial.print()` in an ISR** (it relies on interrupts and can hang) — set a flag and print in the main loop instead.
4. **Touch few globals, and make shared ones `volatile`.**
5. **Do not allocate memory** in an ISR.

The usual pattern: the ISR flips a flag or increments a counter; the main loop does the heavy work.

### Mechanical bouncing
A switch is two pieces of metal colliding. For a few **milliseconds** they chatter — making and breaking contact several times — before settling. To a fast microcontroller each chatter is a legitimate edge, so a single press can count as 2–20 "presses". This is **contact bounce**.

### Hardware debouncing: RC + Schmitt
Two analog parts taming a digital problem:

- **RC low-pass filter** (a resistor into a capacitor) slows the fast chatter: the capacitor voltage rises/falls smoothly, ignoring the microsecond spikes.
- **Schmitt trigger** (e.g. the **74HC14** inverting Schmitt inverter) converts that slow, noisy analogue ramp into a single clean digital edge with **hysteresis** — two different thresholds (one to switch high, one to switch low) so noise near the middle cannot cause extra edges.

**Analogy:** an RC filter is a sponge that smooths the jitter; a Schmitt trigger is a bouncer who only lets you in once and only lets you out once, with a gap in between so you cannot jiggle the door and re-enter.

### Software debouncing with millis()
When hardware is not an option, debounce in code: record the timestamp of the last accepted change and ignore any new edge within a "debounce window" (say 50 ms).

```cpp
unsigned long lastDebounce = 0;
const unsigned long DEBOUNCE = 50;   // ms

void handlePress() {
  unsigned long now = millis();
  if (now - lastDebounce > DEBOUNCE) {
    count++;
    lastDebounce = now;
  }
}
```

Because `millis()` is a free-running millisecond clock that keeps counting regardless of what the code does, you can measure elapsed time without blocking. This is the key trick that also replaces `delay()`.

### millis() vs delay()
`delay(500)` stops everything for half a second — including your ability to react to buttons or interrupts being serviced promptly in the loop. `millis()` timing lets the loop keep spinning and only *act* when enough time has passed:

```cpp
if (millis() - lastTime > interval) {
  lastTime = millis();
  // do the periodic thing
}
```

This is the standard "blink without delay" pattern and the foundation of responsive code.

### Timer interrupts
Beyond pins, the microcontroller has **hardware timers**. You can configure a timer to fire an ISR at a fixed interval (e.g. every 1 ms) with libraries such as **TimerOne**. This gives you a reliable heartbeat independent of the loop — the basis of schedulers, PWM internally, and precise sampling.

---

## Code Walkthrough

### Program 1 — beam-break counter with interrupt + software debounce

```cpp
// Episode 10 - counter with interrupt + millis() debounce
int ledPin = 13;
int beamPin = 2;              // external interrupt pin

volatile int count = 0;
volatile unsigned long lastHit = 0;
const unsigned long DEBOUNCE = 50;   // ms

void onChange() {                     // ISR: keep it tiny
  unsigned long now = millis();
  if (now - lastHit > DEBOUNCE) {     // accept only after the window
    count++;
    lastHit = now;
  }
}

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(beamPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(beamPin), onChange, FALLING);
  Serial.begin(9600);
}

void loop() {
  // Non-blocking periodic report using millis()
  static unsigned long lastPrint = 0;
  if (millis() - lastPrint > 1000) {
    lastPrint = millis();
    Serial.print("Count: ");
    Serial.println(count);
  }

  // Fast blink the LED so we can SEE the loop is still running
  digitalWrite(ledPin, !digitalRead(ledPin));
  delay(150);
}
```

**Reasoning.**

- `volatile` on `count` and `lastHit` — they are written in the ISR and read in `loop`, so the compiler must not cache them.
- The ISR is short: compute `millis()`, compare, increment. No printing, no delays.
- The debounce window is *inside* the ISR here, so bounces are rejected immediately (fast response). It uses only `millis()` and writes — safe for an ISR.
- `loop()` keeps doing its own thing (blinking, periodic printing) — proof that interrupts run *alongside* the main loop rather than replacing it.
- The `static` variable `lastPrint` persists between loop calls, a tidy way to hold a timestamp.

### Program 2 — non-blocking blink with millis() (the pattern)

```cpp
// Blink without delay()
const int led = 13;
unsigned long lastToggle = 0;
const unsigned long PERIOD = 200;

void setup() { pinMode(led, OUTPUT); }

void loop() {
  if (millis() - lastToggle >= PERIOD) {
    lastToggle = millis();
    digitalWrite(led, !digitalRead(led));
  }
  // ...other tasks can run here freely...
}
```

The loop never stops; other code could read sensors or service logic in the same pass.

### Hardware debounce circuit (description)

```
   +5V
    |
   [10k]               74HC14
    |                 +--------+
    +---[ ]---+------>| input  |----> clean digital out
    |  switch |  0.1uF|        |
   GND        +------| GND    |
       (RC forms a low-pass; the Schmitt gang makes one clean edge)
```

The switch and capacitor sit at the input; the RC slows the chatter; the 74HC14 outputs a single crisp edge with hysteresis.

### Interrupt flow

```mermaid
sequenceDiagram
    participant Main as Main loop()
    participant HW as Hardware pin
    participant ISR as ISR onChange()
    Main->>Main: blinking, printing...
    HW->>ISR: FALLING edge on pin 2
    ISR->>ISR: millis(); debounce check; count++
    ISR-->>Main: return; loop resumes exactly here
```

---

## Key Functions Reference

| Function | Syntax | What it does | Example |
|----------|--------|--------------|---------|
| `attachInterrupt` | `attachInterrupt(digitalPinToInterrupt(p), ISR, mode)` | Call ISR on pin event. | `attachInterrupt(digitalPinToInterrupt(2), onChange, FALLING);` |
| `detachInterrupt` | `detachInterrupt(digitalPinToInterrupt(p))` | Disable the interrupt. | `detachInterrupt(digitalPinToInterrupt(2));` |
| `millis` | `millis()` | ms since boot (free-running). | `if(millis()-last>100)` |
| `micros` | `micros()` | µs since boot. | precise timing |
| `volatile` | `volatile int x;` | Tell compiler x may change anytime. | `volatile int count = 0;` |

**Modes:** RISING, FALLING, CHANGE, LOW. **Uno interrupt pins:** 2, 3 only. **Debounce window:** ~50 ms typical. **Schmitt part:** 74HC14.

---

## Common Pitfalls / Gotchas

1. **Forgetting `volatile`.** The counter appears frozen in `loop()` because the compiler cached it. Huge and extremely common bug.
2. **Using a non-interrupt pin.** `attachInterrupt` silently does nothing on pins other than 2/3 on the Uno. Use `digitalPinToInterrupt()`.
3. **Calling `delay()` or `Serial.print()` inside an ISR.** Hangs or misbehaves. Set a flag, print in the loop.
4. **Long ISRs.** Everything else stalls; timing degrades.
5. **Not debouncing.** One press counts many times. Fix in hardware (RC + Schmitt) or software (`millis()` window).
6. **Bounce re-entering a `CHANGE` ISR.** Each bounce is an edge; use `RISING`/`FALLING` *and* a debounce, not `CHANGE` alone.
7. **`millis()` overflow.** `millis()` wraps at ~49.7 days; the `millis() - last` subtraction still works correctly if `last` is `unsigned long` — do not compare raw values.
8. **Blocking with `delay()` in the loop.** You miss events and responsiveness dies; switch to the `millis()` pattern.
9. **Sharing a non-atomic multi-byte variable.** A 16-bit read can be interrupted mid-way; disable interrupts briefly around the read if it matters (`noInterrupts()/interrupts()`).
10. **Skipping the Schmitt trigger.** An RC filter alone gives a slow analogue edge that a digital input can still double-trigger; hysteresis matters.
11. **Expecting interrupts to work while interrupts are off.** Some libraries disable them; ISRs are delayed during that window.

---

## Practice Exercises

1. **Button counter.** Count button presses with an interrupt on pin 2 using FALLING, with software debounce. Verify one press = one count.
2. **Speed comparison.** Track how many times a fast beam break is missed by a *polling* loop versus caught by an interrupt.
3. **Non-blocking two-LED runner.** Blink two LEDs at different periods (200 ms and 500 ms) with *no* `delay()`, using `millis()`.
4. **Hardware debounce.** Build the RC + 74HC14 circuit and compare counts with and without it while flicking a switch rapidly.
5. **Encoder ticks.** If you have a rotary encoder, count its edges with `CHANGE` and a debounce, and display the position. This is the direct on-ramp to the Nexus Robotics encoder drills (T1).

---

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep02-buttons-pwm-functions|Episode 02 — Buttons & PWM]] — introduced switch bounce and a software debounce function; this episode's hardware debounce is the next level.
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Episode 06 — Serial]] — why you must NOT `Serial.print()` inside an ISR.
- [[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication|Episode 09 — Wireless]] — incoming radio data is another thing you may want to service without blocking.
- [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills|Nexus Robotics — Embedded Drills]] — T1 encoder counting via interrupts is exactly this material applied.
- [[01-Areas/Engineering/robotics/robotics-fundamentals|Robotics fundamentals]] — where sense→compute→actuate loops with real-time constraints are formalised.
- [[01-Areas/Programming/c-interview-revision-plain-language|C Revision (plain language)]] — `volatile`, memory, and the C execution model behind ISRs.
