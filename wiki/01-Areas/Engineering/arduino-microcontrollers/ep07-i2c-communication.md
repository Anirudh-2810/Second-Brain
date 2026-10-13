---
course_code: "ARDUINO-EP07"
course_name: "Arduino Tutorial Series — Episode 07"
unit: "Episode 07"
episode_url: "https://www.youtube.com/watch?v=oGbDM0uP0o4"
blog_url: "https://www.jeremyblum.com/2011/02/13/arduino-tutorial-7-i2c-and-processing/"
parts_list_url: "https://www.jeremyblum.com/wp-content/uploads/2011/01/Episode-07-Parts-List.pdf"
schematics_url: "https://www.jeremyblum.com/wp-content/uploads/2011/01/Episode-07-Schematics.zip"
tags: [engineering, arduino, embedded, beginner, i2c, wire, communication, sensors, temperature, processing, tutorial]
last_updated: "2026-10-14"
confidence: high
description: "Episode 7 of Jeremy Blum's Arduino series: the I2C bus using the Wire library — SDA/SCL lines (A4/A5 on the Uno), addressing up to 127 devices, the TC74 I2C temperature sensor (address 72), Wire.begin/beginTransmission/write/endTransmission/requestFrom/read, and a Processing temperature display."
---

## For future agent
This note covers Episode 7 of Jeremy Blum's Arduino Tutorial Series — I2C communication with the Wire library. Key facts: I2C uses two lines, **SDA (data) and SCL (clock)**; on the Uno these are **A4 and A5**. Devices have **7-bit addresses** (up to 127 on a bus), each unique; only **one set of pull-up resistors** is needed per bus. Jeremy uses the **TC74** temperature sensor at address **72** (decimal). Sequence: `Wire.beginTransmission(addr); Wire.write(register); Wire.endTransmission(); Wire.requestFrom(addr, bytes); while(!Wire.available()); Wire.read();`. Processing draws the temperature. I2C is designed for on-board/short-distance comms (Jeremy's reply: use CAN/RS-485/UART/USB for long distance). Confidence: high.

# Episode 07 — I2C Communication and Processing

## Episode Overview

Episode 6 sent data to a computer. Episode 7 sends data between **chips on the same board** using a bus called **I2C** ("I-squared-C", Inter-Integrated Circuit). It is how the Arduino talks to dozens of sensors, memory chips, displays, and expanders using only **two wires** — regardless of how many devices share them.

The episode's project: read a digital **TC74 temperature sensor** over I2C, print the temperature, and draw it on screen with Processing (reusing Episode 6's visualisation skills).

Three ideas anchor it:

1. **A shared two-wire bus.** All devices hang off SDA and SCL in parallel; addresses let you talk to one without disturbing the others.
2. **Master and slave, request and response.** The Arduino (master) initiates every transaction; the sensor (slave) answers. I2C is a polite, turn-based protocol.
3. **Addressing.** Up to 127 devices, each on a unique address, so you can run many sensors together.

### Learning objectives
- Explain I2C's two lines, master/slave model, and addresses.
- Identify the Uno's SDA/SCL pins and the required pull-up resistors.
- Sequence a full read/write transaction with the Wire library.
- Read a register from an I2C sensor (the TC74 temperature).
- Combine I2C input with Processing output.
- Know I2C's distance limits and alternatives.

---

## Core Concepts (ELI5)

### Why a bus?
Earlier projects wired each sensor to its own pin, one-to-one. That does not scale — an Arduino has only ~20 pins. I2C replaces many wires with **two shared wires**:

- **SDA** — Serial DAta (carries the actual bits, both directions).
- **SCL** — Serial CLock (the master's metronome that paces the bits).

Every device connects to the same two wires plus power and ground. It is like a party line telephone where each device has a name (address); when the master calls your name, only you pick up.

**Analogy:** I2C is a classroom. The teacher (master) calls a student's name (address); only that student answers. Everyone is on the same room (bus), but only one scholar talks at a time.

### Addresses
Each I2C device ships with (or can be configured to) a **7-bit address** in the range 0–127. The master always sends the intended address first; only the matching device responds. Because addresses are fixed at manufacture for most chips, you cannot put two identical sensors with the same address on one bus — you either buy a variant with a different address, change hardware-address pins if provided, or use multiple buses (Jeremy's replies confirm all three options). The TC74 used here is at address **72**.

### Pull-up resistors
I2C lines are **open-drain**: devices can only pull a line *low*, never actively high. So the bus needs **pull-up resistors** (typically 4.7–10 kΩ) to +5 V, which restore the high level when nobody pulls down. Usually one pair of pull-ups per bus is enough — do not duplicate them (the lesson from Episode 3's pull-up theory, now with two signals). Many breakout boards include the resistors, so you may not need to add them.

### Master/slave, request/response
The Arduino is the **master**: it drives the clock and starts every transaction. A typical exchange has two phases:

1. **Write a request** — tell the sensor which internal register you want (e.g. "give me the temperature register, register 0").
2. **Read the response** — request *N* bytes and read them.

I2C is turn-based: nothing happens until the master asks.

### Distance
I2C is meant for **on-board or board-to-board** communication — centimetres, not kilometres. Its pull-up + capacitance model degrades over long wires. For long distances Jeremy recommends **CAN, RS-485, UART, or USB** (a direct reply on his blog to a reader asking about long-range use).

### Processing (again)
As in Episode 6, the Arduino prints the temperature over USB serial and a Processing sketch renders it. The difference here is the *source* of the data (I2C sensor rather than a hand-typed command), demonstrating the full pipeline: sensor → I2C → Arduino → serial → Processing → screen.

---

## Code Walkthrough

### Arduino side — read the TC74 temperature

```cpp
// Episode 7 - read_temp
// Reads the TC74 I2C temperature sensor and prints C and F.
#include <Wire.h>

int temp_address = 72;   // I2C address of the TC74 (7-bit)

void setup() {
  Serial.begin(9600);    // USB serial to the computer / Processing
  Wire.begin();          // join the I2C bus as MASTER
}

void loop() {
  // --- 1. Point to register 0 (the temperature register) ---
  Wire.beginTransmission(temp_address);  // start talking to the sensor
  Wire.write(0);                         // ask for register zero
  Wire.endTransmission();                // complete the write

  // --- 2. Request 1 byte back and read it ---
  Wire.requestFrom(temp_address, 1);     // request 1 byte from the sensor
  while (Wire.available() == 0);         // wait for the response
  int c = Wire.read();                   // temperature in Celsius

  // --- 3. Convert and print ---
  int f = round(c * 9.0 / 5.0 + 32.0);   // Celsius -> Fahrenheit
  Serial.print(c);
  Serial.print(",");
  Serial.print(f);
  Serial.println(".");                   // '.' is Processing's delimiter
  delay(500);
}
```

**Transaction anatomy.**

- `Wire.begin()` — initialise the bus as master. (A slave would pass its own address.)
- `Wire.beginTransmission(72)` — begin a message *to* address 72.
- `Wire.write(0)` — send the register number you want (many I2C sensors expose numbered registers; temperature lives in register 0 for the TC74).
- `Wire.endTransmission()` — finish and actually send the write.
- `Wire.requestFrom(72, 1)` — ask the slave to return 1 byte.
- `while (Wire.available() == 0);` — wait until the byte has arrived.
- `Wire.read()` — retrieve it.
- Convert C → F with the standard formula and print a comma-separated pair terminated by `.` so Processing can split it.

This request-then-read rhythm repeats for essentially every I2C sensor, so learn it once.

### Processing side — temperature display

```java
// display_temp.pde
import processing.serial.*;

Serial port;
PFont font;
String data = "";
float tempC, tempF;

void setup() {
  size(400, 400);
  port = new Serial(this, "COM3", 9600);
  port.bufferUntil('.');        // gather until the '.' delimiter
  font = loadFont("AgencyFB-Bold-200.vlw");
  textFont(font, 120);
}

void draw() {
  background(0);
  fill(255);
  text(nf(tempC, 1, 0) + "C", 20, 150);
  text(nf(tempF, 1, 0) + "F", 20, 300);
}

void serialEvent(Serial port) {
  data = port.readStringUntil('.');
  data = data.substring(0, data.length() - 1); // trim the '.'
  String[] parts = split(data, ',');           // split "C,F"
  if (parts.length == 2) {
    tempC = float(parts[0]);
    tempF = float(parts[1]);
  }
}
```

**Reasoning.** The Arduino prints `C,F.`; Processing buffers until `.`, trims it, splits on the comma, and renders both values. The `loadFont(...vlw)` file is produced once via Processing's `Tools → Create Font`.

### Wiring

```
     Arduino UNO                TC74 sensor
     -----------                -----------
     A4 (SDA) <---------------> SDA
     A5 (SCL) <---------------> SCL
     +5V      -----------------> Vcc
     GND      -----------------> GND
     (pull-up resistors SDA/SCL -> +5V, if not on the breakout)
```

### Transaction flow

```mermaid
sequenceDiagram
    participant Arduino as Arduino (master)
    participant TC74 as TC74 (slave @72)
    Arduino->>TC74: beginTransmission(72); write(0); endTransmission()
    Note over TC74: prepares register 0
    Arduino->>TC74: requestFrom(72, 1)
    TC74->>Arduino: 1 byte (temperature)
    Arduino->>Arduino: c = Wire.read()
    Arduino->>Processing: "c,f." over serial
```

---

## Key Functions Reference

| Function | Syntax | What it does | Example |
|----------|--------|--------------|---------|
| `Wire.begin` | `Wire.begin()` | Join I2C bus as master. | `Wire.begin();` |
| `beginTransmission` | `Wire.beginTransmission(addr)` | Start a write to address. | `Wire.beginTransmission(72);` |
| `Wire.write` | `Wire.write(byte)` | Queue a byte to send. | `Wire.write(0);` |
| `endTransmission` | `Wire.endTransmission()` | Send the queued bytes. | `Wire.endTransmission();` |
| `requestFrom` | `Wire.requestFrom(addr, n)` | Ask slave for n bytes. | `Wire.requestFrom(72,1);` |
| `available` | `Wire.available()` | Bytes ready to read. | `while(Wire.available()==0);` |
| `Wire.read` | `Wire.read()` | Read one byte from slave. | `int c = Wire.read();` |

**Pins:** Uno SDA = **A4**, SCL = **A5** (also labelled SDA/SCL on newer boards). **Addresses:** 7-bit, 0–127. **Pull-ups:** one pair per bus. **Distance:** on-board/short only — use CAN/RS-485/UART/USB for long haul.

---

## Common Pitfalls / Gotchas

1. **No pull-up resistors.** The bus stays undefined and reads fail or hang. Many breakout boards include them — check before adding your own (do not double them up).
2. **Two devices with the same address.** They collide; the master cannot tell them apart. Use a differently-addressed variant, hardware address pins, or a second bus.
3. **Wrong register number.** The `Wire.write(register)` value selects *which* internal register — sending the wrong one gives the wrong data or nothing.
4. **Forgetting `Wire.endTransmission()`.** The write never actually goes out; the subsequent read returns stale/garbage.
5. **Not waiting for `Wire.available()`.** Reading before the byte arrives returns −1 or junk.
6. **Trying long-distance I2C.** It is not designed for it; errors and lockups result. Use a differential bus (RS-485/CAN) instead.
7. **Confusing I2C and SPI.** They are different buses with different pins and libraries (SPI is Episode 8).
8. **Address shown in hex vs decimal.** Datasheets often list 0x48 etc.; `Wire.beginTransmission` wants the decimal (or `0x48`)
   value — convert carefully (72 decimal = 0x48).
9. **Mixed libraries / missing `#include <Wire.h>`.** Compile errors until the include is present.

---

## Practice Exercises

1. **Address scan.** Write a loop that calls `Wire.beginTransmission(i); if (Wire.endTransmission()==0)` for `i` 0–127 and prints every address that responds. This "I2C scanner" is the most useful debugging tool for the bus.
2. **Print raw bytes.** Change the sketch to print the raw byte returned before converting, so you can see exactly what the sensor sends.
3. **Celsius only.** Simplify the Processing sketch to show just C, then re-add F. Confirm the delimiter contract still holds.
4. **Two registers.** If your sensor has a config register, write a different register number and observe the change.
5. **Refresh rate.** Change `delay(500)` to `delay(50)` and watch the display. At what point does it become unreadable — why?

---

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Episode 06 — Serial & Processing]] — the serial-to-Processing pipeline reused here.
- [[01-Areas/Engineering/arduino-microcontrollers/ep08-spi-interfaces|Episode 08 — SPI Interfaces]] — the other short-range embedded bus, contrasted with I2C.
- [[01-Areas/Engineering/arduino-microcontrollers/ep03-electrical-basics|Episode 03 — EE Basics]] — why open-drain buses need pull-ups.
- [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire|Nexus Robotics — theory rapid-fire]] — I2C/SPI/UART comparisons appear in the comms-buses section.
- [[01-Areas/Engineering/BEE/INDEX|Basic Electrical Engineering]] — signals and circuit fundamentals.
