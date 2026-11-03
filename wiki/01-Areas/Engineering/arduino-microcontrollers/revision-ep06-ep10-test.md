---
course_code: "ARDUINO-REVISION-EP06-10"
course_name: "Arduino Tutorial Series — Revision & Test (Ep 06–10)"
unit: "Episodes 06–10"
tags: [engineering, arduino, microcontroller, embedded, revision, test, exam-prep, serial, i2c, spi, wireless, interrupts]
last_updated: "2026-11-04"
confidence: high
description: "Condensed recall surface + self-test for Jeremy Blum Arduino Episodes 6–10: serial/ASCII, I2C/Wire, SPI, XBee wireless, interrupts and hardware debouncing. Formula/constants table, key functions, wiring topologies, protocol comparison, 20-question test with answers."
---

## For future agent
This is the recall-and-test surface for [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino module]] Episodes 6–10, the companion to [[01-Areas/Engineering/arduino-microcontrollers/revision-ep01-ep05-test|revision-ep01-ep05-test]]. It condenses the five deep episode notes into facts to recall cold (values, formulas, function signatures, wiring) plus a 20-question self-test with an answer key. Use it before a viva, before hardware work, or after reading Ep06–Ep10. For full annotated code and derivations, open the linked episode notes. The **wired two-Arduino** case is not an episode and lives in [[01-Areas/Engineering/arduino-microcontrollers/two-arduino-serial-communication|two-arduino-serial-communication]]; the unified pin/VDR/motor reference is [[01-Areas/Engineering/arduino-microcontrollers/arduino-uno-hardware-reference|arduino-uno-hardware-reference]]. Confidence: high (distilled from the high-confidence episode notes).

# Arduino EP06–10 — Full Revision & Test

## 1. Episode Map (what each episode owns)

| Ep | Title | One-line core | Must-recall facts |
|----|-------|---------------|-------------------|
| 06 | Serial Communication & Processing | Arduino ↔ computer text | `Serial.begin(9600)`; `print`/`println`; `available`/`read`; ASCII `'0'`=48, `'1'`=49, `'\n'`=10, `'\r'`=13; subtract `'0'`; `flush()` changed in 1.0; Processing reads the port and draws |
| 07 | I2C Communication & Processing | Two-wire addressed bus | SDA=A4, SCL=A5; 7-bit addresses 0–127; pull-ups (4.7–10 kΩ); TC74 @ **72** (0x48); beginTransmission/write/endTransmission/requestFrom/read; short distance |
| 08 | SPI Interfaces | Four-wire fast bus | SS=10, MOSI=11, MISO=12, SCK=13; full-duplex; **SS active low**; one SS per slave; MCP42010 digital pot (8-bit, registers from 0); `SPI.setClockDivider(SPI_CLOCK_DIV16)` → 1 MHz; daisy-chaining |
| 09 | Wireless (XBee) | Serial over radio | 2.4 GHz; **3.3 V only**; Series 1 = 802.15.4, Series 2 = ZigBee; PAN ID match, MY = own, DL = destination; transparent mode; `SoftwareSerial`; X-CTU config |
| 10 | Interrupts & Hardware Debouncing | Catch events + clean contacts | `attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)`; Uno interrupts = **pins 2, 3**; modes RISING/FALLING/CHANGE/LOW; `volatile`; ISR fast, no `delay`/`Serial`; RC + **74HC14** Schmitt debounce; `millis()` debounce ~50 ms; `millis()` vs `delay()` |

---

## 2. Formula & Constants Sheet

| Quantity | Formula / value | Notes |
|----------|-----------------|-------|
| Baud (series) | **9600** | both ends must match |
| Baud mismatch | garbage/no data | first thing to check |
| ASCII `'0'`…`'9'` | **48…57** | `char - '0'` → integer |
| Newline / carriage return | **10 / 13** | explains `49 10` and `-38` bugs |
| Arduino frame | **8N1** | 8 data, no parity, 1 stop |
| I2C address space | **7-bit, 0–127** | TC74 = 72 = 0x48 |
| I2C pull-ups | 4.7–10 kΩ to +5 V | one pair per bus |
| Uno I2C pins | **SDA=A4, SCL=A5** | |
| Uno SPI pins | **SS=10, MOSI=11, MISO=12, SCK=13** | SS active low |
| SPI clock | 16 MHz / divider | DIV16 → **1 MHz** |
| Digital pot steps | **0–255** (8-bit) | not 0–1023 |
| XBee band / logic | **2.4 GHz / 3.3 V** | 5 V destroys it |
| XBee params | PAN ID, MY, DL, DH, channel | both PANs match; MY↔DL cross |
| Uno interrupt pins | **2 (INT0), 3 (INT1)** | others silently ignored |
| Debounce window | **~50 ms** | typical software value |
| `millis()` wrap | **~49.7 days** | use `unsigned long` subtraction |
| PWM | 0–255 | pins 3,5,6,9,10,11 |
| ADC | 0–1023 over 0–5 V | ≈4.883 mV/step |

**Constants:** `HIGH`=5 V, `LOW`=0 V; ADC 10-bit; PWM 8-bit; serial 9600; I2C clock 100 kHz default (400 kHz fast); SPI default often too fast for a given slave.

---

## 3. Key Functions — Signature + Use

| Function | Signature | Ep | Gotcha |
|----------|-----------|----|--------|
| `Serial.begin` | `Serial.begin(baud)` | 06 | must match the other end |
| `Serial.print/println` | `Serial.print(x)` / `println(x)` | 06 | `print` = text; `write` = raw byte |
| `Serial.available` | `Serial.available()` → count | 06 | guard before reading |
| `Serial.read` | `Serial.read()` → byte or −1 | 06 | −1 corrupts arithmetic |
| `Serial.parseInt` | `Serial.parseInt()` | 06/09 | blocks up to timeout; skips non-digits |
| `Serial.readStringUntil` | `Serial.readStringUntil('\n')` | 06 | `trim()` the `\r` |
| `Serial.flush` | `Serial.flush()` | 06 | 1.0+ waits for TX; clear RX with a `while` read loop |
| `Wire.begin` | `Wire.begin()` | 07 | master; slave passes its address |
| `Wire.beginTransmission` | `Wire.beginTransmission(addr)` | 07 | decimal or `0x` address |
| `Wire.write` | `Wire.write(byte)` | 07 | register number, then data |
| `Wire.endTransmission` | `Wire.endTransmission()` | 07 | forget it → nothing sent |
| `Wire.requestFrom` | `Wire.requestFrom(addr, n)` | 07 | ask for n bytes |
| `Wire.available` | `Wire.available()` | 07 | wait before `read` |
| `Wire.read` | `Wire.read()` | 07 | one byte |
| `SPI.begin` | `SPI.begin()` | 08 | configures 11/12/13 |
| `SPI.transfer` | `SPI.transfer(byte)` | 08 | sends one, receives one |
| `SPI.setClockDivider` | `SPI.setClockDivider(SPI_CLOCK_DIV16)` | 08 | match the slave's max |
| `SoftwareSerial` | `SoftwareSerial(rx, tx)` | 09 | **RX first**, then TX |
| `Servo` | `myServo.attach(pin)` / `.write(deg)` | 05/09 | angle 0–180 |
| `attachInterrupt` | `attachInterrupt(digitalPinToInterrupt(p), ISR, mode)` | 10 | pins 2/3 only on Uno |
| `detachInterrupt` | `detachInterrupt(digitalPinToInterrupt(p))` | 10 | |
| `millis` / `micros` | `millis()`, `micros()` | 10 | non-blocking timing |
| `volatile` | `volatile int count;` | 10 | required for ISR-shared vars |

---

## 4. Wiring Topologies (recall cold)

**I2C (Ep07):**
```
Arduino A4 (SDA) ---> SDA ─┐
Arduino A5 (SCL) ---> SCL ─┤
+5V ----------------> Vcc  ├─ TC74 (addr 72)
GND ----------------> GND ─┘
SDA/SCL --[4.7k–10k]-- +5V   (one pair per bus)
```

**SPI (Ep08):**
```
D10 (SS)   ---> CS/SS   (active LOW)
D11 (MOSI) ---> SI
D12 (MISO) <--- SO
D13 (SCK)  ---> SCK
+5V --------> VDD/RS/SHDN
GND --------> VSS
Wiper ---[220R]--- LED --- GND
```

**XBee (Ep09):**
```
Arduino D2/D3 (SoftwareSerial) ---> XBee DIN/DOUT
3.3 V regulated ----------------> XBee VCC   (NEVER 5 V)
GND -----------------------------> XBee GND
PAN ID same on both; A.MY <-> B.DL; A.DL <-> B.MY
```

**Interrupt + software debounce (Ep10):**
```
+5V
 |
[10k]
 |
+--- pin 2
|
[switch]
|
GND
(ISR: if (millis()-last > 50) count++;)
```
Hardware version: same switch → **RC low-pass** (R + C to GND) → **74HC14 Schmitt trigger** → clean edge → pin 2.

**Two-Arduino wired UART (extension):**
```
A.TX ---> B.RX
A.RX <--- B.TX
A.GND --- B.GND
both begin(9600); send '\n' delimiters
```

---

## 5. Protocol Comparison (must be able to reproduce)

| | UART | I2C | SPI | XBee |
|---|---|---|---|---|
| Wires | 2 + GND | 2 (SDA/SCL) | 4 | 0 (radio) |
| Addressing | none (point-to-point) | 7-bit address | SS line per slave | PAN/MY/DL |
| Duplex | full | half | full | full |
| Clock | async | sync | sync | radio |
| Speed | 9.6–115.2 kbps | 100–400 kbps | MHz | ~250 kbps |
| Distance | short; RS-485 long | cm | cm | tens of m |
| Uno pins | 0/1, or SoftwareSerial | A4/A5 | 10–13 | D2/D3 (SoftwareSerial) |

---

## 6. The 10 Gotchas That Bite (Ep06–10)

1. **Baud mismatch** → garbage. Match both ends.
2. **ASCII vs value** — `'1'` = 49; subtract `'0'`; flush the newline.
3. **`Serial.flush()` is not "clear input" since Arduino 1.0** — it waits for TX. Clear RX with `while (Serial.available() > 0) Serial.read();`.
4. **I2C without pull-ups / with duplicate pull-ups** → dead or unstable bus.
5. **Two I2C devices with the same address** → collision; change address or bus.
6. **SPI SS left HIGH or forgotten** → slave never selected; **active low**.
7. **SPI clock too fast for the slave** → garbled/lost first byte; use `setClockDivider`.
8. **5 V into a 3.3 V XBee** → destroyed module; use a shield/level shifter.
9. **Forgetting `volatile` on an ISR-shared variable** → loop reads a stale cached value; counter appears frozen.
10. **Doing `delay()` or `Serial.print()` inside an ISR** → hang or broken timing; set a flag, handle it in `loop()`.

Bonus: **`map()` does not clamp** — always `constrain()`; **register numbering starts at 0** on the digital pot; **`millis()` must use `unsigned long` subtraction** to survive wrap.

---

## 7. Self-Test (20 questions)

Answer from memory before checking the key (§8).

**Episode 06**
1. What are the ASCII codes for `'0'`, `'1'`, `'\n'`, and `'\r'`? Why does typing `1` sometimes show `49 10`?
2. What does `Serial.available()` return, and why guard `Serial.read()` with it?
3. How do you correctly clear the *receive* buffer on Arduino 1.0+, and why not `Serial.flush()`?
4. In the Processing pipeline, what is the purpose of `bufferUntil('.')` / `readStringUntil('.')`?

**Episode 07**
5. Which two pins are SDA/SCL on the Uno, and why does I2C need pull-up resistors?
6. What is the TC74's address, and what is the sequence to read one byte from register 0?
7. How many devices can share an I2C bus, and what happens if two have the same address?

**Episode 08**
8. Name the four SPI lines, their Uno pins, and which one is active low.
9. Why did Jeremy need `SPI.setClockDivider(SPI_CLOCK_DIV16)`, and what clock does that produce?
10. What is the MCP42010's value range and register numbering, and what is the "LED 1 = register 0" trap?
11. Contrast SPI and I2C on wires, duplex, and addressing.

**Episode 09**
12. Why is powering an XBee from a 5 V Arduino pin dangerous, and what are two safe ways to do it?
13. What do PAN ID, MY, and DL mean, and how must they be set on two radios?
14. What is "transparent mode," and why does the receiver sketch differ from the sender only in what it does with the data?

**Episode 10**
15. Why does a beam-break need an interrupt instead of polling?
16. Which Uno pins support external interrupts, and what are the four trigger modes?
17. Why must an ISR-shared variable be `volatile`? What happens if it is not?
18. List four rules for a safe ISR.
19. Explain how an RC filter + 74HC14 debounces a switch. Why is the Schmitt trigger necessary?
20. How does `millis()`-based debounce/timing differ from `delay()`, and why does `millis() - last` survive overflow?

---

## 8. Answer Key

1. `'0'`=48, `'1'`=49, `'\n'`=10, `'\r'`=13. Typing `1` sends the **character** `'1'` (49) plus a line ending (10/13); printing the raw bytes shows `49 10`.
2. `available()` returns how many bytes are waiting. `read()` returns −1 when empty, which corrupts arithmetic; guard with `if (available() > 0)` or a wait loop.
3. `while (Serial.available() > 0) Serial.read();`. Since Arduino 1.0, `flush()` waits for **outgoing** data to finish, not incoming data to be discarded.
4. `bufferUntil('.')` tells Processing to accumulate until the delimiter; `readStringUntil('.')` returns that complete message, so the sketch gets whole values, not fragments.
5. **A4 = SDA, A5 = SCL.** I2C is open-drain: devices can only pull low, so pull-ups restore the high level.
6. Address **72** (0x48). `beginTransmission(72); write(0); endTransmission(); requestFrom(72,1); while(!available()); read();`
7. Up to **127** (7-bit addresses). Two identical addresses collide — the master cannot distinguish them; use a differently-addressed part, address pins, or a second bus.
8. **SS=10 (active low), MOSI=11, MISO=12, SCK=13.**
9. The MCP42010 could not keep up with the default SPI clock; DIV16 gives 16 MHz / 16 = **1 MHz**.
10. **0–255** per pot (8-bit), **registers start at 0**, so "LED 1" is register 0. Off-by-one sends commands to the wrong pot.
11. SPI: **4 wires, full-duplex, no addressing** (one SS per slave). I2C: **2 wires, half-duplex, 7-bit addressing** (many devices share the bus).
12. XBee is a **3.3 V** device; 5 V on its pins/power damages it. Use an XBee **shield** or an **explorer/breakout with a 3.3 V regulator and level shifting**.
13. **PAN ID** = network ID (must match on both); **MY** = this radio's own address; **DL** = the destination radio's address. Set each radio's DL to the other's MY and give both the same PAN ID.
14. Transparent mode makes the XBee behave like a **wireless serial cable**: bytes in one side appear at the other, so the sketch only decides what to send/do — the radio handles framing/addressing.
15. A beam break is a **microsecond** event; a polling loop can miss it between checks. An interrupt latches the edge immediately.
16. **Pins 2 and 3** (INT0, INT1). Modes: **RISING, FALLING, CHANGE, LOW**.
17. The compiler may cache a variable in a register; an ISR can change it asynchronously. Without `volatile`, `loop()` may read a stale value and the counter looks frozen.
18. Any four: be fast; no `delay()`; no `Serial.print()`; touch few globals; mark shared globals `volatile`; no dynamic allocation.
19. The **RC low-pass** smooths the fast contact chatter into a slow ramp; the **Schmitt trigger** converts that ramp into one clean edge using **hysteresis** (separate high/low thresholds), so noise near the middle cannot create extra edges. Without hysteresis, a slow edge can still double-trigger a digital input.
20. `delay()` blocks the whole CPU; `millis()` polling lets the loop keep running and act only when the interval has elapsed. `millis() - last` uses `unsigned long` arithmetic, so it gives the correct elapsed time even when the counter wraps (~49.7 days).

**Scoring:** 18–20 solid · 14–17 re-read the missed episode · <14 re-read §2–§6 and retake.

---

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
- [[01-Areas/Engineering/arduino-microcontrollers/revision-ep01-ep05-test|Ep01–05 Revision & Test]] — the first-half companion.
- [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep06-ep10|Ep06–10 Viva Recap]] — full forms, oral Q&A.
- [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep06-ep10|Ep06–10 All Programs]] — code half.
- [[01-Areas/Engineering/arduino-microcontrollers/two-arduino-serial-communication|Two-Arduino Wired Serial]] — the extra case.
- [[01-Areas/Engineering/arduino-microcontrollers/arduino-uno-hardware-reference|Arduino Uno Hardware Reference]] — pins, VDR, motors.
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Ep06]] · [[01-Areas/Engineering/arduino-microcontrollers/ep07-i2c-communication|Ep07]] · [[01-Areas/Engineering/arduino-microcontrollers/ep08-spi-interfaces|Ep08]] · [[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication|Ep09]] · [[01-Areas/Engineering/arduino-microcontrollers/ep10-interrupts-debouncing|Ep10]]
- [[01-Areas/Engineering/BEE/INDEX|Basic Electrical Engineering]] — formal circuit theory.
