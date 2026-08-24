---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 0
topic: "Computational Thinking, Binary, Abstraction, Algorithms & Scratch"
tags: [programming, computer-science, cs50, harvard, scratch, binary, ascii, unicode, algorithm, pseudocode, abstraction]
last_updated: "2026-08-11"
---

# Week 0 — Scratch & Computational Thinking

> **Goal of the week:** define what computer science *is* (problem solving with binary representation + algorithms + abstraction), and write your first programs in Scratch — a language that makes all four ideas visible.
> **PSet 0:** a Scratch animation/game (creativity + event-driven code).

---

## 1. Computational Thinking — Computer Science Is Problem Solving

- **CS is not "computers"** — computers are just the vehicle. CS is the discipline of **taking a problem, representing its information, and designing step-by-step procedures (algorithms)** to solve it.
- **Input → Algorithm → Output:** every program reduces to this pipeline.

```
            INPUT (representation)
                    │
                    ▼
   (steps, one at a time, in an order)  ← algorithm
                    │
                    ▼
            OUTPUT (results)
```

- **Decomposition, pattern-matching, abstraction** are the three thinking habits: break big problems into small ones; reuse known solutions; hide details behind names.

---

## 2. Representing Information — Binary

- Computers are **bipolar**: electricity is on/off. That gives us **two digits: 0 and 1**, i.e. **base-2 (binary)** vs our customary base-10 (decimal).
- **Bits & bytes:** a **bit** (binary digit) is one 0/1; a **byte** is 8 bits. One byte can represent $2^8 = 256$ distinct values.
- **Decimal → binary conversion** ("counting on your hands" — finger up = 1):

| Power | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
|---|---|---|---|---|---|---|---|---|
| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| Example: 50 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |

$$50_{10} = 00110010_2 \quad(= 32+16+2)$$

- **Pattern to internalize:** doubling is a power-of-two rule — $1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, \dots$ — and byte values always "roll over" at powers of two. (This is why 1 **KB** = 1024 bytes, etc.)

### ASCII, Unicode, and the "text vs number" illusion
- **ASCII** maps each character to a byte: `A` = 65, `B` = 66, … `a` = 97, `0` = 48, space = 32. So *text is just agreed-upon numbers*.
- **Unicode** extends the mapping (hundreds of thousands of characters — emoji, non-Latin alphabets) because one byte is not enough for every human language.
- **Colors:** RGB — each pixel is three bytes (red, green, blue). Millions of colors from 3×8 bits.
- **Video:** ~30 images per second × resolution × color depth → massive bit rates. Everything is bits.

> **Takeaway:** representation is *always* a trick — bits have no inherent meaning; **context/agreement (the "standard")** gives them meaning.

---

## 3. Algorithms — Step-by-Step Problem Solving

- **Algorithm** = a precise, ordered set of steps to transform input into output; unambiguous enough that a "dumb" machine can follow it.
- **Pseudocode** = describing the algorithm in plain English with programming vocabulary (**$function$, $condition$, $loop$, $boolean\;expression$, $return$**), independent of any language.
- **Running time:** some algorithms are faster than others (e.g., finding a name in a phone book: flipping page-by-page vs. **binary search** — opening to the middle and halving each time). Formal trade-offs arrive in [[cs50/week-3-algorithms]] (big-$O$).
- **Correctness vs design:** an algorithm can be *right* (correct output) but *badly designed* (too slow). Good CS optimizes both.

---

## 4. Abstraction — The Most Powerful Idea

- **Abstraction** = taking a detail and hiding it behind a name/interface, so you can reason at a higher level.
- Malan's stage example: a "stage" function (lighting, sound, projector, screen) means the teacher doesn't re-invent wiring every lecture.
- In code this becomes **functions**, **libraries**, and later **classes/interfaces** — used so relentlessly in the course that a whole lesson (Week 5) exists to show what's *underneath* on that layer.

---

## 5. Scratch — Your First Programming Language

Scratch is a **visual, block-based** language that nonetheless contains *every* construct C, Python, and Flask will use:

| CS concept | Scratch block | Appears next in |
|---|---|---|
| Triggering code / **events** | `when [green flag] clicked`, `when key pressed` | Web app routes, JS event listeners |
| **Sequencing** | blocks stack top-to-bottom | every language |
| **Functions** | `define myBlock`, `My Blocks` | Week 1 C functions |
| **Loops** | `forever`, `repeat 10`, `until <>` | Week 1 loops |
| **Conditionals** | `if <> then`, `if <> then else` | Week 1 conditionals |
| **Variables** | `set myVariable to 0` ("variables are in the cloud" = persistence) | Week 1 variables |
| **Booleans** | `touching edge?`, `< 50`, `not`, `and`, `or` | Week 1 logical operators |
| **Input/Output** | `ask and wait`, `say`, `change x by` | C's `get_*`/`printf` |

### A canonical Scratch design pattern
```
when [green flag] clicked
  set score to 0
  forever
     if <touching color [red]> then
        say [Game Over]
        stop [all]
     end
  end
```

### Key lesson Scratch teaches before C
- **The machine is dumb**: blocks do *exactly* what you say — and the "cost" of wrong instructions is visible immediately, so the debugging habit (predict → run → compare) forms early.
- **Event-driven thinking:** programs start running when *something happens* (mouse click, key press) — the same model as web/JS and apps.

---

## 6. Computational Thinking Vocabulary (must know after this week)

- binary · bit · byte · ASCII · Unicode · RGB · algorithm · pseudocode · boolean expression · condition · loop · function · event · variable · abstraction · running time (informal) · correctness · design

## 7. Cross-Links

- [[cs50/week-1-c]] — Scratch blocks become C syntax next week.
- [[programming-cs-fundamentals]] — segments #1–7 echo these concepts.
- [[math-for-programming]] — binary/ASCII are the "math is everywhere" proof from Week 0.
- [[cs50/problem-sets]] — PSet 0 requirements and ideas.