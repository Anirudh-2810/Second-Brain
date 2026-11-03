---
course_code: "ARDUINO-VIVA-RECAP-EP06-10"
course_name: "Arduino Viva Recap — Ep06–10 (concepts, full-forms, oral Q&A)"
unit: "Episodes 06–10"
tags: [engineering, arduino, microcontroller, embedded, beginner, viva, exam-prep, glossary, serial, i2c, spi, wireless, interrupts]
last_updated: "2026-11-04"
confidence: high
description: "Beginner-depth viva recap for Jeremy Blum Arduino Episodes 6–10: every acronym expanded, a plain-language episode-by-episode recap, formula/constants sheet, protocol and circuit topologies, and a 30-question oral Q&A with model answers. Pairs with the all-programs note."
---

## For future agent
This is the **concept half** of the Arduino Ep06–10 viva pack, companion to [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep01-ep05|viva-recap-ep01-ep05]]. It gives a full-forms glossary, an ELI5 recap of each episode, the formula/constants sheet, the wiring topologies, and a 30-question oral Q&A. The **code half** (all programs + demo checklists + write-it-live drills) is [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep06-ep10|viva-programs-ep06-ep10]]. Deep per-episode theory: [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Ep6]]–[[01-Areas/Engineering/arduino-microcontrollers/ep10-interrupts-debouncing|Ep10]]. The wired two-Arduino case is an extension in [[01-Areas/Engineering/arduino-microcontrollers/two-arduino-serial-communication|two-arduino-serial-communication]]. Manual-verification: values/formulas are exam-grade and stable; IDE/menu details and clone hardware drift by version.

# Arduino Ep06–10 — Viva Recap (concepts, full forms, oral answers)

## How to use this pack

Two notes:
- **This note** — understand and *say* the concepts (glossary, recap, formulas, oral Q&A).
- **[[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep06-ep10|All programs note]]** — *write* and *demonstrate* the code.

If asked "what did Episodes 6–10 cover?", the one-line answer: **6) serial communication with a computer and visualising data in Processing, 7) the I2C two-wire bus and a temperature sensor, 8) the SPI four-wire bus and a digital potentiometer, 9) wireless serial over XBee between two Arduinos, 10) interrupts and debouncing for reliable event handling.**

---

## 1. Full-Forms Glossary (every acronym expanded)

| Short form | Full form | Plain meaning | First seen |
|-----------|-----------|---------------|-----------|
| **UART** | Universal Asynchronous Receiver-Transmitter | The hardware serial block (start/stop bits, no shared clock) | Ep6 |
| **USART** | Universal Synchronous/Asynchronous Receiver-Transmitter | UART + optional clock; the ATmega has a USART used as UART | Ep6 |
| **TTL** | Transistor-Transistor Logic | The 0/5 V signal levels used between boards | Ep6 |
| **TX / RX** | Transmit / Receive | The two serial data lines; cross TX→RX | Ep6 |
| **ASCII** | American Standard Code for Information Interchange | Number-to-character table (`'0'`=48, `'1'`=49, `'\n'`=10) | Ep6 |
| **CR / LF** | Carriage Return / Line Feed | `'\r'`=13 and `'\n'`=10, the line endings that cause `49 10` | Ep6 |
| **baud** | (from Émile Baudot) | Symbols per second; both ends must match (9600 here) | Ep6 |
| **8N1** | 8 data bits, No parity, 1 stop bit | Arduino's default serial frame | Ep6 |
| **COM** | Communications port | Windows name for a serial port (`COM3`) | Ep6 |
| **IDE** | Integrated Development Environment | The Arduino app (and Processing's app) | Ep1/Ep6 |
| **I2C / I²C** | Inter-Integrated Circuit | Two-wire addressed bus (SDA + SCL) | Ep7 |
| **SDA** | Serial DAta | I2C data line (Uno **A4**) | Ep7 |
| **SCL** | Serial CLock | I2C clock line (Uno **A5**) | Ep7 |
| **SPI** | Serial Peripheral Interface | Four-wire high-speed synchronous bus | Ep8 |
| **MOSI** | Master Out, Slave In | SPI data from Arduino to device (Uno **11**) | Ep8 |
| **MISO** | Master In, Slave Out | SPI data from device to Arduino (Uno **12**) | Ep8 |
| **SCK / SCLK** | Serial CLocK | SPI clock from the master (Uno **13**) | Ep8 |
| **SS / CS** | Slave Select / Chip Select | Per-device select line, **active LOW** (Uno **10**) | Ep8 |
| **MSB / LSB** | Most / Least Significant Bit | Bit order in a byte (SPI default MSB first) | Ep8 |
| **full duplex** | — | Send and receive at the same time (SPI, UART) | Ep8 |
| **half duplex** | — | One direction at a time (I2C) | Ep7 |
| **open-drain** | — | A line that can only pull low; needs a pull-up to go high (I2C) | Ep7 |
| **XBee** | (brand name) | Digi radio module that acts as a wireless serial cable | Ep9 |
| **802.15.4** | IEEE 802.15.4 | Low-rate wireless standard; XBee **Series 1** | Ep9 |
| **ZigBee** | (ZigBee Alliance standard) | Mesh protocol; XBee **Series 2** (coordinator/router/end device) | Ep9 |
| **PAN ID** | Personal Area Network Identifier | The radio "network name"; must match on both | Ep9 |
| **MY** | (this module's address) | The radio's own source address | Ep9 |
| **DL / DH** | Destination Low / Destination High | Address of the radio this one sends to | Ep9 |
| **X-CTU** | (Digi configuration utility) | Windows tool to read/write XBee settings | Ep9 |
| **ISR** | Interrupt Service Routine | The small function the hardware calls on an event | Ep10 |
| **IRQ** | Interrupt ReQuest | The signal/event that triggers an ISR | Ep10 |
| **volatile** | — | C keyword: "this variable may change at any time; do not cache it" | Ep10 |
| **RC** | Resistor–Capacitor | The low-pass filter that slows switch chatter | Ep10 |
| **Schmitt trigger** | (named after Otto Schmitt) | A comparator with hysteresis; cleans a slow/noisy edge (74HC14) | Ep10 |
| **hysteresis** | — | Two thresholds (high and low) so noise near the middle cannot re-trigger | Ep10 |
| **PWM** | Pulse Width Modulation | Fast on/off that averages to a variable level | Ep2/Ep5 |
| **ADC** | Analog-to-Digital Converter | 0–5 V → 0–1023 | Ep4 |
| **SRAM / EEPROM** | Static RAM / Electrically Erasable Programmable ROM | Working memory / non-volatile settings | Ep1 |
| **VDR** | Voltage Divider Rule | $V_{out}=V_{in}\frac{R_2}{R_1+R_2}$ | Ep3 |
| **BJT / NPN** | Bipolar Junction Transistor / N-P-N | The switch transistor used for motors (BC547) | Ep5 |
| **GND** | Ground | The 0 V reference that must be common between boards | Ep1/Ep5 |

> In a viva, name the acronym and immediately give the full form — it signals understanding, not memorisation.

---

## 2. Episode-by-episode plain-language recap

### Episode 6 — Serial communication and Processing
- **Serial** sends bits one at a time down a pair of wires: **TX** from Arduino to computer, **RX** back. Over USB these are virtual, but the model is identical.
- Both ends must agree on **baud** (9600). Mismatch = garbage. This is the digital version of talking too fast for the listener.
- **Characters are not numbers.** Typing `1` sends the character `'1'`, whose **ASCII** code is **49**. The line ending adds **10** (`\n`) or **13** (`\r`) — hence `49 10` or the infamous `-38` (10 − 48).
- **Fix:** subtract `'0'`: `int val = Serial.read() - '0';`. Clear leftovers with `while (Serial.available() > 0) Serial.read();`. `Serial.flush()` changed in Arduino 1.0 (now waits for outgoing data), so it does *not* clear the input.
- **`Serial.available()`** = bytes waiting; **`Serial.read()`** = one byte; **`parseInt()`** = read a number until a non-digit.
- **Processing** is a Java-based visual IDE. It opens the same COM port, buffers until a delimiter (`.`), and draws the data. Arduino adds the delimiter; Processing splits on it.

### Episode 7 — I2C communication and Processing
- **Why a bus?** Wiring one sensor per pin does not scale. **I2C** puts many devices on **two shared wires**: **SDA** (data) and **SCL** (clock).
- **Addresses:** each device has a **7-bit address** (0–127). The master calls an address; only that device answers. The **TC74** temperature sensor is at **72** (0x48).
- **Open-drain + pull-ups:** devices can only pull a line low, so **pull-up resistors** (4.7–10 kΩ) restore high. One pair per bus; many breakout boards include them.
- **Master/slave, request/response:** the Arduino initiates. Write a register number (`beginTransmission` → `write` → `endTransmission`), then request bytes (`requestFrom` → `available` → `read`).
- **Distance:** I2C is for **centimetres** (on-board). Use **CAN, RS-485, UART, or USB** for long runs.
- **Pipeline:** sensor → I2C → Arduino → USB serial → Processing → screen.

### Episode 8 — SPI interfaces
- **SPI** is the other workhorse bus: **4 wires**, **full-duplex**, **much faster** than I2C.
- **Lines:** **SCK** (clock), **MOSI** (master out), **MISO** (master in), **SS/CS** (select, **active LOW**). Uno: **10/11/12/13**.
- **No addressing.** Each slave needs its own **SS** line; pulling it low selects that device. Forgetting to select → nothing happens; leaving it low → confusion.
- **The project:** an **MCP42010 digital potentiometer** (two 8-bit pots, **0–255**, registers start at **0**) fades LEDs. Two bytes per command: register, then value.
- **Clock speed:** the slave has a maximum. Jeremy used **`SPI.setClockDivider(SPI_CLOCK_DIV16)`** → 16 MHz / 16 = **1 MHz** when writes misbehaved.
- **Daisy-chaining:** share SCK/SS, wire data in series, and one select pulse updates many chips (e.g. 74HC595 shift registers).

### Episode 9 — Wireless communication (XBee)
- The **XBee** is a radio that looks like a **serial port**. In **transparent mode** it is a wireless serial cable: bytes in one side come out the other.
- **Series 1** = **802.15.4** (simple point-to-point/star, beginner-friendly). **Series 2** = **ZigBee** (mesh: coordinator/router/end device, more configuration). Both **2.4 GHz**.
- **Three settings:** **PAN ID** (network, must match), **MY** (own address), **DL** (destination). Each radio's DL points at the other's MY.
- **3.3 V only** — both power and logic. 5 V can destroy it. Use an **XBee shield** or an explorer board with regulation and level shifting. Keep the supply clean.
- **X-CTU** configures it on Windows (awkward on Mac; AT commands are the alternative).
- **Project:** pot on sender → `map` to 0–180 → `SoftwareSerial` → radio → receiver `parseInt` → `Servo.write`. Only the radio changed; the serial model is Ep06's.

### Episode 10 — Interrupts and hardware debouncing
- **Polling** repeatedly checks; **interrupts** ring a doorbell. For a microsecond beam-break, polling misses; an interrupt catches it.
- **`attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)`** with **RISING / FALLING / CHANGE / LOW**. On the Uno, **only pins 2 and 3**.
- **`volatile`** tells the compiler a variable can change at any time (inside an ISR). Without it, the loop may read a stale cached value.
- **ISR rules:** be fast; **no `delay()`**, **no `Serial.print()`**; touch few globals; no dynamic memory. Set a flag or increment a counter; do the work in `loop()`.
- **Bounce:** mechanical contacts chatter for a few milliseconds, so one press looks like many edges.
  - **Hardware debounce:** **RC low-pass** (R + C) smooths the chatter; **74HC14 Schmitt trigger** turns the ramp into one clean edge with **hysteresis**.
  - **Software debounce:** record `millis()` of the last accepted edge and ignore edges within a window (~50 ms).
- **`millis()` vs `delay()`:** `delay()` blocks everything; `millis()` timing lets the loop keep running. `millis() - last` works across the ~49.7-day overflow because the subtraction is unsigned.
- **Timer interrupts** (e.g. TimerOne) fire an ISR at a fixed interval — the heartbeat for schedulers and precise sampling.

---

## 3. Formula & constants sheet

| Quantity | Formula / value | Episode |
|----------|-----------------|---------|
| Baud | 9600 (series) | 6, 9 |
| ASCII | `'0'`=48, `'1'`=49, `'\n'`=10, `'\r'`=13 | 6 |
| Digit conversion | `value = char - '0'` | 6 |
| Serial frame | 8N1 | 6 |
| I2C addresses | 7-bit, 0–127; TC74 = 72 = 0x48 | 7 |
| I2C pull-ups | 4.7–10 kΩ to +5 V, one pair | 7 |
| SPI clock | 16 MHz / divider; DIV16 → 1 MHz | 8 |
| Digital pot | 0–255, registers from 0 | 8 |
| XBee | 2.4 GHz, 3.3 V, PAN/MY/DL | 9 |
| Uno interrupts | pins 2, 3 | 10 |
| Debounce window | ~50 ms | 10 |
| `millis()` wrap | ~49.7 days; use unsigned subtraction | 10 |
| PWM | 0–255, pins 3/5/6/9/10/11 | 2, 5 |
| ADC | 0–1023 over 0–5 V, ≈4.883 mV/step | 4 |
| VDR | $V_{out}=V_{in}\frac{R_2}{R_1+R_2}$ | 3 |
| LED resistor | $R=(V_s-V_f)/I$ | 3 |

---

## 4. Circuit and protocol topologies (be able to draw + explain)

1. **Serial to PC (Ep6):** USB cable; pin 0/1 internally; `Serial.begin(9600)` both sides. Arduino prints, Monitor shows; Monitor types, Arduino reads.
2. **I2C (Ep7):** A4→SDA, A5→SCL, +5V→Vcc, GND→GND, pull-ups SDA/SCL→+5V. TC74 at 72.
3. **SPI (Ep8):** D10→SS (active low), D11→MOSI, D12→MISO, D13→SCK; 5 V/GND; digital pot wiper→LED.
4. **XBee (Ep9):** Arduino ↔ XBee over serial; 3.3 V regulated power; PAN matched; MY↔DL crossed; antenna clear.
5. **Interrupt debounce (Ep10):** switch → RC low-pass → 74HC14 Schmitt → pin 2 (INT0); ISR increments a `volatile` counter.
6. **Two-Arduino wired UART (extension):** A.TX→B.RX, A.RX→B.TX, common GND, both 9600, `'\n'` delimiters.

---

## 5. Top gotchas (the ones an examiner probes)

1. Baud mismatch → garbage.
2. ASCII vs value → subtract `'0'`; line ending causes `49 10`/`-38`.
3. `Serial.flush()` no longer clears the input buffer.
4. I2C missing/duplicated pull-ups; duplicate addresses.
5. SPI SS active-low confusion; forgetting to select/deselect.
6. SPI clock too fast for the slave.
7. 5 V into a 3.3 V XBee.
8. XBee PAN/DL misconfiguration.
9. Forgetting `volatile` on an ISR-shared variable.
10. `delay()`/`Serial.print()` inside an ISR.
11. Not debouncing a mechanical input.
12. `map()` without `constrain()`; digital-pot register off-by-one.

---

## 6. Oral viva Q&A (30 questions with model answers)

**Episode 6**
1. **What is serial communication?** Sending bits one after another down a wire pair; the Arduino's UART converts bytes to/from that stream.
2. **What is baud, and what happens on mismatch?** Symbols per second; a mismatch makes the receiver sample at the wrong times, producing garbage.
3. **Why does typing `1` sometimes show `49`?** `1` is a character, and its ASCII code is 49. Subtract `'0'` to get the integer 1.
4. **What are `available()` and `read()`?** `available()` counts waiting bytes; `read()` returns one byte (or −1 if none).
5. **Why did `Serial.flush()` break old tutorials?** Arduino 1.0 changed it to wait for outgoing data; it no longer discards incoming bytes.
6. **What does Processing add?** A computer-side program that reads the serial port and visualises the data (graphs, gauges, text).

**Episode 7**
7. **What is I2C and why use it?** A two-wire addressed bus that lets many devices share SDA/SCL, saving pins.
8. **Which Uno pins are SDA/SCL?** A4 (SDA), A5 (SCL).
9. **Why pull-ups?** I2C is open-drain; devices only pull low, so pull-ups restore the high level.
10. **How many devices, and what if addresses collide?** Up to 127; identical addresses collide — change address pins/part or use another bus.
11. **What address is the TC74, and how do you read it?** 72 (0x48); write register 0, then request one byte and read it.
12. **Why is I2C unsuitable for long cables?** Its pull-up/capacitance model degrades; use CAN/RS-485/UART/USB instead.

**Episode 8**
13. **Name the four SPI lines.** SCK, MOSI, MISO, SS.
14. **What does active-low SS mean?** Pull it LOW to select a device, HIGH to release it.
15. **How does SPI differ from I2C?** SPI: 4 wires, full-duplex, no addressing, one SS per slave, much faster. I2C: 2 wires, half-duplex, addressed, slower.
16. **Why slow the SPI clock?** A slave has a maximum clock; too fast causes misread/lost bytes. DIV16 gives 1 MHz.
17. **What is daisy-chaining?** Sharing SCK/SS and wiring data in series so one select pulse updates many chips.

**Episode 9**
18. **What is an XBee in transparent mode?** A wireless serial cable: bytes in one side appear at the other.
19. **Series 1 vs Series 2?** Series 1 = 802.15.4 point-to-point/star; Series 2 = ZigBee mesh with coordinator/router/end device.
20. **What are PAN ID, MY, and DL?** Network ID, own address, destination address. Both PANs match; each DL points at the other's MY.
21. **Why 3.3 V only?** XBee logic and supply are 3.3 V; 5 V damages it. Use a shield/explorer with regulation and level shifting.
22. **Why does the receiver use `parseInt()`?** It reads digits until the newline delimiter, robustly parsing the angle; `constrain` guards bad values.

**Episode 10**
23. **Polling vs interrupts?** Polling checks repeatedly and can miss brief events; an interrupt runs an ISR immediately on the event.
24. **Which Uno pins, and which modes?** Pins 2 and 3; RISING, FALLING, CHANGE, LOW.
25. **Why `volatile`?** It stops the compiler caching a variable that an ISR may change asynchronously.
26. **What can an ISR not do?** Be slow, call `delay()`, call `Serial.print()`, allocate memory, or touch many globals.
27. **What is switch bounce?** Mechanical contacts make/break several times in a few milliseconds, producing false edges.
28. **How does hardware debouncing work?** An RC low-pass smooths chatter; a Schmitt trigger (74HC14) produces one clean edge with hysteresis.
29. **How does software debouncing work?** Record `millis()` of the last accepted edge and ignore new edges within ~50 ms.
30. **Why `millis()` instead of `delay()`?** `delay()` blocks the whole program; `millis()` lets the loop keep running and act only when the interval elapses; unsigned subtraction survives wraparound.

---

## 7. Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep06-ep10|All programs (write + demonstrate) — companion note]]
- [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep01-ep05|Ep01–05 Viva Recap]] — the first-half concept pack.
- [[01-Areas/Engineering/arduino-microcontrollers/revision-ep06-ep10-test|Ep06–10 Revision & Self-Test]]
- [[01-Areas/Engineering/arduino-microcontrollers/two-arduino-serial-communication|Two-Arduino Wired Serial]]
- [[01-Areas/Engineering/arduino-microcontrollers/arduino-uno-hardware-reference|Arduino Uno Hardware Reference]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Ep6]] · [[01-Areas/Engineering/arduino-microcontrollers/ep07-i2c-communication|Ep7]] · [[01-Areas/Engineering/arduino-microcontrollers/ep08-spi-interfaces|Ep8]] · [[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication|Ep9]] · [[01-Areas/Engineering/arduino-microcontrollers/ep10-interrupts-debouncing|Ep10]]
- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
- [[01-Areas/Engineering/BEE/INDEX|Basic Electrical Engineering]] — circuit theory behind the hardware.
