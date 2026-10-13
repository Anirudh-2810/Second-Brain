---
course_code: "ARDUINO"
course_name: "Jeremy Blum Arduino Tutorial Series"
unit: "Module Hub"
tags: [engineering, arduino, microcontroller, embedded, tutorials, beginner]
last_updated: "2026-10-14"
confidence: high
description: "Jeremy Blum's 15-part Arduino Tutorial Series (element14 sponsored). Episodes 1-10 cover fundamentals: IDE/setup, buttons/PWM/EE basics, analog inputs, motors/transistors, serial/Processing, I2C/SPI, wireless/XBee, and hardware interrupts/debouncing. Designed for beginners moving from zero to standalone projects."
---

## For future agent
This module contains in-depth beginner-friendly notes for all 10 episodes of Jeremy Blum's Arduino Tutorial Series (element14/sponsored by element14). Each episode note (ep01–ep10) includes: YAML frontmatter with episode metadata, ELI5 concept analogies, fully annotated code walkthroughs, circuit/ASCII diagrams with Mermaid flowcharts, key functions reference tables, common pitfalls/gotchas linked to vault brain/gotchas, 3–5 practice exercises, and cross-links to related engineering concepts (BEE, nexus-robotics SPM C, Programming C). Source: YouTube playlist PLA567CE235D39FA84 + Jeremy Blum blog writeups (jeremyblum.com/category/arduino-tutorials). Staleness: Arduino C language is stable; circuit diagrams may need verification against latest hardware.

## Module Scope
**What this covers:** Episodes 1–10 of Jeremy Blum's Arduino Tutorial Series — from first-time Arduino setup through hardware interrupts and hardware debouncing. Topics span: IDE installation & blink sketch, digital I/O (buttons, PWM, functions), electrical engineering fundamentals (Ohm's law, pull-up/down resistors, voltage dividers, regulators), analog sensors (photoresistors, Sharp IR, `analogRead()`, `map()`), motor control (DC motors with NPN transistors, servos with voltage regulation), serial communication (USB serial, Processing visualization, ASCII data), I2C protocol (Wire library, multi-device addressing, TC74 temperature sensor), SPI protocol (SPI library, digital potentiometers MCP42010, clock dividers, daisy-chaining), wireless communication (XBee Series 1, PAN ID/AT commands, wireless serial passthrough), and hardware interrupts (attachInterrupt, volatile, RC + Schmitt trigger debounce circuits). **What this does NOT cover:** Episodes 11–15 of the series (LCD displays, GPS/GSM tracking, addressable LED strips, and sound) — these are advanced topics beyond the beginner scope.

## Episode Map
| Episode | Title | Key Topics | Note File |
|---------|-------|-----------|-----------|
| 01 | Getting Acquainted with Arduino | IDE, blink, drivers, `setup()`/`loop()`, pinMode, digitalWrite, delay, USB drivers | `ep01-getting-acquainted.md` |
| 02 | Buttons, PWM, and Functions | Push buttons, software debounce, functions, `analogWrite()` PWM, `debounce()` function | `ep02-buttons-pwm-functions.md` |
| 03 | Electrical Engineering Basics | Ohm's law, current-limiting resistors, pull-up/pull-down resistors, voltage dividers, potentiometers, voltage regulators, multimeters | `ep03-electrical-basics.md` |
| 04 | Analog Inputs | `analogRead()`, voltage divider, photoresistors, Sharp IR distance sensor, `map()`, `constrain()`, serial calibration | `ep04-analog-inputs.md` |
| 05 | Motors and Transistors | DC motors with 9V battery, NPN transistors (BC547), base resistor, 1N4004 flyback diode, PWM speed control, 180° servos, independent 5V rail (7805), H-bridge overview | `ep05-motors-transistors.md` |
| 06 | Serial Communication and Processing | USB Serial Monitor, `Serial.begin()`, `Serial.print()`, `Serial.read()`, `Serial.available()`, Processing IDE, ASCII table, the `Serial.flush()` 1.0 change, baud rate | `ep06-serial-processing.md` |
| 07 | I2C Communication and Processing | Wire library, I2C protocol, SDA (A4) & SCL (A5), pull-ups, TC74 temperature sensor, addressing up to 127 devices, `Wire.beginTransmission()`/`requestFrom()`/`read()`, Processing display | `ep07-i2c-communication.md` |
| 08 | SPI Interfaces | SPI protocol, MCP42010 digital potentiometer, `SPI.begin()`, `SPI.transfer()`, `SPI.setClockDivider()`, MOSI(11)/MISO(12)/SCK(13)/SS(10), slave-select, daisy-chaining | `ep08-spi-interfaces.md` |
| 09 | Wireless Communication | XBee (802.15.4 / ZigBee), 3.3V logic, X-CTU config (PAN ID, MY, DL), transparent serial mode, pot-to-servo link, `SoftwareSerial` | `ep09-wireless-communication.md` |
| 10 | Interrupts and Hardware Debouncing | `attachInterrupt()`, interrupt modes, `volatile`, ISR rules, hardware debounce (RC + Schmitt 74HC14), software debounce with `millis()`, timer interrupts, beam-break counter | `ep10-interrupts-debouncing.md` |

> **Video IDs:** individual YouTube video IDs are **not recorded** here (unverified). Use the playlist link below to reach every episode.

## Quick Answers
- "How do I fix error: function 'void setup()' is initialized like a variable?" → Always use curly braces `{ }` for function bodies. `void setup() { /* code */ }` (see Ep1 comments: Spur's June 2013 error).
- "What's the difference between analogRead() and digitalRead()" → `analogRead()` returns 0–1023 (10-bit ADC, 0–5V); `digitalRead()` returns HIGH or LOW (5V or 0V).
- "When do I need a pull-up vs pull-down resistor?" → Pull-down: button to ground, pin reads LOW when unpressed (Ep3). Pull-up: button to 5V, pin reads HIGH when unpressed (use `INPUT_PULLUP` in Ep10).
- "Why is my LED dim even with analogWrite(255)?" → `analogWrite()` is PWM, not analog. Use 8-bit (0–255) duty cycle. 0 = off, 255 = full on. See Ep2 PWM explanation.
- "How do I configure XBees for wireless communication?" → Use X-CTU software: set MY (our ID), DL (destination low), DH (destination high), PAN ID (personal area network). Both modules same PAN ID. See Ep9.
- "What's the difference between SoftwareDebounce (Ep2) and HardwareDebounce (Ep10)?" → Software: waits `delay(5–10ms)` in loop, checks state. Hardware: RC circuit + 74HC14 Schmitt trigger removes noise before pin sees it (Ep10).

## Cross-Domain Links
| Target | Relevance |
|--------|-----------|
| `[[01-Areas/Engineering/BEE/INDEX|BEE]]` | Ohm's law, Kirchhoff's laws, DC circuit theory foundation |
| `[[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills|nexus-robotics embedded drills]]` | T4 debounce state machine, T7 PID anti-windup, fixed-point arithmetic |
| `[[01-Areas/Programming/c-interview-revision-plain-language#15-embedded-c-idioms|c-interview plain C §15]]` | `volatile`, ISR discipline, fixed-point, no `malloc` in ISR |
| `[[01-Areas/Engineering/SPM/module-1-spm-c-basics|SPM C Basics]]` | Memory layout (Text/Data/BSS/Heap/Stack), compilation pipeline, embedded targets |
| `[[01-Areas/Engineering/robotics/ros2-architecture|ROS2 micro-ROS]]` | When advancing beyond Arduino: rclc executor, LET semantics for embedded MCUs |

## Related Resources (outside vault)
- **YouTube Playlist:** `https://www.youtube.com/playlist?list=PLA567CE235D39FA84`
- **Blog Index:** `https://www.jeremyblum.com/category/arduino-tutorials/`
- **Parts Lists (PDFs):** `https://www.jeremyblum.com/wp-content/uploads/2011/01/Episode-01-Parts-List.pdf` through `Episode-10-Parts-List.pdf`
- **Arduino Reference:** `https://www.arduino.cc/reference/en/`
- **Processing Tutorials:** `https://processing.org/tutorials/`

## Revision Guide
Use these notes to:
1. Rebuild circuits from ASCII diagrams + parts lists
2. Adapt code snippets for own projects (always credit Jeremy Blum)
3. Reference function tables for `pinMode`, `digitalWrite`, `digitalRead`, `analogRead`, `analogWrite`, `delay`, `setup()`, `loop()`, `map()`, `Serial.*`, `Wire.*`, `SPI.*`, `attachInterrupt()`
4. Cross-check gotchas before debugging own hardware
5. Practice 3 exercises per episode to cement concepts