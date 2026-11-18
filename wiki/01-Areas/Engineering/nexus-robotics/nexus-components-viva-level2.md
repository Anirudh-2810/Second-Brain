---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Hardware Viva"
unit: "Component Sheet Level 2"
date: 2026-11-19
tags: [btech, kjsce, nexus-robotics, viva, communications, sensors, microcontrollers, op-amps]
last_updated: "2026-11-19"
confidence: high
description: "Viva answers for every Level-2 row of the Nexus component sheet — HC-05, MPU6050/9250, UART/I2C/SPI/WiFi/Zigbee/CAN/Ethernet, Roboclaw/Cytron/VNH/ODESC/ESC, LIDAR/ultrasonic/IR/LDR, Jetson/RPi, 328P/2560/ESP32/STM32, op-amps, optocouplers, encoders, level shifters, mux."
---

## For future agent

Viva Q&A over the **Level 2** half of the Nexus component sheet. Level 1 (passives, power, motors, drivers, 555, protection) is [[nexus-components-viva-level1]]. Theory depth: [[nexus-theory-rapidfire]] §2–3. Each entry = one-line *what it does* + traps; say answers out loud.

# Nexus Hardware Viva — Level 2 Components

## 1. Bluetooth — HC-05

- **Does:** serial-port-profile Bluetooth module — wires your MCU's UART to a phone/PC wirelessly; ~10 m, 2.4 GHz.
- **Architecture:** on-board Bluetooth radio + SPP firmware + breakout of UART (TX/RX) + EN/KEY pin for AT-command mode.
- **Traps:** *HC-05 logic level?* → module RX is **3.3 V** — level-shift or divide the MCU TX (its TX usually tolerates 5 V, check module). *How do you pair?* → slave mode auto-pairs; AT mode (EN HIGH / button) sets name, baud, master/slave. *HC-05 vs BLE (HM-10)?* → classic SPP (Android serial apps) vs BLE (low power, iOS-friendly). *Baud?* → default 9600 (or 38400); both ends must match.

## 2. Gyro / IMU — MPU6050, MPU9250

- **Does:** MPU6050 = 6-axis IMU (3-axis accelerometer + 3-axis gyro, ±2000 °/s, ±16 g) on one die with a DMP; MPU9250 = 9-axis (adds magnetometer → absolute yaw).
- **I2C:** default addr 0x68 (AD0 low) / 0x69; gyro outputs raw ±32768 → scale by sensitivity (e.g. 131 LSB/(°/s) at ±250 °/s).
- **Traps:** *Why both accel and gyro?* → accel = absolute tilt but noisy/vibration-sensitive; gyro = clean short-term rate but drifts — **fuse them** (complementary/Kalman). *Why does yaw drift?* → gyro bias integrates to unbounded error; magnetometer (9250) or correction term fixes it. *DMP?* → on-chip fusion engine outputs quaternions, offloads MCU. *Accelerometer reading 1 g on Z at rest?* → yes, it measures reaction force, not gravity directly.

## 3. Communications buses

| Bus | Wires | Speed | Line | Key viva line |
|---|---|---|---|---|
| **UART** | TX, RX (+GND) | 9600–1 Mbaud | point-point | Async — **no clock line**, both sides agree on baud; 8N1 framing |
| **USART** | + sync clock | same + | point-point | UART + optional clock → can be synchronous (SPI-like) |
| **I2C** | SDA, SCL | 100 k / 400 k / 3.4 M | multi-drop | 7-bit addr (128 devices), open-drain + **pull-ups**, ACK/NACK each byte |
| **SPI** | MOSI, MISO, SCK, CS | 10–100+ MHz | multi-drop | Full duplex, fastest; no addressing — one **CS line per slave** |
| **Wi-Fi (802.11)** | radio | Mbps | LAN/IP | TCP/IP stack, high power; video/telemetry |
| **Zigbee (802.15.4)** | radio | 250 kbps | mesh | Low power, self-healing mesh — remote control (rule 11.9 allows it) |
| **CAN bus** | CAN_H, CAN_L (differential) | 1 Mbit | multi-master | **Collision-free arbitration by ID** (lowest ID wins), extremely noise-tolerant — automotive standard |
| **Ethernet (802.3)** | RJ45 pairs | 100 M–1 G | LAN/IP | Wired, deterministic-ish, backbone for LIDAR/cameras |

**Traps:**
- *I2C without pull-ups?* → bus floats, nothing works — open-drain needs external R (4.7 k typical).
- *I2C vs SPI choice?* → I2C: 2 wires, many slow devices, addressing; SPI: fast, dedicated CS, full-duplex (displays, SD cards).
- *SPI clock polarity/phase?* → 4 modes (CPOL/CPHA) — master and slave must match.
- *UART vs I2C on a sensor?* → UART is point-to-point and unsolicited; I2C lets you poll many sensors on 2 pins.
- *CAN differential → why?* → noise couples equally on both wires; receiver reads the *difference* → immune.
- *Wi-Fi vs Zigbee for robot remote?* → Wi-Fi: high bandwidth, IP, power-hungry; Zigbee: mesh, low power, low data (and both allowed by rule 11.9 alongside Bluetooth).

## 4. Motor controllers (the Level-2 driver row)

| Controller | Does | Key line |
|---|---|---|
| **Roboclaw** | Closed-loop **encoder** motor controller, 2 channels, serial/PWM input | On-board PID on encoders → precise velocity/position; regenerative braking; popular for wheeled bases |
| **Cytron** | Simple PWM + direction (or RC) motor driver, e.g. MD10/MD20 | Hobby-grade workhorse; **locked-antiphase or sign-magnitude** PWM; cheap, robust |
| **VNH** | ST's automotive half-bridge driver (VNH5019/7070) | ~30 A, SPI fault feedback (overtemp/short), used as an Arduino-shield H-bridge |
| **ODESC** | Open-source high-power ESC/motor controller | FOC-capable, current sensing, open firmware — the "we built our own drive" option |
| **ESC** | Electronic Speed Controller for **BLDC** | 3-phase bridge + BEMF/hall commutation; RC PWM (1–2 ms) or digital command sets speed; handles the 6-step commutation |

**Traps:** *ESC vs Cytron for a BLDC?* → BLDC needs phase commutation → ESC; brushed DC motor → Cytron/H-bridge. *Why current sensing in ODESC/Roboclaw?* → torque control + protection (stall = limit current). *Regenerative braking?* → motor spins as generator, controller pushes energy back into the battery — must be battery-safe.

## 5. Sensors

- **LIDAR:** laser range measurement (time-of-flight / phase) → 2D distance map; cm accuracy, tens of m range; used for SLAM, obstacle fields. *Trap:* fails on glass/dark/reflective-absorbing surfaces; spinning LIDAR needs power + has a blind radius.
- **Ultrasonic (HC-SR04):** 40 kHz chirp → echo time → $d = v_{sound}\times t/2$; cheap 2 cm–4 m; cone beam ~15°. *Traps:* soft/fuzzy surfaces absorb echo; two sensors cross-talk (fire together → wrong readings); speed of sound varies with temp.
- **Proximity:** generic near-presence — inductive (metal, few mm), capacitive (any material incl. liquids), IR-reflective (short range). *Trap:* inductive only senses metals (metal-detection, not ranging).
- **IR (obstacle sensor):** IR LED + phototransistor pair — reflection threshold = digital output (and the same pair is the line sensor). *Trap:* threshold not distance — ambient light and surface color shift it; no absolute ranging.
- **LDR:** photoresistor — resistance falls with light ($\sim$kΩ dark → few hundred Ω lit); wired in a **voltage divider** into an ADC for light level. *Trap:* slow response, imprecise, not for communication (photodiode is).

## 6. Microprocessor vs microcontroller

- **Jetson (Nvidia):** GPU-rich **SoC running Linux** — CUDA/PyTorch inference, camera pipelines, ROS2 nodes; ~10–15 W, 3.3 V GPIO but needs carrier board + 5 V supply; the "AI brain".
- **Raspberry Pi:** ARM **Linux SBC** — GPIO (3.3 V, not 5 V tolerant), Wi-Fi, HDMI; great for logging/vision/ROS but **not real-time** (no hard deadlines — kernel + cache jitter).
- **Trap — the classic:** *Pi or MCU for motor PID at 1 kHz?* → MCU (deterministic interrupt); *Pi or MCU for running a neural net / serving video?* → Pi/Jetson. *Why not control motors directly from Linux?* → scheduling jitter; offload loop to MCU/ESC, Pi supervises.
- **MCU vs MPU:** MCU = CPU+RAM+peripherals on one die, boots in µs, interrupts in ns; MPU = application processor with cache/OS, boots in seconds.

## 7. Microcontrollers — 328P, 2560, ESP32, STM32

| MCU | Where | Key viva facts |
|---|---|---|
| **ATmega328P** | Arduino UNO | 8-bit AVR, 16 MHz, 32 KB flash, 2 KB RAM, 5 V logic, 6 PWM, 6 ADC (10-bit), 1 UART |
| **ATmega2560** | Arduino Mega | Same family, 256 KB flash, 54 DIO, 15 PWM, 16 ADC, **4 UARTs** — more of everything |
| **ESP32** | cheap Wi-Fi/BT boards | Dual-core 240 MHz Xtensa, **3.3 V (not 5 V tolerant)**, Wi-Fi+BLE, ADC+DAC+PWM, ~$5; ADC nonlinearity known quirk |
| **STM32** | CubeHAL / HAL libs | 32-bit ARM Cortex-M (F1/F4…), 72–180 MHz, rich timers/CAN/USB, 3.3 V, professional default |

**Traps:**
- *328P vs STM32?* → 8-bit vs 32-bit: ARM runs 4× faster at same clock, hardware multiply/FPU (F4), more peripherals.
- *Bootloader's job?* → sits in flash, accepts new program over UART/USB before user code runs.
- *How fast can ADC/PWM actually run?* → know *your* board's timer clock — don't quote datasheet maxima you haven't verified `(TBC on your exact part)`.
- *FreeRTOS on ESP32?* → yes, tasks map to cores; use it when Wi-Fi + control loop coexist.
- *3.3 V vs 5 V pins?* → never feed 5 V into ESP32/STM32 — level shift (next section).

## 8. Op-amps

- **Does:** differential amplifier with huge open-loop gain ($A_{OL}$ ≈ 10⁵); with feedback, sets gain by resistor ratio.
- **Golden rules:** (1) with negative feedback, $V_+ \approx V_-$ ("virtual short"); (2) inputs draw ~zero current.
- **Circuits:** inverting ($A_v = -R_f/R_{in}$), non-inverting ($A_v = 1 + R_f/R_g$), buffer (gain 1, impedance isolation), summing, integrator, active filter.
- **Traps:** *Ideal vs real?* → ideal: infinite gain/Zin, zero Zout; real: offset voltage, finite GBW, slew rate, rail limits (LM741 can't reach rails, needs ± supply). *Open-loop op-amp as comparator?* → yes but slow/saturating — comparator IC is faster. *GBW?* → gain × bandwidth = const (gain 100 → usable BW = GBW/100). *Virtual ground?* → inverting config's junction sits at ~0 V without being connected.

## 9. Optocouplers

- **Does:** LED + phototransistor in one package — signal crosses as **light**, so input and output circuits share **no electrical connection** (galvanic isolation, kV-rated).
- **Why:** protect MCU from motor/mains voltage spikes, break ground loops, level-shift.
- **Traps:** *CTR?* → current transfer ratio (output mA per input mA) — design input LED current with margin. *Speed?* → phototransistor ~µs; photodiode/FET-output faster. *Isolated supply also needed?* → true isolation requires isolated *power* too — the opto alone doesn't isolate the rails.

## 10. Encoders

- **Does:** converts motion → pulses; **incremental** quadrature = two channels (A, B) 90° out of phase → count speed, phase order → direction; **absolute** = unique code per position (no homing).
- **Specs:** PPR/CPR (pulses per rev; ×4 with quadrature decoding), mounting (hollow-shaft on motor, magnetic vs optical).
- **Traps:** *How direction from quadrature?* → A leads B = one way; B leads A = other (decode both edges = ×4 resolution). *Open vs closed loop?* → stepper open-loop assumes no missed steps; encoder closes it (Roboclaw PID). *Why mount on motor not wheel?* → gear ratio means motor-side counts × ratio = wheel counts; backlash lives in the gearbox.

## 11. Voltage level shifter

- **Does:** maps 3.3 V ↔ 5 V logic safely (ESP32/STM32 ⇄ Arduino/5 V sensors).
- **Methods:** resistor divider (5→3.3 only, one-way, slow edges), **bidirectional MOSFET + pull-ups** (the classic I2C shifter), dedicated IC (74LVC/TB-family, fast, bus-wide), buffers/optocouplers (isolation).
- **Traps:** *Why can't a plain divider do I2C?* → I2C is open-drain bidirectional; a divider can't pull up the other side's high state. *Is 5 V out of Arduino ever OK into ESP32?* → **no** — ESP32 pins aren't 5 V tolerant (some pins clamp, but don't rely on it). *Logic thresholds?* → 5 V CMOS reads ≥3.5 V as HIGH; 3.3 V HIGH is 3.3 V — usually OK 3.3→5, not 5→3.3.

## 12. Mux / Demux

- **Does:** **multiplexer** = many inputs → one output (select lines choose which); **demux** = one input → many outputs. e.g. CD4051 = 8:1 analog mux (3 select lines).
- **Why:** MCU pins are scarce — 3 select lines switch 8 (or 16) signals; also channel isolation and bus-sharing.
- **Traps:** *Analog mux vs digital?* → 4051 passes real analog voltages (ADC expansion); 74HC151 is digital. *On-resistance?* → $R_{ON}$ adds error — keep it small vs source impedance. *Demux use?* → chip-select distribution, output scanning, time-division.

## 13. Rapid-fire round (answer, then stop)

1. HC-05 carries what protocol? → UART wrapped in Bluetooth SPP.
2. MPU6050 on which bus, which addr? → I2C, 0x68/0x69.
3. Why does yaw drift but roll doesn't? → no absolute reference; magnetometer or fusion fixes it.
4. SPI or I2C for a 10 MHz display? → SPI.
5. What makes CAN noise-immune? → differential pair + arbitration by ID.
6. ESC for which motor? → BLDC (commutation); Cytron/H-bridge → brushed DC.
7. Jetson vs STM32? → Linux AI brain vs real-time deterministic loop.
8. Why is the Pi bad at hard realtime? → OS scheduling + cache jitter.
9. Optocoupler isolates signal — what else must be isolated? → the power rails.
10. Encoder quadrature gives direction how? → which channel leads the other (90° phase order).

## See also

- Level 1 (passives, power, motors, drivers, 555, MCB): [[nexus-components-viva-level1]]
- Theory bank: [[nexus-theory-rapidfire]] · Morning sheet: [[nexus-master-cheatsheet]] · INDEX: [[01-Areas/Engineering/nexus-robotics/INDEX]]
- Rulebook viva: [[nexus-robocon-rulebook-viva]]
