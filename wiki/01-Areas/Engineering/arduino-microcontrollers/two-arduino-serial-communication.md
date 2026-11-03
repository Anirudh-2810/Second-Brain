---
course_code: "ARDUINO-SERIAL-LINK"
course_name: "Two-Arduino Wired Serial Communication"
unit: "Extension — after Episode 06"
tags: [engineering, arduino, embedded, serial, uart, softwareserial, communication, two-arduino, practice]
last_updated: "2026-11-04"
confidence: high
description: "Pure notes on wired UART serial between two Arduino Unos: TX/RX crossover, common ground, baud, hardware Serial vs SoftwareSerial, framing and parsing, request-response handshakes, debugging, wiring diagrams, and 10 practice problems."
---

## For future agent
This note is a **practical extension**, not a Jeremy Blum episode. Episode 6 covers serial between an Arduino and a **computer**; Episode 9 links two Arduinos only **wirelessly** over XBee. This page fills the missing case: two Arduinos connected by **wires** over UART, which is the cheapest and most common way to split work across two boards. It assumes Ep06 (baud, `Serial.read()`, ASCII, `parseInt`) and Ep09 (two-board sender/receiver, `SoftwareSerial`) have been read. Code is standard Arduino C++; pin numbers are Uno-specific. Confidence: high for wiring/protocol; `SoftwareSerial` speed limits are empirical, not datasheet guarantees.

# Two-Arduino Wired Serial Communication

## Episode context — what this is and is not

| Case | Covered by | Medium |
|------|-----------|--------|
| Arduino ↔ PC (Serial Monitor) | [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing\|Ep06]] | USB |
| Arduino ↔ Arduino, wireless | [[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication\|Ep09]] | XBee radio |
| **Arduino ↔ Arduino, wired** | **this note** | 3 jumper wires (TX, RX, GND) |

Why bother linking two boards when one can do a lot? Three real reasons:

1. **Pin starvation.** One Uno has ~20 usable pins. A robot with many sensors + many motors runs out; a second board adds pins.
2. **Work split.** Board A does time-critical sensing/interrupts (Ep10); Board B does slow work (display, logging, motor ramps). Neither blocks the other.
3. **Distance.** A sensor cluster can sit at the far end of a machine and send results over a serial cable instead of running dozens of analog wires back.

The link is a **serial cable in software**: whatever one board prints, the other can read — after the two ends agree on speed and framing.

---

## 1. The physical link (3 wires)

UART is **asynchronous, full-duplex, point-to-point**. Two data wires, opposite directions, plus a shared reference.

```
   Arduino A (sender)                    Arduino B (receiver)
   ------------------                    ------------------
   pin 3  (TX) ------------------------> pin 2  (RX)
   pin 2  (RX) <------------------------ pin 3  (TX)
   GND     ------------------------------ GND
```

Rules that cause 90% of failures:

- **TX → RX, RX → TX.** Never TX→TX. Each board talks on its transmit pin and listens on its receive pin; the wires must cross.
- **GND is mandatory.** A voltage is only meaningful relative to a reference. No common ground → garbage or nothing.
- **Do not connect 5V between boards.** Each board powers itself (USB or its own supply). You are linking signals, not supplies. (If you must share power, be deliberate about which board's regulator is the source, and never back-feed two supplies into each other.)
- **Both ends must use the same baud rate** (start with **9600**), and the same frame format (Arduino default **8N1**: 8 data bits, no parity, 1 stop bit).

### 5 V vs 3.3 V boards

Arduino Uno/Nano (5 V) logic drives a 3.3 V board's RX pin beyond its spec. When linking a **5 V Uno to a 3.3 V board (ESP32, ESP8266, 3.3 V Pro Mini, some STM32)**:

- 3.3 V **TX → 5 V RX** usually works directly (3.3 V is read as HIGH by a 5 V input; check the specific board's VIH).
- 5 V **TX → 3.3 V RX** needs a **voltage divider** or level shifter. A 1 kΩ / 2 kΩ divider gives $5\times\frac{2}{1+2}=3.33$ V — see [[01-Areas/Engineering/arduino-microcontrollers/arduino-uno-hardware-reference|the hardware reference]] for the VDR.
- Cheapest safe option: a ready-made **bidirectional logic level converter** module.

---

## 2. Hardware `Serial` vs `SoftwareSerial`

The Uno has **one hardware UART**, on **pins 0 (RX) and 1 (TX)**. Those pins are also wired to the USB-serial chip, which is how uploads and the Serial Monitor work. That creates a conflict.

| | Hardware `Serial` (pins 0/1) | `SoftwareSerial` (any 2 pins) |
|---|---|---|
| Library | built in | `#include <SoftwareSerial.h>` |
| Pins | **fixed** 0 = RX, 1 = TX | your choice, e.g. 2 = RX, 3 = TX |
| Speed | reliable to 115200+ | reliable ~9600–38400; 57600 variable; avoid above |
| USB conflict | **yes** — the link shares pins with upload/Monitor | **no** — USB stays free for debugging |
| Simultaneous RX+TX | yes (true hardware) | one direction at a time, CPU-timed |
| Good for | one link, board not also used with USB | debugging + linking, or multiple ports |

**The practical default for two Arduinos you also want to debug: use `SoftwareSerial` on pins 2 and 3.** Hardware `Serial` stays connected to your laptop's Serial Monitor. If you use hardware pins 0/1 for the link, **disconnect the link wires while uploading** or the upload fails (the other board's TX fights the USB-serial chip).

`SoftwareSerial` constructor order is **RX first, then TX**:

```cpp
SoftwareSerial link(2, 3);   // RX = pin 2, TX = pin 3
```

That means: this board **listens on 2** and **talks on 3**. The other board must listen on the wire coming from 3, i.e. it listens on its own RX pin connected to this board's 3.

### One-link wiring with SoftwareSerial (recommended)

```
        Board A                                 Board B
   SoftwareSerial(2,3)                     SoftwareSerial(2,3)
   -------------------                     -------------------
   TX pin 3  --------------------------->  RX pin 2
   RX pin 2  <---------------------------  TX pin 3
   GND       ----------------------------  GND
   USB -> laptop (Serial Monitor)          USB -> laptop (optional)
```

### Hardware-Serial wiring (pins 0/1)

```
        Board A                                 Board B
   pin 1 (TX) ---------------------------> pin 0 (RX)
   pin 0 (RX) <--------------------------- pin 1 (TX)
   GND       ---------------------------- GND
   (unplug these two data wires before uploading either board)
```

---

## 3. Baud rate and framing

- **Baud** = symbols per second. Both ends must match exactly. Use **9600** for `SoftwareSerial`; 115200 is fine on hardware `Serial`.
- Arduino uses **8N1**: 8 data bits, no parity, 1 stop bit. Both ends using Arduino defaults → no configuration needed.
- A mismatch is not subtle: you get **garbage characters** or nothing. It is the first thing to check.
- No clock wire is needed. Each side times the bits from the agreed baud; drift over long messages is why both sides must be accurate. (This is why UART is called *asynchronous* — no shared clock, unlike SPI in [[01-Areas/Engineering/arduino-microcontrollers/ep08-spi-interfaces|Ep08]].)

---

## 4. Minimal working link

### Sender — send a number every half second

```cpp
// SENDER (Board A)
#include <SoftwareSerial.h>

SoftwareSerial link(2, 3);   // RX=2, TX=3 (RX unused here)

int counter = 0;

void setup() {
  link.begin(9600);          // must match receiver
  Serial.begin(9600);        // USB debug
}

void loop() {
  link.print(counter);       // send as ASCII text, e.g. "42"
  link.print('\n');          // newline = message boundary
  Serial.print("sent: ");
  Serial.println(counter);
  counter++;
  delay(500);
}
```

### Receiver — read a line and print it

```cpp
// RECEIVER (Board B)
#include <SoftwareSerial.h>

SoftwareSerial link(2, 3);   // RX=2, TX=3

void setup() {
  link.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if (link.available() > 0) {
    int value = link.parseInt();     // reads digits until a non-digit
    Serial.print("got: ");
    Serial.println(value);
  }
}
```

**Why send `'\n'`?** `parseInt()` reads digits until it hits a non-digit. The newline (1) terminates the number cleanly, and (2) prevents two consecutive numbers from fusing into one (`"12" "34"` → `1234`). Every text protocol needs a delimiter.

**Why `if (available())` before reading?** `parseInt()` with nothing available will **block for up to the timeout** (default 1 s), stalling the loop. Guarding keeps the receiver responsive.

---

## 5. Sending more than one value (framing and parsing)

### Comma-separated values (CSV)

```cpp
// SENDER: three sensor values per line
link.print(a); link.print(',');
link.print(b); link.print(',');
link.println(c);          // println adds '\n'
```

```cpp
// RECEIVER: parse on the receiver
if (link.available() > 0) {
  String line = link.readStringUntil('\n');   // "123,456,789"
  line.trim();                                // drop '\r' if present

  int c1 = line.indexOf(',');
  int c2 = line.indexOf(',', c1 + 1);
  if (c1 > 0 && c2 > c1) {                    // validate before using
    int a = line.substring(0, c1).toInt();
    int b = line.substring(c1 + 1, c2).toInt();
    int c = line.substring(c2 + 1).toInt();
    // use a, b, c
  }
}
```

`readStringUntil('\n')` returns everything up to the newline. Always `trim()` first: some terminals send `\r\n`, and a trailing `\r` makes the last field fail.

### Start/end markers (more robust)

Numbers can be corrupted by radio noise or a reset mid-message. Wrap each message in unambiguous delimiters:

```cpp
// SENDER
link.print('<');      // start
link.print(a); link.print(',');
link.print(b); link.print(',');
link.print(c);
link.print('>');      // end
link.print('\n');
```

Receiver reads a line, then checks it starts with `<` and ends with `>`. If not, discard. This is the smallest useful form of **framing**: it lets the receiver resynchronise after a partial message instead of trusting garbage.

### Checksum (integrity check)

A one-byte XOR checksum catches most single-byte corruption cheaply:

```cpp
// SENDER
String msg = String(a) + "," + String(b);
byte sum = 0;
for (unsigned int i = 0; i < msg.length(); i++) sum ^= (byte)msg[i];
link.print('<'); link.print(msg); link.print('*');
if (sum < 16) link.print('0');          // keep two hex digits
link.print(sum, HEX);
link.print('>'); link.print('\n');
```

The receiver recomputes the XOR over the payload and compares. If unequal → drop the message. Full CRC is overkill for two short jumper wires; XOR is right-sized for RF or noisy cables.

### Binary vs text

- `link.print(value)` sends the **ASCII text** of the number (`"42"` = bytes `52, 50`). Easy to debug, human-readable.
- `link.write(byte)` sends **one raw byte** (value 42 = one byte). Compact and fast, but harder to inspect and requires a fixed-length agreement.
- **Do not mix them** without knowing which you are doing: `Serial.read()` returns a byte; `parseInt()` expects text.

---

## 6. Bidirectional link and request-response

UART is full-duplex, so both boards can talk. Two common patterns:

### A. Independent streams (both send whenever)

Each board prints its own messages and parses the other's. Simple, but both must be able to ignore messages meant for the other side — use a one-letter prefix (`'A'`, `'B'`) or give each direction a different delimiter.

### B. Request-response (master asks, slave answers)

Cleaner when one board is clearly in charge. Board A asks; Board B answers only when asked.

```cpp
// MASTER (A): ask for a reading, wait briefly for the reply
link.print("?\n");

unsigned long start = millis();
while (millis() - start < 200) {          // 200 ms timeout
  if (link.available() > 0) {
    int reading = link.parseInt();
    Serial.print("sensor: ");
    Serial.println(reading);
    break;
  }
}
```

```cpp
// SLAVE (B): answer only on request
void loop() {
  if (link.available() > 0) {
    char c = link.read();
    if (c == '?') {
      int reading = analogRead(A0);
      link.print(reading);
      link.print('\n');
    }
  }
}
```

The timeout matters: if the slave is unplugged, the master must not wait forever. `millis()` non-blocking timing is the same pattern as [[01-Areas/Engineering/arduino-microcontrollers/ep10-interrupts-debouncing|Ep10]].

---

## 7. Debugging the link

The single best habit: **use `SoftwareSerial` for the link and hardware `Serial` for the laptop.**

- If the link is on pins 2/3, `Serial.println()` still goes to the Serial Monitor. You can watch what each board thinks it sent and received.
- If you used hardware pins 0/1 for the link, the Serial Monitor **is the link** — you cannot watch both sides, and uploads fight the link. This is why 0/1 is a poor choice for a permanent two-board project.
- Diagnostic sketch for the receiver: print **raw bytes and their ASCII codes**, not parsed values. This instantly reveals a baud mismatch (consistent garbage), a missing ground (noise), or a wrong delimiter.

```cpp
while (link.available() > 0) {
  int b = link.read();
  Serial.print(b);
  Serial.print(' ');
}
```

Expected `49 50 10` for `"12\n"` (ASCII `1`=49, `2`=50, newline=10). If you see random high numbers, suspect baud or ground.

### Link-up checklist

1. TX↔RX crossed? (Most common error.)
2. GND connected between boards?
3. Both `begin(9600)`?
4. `SoftwareSerial` argument order `(RX, TX)` correct?
5. Delimiter sent and parsed?
6. 5 V→3.3 V level shifting present where needed?
7. Reading guarded by `available()`?
8. Both boards powered and not sharing a conflicting 5 V connection?

---

## 8. UART vs the other buses

| Feature | UART (this note) | I2C ([[01-Areas/Engineering/arduino-microcontrollers/ep07-i2c-communication\|Ep07]]) | SPI ([[01-Areas/Engineering/arduino-microcontrollers/ep08-spi-interfaces\|Ep08]]) | XBee ([[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication\|Ep09]]) |
|---|---|---|---|---|
| Wires | 2 data + GND | 2 (SDA, SCL) + power | 4 (MOSI, MISO, SCK, SS) + power | 0 wires (radio) |
| Topology | point-to-point | bus, addressed (127) | master + N slaves (one SS each) | paired radios / network |
| Duplex | full | half | full | full (serial bridge) |
| Clock | asynchronous | synchronous | synchronous | radio |
| Speed | 9.6–115.2 kbps typical | 100–400 kbps | MHz range | ~250 kbps |
| Distance | short cable (cm–m); RS-485 for long | cm (on-board) | cm (on-board) | tens of metres line-of-sight |
| Best for | two boards, debug-friendly | many sensors on 2 wires | fast peripherals, SD, displays | untethered link |

**Rule of thumb:** two boards and you want to debug → **UART**. Many sensors on a short bus → **I2C**. Fast or streaming peripheral → **SPI**. No wires possible → **XBee/ESP-NOW/Bluetooth**. Need robust long cable in a noisy environment → **RS-485** (differential UART).

---

## 9. Common pitfalls

1. **TX connected to TX.** Nothing arrives. Cross the wires.
2. **No common ground.** Garbage or silence. Tie the GNDs.
3. **Baud mismatch.** Consistent garbage. Match both `begin()` calls.
4. **`SoftwareSerial` RX/TX order reversed.** Constructor is `(RX, TX)`, not `(TX, RX)`.
5. **Using pins 0/1 while also uploading / using Serial Monitor.** Upload fails or the link corrupts. Disconnect link wires to upload, or use SoftwareSerial.
6. **Reading without `available()`.** `parseInt()` blocks for the timeout; the loop stutters.
7. **No delimiter.** Two numbers fuse (`"1"` + `"2"` → `12`). Always send `'\n'` or a sentinel.
8. **`\r\n` poisoning the last field.** `trim()` (or `readStringUntil('\r')` handling) before parsing.
9. **5 V TX into a 3.3 V RX.** Damages the 3.3 V board over time. Use a divider/level shifter.
10. **Sharing 5 V between boards casually.** Back-feeding regulators; one board trying to power the other through a signal pin. Power each separately.
11. **Long, unshielded cables at high baud.** Reflections/noise. Lower the baud, shorten the cable, or move to RS-485.
12. **`SoftwareSerial` above ~38400.** Unreliable, especially while doing other work. Use hardware Serial or a board with multiple UARTs (Mega, ESP32).
13. **Mixing text and binary.** `write()` bytes read by `parseInt()`, or vice versa, gives nonsense.
14. **Assuming `parseInt` validates.** It skips non-digits and returns 0 on timeout; it does not tell you the message was well-formed. Frame and validate.

---

## 10. Practice problems

Work through these in order; each adds one new idea. Hints follow.

1. **Echo link.** Board A sends `"hello\n"` once per second. Board B prints whatever it receives to the USB Serial Monitor, raw and then as a String. Get this working before anything else.
2. **Button → remote LED.** A button on Board A (with pull-down, Ep02) sends `'1'` when pressed and `'0'` when released. Board B turns its pin-13 LED on/off. Handle the case where the button is held (do not flood the link).
3. **Pot → remote servo.** Board A reads a potentiometer (Ep04) and sends the mapped angle (0–180) once per 50 ms. Board B drives a servo (Ep05) with `constrain()` on the received value.
4. **Two-value CSV.** Send `light,temperature\n` from Board A. Board B parses both fields and prints them separately. Include one deliberately malformed line and verify the receiver rejects it instead of printing garbage.
5. **Command protocol.** Define text commands `LED:1`, `LED:0`, `BUZZ:500` (buzz for 500 ms). Board B parses the command name and argument. Unknown command → reply `ERR`.
6. **Bidirectional ping-pong.** Board A sends `PING`, Board B replies `PONG`, A prints the round-trip time using `millis()`. Add a timeout so A prints `TIMEOUT` if B is unplugged.
7. **Checksummed frames.** Wrap each message as `<payload*HH>\n` where `HH` is an XOR checksum in hex. On the receiver, drop frames whose checksum fails, and count dropped frames.
8. **Non-blocking telemetry.** Board A sends a sensor reading every 100 ms **without `delay()`** (use `millis()`), while also blinking an LED at 200 ms. Prove both happen independently.
9. **Handshake before data.** On boot, Board B sends `READY`. Board A waits for `READY` before sending any sensor data. Reboot B mid-stream and confirm A waits again instead of spamming.
10. **Baud-mismatch diagnosis.** Deliberately set A to 9600 and B to 115200. Capture the receiver's raw byte output and explain why it looks random. Then fix it and explain what changed at the electrical level.

### Answer hints

1. Use `link.print("hello\n")`; receiver `readStringUntil('\n')`.
2. Detect the **edge** (`last != current`) before sending, so holding the button does not spam.
3. Reuse `map()` + `constrain()`; send as text with `'\n'`.
4. `readStringUntil('\n')`, `trim()`, split on commas, **validate field count and ranges** before use.
5. `indexOf(':')`, compare the prefix, `toInt()` the argument. Keep a single `ERR\n` path for everything unknown.
6. `millis()` before send, parse `PONG`, subtract; a `while` with a deadline handles the timeout.
7. Compute XOR over the payload bytes; print as two hex digits (pad with a leading zero). Receiver recomputes and compares.
8. `if (millis() - lastSend >= 100) { ... }` and a separate `if (millis() - lastBlink >= 200) { ... }`; no `delay()`.
9. State machine: `WAITING` until `READY` is seen, then `RUNNING`. On timeout, return to `WAITING`.
10. Baud mismatch means the receiver samples bits at the wrong instants, so the same voltage pattern is decoded as different bytes — deterministic garbage, not "no data". A logic analyser or the raw-byte print makes it visible.

---

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Episode 06 — Serial & Processing]] — ASCII, `available()`, `read()`, `parseInt()`, baud.
- [[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication|Episode 09 — Wireless]] — the same sender/receiver shape, over XBee instead of wires.
- [[01-Areas/Engineering/arduino-microcontrollers/ep10-interrupts-debouncing|Episode 10 — Interrupts]] — `millis()` timeouts and non-blocking loops used in the handshake.
- [[01-Areas/Engineering/arduino-microcontrollers/arduino-uno-hardware-reference|Arduino Uno Hardware Reference]] — pins 0/1, VDR level shifting, current limits.
- [[01-Areas/Engineering/arduino-microcontrollers/revision-ep06-ep10-test|Ep06–10 Revision & Self-Test]] — test the serial facts cold.
- [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep06-ep10|Ep06–10 All Programs]] — copy-ready versions of the episode programs plus these link sketches.
- [[01-Areas/Engineering/robotics/ros2-communication|ROS2 communication]] — the next step up: named topics over a network instead of a raw byte stream.
