---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Coding Interview Prep"
unit: "Live Coding Drills — Embedded C"
date: 2026-10-05
description: "Eight graded live-coding tasks in embedded C for the Nexus Robotics interview - bit-field macros, saturating clamp and Q8 fixed-point, SPSC ring buffer, non-blocking debounce, ISR flag handoff, CRC-8, integer PID with anti-windup, O(1) moving average."
tags: [btech, kjsce, nexus-robotics, interview-prep, embedded, c-programming, live-coding, interrupts]
last_updated: "2026-10-05"
confidence: medium
---

## For future agent
Part A of the live-coding drill set for the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics pack]] — the eight C tasks. Each carries a time box, a narration script, and a follow-up ladder, because the failure being defended against is silence under a clock (F3 timed-freeze in [[01-Areas/Programming/dsa-interview-playbook]]). **Verification status:** no C toolchain exists on this machine (`gcc`, `clang`, `cl`, `tcc` all absent), so nothing here is compiled. T1/T2/T3/T6/T8 had their logic re-implemented identically in Python and executed to confirm the stated values; T4/T5/T7 are hand-checked only. Verify status per task before trusting an expected output.

# Embedded C Drills (T1–T8)

Run them from the [[01-Areas/Engineering/nexus-robotics/nexus-embedded-coding-drills|dril hub]] loop — restate, brute force, get the nod, narrate while coding, dry-run one edge case, state complexity unprompted.
# Part A — Embedded C (T1–T8)

## T1 · Bit field helpers (12 min) — START HERE

**Prompt:** "Write three helpers: set bit *n*, clear bit *n*, and test bit *n* in a 16-bit register value."

```c
#include <stdint.h>

#define BIT(n)        (1u << (n))
#define BIT_SET(v,n)  ((v) |  BIT(n))
#define BIT_CLR(v,n)  ((v) & ~BIT(n))
#define BIT_TST(v,n)  (((v) >> (n)) & 1u)

/* why ~BIT(n) is safe: ~ produces all-ones except the target bit,
   so AND-ing clears exactly one bit and leaves the rest untouched. */
```

**Expected (verified by simulation):** `BIT_SET(0x0000,3) == 0x0008` · `BIT_CLR(0xFFFF,0) == 0xFFFE` · `BIT_TST(0x0008,3) == 1`.

**Narration beat:** *"I'm using `1u` not `1` — with a signed `1`, shifting into bit 31 would be signed overflow, which is undefined behaviour."*

**Follow-ups:** (a) toggle = `^`; (b) count set bits — Kernighan's `x &= x-1` is O(popcount); (c) is bit 0 the MSB or LSB? (LSB — rightmost — because we `<<` to move up.)

**Links:** [[01-Areas/Programming/c-programming/practice/01-basics-operators]] · bitwise is *out of syllabus scope* per [[01-Areas/Engineering/SPM/spm-module1-faculty-companion]] §6a, so expect it anyway.

---

## T2 · Saturating clamp + fixed-point (15 min)

**Prompt:** "Sensor raw counts arrive as `int32_t`. Clamp them to `[-32768, 32767]`. Then convert the clamped value to a Q8 fixed-point number (`value × 256`)."

```c
#include <stdint.h>

int32_t clamp_i32(int32_t x, int32_t lo, int32_t hi) {
    if (x < lo) return lo;
    if (x > hi) return hi;
    return x;
}

int32_t to_q8(int32_t x) {
    return x * 256;          /* << 8 would be UB on overflow; * is defined */
}

/* safer for wide ranges: shift with a divide first */
int32_t to_q8_safe(int32_t x) {
    return (int32_t)((int64_t)x << 8);
}
```

**Expected (verified by simulation):** `clamp_i32(40000,-32768,32767) == 32767` · `to_q8(100) == 25600`.

**Narration beat:** *"Embedded compilers support 64-bit math in software, so I widen to `int64_t` before the shift — on an 8-bit MCU a 64-bit shift is expensive, so I'd ask about the target before choosing."*

**Follow-ups:** (a) why Q8 instead of `float`? — no FPU, deterministic timing, no library bloat. (b) round-to-nearest instead of truncate? (c) overflow when × 256 → saturating multiply.

**Links:** [[01-Areas/Engineering/SPM/module-2-program-control-functions]] (flag/guard style) · [[01-Areas/Engineering/SPM/module-4-user-defined-functions]] (storage classes, `static` locals).

---

## T3 · Single-producer single-consumer ring buffer (18 min) — THE signature embedded task

**Prompt:** "An ISR pushes samples, the main loop pops them. No `malloc`. Fixed capacity. Tell me when it's full or empty."

```c
#include <stdint.h>

#define RB_SIZE 8                 /* power of two */

typedef struct {
    uint16_t        buf[RB_SIZE];
    volatile uint16_t head;       /* written by ISR  */
    volatile uint16_t tail;       /* written by main */
} ring_t;

void rb_init(ring_t *rb) { rb->head = rb->tail = 0; }

uint8_t rb_push(ring_t *rb, uint16_t v) {
    uint16_t next = (rb->head + 1) % RB_SIZE;
    if (next == rb->tail) return 0;   /* full: one slot kept empty */
    rb->buf[rb->head] = v;
    rb->head = next;
    return 1;
}

uint8_t rb_pop(ring_t *rb, uint16_t *out) {
    if (rb->head == rb->tail) return 0;   /* empty */
    *out = rb->buf[rb->tail];
    rb->tail = (rb->tail + 1) % RB_SIZE;
    return 1;
}
```

**Expected (verified by simulation):** pushing values 1…9 into an 8-slot ring returns `[1,1,1,1,1,1,1,0,0]` — the 8th push fails because only 7 usable slots exist. Interleaved push/pop round-trips in order.

**Narration beats (say these, they're the scoring points):**
- *"Wasted one slot deliberately — that lets `head == tail` mean unambiguously 'empty', so I don't need a separate count variable."*
- *"`volatile` because `head` is written by the ISR and the compiler would otherwise cache it in a register across the loop."*
- *"`volatile` does **not** make this atomic. A `uint16_t` is two bytes, so on an 8-bit AVR the compiler emits two byte-writes and an interrupt landing between them corrupts the index — even on a 32-bit Cortex-M, a 16-bit write isn't atomic. The honest fixes are: make the index a type the CPU writes atomically (`uint8_t`, or `uint32_t`), or disable interrupts around the index update. Volatile alone is not a lock."*

**Follow-ups:** (a) make it multi-producer — needs a critical section or lock-free CAS; (b) why `%` when size is a power of two — `% RB_SIZE` becomes a mask `& (RB_SIZE-1)`, cheaper on hardware without division; (c) overflow policy — drop newest, drop oldest, or count the loss (a `dropped` counter is what you'd actually ship).

**Links:** [[01-Areas/Engineering/SPM/module-3-arrays]] (contiguity, FIFO) · [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers]] (the struct, `sizeof`).

---

## T4 · Non-blocking button debounce (15 min)

**Prompt:** "Button on a pin, active-low with a pull-up. `loop()` must never block. Debounce and emit one event per real press."

```c
#include <stdint.h>

#define DEBOUNCE_MS 20

typedef struct {
    uint8_t  last_raw;
    uint8_t  stable;
    uint32_t changed_at;
} button_t;

void button_init(button_t *b, uint8_t raw) {
    b->last_raw = b->stable = raw;
    b->changed_at = 0;
}

/* returns 1 exactly once, on the debounced transition to pressed(0) */
uint8_t button_poll(button_t *b, uint8_t raw, uint32_t now_ms) {
    if (raw != b->last_raw) {          /* something moved */
        b->last_raw  = raw;
        b->changed_at = now_ms;        /* restart the settle timer */
    }
    if (raw != b->stable && (now_ms - b->changed_at) >= DEBOUNCE_MS) {
        b->stable = raw;               /* commit: it held long enough */
        return (raw == 0);             /* active-low: 0 means pressed */
    }
    return 0;
}
```

**Expected (hand-checked, not compiled):** feed `1,1,0,0,1,0` with a 5 ms gap between each → **exactly one** `1` returned (the settled 0). Feed `0,1,0,1,0` with 1 ms gaps → returns 0 every time (never settled).

**Narration beat:** *"`now_ms - b->changed_at` is unsigned subtraction, so it stays correct across the `millis()` rollover at ~49.7 days. If I used signed ints the comparison would break at the wrap."*

**Follow-ups:** (a) detect long-press (hold > 1 s) — add a second timestamp; (b) handle two buttons — one state struct each, poll both; (c) why not just `delay(20)` and read — it freezes everything else, including the control loop.

**Links:** theory Q23–24 in [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]] · [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] Onyx Set C (`delay` vs `millis`).

---

## T5 · ISR → main-loop handoff (15 min)

**Prompt:** "The ADC ISR computes a sample. `loop()` must consume it without ever missing one and without doing work in the ISR. Show me the flag pattern."

```c
#include <stdint.h>

volatile uint16_t g_sample;     /* written by ISR   */
volatile uint8_t  g_sample_ready;/* the handshake   */

void ADC_ISR_Handler(void) {
    g_sample = ADC_read();      /* hardware register read - fine in ISR */
    g_sample_ready = 1;         /* set LAST, after the data is valid    */
}

void loop(void) {
    if (g_sample_ready) {
        disable_interrupts();   /* critical section: read data + clear flag together */
        uint16_t s = g_sample;
        g_sample_ready = 0;
        enable_interrupts();
        process(s);             /* slow work happens HERE, outside the critical section */
    }
    do_other_stuff();
}
```

**Expected:** conceptual — no compile. The correctness claim: a sample is never missed, and `process()` never runs inside the ISR.

**Narration beats:** *"Order matters: write the data, then the flag. If you set the flag first, the main loop could wake up and read a stale sample."* · *"Clearing the flag inside a critical section means the ISR cannot fire between reading the data and clearing the flag — otherwise a new sample's data could be overwritten while its flag is already cleared."*

**Follow-ups:** (a) what if samples arrive faster than `process()` can consume them? — you drop; that's what T3's ring buffer is for. (b) `volatile` isn't atomic — why does the critical section matter here? (c) what does the compiler do to a non-`volatile` flag? — hoists it out of the loop as loop-invariant and the code never sees the ISR's write.

**Links:** theory Q4–6, Q21–22 in [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]] · [[01-Areas/Engineering/SPM/module-4-user-defined-functions]] §16 (function pointers → ISR dispatch).

---

## T6 · CRC-8 for a sensor frame (15 min)

**Prompt:** "We're checking sensor frames over a noisy UART link. Implement CRC-8, polynomial 0x07."

```c
#include <stdint.h>
#include <stddef.h>

uint8_t crc8(const uint8_t *data, size_t n) {
    uint8_t crc = 0x00;
    for (size_t i = 0; i < n; i++) {
        crc ^= data[i];
        for (uint8_t b = 0; b < 8; b++) {
            crc = (crc & 0x80) ? (uint8_t)((crc << 1) ^ 0x07)
                               : (uint8_t)(crc << 1);
        }
    }
    return crc;
}
```

**Expected (verified — algorithm re-run in Python):** `crc8("123456789", 9) == 0xF4`, the standard CRC-8 check value for poly 0x07, init 0x00, no reflection, no final XOR. If your drill computes something else, the bug is almost always the missing `^ 0x07` on the top-bit branch.

**Narration beat:** *"Eight shift iterations per byte, so it's O(8n) — constant time per byte, O(1) extra space, no lookup table. A 256-entry table trades flash for speed if the link is the bottleneck."*

**Follow-ups:** (a) why CRC and not a plain sum — a sum misses reordering and many single-bit errors; (b) checksum vs CRC vs Hamming — detection strength vs bit overhead; (c) what happens on a bad frame — drop it, count it, and re-request. This pairs with T12.

---

## T7 · Integer PID step (18 min) — the control-loop task

**Prompt:** "Write one PID step. Everything's `int32_t`, no floats. Include output clamping so the integrator can't run away."

```c
#include <stdint.h>

typedef struct {
    int32_t kp, ki, kd;
    int32_t integral;
    int32_t prev_error;
    uint8_t primed;
} pid_t;

void pid_init(pid_t *p, int32_t kp, int32_t ki, int32_t kd) {
    p->kp = kp; p->ki = ki; p->kd = kd;
    p->integral = p->prev_error = 0;
    p->primed = 0;
}

int32_t pid_step(pid_t *p, int32_t setpoint, int32_t measured,
                 int32_t dt_ms, int32_t out_min, int32_t out_max) {
    int32_t error = setpoint - measured;

    /* conditional integration: don't accumulate while saturated */
    if (!(error > 0 && p->integral >= 0 && p->ki * p->integral >= out_max) &&
        !(error < 0 && p->integral <= 0 && p->ki * p->integral <= out_min)) {
        p->integral += error * dt_ms;
    }

    int32_t derivative = 0;
    if (p->primed) derivative = (error - p->prev_error) / (dt_ms ? dt_ms : 1);
    p->prev_error = error;
    p->primed = 1;

    int32_t out = p->kp * error + p->ki * p->integral + p->kd * derivative;
    if (out < out_min) out = out_min;
    if (out > out_max) out = out_max;
    return out;
}
```

**Expected (hand-checked, not compiled):** `kp=1, ki=0, kd=0`, setpoint 100, measured 90 → returns 10. With a huge `ki` and a sustained error the output stays pinned at `out_max` and `integral` stops growing — that's the windup guard working. The equivalent Python in **T11** *was* executed and shows the guard holding the integral at `1.0` versus `5.0` unguarded, so the logic is sound; only this C transcription is unverified.

**Narration beats:** *"`integral` accumulates error × time, so `dt_ms` has to be in there or the gain is meaningless — that's the #1 bug in hand-rolled PID."* · *"Derivative on the first call is meaningless because there's no previous error — hence the `primed` flag. Skipping it gives a kick on startup."* · *"`dt_ms ? dt_ms : 1` guards divide-by-zero rather than an early return, so timing stays uniform."

**Follow-ups:** (a) why clamp the output and not just the integral — clamping output alone still lets the integral wind; (b) filter the derivative — `derivative = (prev_d + (new_d - prev_d)/8)` is a one-pole low-pass, and it's why real loops don't explode on sensor noise; (c) sampling rate — must be ≥10× loop bandwidth.

**Links:** theory Q46–55 in [[01-Areas/Engineering/nexus-robotics/nexus-theory-rapidfire]] · derivations in [[01-Areas/Engineering/robotics/robotics-fundamentals]].

---

## T8 · Fixed-window moving average, no division in the hot path (15 min)

**Prompt:** "Smooth an ADC stream with a 4-sample moving average. No `malloc`, and I want it O(1) per sample."

```c
#include <stdint.h>

#define WIN 4

typedef struct { int32_t buf[WIN]; uint8_t idx; int64_t sum; } mover_t;

void    mover_init(mover_t *m) { m->idx = 0; m->sum = 0; }
int32_t mover_push(mover_t *m, int32_t x) {
    m->sum -= m->buf[m->idx];   /* subtract the sample leaving the window */
    m->buf[m->idx] = x;         /* add the sample entering            */
    m->sum += x;
    m->idx = (m->idx + 1) % WIN;
    return (int32_t)(m->sum / WIN);
}
```

**Expected (verified by simulation):** pushing 10, 20, 30, 40, 50, 60 returns `2, 7, 15, 25, 35, 45`.

**Why the early numbers look wrong — and why that is the teaching point:** the buffer starts zeroed, so the first outputs average against implicit zeros — `(10+0+0+0)/4 = 2`, `(10+20+0+0)/4 = 7`, `(10+20+30+0)/4 = 15`, `(10+20+30+40)/4 = 25`. From the 5th sample on, the window is genuinely full. **Say this out loud** — an examiner who sees `2, 7, 15…` and asks "is that a bug?" is testing whether you understand your own warm-up. Fixes if they push: prime the buffer by filling it with the first sample in `mover_init`, or discard the first `WIN-1` outputs.

**Narration beat:** *"Subtract-then-add keeps the window sum O(1) per sample instead of re-summing four elements — same result, constant time. This is the exact technique from [[01-Areas/Engineering/SPM/module-3-arrays]] sliding-window problems, applied to a stream."* · *"`int64_t` sum because 4 × int32 max overflows int32 — widening the accumulator is the standard guard."

**Follow-ups:** (a) why moving average over a median filter for an ultrasonic sensor — a median kills single-sample spikes, an average smears them; (b) what does averaging do to phase — adds group delay of ~N/2 samples, which is why you don't average inside a fast control loop without accounting for it; (c) exponential moving average `ema += alpha*(x - ema)` — O(1) memory, no buffer, but it never fully forgets.

---

