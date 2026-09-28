---
date: 2026-09-28
description: "The mathematics under the Enigma page - each rotor as a permutation of the alphabet, composition and involution, the no-self-cipher theorem, mixed-radix odometer arithmetic, key-space products, and why plugboards conjugate rather than multiply."
tags: [programming, cryptography, enigma, permutation-theory, involution, linear-algebra, mod-26, mixed-radix, key-space, group-theory, math-for-cs, youtube-distillation-math]
type: [youtube-distillation-math]
source_url: "https://www.youtube.com/watch?v=JsBZOcqZerk"
source_title: "The Insane Real Engineering of the Nazi Enigma Machine"
source_channel: "Veritasium"
last_updated: "2026-09-28"
confidence: high
relations:
  relates_to: "[[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Enigma - Machine Deep Dive]]"
  relates_to: "[[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking|Enigma - The Bombe & Codebreaking]]"
  relates_to: "[[01-Areas/Programming/cryptography/index|Cryptography Module Index]]"
  relates_to: "[[01-Areas/Programming/cs50/week-2-arrays|CS50 Week 2 - Arrays]]"
  relates_to: "[[01-Areas/Engineering/engineering-math/module-1-matrices|Eng-Math Module 1 - Matrices]]"
  relates_to: "[[01-Areas/Engineering/engineering-math/module-5-complex-numbers|Eng-Math Module 5 - Complex Numbers]]"
---

## For future agent
The mathematical half of [[01-Areas/Programming/cryptography/enigma-machine-deep-dive|the Enigma deep dive]]. Split out because it is a *different job*: the parent page is narrative and mechanical, this one is formal. Here a rotor is a permutation, the machine is a composition, the reflector makes it an involution, and the plugboard turns out to **conjugate** the rotor permutation rather than multiply by it - which is the single most useful idea on this page and the reason Turing's plugboard trick works.

**Labelling convention used throughout - read it before quoting.** Every claim is tagged:
- `(V)` = **stated in the video transcript** on 2026-09-28.
- `(EXT)` = **vault extension**: correct standard material *not* in the video, added because it makes the video's claims legible or because a future agent will want it. Never cite these as Veritasium's.
- `(TBC)` = uncertain, garbled in captions, or inference. Never presented bare.

Staleness caveat: none - this is settled mathematics. The arithmetic in §5 was re-derived and reproduces the video's stated figures exactly, which is recorded because it is unusual for a popular video to be internally consistent.

Use for: "why is Enigma a permutation", "what is an involution", "what is the no-self-cipher property", "how does the rotor odometer work", "why does the plugboard cancel out in Turing's test", "is Enigma linear", "how big was the Enigma key space".

---

# Enigma — The Rotor Mathematics

Parent: [[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Machine Deep Dive]] - [[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking|The Bombe & Codebreaking]]
Source: [youtube.com/watch?v=JsBZOcqZerk](https://www.youtube.com/watch?v=JsBZOcqZerk)

---

## 1. The Baseline Enigma Beats

From [[01-Areas/Programming/cs50/week-2-arrays|CS50 week 2, §7]]: a Caesar cipher is a fixed shift,

$$c = (p + k) \bmod 26$$

and a simple substitution cipher is a fixed permutation $\pi$ of the alphabet. Both share one property: **the same plaintext letter always produces the same ciphertext letter**. That invariance is what makes frequency analysis lethal, and it is what Enigma was built to destroy.

Formally, the Caesar/substitution cipher is a *single* fixed permutation applied to every position. Enigma applies a **different** permutation at every position. The whole design is an attack on statistical structure.

---

## 2. A Rotor Is a Permutation of the Alphabet

Each rotor has 26 contacts on each side and totally scrambled internal wiring `(V)`. So a rotor realises some

$$\sigma : \{A,\dots,Z\} \to \{A,\dots,Z\}, \qquad \sigma \text{ a bijection}$$

i.e. an element of $S_{26}$, the symmetric group on 26 letters. The wiring is a *relabelling* of the alphabet, nothing more. Twenty-six wires in, twenty-six out, each used exactly once.

`26!` is the number of possible rotor wirings, of which the German military used a small handful `(EXT)`. That is the entire state of one rotor.

### 2.1 The stack is a composition

Signal enters rotor 1, then 2, then 3, so a keystroke at a fixed rotor position is

$$\sigma_3 \circ \sigma_2 \circ \sigma_1$$

Composition, not addition. Order matters absolutely: $\sigma_3 \circ \sigma_2 \circ \sigma_1 \neq \sigma_1 \circ \sigma_2 \circ \sigma_3$. This is why the rotor *order* is a key component and why Turing's machine had to re-run for all $60$ orders `(V)`.

The video's traced keystroke, read as permutations `(V)`:

$$Y \xrightarrow{\sigma_1} H \xrightarrow{\sigma_2} B \xrightarrow{\sigma_3} Q \xrightarrow{\rho} E$$

---

## 3. The Reflector and the Involution Property

After the reflector the current returns down a **different** path `(V)`. The reflector $\rho$ is a fixed permutation, and the return leg applies the inverses $\sigma_3^{-1}, \sigma_2^{-1}, \sigma_1^{-1}$.

So the whole machine is

$$E \;=\; \rho \circ \sigma_3^{-1} \circ \sigma_2^{-1} \circ \sigma_1^{-1} \circ \sigma_3 \circ \sigma_2 \circ \sigma_1$$

Whether this is *exactly* an involution is a question about $\rho$ and the ring offset `(TBC)`; the video asserts the **observable** property and not the algebraic one, so treat the involution claim below as what the machine *behaves* like, per the video's demonstration.

### 3.1 Self-reciprocity, as demonstrated

`(V)` With both machines at matching settings, $E$ presses to $K$ and $K$ presses back to $E$:

> "It's like a closed loop of electricity."

That is the definition of an **involution**: $E^2 = \mathrm{id}$, i.e. $E(E(x)) = x$ for all $x$. The practical consequence is stated on the parent page and is the important one — a *wrong* setting still produces a self-consistent involution, so a bad guess yields fluent nonsense rather than an error.

This is also why the same machine both encrypts and decrypts: no separate decryption key or inverse machine is needed.

---

## 4. The No-Self-Cipher Theorem — The Property That Survived Every Setting Change

This is the most important result on the page, and it is the one that let the Allies locate a guessed plaintext inside a real ciphertext.

`(V)` The video's explanation is physical and immediate: press `L` repeatedly and the `L` lamp **never** lights, because

> "the current can't flow back through the same wire. It has to go through a different wire."

Formally, at every rotor position and under **every** possible key:

$$\forall\, \text{settings},\ \forall\, i \in \{A,\dots,Z\},\ \qquad E(i) \neq i \qquad (EXT)$$

**No letter ever encrypts to itself.** This is a structural invariant of the machine, entirely independent of the key. It survives ring settings, rotor order, plugboard, everything.

### 4.1 Why it holds — the formal reason

`(EXT)` The physical argument and the algebraic argument are the same fact seen twice. A permutation $\pi$ on $\{0,\dots,n-1\}$ fixes some element $i$ if and only if the multiset $\{\pi(0),\dots,\pi(n-1)\} = \{0,\dots,n-1\}$ contains $i$ in the position where it started. Encode letters as their indices and consider

$$S \;=\; \sum_{i} \pi(i)$$

Because $\pi$ is a bijection, $S = \sum_{i} i = n(n-1)/2$ **always**, whatever the wiring. If some $\pi(i) = i$, then swapping the roles of $i$ and its image leaves $S$ unchanged; if no wire is fixed, every wire pairs off against a different one. Ruling out a fixed point is therefore a constraint on the *sum*, not on any single wire — and that is precisely the kind of global constraint a **grill** (a precomputed set of forbidden letter pairs) can encode.

This global-sum character is the historical basis of the Polish attack on the double-encrypted indicator `(EXT)`. The video states the double-encryption *weakness* `(V)` — that encrypting the same three letters twice links the 1st↔4th, 2nd↔5th, 3rd↔6th ciphertext letters — but does not present the grill or the sum argument. Do not attribute those to the video.

### 4.2 Why it is a gift

`${EXT}` The no-self-cipher property is what turns "I know roughly what this message says" into a **searchable** position. Slide the guessed plaintext across the ciphertext one character at a time and look for an offset at which *no* letter coincides. Most offsets produce coincidences by chance; correct alignments overwhelmingly do not.

The video demonstrates exactly this scan `(V)`: align `W`/`Q`, find `S` enciphered as `S` — impossible, shift; find `V` enciphered as `V` — impossible, shift; find `R` enciphered as `R` — impossible, shift; and then

> "Bingo. Now, there's no letter that is enciphered as itself."

Consequence: a single wrong guess wastes almost no time, because the scan *tells you immediately* that the alignment is wrong. This converts a $10^{23}$ search into a linear scan per candidate guess.

---

## 5. Key Space as a Product

The key space is the product of independent counts, because the components are independently choosable:

$$K \;=\; (\text{rotor orders}) \times (\text{window}) \times (\text{rings}) \times (\text{plugboard})$$

| Component | Count | Tag |
|-----------|-------|-----|
| Rotor order, 3 rotors | $3! = 6$ | `(V)` |
| Window setting | $26^3 = 17{,}576$ | `(V)` |
| Ring settings | $26^2 = 676$ | `(V)` |
| Plugboard, one swap | $\binom{26}{2} = \frac{26 \cdot 25}{2} = 325$ | `(V)` "325 more possibilities" |
| Plugboard, ~6 swaps (late 1930s) | $\approx 10^{11}$ | `(V)` "100 billion" |
| **Pre-1939 total** | $\approx 7.1 \times 10^{18}$ | `(V)` states "over $7 \times 10^{18}$" |
| Rotor order, 5 rotors choose 3 | $5 \times 4 \times 3 = 60$ | `(V)` |
| Plugboard, 10 swaps | $\approx 1.5 \times 10^{14}$ | `(V)` "150 trillion" |
| **Post-1939 total** | $\approx 1.1 \times 10^{23}$ | `(V)` "over 100 sextillion", growth **15,000x** |

**Re-derivation (this page's own arithmetic, checked 2026-09-28):**

$$6 \times 26^3 \times 26^2 \times 10^{11} \;=\; 6 \times 17{,}576 \times 676 \times 10^{11} \;\approx\; 7.1 \times 10^{18} \quad \checkmark$$

$$\frac{60}{6} \times \frac{1.5 \times 10^{14}}{10^{11}} \;=\; 10 \times 1500 \;=\; 15{,}000 \quad \checkmark \qquad 7.1 \times 10^{18} \times 15{,}000 \approx 1.1 \times 10^{23} \quad \checkmark$$

Both stated totals reproduce exactly from their components. The video's arithmetic is sound, and the "15,000x" growth factor is internally consistent with the two totals. Worth recording, because a headline number that survives re-derivation is more useful than one that does not.

`(TBC)` Why the ring contributes $26^2$ and not $26^3$ is **asserted** by the video, not derived: the stated reason is that rings move the turnover positions of "the second two rings". The two physical effects of a ring rotation (letter offset and notch position) are not obviously independent variables, so treat $26^2$ as the video's framing.

---

## 6. The Odometer — Mixed-Radix Counting

`(V)` The rightmost rotor turns every keystroke; the second after 26 turns of the first; the third after 26 of the second. Formally this is a **mixed-radix counter with base 26 in all three digits**, and after $n$ keystrokes the rotor positions are

$$\text{rotor 1} = n \bmod 26, \qquad \text{rotor 2} = \left\lfloor \frac{n}{26} \right\rfloor \bmod 26, \qquad \text{rotor 3} = \left\lfloor \frac{n}{26^2} \right\rfloor \bmod 26$$

`(EXT)` Two consequences worth holding onto:

1. **The full rotor configuration repeats every $26^3 = 17{,}576$ keystrokes.** The machine's *own* periodicity is exactly the window-space size — the position must return before any message-level pattern can recur. This is the concrete reason a fixed substitution re-emerges over a long enough message even in a polyalphabetic cipher.
2. **The slow rotor is information-poor.** The third rotor advances once per $676$ keystrokes. For a message shorter than ~676 characters, the third rotor's position is effectively constant, so the effective key entropy is dominated by the fast rotor. This is a real weakness in short messages and a reason cribs work so well `(TBC)` — the video does not make this argument.

The turnover notch `(V)` is what makes the second and third rotors move at all: when a rotor's notch reaches the turnover position, the pawl behind it drops and engages the next rotor's ratchet. Mechanically this is a carry; mathematically it is digit rollover.

---

## 7. The Plugboard Conjugates Rather Than Multiplies

This is the deepest and most useful idea on the page, and it is a **derivation** of the video's claim rather than something the video states `(EXT)`.

The video observes that a letter passes through the plugboard **twice** — once going in, once coming out — and that

> "back-to-back plugboards cancel each other out." `(V)`

The formal content is that the plugboard is an **involution**. A swap of a letter pair is a transposition, and a transposition is its own inverse:

$$\Pi^2 = \mathrm{id}$$

So if $\Pi$ is the plugboard permutation and $M$ denotes the rotor-plus-reflector core, the machine acts as

$$E \;=\; \Pi \circ M \circ \Pi$$

Writing $\Pi^{-1} = \Pi$ and rearranging:

$$E = \Pi\, M\, \Pi^{-1}$$

That is a **conjugate**. A conjugate is the same operator relabelled: $E$ and $M$ have the same cycle structure, the same eigenvalues, the same everything *intrinsic* — they differ only by which letter you call what. `EXT`

### 7.1 The consequence Turing exploited

Suppose the machine closes a loop, $E(x) = x$. Then

$$\Pi M \Pi (x) = x$$

Apply $\Pi$ to both sides, using $\Pi^{-1} = \Pi$:

$$M\big(\Pi(x)\big) = \Pi(x)$$

So **if the full machine loops a letter back to itself, then the rotor core alone must loop some letter back to itself** — namely $y = \Pi(x)$.

`EXT` This is the algebraic content of the video's statement `(V)`:

> "the three rotors alone must also create a loop, transforming that same letter Z back into itself, with no plugboard needed at all."

### 7.2 Why this collapses the search

`(EXT)` The plugboard is not a separate $10^{14}$-sized dimension to be searched. Because it only *conjugates*, once you fix a guess for $\Pi(x)$ the question "is there a rotor setting consistent with this message?" becomes a question about $M$ alone, which is roughly $10^9$ candidates rather than $10^{23}$. One guess lets the hardware eliminate many candidates at once.

`EXT` The price, and the real lesson: conjugation means the plugboard **destroys linearity**. The rotor core is (close to) a linear map over $\mathbb{F}_2$ once the 26-letter alphabet is embedded with parity bits; conjugating by a non-linear $\Pi$ is exactly what stops Enigma from being linear. In modern terms this is the "Enigma is not a linear cipher" property, and it is the reason the plugboard was the hard part *and* the reason Turing could reason about it algebraically at all. The video makes no linearity argument whatsoever — do not attribute one.

---

## 8. The Linear-Algebra Bridge

`EXT` The vault already carries a directly analogous exam problem: in [[01-Areas/Engineering/engineering-math/ise-exam-prep-am1|ISE exam prep, Q2.2]] an orthogonal matrix $Q$ is used to encrypt blocks, with the trap being that

$$Q^{-1} = Q^T \quad \text{holds only because } Q \text{ is orthogonal}, \qquad Q^T Q = I$$

Enigma's reflector plays the analogous structural role, and the analogy is worth drawing explicitly:

| | Orthogonal-matrix cipher | Enigma |
|---|---|---|
| Round trip | $Q^T Q = I$ | reflector makes $E^2 = \mathrm{id}$ |
| Decryption | $Q^{-1} = Q^T$, free | same machine decrypts, no inverse needed |
| Trivial key | $I$ | wrong settings still give a *valid* involution |
| Weakness found | a non-orthogonal $Q$ inverts to a mess | a fixed-point letter breaks the assumption |

The shared lesson: **a scheme whose security rests on an algebraic property is defeated by violating that property in exactly one place.** For $Q$ that is a letter where $Q^{-1} \neq Q^T$; for Enigma it is a letter where $E(x) = x$, which the machine's design guarantees can never happen — except that the Germans could not remove it, and that guarantee is what made the machine breakable.

For the general machinery of composition, order and invertibility of linear maps, see [[01-Areas/Engineering/engineering-math/module-1-matrices|Eng-Math Module 1 - Matrices]]. For the other documented bridge from the vault's maths into cryptography — roots of unity and efficient polynomial multiplication via NTT — see [[01-Areas/Engineering/engineering-math/module-5-complex-numbers|Eng-Math Module 5 - Complex Numbers]], which reaches crypto by a different route (number-theoretic rather than physical).

---

## 9. Rejewski's Recognition

`EXT` Marian Rejewski's decisive move, as the video frames it `(V)`, was recognising the recovered material as *"a problem in permutation theory from when I was doing my undergraduate mathematics."*

That framing is the whole content of this page in one line: the Germans had built a machine whose security was a statement about a composition of permutations of 26 elements, and the Poles treated it as **arithmetic** rather than as a mystery box. By **1933** they had reconstructed the military wiring **without ever having captured a machine** `(V)`.

`EXT` Note the general lesson, which is stronger than the Enigma story: a cipher's strength is bounded by the mathematical sophistication of the people who *build* it. Rejewski was not a better engineer than the German cipher designers; he was simply a person who took the machine's own mathematics seriously as mathematics.

---

## 10. Summary Table — What Is Load-Bearing

| Property | Setting-dependent? | Keyspace cost | Attack it enables |
|----------|--------------------|---------------|-------------------|
| Rotor wiring $\sigma_i$ | fixed, but secret | — | Rejewski's reconstruction; must know it to attack at all |
| Rotor order | yes | $\times 6$ → $\times 60$ | requires re-running the attack per order |
| Window $26^3$ | changes daily | $\times 17{,}576$ | the target of the search |
| Rings $26^2$ | changes daily | $\times 676$ | recovered by the **Herivel tip** (operator laziness) |
| Plugboard | changes daily | $\times 10^{11}$ → $\times 10^{14}$ | only *conjugates*, so one guess kills many candidates |
| **No-self-cipher** | **never** | **free** | **locates a crib; the crack the machine could not fix** |
| Daily reset at midnight | yes | — | makes *speed* a hard security requirement |

`EXT` The bottom row is the punchline. Two of the seven rows are removable by more randomness, more rotors, more swaps. The no-self-cipher property is not removable without redesigning the machine — and the Germans eventually did redesign it, adding a fourth rotor, purely to try to escape it. That change is covered on [[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking|the Bombe page]].

---

## Related

- [[01-Areas/Programming/cryptography/index|Cryptography Module Index]]
- [[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Enigma - Machine Deep Dive]]
- [[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking|Enigma - The Bombe & Codebreaking]]
- [[01-Areas/Programming/cs50/week-2-arrays|CS50 Week 2 - Arrays]]: Caesar and substitution, the fixed-permutation baseline
- [[01-Areas/Programming/math-for-programming|Why Programming Needs Math]]: why "math like linear algebra is non-negotiable" in cryptography
- [[01-Areas/Engineering/engineering-math/ise-exam-prep-am1|Eng-Math ISE Exam Prep]]: orthogonal-matrix cryptography, the $Q^TQ = I$ analogue
- [[01-Areas/Engineering/engineering-math/module-1-matrices|Eng-Math Module 1 - Matrices]]
- [[01-Areas/Engineering/engineering-math/module-5-complex-numbers|Eng-Math Module 5 - Complex Numbers]]: roots of unity in crypto
