---
course_code: "ARDUINO-VIVA-PROGRAMS-EP06-10"
course_name: "Arduino Viva Programs — Ep06–10 (all sketches + demo checklists)"
unit: "Episodes 06–10"
tags: [engineering, arduino, microcontroller, embedded, beginner, viva, exam-prep, code, serial, i2c, spi, wireless, interrupts]
last_updated: "2026-11-04"
confidence: high
description: "Every program from Jeremy Blum Arduino Episodes 6–10 in full with beginner line-by-line commentary, wiring, per-program demo checklists, and write-it-live drills — plus a bonus wired two-Arduino serial link. Companion to the concept recap."
---

## For future agent
This is the **code half** of the Arduino Ep06–10 viva pack, companion to [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep06-ep10|viva-recap-ep06-ep10]]. It contains every sketch from Episodes 6–10 (serial echo, keyboard LED, Processing, TC74 temperature, SPI digital pot, XBee sender/receiver, interrupt counter, blink-without-delay) plus a bonus **wired two-Arduino** link that is not in the series. Each program has an annotated listing, wiring, a demo checklist, and a "write it live" prompt. The Processing sketches are Java/`.pde`, not Arduino C++. Pin numbers are Uno-specific. Version caveats: `Serial.flush()` semantics (1.0+), `attachInterrupt` uses `digitalPinToInterrupt`, and Processing font `.vlw` files are generated locally. Confidence: high for the Arduino code; Processing details depend on the Processing version and installed serial library.

# Arduino Ep06–10 — All Programs (write + demonstrate)

## How to use this note

- **Concept side:** [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep06-ep10|viva-recap-ep06-ep10]].
- Read each listing top to bottom; the **comments explain intent**, not just syntax.
- For a practical viva: rebuild the wiring, run the program, then **type it from memory** using only the "write it live" prompt.
- Processing sketches are optional unless the viva includes the PC side; the Arduino programs are the core.

---

## Episode 06 — Serial communication and Processing

### Program 1 — Serial echo (ASCII → number)

```cpp
// Ep6 P1: type a digit; print its integer value
void setup() {
  Serial.begin(9600);              // open serial at 9600 baud
}

void loop() {
  while (Serial.available() == 0); // busy-wait until a byte arrives
  int val = Serial.read() - '0';   // ASCII '1'(49) - '0'(48) = 1
  Serial.println(val);             // print the number + newline
}
```

**Line notes.**
- `Serial.begin(9600)` — must match the Serial Monitor's baud.
- `while (Serial.available() == 0);` — blocks until input; fine for a demo, bad in a real control loop.
- `Serial.read() - '0'` — the ASCII-to-integer idiom. `'0'` is 48, so `'7'` (55) becomes 7.
- `Serial.println` — prints and moves to a new line.

**Wiring:** USB cable only.
**Demo checklist:** open Serial Monitor → set 9600 → type `5` → Send → see `5`. Type `a` → see `49` (because `'a'` is 97, and 97 − 48 = 49) — proof that the code does raw ASCII arithmetic, not validation. Explain that this is why you must validate input.

**Write it live:** "Write a sketch that reads one digit and prints whether it is even or odd."

```cpp
void setup() { Serial.begin(9600); }
void loop() {
  while (Serial.available() == 0);
  int v = Serial.read() - '0';
  Serial.println(v % 2 == 0 ? "even" : "odd");
}
```

### Program 2 — Keyboard-controlled LED

```cpp
// Ep6 P2: '1' = LED on, '0' = LED off, anything else = invalid
int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  while (Serial.available() == 0);
  int val = Serial.read() - '0';

  if (val == 1) {
    Serial.println("LED is on");
    digitalWrite(ledPin, HIGH);
  } else if (val == 0) {
    Serial.println("LED is off");
    digitalWrite(ledPin, LOW);
  } else {
    Serial.println("Invalid!");
  }

  // discard leftover bytes (line ending / extra chars)
  while (Serial.available() > 0) Serial.read();
}
```

**Line notes.**
- The final `while` is the fix for the classic "Invalid! in between everything" bug: the newline (`\n` = 10) or carriage return (`\r` = 13) left in the buffer would read as `10−48 = −38` or `13−48 = −35`.
- Setting the Monitor's line-ending to **"No line ending"** also avoids it, but code-side flushing is more robust.
- `ledPin = 13` uses the onboard LED and resistor.

**Wiring:** USB only (onboard LED).
**Demo checklist:** type `1` → LED on + "LED is on"; `0` → off; `5` → "Invalid!"; verify no stray "Invalid!" appears after each valid command.

**Write it live:** "Extend it so `2` sets pin 9 PWM to 128 and `3` sets it to 255."

```cpp
int ledPin = 13, pwmPin = 9;
void setup() { Serial.begin(9600); pinMode(ledPin, OUTPUT); pinMode(pwmPin, OUTPUT); }
void loop() {
  while (Serial.available() == 0);
  int v = Serial.read() - '0';
  if (v == 1) { Serial.println("LED on"); digitalWrite(ledPin, HIGH); }
  else if (v == 0) { Serial.println("LED off"); digitalWrite(ledPin, LOW); }
  else if (v == 2) { Serial.println("PWM 128"); analogWrite(pwmPin, 128); }
  else if (v == 3) { Serial.println("PWM 255"); analogWrite(pwmPin, 255); }
  else Serial.println("Invalid!");
  while (Serial.available() > 0) Serial.read();
}
```

### Program 3 — Processing visualiser (computer side, `.pde`)

```java
// Ep6 P3: read Arduino serial and display it as large text
import processing.serial.*;

Serial port;
String data = "";
PFont font;

void setup() {
  size(400, 400);
  port = new Serial(this, "COM3", 9600);   // match your port + baud
  port.bufferUntil('.');                    // accumulate until '.'
  font = loadFont("AgencyFB-Bold-200.vlw"); // created via Tools > Create Font
  textFont(font, 200);
}

void draw() {
  background(0);
  fill(255);
  text(data, 10, 300);
}

void serialEvent(Serial port) {
  data = port.readStringUntil('.');           // read the whole message
  data = data.substring(0, data.length() - 1); // drop the '.'
}
```

**Line notes.**
- `new Serial(this, "COM3", 9600)` — opens the port the Arduino is on (list with `Serial.list()`).
- `bufferUntil('.')` — collect characters until the delimiter; the Arduino must print a `.` at the end of each message.
- `serialEvent` — fires when a full message arrives; strips the delimiter; `draw()` renders each frame.

**Wiring:** USB only; the Arduino must print a value followed by `.`.

**Demo checklist:** upload an Arduino sketch that prints a number + `.` (e.g. `Serial.print(x); Serial.println(".");`), set the correct COM port, run the Processing sketch, confirm the number updates.

**Write it live:** "Change the Processing sketch to plot a moving line graph of the last 200 values instead of a big number." (Hint: store values in an `int[]`, shift or index circularly, draw `line()` between successive points.)

---

## Episode 07 — I2C temperature sensor + Processing

### Program 4 — Read the TC74 over I2C

```cpp
// Ep7 P4: read TC74 temperature (C and F) and print "C,F."
#include <Wire.h>

int temp_address = 72;   // TC74 I2C address (7-bit)

void setup() {
  Serial.begin(9600);
  Wire.begin();          // join the bus as master
}

void loop() {
  // 1) point the sensor at register 0 (temperature)
  Wire.beginTransmission(temp_address);
  Wire.write(0);
  Wire.endTransmission();

  // 2) request one byte and read it
  Wire.requestFrom(temp_address, 1);
  while (Wire.available() == 0);   // wait for the reply
  int c = Wire.read();

  // 3) convert and print with a delimiter
  int f = round(c * 9.0 / 5.0 + 32.0);
  Serial.print(c);
  Serial.print(",");
  Serial.print(f);
  Serial.println(".");              // '.' is Processing's delimiter
  delay(500);
}
```

**Line notes.**
- `Wire.begin()` — master mode. (A slave would pass its own address.)
- `beginTransmission(72)` → `write(0)` → `endTransmission()` — select register 0.
- `requestFrom(72, 1)` — ask for one byte.
- `while (Wire.available() == 0);` — wait; reading early returns −1/junk.
- `round(...)` — C→F conversion to the nearest integer.
- The trailing `.` is a contract with the Processing sketch.

**Wiring:** A4→SDA, A5→SCL, +5V→Vcc, GND→GND; pull-ups if not on the breakout.
**Demo checklist:** open Serial Monitor at 9600; see `C,F.` updating; warm the sensor with a finger and watch it rise; confirm the address is 72.

**Write it live:** "Write an I2C scanner that prints every responding address from 0 to 127."

```cpp
#include <Wire.h>
void setup() {
  Wire.begin();
  Serial.begin(9600);
  for (byte a = 0; a < 128; a++) {
    Wire.beginTransmission(a);
    if (Wire.endTransmission() == 0) {
      Serial.print("found 0x");
      Serial.println(a, HEX);
    }
  }
}
void loop() {}
```

---

## Episode 08 — SPI digital potentiometer

### Program 5 — Fade LEDs through the MCP42010

```cpp
// Ep8 P5: drive an MCP42010 digital pot over SPI to fade LEDs
#include <SPI.h>

const int Slave = 10;    // chip-select (active low)

void setup() {
  pinMode(Slave, OUTPUT);
  digitalWrite(Slave, HIGH);                 // unselected at rest
  SPI.begin();                               // configure 11/12/13
  SPI.setClockDivider(SPI_CLOCK_DIV16);      // 16 MHz / 16 = 1 MHz
}

// reg = 0 or 1 (pot), level = 0..255
void setLed(byte reg, int level) {
  digitalWrite(Slave, LOW);   // select the chip
  SPI.transfer(reg);          // first byte: which pot
  SPI.transfer(level);        // second byte: value
  digitalWrite(Slave, HIGH);  // release
}

void loop() {
  for (int pot = 0; pot < 3; pot++) {
    for (int level = 50; level <= 255; level++) {   // fade up
      setLed(pot, level);
      delay(20);
    }
    delay(300);
    for (int level = 255; level >= 50; level--) {   // fade down
      setLed(pot, level);
      delay(20);
    }
  }
}
```

**Line notes.**
- `pinMode(Slave, OUTPUT)` + `digitalWrite(HIGH)` — only SS is manual; MOSI/MISO/SCK are configured by `SPI.begin()`.
- `setClockDivider(SPI_CLOCK_DIV16)` — the MCP42010 cannot keep up with the default clock; DIV16 → 1 MHz.
- `SPI.transfer(reg)` then `SPI.transfer(level)` — two-byte command: register, then value.
- The select must wrap the **whole** two-byte transfer; raising SS between bytes aborts the command.
- Starting at 50 skips the LED "dead zone" (invisible light below ~50).

**Wiring:** D10→CS/SS, D11→SI (MOSI), D12→SO (MISO, unused), D13→SCK; +5V→VDD/RS/SHDN; GND→VSS; wiper→220 Ω→LED→GND; 10 kΩ from B side to GND to sweep the top half of the range.

**Demo checklist:** LED holds mid-brightness at register 0 = 128; both pots independent; a smooth fade up/down; observe the dead zone if you start at 0.

**Write it live:** "Write a function that crossfades pot 0 up while pot 1 goes down, then reverses." (Hint: one loop, `setLed(0, i)` and `setLed(1, 255 - i)`.)

---

## Episode 09 — XBee wireless link

### Program 6 — Sender: potentiometer over the air

```cpp
// Ep9 P6: read a pot, send the servo angle wirelessly
#include <SoftwareSerial.h>

SoftwareSerial xbee(2, 3);   // RX, TX to the XBee
int potPin = 0;
int angle = 0;

void setup() {
  xbee.begin(9600);          // match the XBee's configured baud
}

void loop() {
  int reading = analogRead(potPin);          // 0..1023
  angle = map(reading, 0, 1023, 0, 180);     // to servo degrees
  angle = constrain(angle, 0, 180);          // clamp
  xbee.print(angle);                         // send ASCII text
  xbee.print('\n');                          // message delimiter
  delay(50);
}
```

**Line notes.**
- `SoftwareSerial xbee(2, 3)` — RX first. Keeps USB `Serial` free for debugging.
- `analogRead(A0)` → 0–1023; `map` → 0–180; `constrain` clamps.
- `print(angle)` sends text like `"90"`; the newline marks the end.
- The XBee must be configured for 9600 serial and a matching PAN/DL.

**Wiring:** Arduino D2/D3 ↔ XBee DOUT/DIN (through the shield/explorer); 3.3 V regulated power; common ground. Pot on A0.

### Program 7 — Receiver: drive the servo

```cpp
// Ep9 P7: receive the angle wirelessly and move the servo
#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial xbee(2, 3);
Servo myServo;
int angle = 0;

void setup() {
  xbee.begin(9600);
  myServo.attach(9);
}

void loop() {
  if (xbee.available() > 0) {
    angle = xbee.parseInt();     // read until a non-digit
    angle = constrain(angle, 0, 180);
    myServo.write(angle);
  }
}
```

**Line notes.**
- `available() > 0` — only touch the servo when data arrives.
- `parseInt()` — reads digits until the newline; robust against partial reads.
- `constrain` — guards against RF corruption commanding an out-of-range angle.
- `attach(9)` — any digital pin; 9 is used in the series.

**Wiring:** same radio setup on the receiver; servo signal→D9, servo power→separate 5 V rail, grounds common.

**Demo checklist:** turn the pot on the sender; the servo on the receiver follows with a small lag; disconnect the sender and confirm the servo holds (does not jitter to random angles).

**Write it live:** "Send the pot value plus a button state as `button,angle\n`, and on the receiver light an LED when the button is pressed." (Hint: parse two CSV fields exactly as in the two-Arduino note.)

---

## Episode 10 — Interrupts and debouncing

### Program 8 — Beam-break counter (interrupt + millis debounce)

```cpp
// Ep10 P8: count beam breaks with an interrupt; debounce with millis()
int ledPin = 13;
int beamPin = 2;                       // external interrupt pin

volatile int count = 0;
volatile unsigned long lastHit = 0;
const unsigned long DEBOUNCE = 50;     // ms

void onChange() {                      // ISR: keep it tiny
  unsigned long now = millis();
  if (now - lastHit > DEBOUNCE) {      // accept only after the window
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
  static unsigned long lastPrint = 0;
  if (millis() - lastPrint > 1000) {   // non-blocking report
    lastPrint = millis();
    Serial.print("Count: ");
    Serial.println(count);
  }

  digitalWrite(ledPin, !digitalRead(ledPin));
  delay(150);                          // proves the loop still runs
}
```

**Line notes.**
- `volatile` on `count` and `lastHit` — written in the ISR, read in `loop`.
- The ISR computes `millis()`, checks the window, increments — no printing, no delays.
- `attachInterrupt(digitalPinToInterrupt(2), ..., FALLING)` — pin 2 only (or 3).
- `static unsigned long lastPrint` — persists across `loop()` calls.
- The blink is evidence the main loop keeps running while interrupts fire.

**Wiring:** beam-break/switch output → D2 (with the required pull-up/pull-down); onboard LED on D13.

**Demo checklist:** one beam interruption = one count; rapid interruptions do not multi-count within 50 ms; the LED blinks continuously (loop alive); Serial prints once per second.

**Write it live:** "Change the mode to RISING and explain the difference; then remove the debounce and show the over-count."

### Program 9 — Blink without delay (the pattern)

```cpp
// Ep10 P9: non-blocking blink
const int led = 13;
unsigned long lastToggle = 0;
const unsigned long PERIOD = 200;

void setup() { pinMode(led, OUTPUT); }

void loop() {
  if (millis() - lastToggle >= PERIOD) {
    lastToggle = millis();
    digitalWrite(led, !digitalRead(led));
  }
  // other tasks can run here with no blocking
}
```

**Line notes.**
- `millis()` returns milliseconds since boot; `unsigned long` survives the wrap.
- `lastToggle = millis()` (not `+= PERIOD`) keeps the schedule from drifting wildly if a pass is late.
- No `delay()` — the loop can service sensors/buttons every pass.

**Demo checklist:** LED toggles every 200 ms; add a second independent task and show both run.

**Write it live:** "Blink two LEDs at 200 ms and 500 ms simultaneously with no `delay()`."

---

## Bonus (not in the series) — Wired two-Arduino link

Full theory and practice problems: [[01-Areas/Engineering/arduino-microcontrollers/two-arduino-serial-communication|two-arduino-serial-communication]].

### Sender (Board A)

```cpp
#include <SoftwareSerial.h>
SoftwareSerial link(2, 3);      // RX=2, TX=3
int counter = 0;

void setup() {
  link.begin(9600);
  Serial.begin(9600);           // USB debug
}

void loop() {
  link.print(counter);
  link.print('\n');
  Serial.print("sent: "); Serial.println(counter);
  counter++;
  delay(500);
}
```

### Receiver (Board B)

```cpp
#include <SoftwareSerial.h>
SoftwareSerial link(2, 3);

void setup() {
  link.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if (link.available() > 0) {
    int v = link.parseInt();
    Serial.print("got: "); Serial.println(v);
  }
}
```

**Wiring:** A.TX(3)→B.RX(2), A.RX(2)→B.TX(3), common GND. Both 9600.
**Demo checklist:** receiver prints `got: 0,1,2,...`; unplug GND → garbage/stops; swap TX wires → stops; change one baud → garbage.

**Write it live:** "Add a checksum and a `<...>` frame, then prove the receiver drops a corrupted frame."

---

## Write-it-live drills (mixed)

1. Serial: read two digits (e.g. `42`) into one integer without `parseInt()` (multiply-and-add).
2. I2C: print the temperature only when it changes by ≥1 °C.
3. SPI: set both digital-pot registers from one function call with a `struct`.
4. XBee: send `angle` plus a heartbeat counter; the receiver logs a warning if the counter stalls.
5. Interrupts: count encoder edges with `CHANGE`, debounce in the ISR, and print RPM once per second using `millis()`.
6. Serial link: implement a `PING`/`PONG` handshake with a 200 ms timeout.

---

## Cross-Links

- [[01-Areas/Engineering/arduino-microcontrollers/viva-recap-ep06-ep10|Ep06–10 Viva Recap (concepts)]]
- [[01-Areas/Engineering/arduino-microcontrollers/revision-ep06-ep10-test|Ep06–10 Revision & Self-Test]]
- [[01-Areas/Engineering/arduino-microcontrollers/viva-programs-ep01-ep05|Ep01–05 All Programs]] — the first-half code pack.
- [[01-Areas/Engineering/arduino-microcontrollers/two-arduino-serial-communication|Two-Arduino Wired Serial]]
- [[01-Areas/Engineering/arduino-microcontrollers/arduino-uno-hardware-reference|Arduino Uno Hardware Reference]]
- [[01-Areas/Engineering/arduino-microcontrollers/ep06-serial-processing|Ep6]] · [[01-Areas/Engineering/arduino-microcontrollers/ep07-i2c-communication|Ep7]] · [[01-Areas/Engineering/arduino-microcontrollers/ep08-spi-interfaces|Ep8]] · [[01-Areas/Engineering/arduino-microcontrollers/ep09-wireless-communication|Ep9]] · [[01-Areas/Engineering/arduino-microcontrollers/ep10-interrupts-debouncing|Ep10]]
- [[01-Areas/Engineering/arduino-microcontrollers/INDEX|Arduino Module Index]]
