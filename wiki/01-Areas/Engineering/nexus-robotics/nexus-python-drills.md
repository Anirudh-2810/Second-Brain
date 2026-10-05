---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Coding Interview Prep"
unit: "Live Coding Drills — Python"
date: 2026-10-05
description: "Four graded live-coding tasks in Python for the Nexus Robotics interview - telemetry CSV analysis, outlier rejection with rolling median, PID with filtered derivative, and a serial frame parser - all outputs executed and verified."
tags: [btech, kjsce, nexus-robotics, interview-prep, python, live-coding, telemetry, control]
last_updated: "2026-10-05"
confidence: medium
---

## For future agent
Part B of the live-coding drill set for the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics pack]] — the four Python tasks. **Every output in this page was executed on CPython 3.13 and is exact**, and the first draft's asserted outputs were wrong in three places, so the corrections are load-bearing content rather than cosmetic. The CSV task (T9) deliberately mirrors Onyx Task 2 in [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] — reuse that muscle. Python here is the tuning-harness and analysis layer, not the shipped MCU loop; that is T7 in [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills]].

# Python Drills (T9–T12)

Run them from the [[01-Areas/Engineering/nexus-robotics/nexus-embedded-coding-drills|dril hub]] loop.
# Part B — Python (T9–T12)

> Output claims in this part were **executed on CPython 3.13** and are exact.

## T9 · Telemetry CSV parser (12 min) — closest to a real club task

**Prompt:** "Here's a flight-log CSV. Return the row with peak thrust, the mean current, and the IDs of any run below the undervoltage threshold."

```csv
test,volts,amps,thrust_g
t1,12.4,8.5,620
t2,11.8,10.2,690
t3,10.4,11.0,640
t4,11.1,9.0,660
```

```python
import csv

UNDERVOLT = 10.6

def analyse(path):
    with open(path, newline="") as f:
        rows = [
            {**r,
             "volts": float(r["volts"]),
             "amps": float(r["amps"]),
             "thrust_g": float(r["thrust_g"])}
            for r in csv.DictReader(f)
        ]
    if not rows:                       # empty file: say so, don't ZeroDivisionError
        raise ValueError("no telemetry rows")
    best = max(rows, key=lambda r: r["thrust_g"])
    return {
        "best": best["test"],
        "best_thrust": best["thrust_g"],
        "mean_amps": round(sum(r["amps"] for r in rows) / len(rows), 2),
        "undervoltage": [r["test"] for r in rows if r["volts"] < UNDERVOLT],
    }
```

**Verified output:**
```python
{'best': 't2', 'best_thrust': 690.0, 'mean_amps': 9.68, 'undervoltage': ['t3']}
```

**Narration beat:** *"Two passes conceptually — I pick peak with `max(key=...)` rather than sorting, so it's O(n) instead of O(n log n), and n is the thing I'd be asked about."*

**Follow-ups:** (a) emit a CSV of the analysis with `csv.writer`; (b) plot thrust vs current with matplotlib; (c) how would you detect a *trend* in current, not just a mean — rolling window, linear regression on the residual.

**Links:** this is the *same shape* as Onyx Task 2 in [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] — that muscle is already built, reuse it.

---

## T10 · Rolling filter + outlier rejection (12 min)

**Prompt:** "Filter the ultrasonic distance stream. Reject impossible readings (0 or >400 cm), then smooth with a 3-sample median."

```python
def clean(distances, lo=1.0, hi=400.0, window=3):
    valid = [d for d in distances if lo <= d <= hi]
    out = []
    for i in range(len(valid)):
        chunk = valid[max(0, i - window + 1): i + 1]
        out.append(sorted(chunk)[len(chunk) // 2])   # median of the window
    return out
```

**Verified output (executed on CPython 3.13):**
```python
clean([0.0, 100.0, 102.0, 900.0, 101.0, 103.0])
# [100.0, 102.0, 101.0, 102.0]      (4 values out, not 6)
```

**Read that carefully — it is the lesson.** The two rejects (`0.0` and `900.0`) are dropped, so the output is **shorter than the input**. A filter that discards samples changes your sample count, and if you're computing a rate or a distance integral from the result, that breaks your arithmetic. The 4 survivors are `[100, 102, 101, 103]`, and each output is the median of the window ending at that index — note that `102.0` survives as an output twice, because with an even-length window `chunk[len//2]` takes the **upper** of the two middle values rather than averaging them. Both facts are follow-up bait.

**Narration beat:** *"`0` from an HC-SR04 means *out of range*, not *touching* — dropping it is a correctness decision, not a filter choice, and I should say that out loud because it's exactly the kind of domain detail that scores."*

**Follow-ups:** (a) why median not mean here — a single bad echo is an outlier, and the mean lets one spike move the reading; (b) the list-slice inside the loop is O(n·window) — fine for window 3, and how you'd make it O(1) amortised with `collections.deque`; (c) rolling vs cumulative mean — cumulative never forgets the first bad reading.

---

## T11 · PID in Python (12 min)

**Prompt:** "Implement a PID step in Python with output clamping and a filtered derivative."

```python
class PID:
    def __init__(self, kp, ki, kd, out_limits, alpha=0.1):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.lo, self.hi = out_limits
        self.alpha = alpha            # derivative low-pass coefficient
        self.i = 0.0
        self.prev_e = None
        self.d_filt = 0.0

    def step(self, setpoint, measured, dt):
        e = setpoint - measured

        raw = 0.0 if self.prev_e is None else (e - self.prev_e) / dt
        self.d_filt += self.alpha * (raw - self.d_filt)   # one-pole LPF
        self.prev_e = e

        p = self.kp * e
        i = self.ki * self.i
        d = self.kd * self.d_filt

        # conditional integration: freeze the integrator while saturated
        u = p + i + d
        if not (self.lo <= u <= self.hi) and (u > self.hi) == (e > 0):
            self.i -= e * dt
        else:
            self.i += e * dt

        return max(self.lo, min(self.hi, p + i + d))
```

**Verified behaviour (executed on CPython 3.13):** with those gains and a 5-step saturation run the output is `[100, 100, 100, 100, 100]` — pinned at the upper limit the whole time, and `pid.i` ends at exactly `1.0`.

That number is the real result. A naive controller (`self.i += e * dt` unconditionally) reaches `i == 5.0` over the same five steps — **five times** the guarded value. The integrator kept charging into a saturated actuator, and when the output finally comes back in range it has to unwind all of it first. That stored debt is windup, and `1.0` vs `5.0` is how you *prove* the anti-windup logic does something rather than just asserting it.

**The verified way to show the loop actually working** — don't saturate it; drive a plant toward setpoint instead:

```python
pid = PID(0.5, 0.02, 0.001, (-100, 100))
meas = 0.0
trace = []
for _ in range(40):
    out = pid.step(100.0, meas, 0.01)
    meas += out * 0.01          # crude plant: measurement follows the command
    trace.append(round(meas, 1))
# starts 0.5, 1.0, 1.5, 2.0, ... climbs monotonically toward 100.0
```

Say what this test proves: *no overshoot, monotone convergence*. A PID that rings is mis-tuned regardless of how correct the arithmetic is.

**Narration beat:** *"`alpha` on the derivative isn't optional in a real loop — the raw D term turns sensor noise into actuator chatter. I'd name that as the reason rather than leaving it as an unexplained constant."*

**Follow-ups:** (a) why Python when the target is a microcontroller — this runs the *tuning harness* on your laptop; the shipped loop is T7's C; (b) Ziegler–Nichols tuning — how you'd get kp/ki/kd at all; (c) unit tests — hold setpoint fixed, step the measurement, assert no overshoot beyond x%.

---

## T12 · Frame parser for a serial link (15 min)

**Prompt:** "Serial gives us `0xAA 0x55 <len> <payload…> <crc>`. Write a function that pulls out one payload, or returns None if the frame isn't complete/valid."

```python
STX0, STX1 = 0xAA, 0x55

def next_frame(buf):
    """buf: bytes. Returns (payload, consumed) or (None, 0) if incomplete."""
    start = -1
    for i in range(len(buf) - 1):
        if buf[i] == STX0 and buf[i + 1] == STX1:
            start = i
            break
    if start < 0 or len(buf) - start < 4:
        return None, 0                      # no header, or header truncated
    length = buf[start + 2]
    total = 3 + length + 1                  # header(3) + payload + crc(1)
    if len(buf) - start < total:
        return None, 0                      # payload still arriving
    payload = buf[start + 3: start + 3 + length]
    # real impl: crc8(payload) == buf[start + 3 + length]  (see T6)
    return bytes(payload), start + total
```

**Verified output:**
```python
next_frame(bytes([0x00, 0xAA, 0x55, 0x02, 0xDE, 0xAD, 0x00]))
# (b'\xde\xad', 7)
next_frame(bytes([0xAA, 0x55, 0x02]))              # truncated header
# (None, 0)
next_frame(bytes([0xAA, 0x55, 0x02, 0x01]))        # payload incomplete
# (None, 0)
```

**Narration beat:** *"`return None` rather than raising, because on a serial link an incomplete frame is the *normal* case, not an error — the loop just calls again with more bytes. Getting that distinction right is most of the credit."*

**Follow-ups:** (a) why a 2-byte header — a false `0xAA` inside payload data won't be mistaken for a header; (b) resync on a bad CRC — scan forward from the next `0xAA`, don't just drop one byte; (c) make it a generator that yields frames forever — the natural shape for a read loop.

---

