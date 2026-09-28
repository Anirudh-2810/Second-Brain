---
date: 2026-09-28
description: "How Turing turned Enigma's structure into an automated attack - cribs from weather reports, the no-self-cipher scan, loop-closing menus, plugboard isolation by contradiction, Welchman's diagonal board, and the slow climb to Naval Enigma."
tags: [programming, cryptography, enigma, bombe, crib, known-plaintext, contradiction-search, diagonal-board, welchman, bletchley-park, naval-enigma, codebreaking, turing, youtube-distillation]
type: [youtube-distillation]
source_url: "https://www.youtube.com/watch?v=JsBZOcqZerk"
source_title: "The Insane Real Engineering of the Nazi Enigma Machine"
source_channel: "Veritasium"
last_updated: "2026-09-28"
confidence: high
relations:
  relates_to: "[[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Enigma - Machine Deep Dive]]"
  relates_to: "[[01-Areas/Programming/cryptography/enigma-rotor-math|Enigma - The Rotor Mathematics]]"
  relates_to: "[[01-Areas/Programming/cryptography/index|Cryptography Module Index]]"
  relates_to: "[[01-Areas/Programming/cs50/week-10-cybersecurity|CS50 Week 10 - Cybersecurity]]"
---

## For future agent
The attack half of the Enigma set, and the page a future agent should read for the **method** rather than the history. The payload is Turing's logical test: turn a structural invariant into a yes/no predicate, then build hardware that evaluates the predicate over millions of candidate settings per minute.

`(V)` = stated in the video transcript on 2026-09-28. `(EXT)` = vault extension, not in the video. `(TBC)` = uncertain or garbled.

Companion pages: [[01-Areas/Programming/cryptography/enigma-machine-deep-dive|mechanics and key space]] · [[01-Areas/Programming/cryptography/enigma-rotor-math|permutations, involutions, and why plugboards conjugate]] (the algebraic justification for the plugboard trick lives there — read it before §5).

Staleness caveat: none. Historical. The sponsor segment (23:41-24:37) is stripped. The video's closing claim of a specific Enigma key space of ~$10^{23}$ and Hitler's machine at ~$10^{170}$ is recorded as stated; the latter is compared in-video to "the number of atoms in the observable universe squared".

Use for: "what is a crib", "known-plaintext attack", "how did the Bombe work", "what is a diagonal board", "why do contradictions help search", "what is a dragon break", "Turing vs Welchman".

---

# Enigma — The Bombe & Codebreaking

Parent: [[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Machine Deep Dive]] - [[01-Areas/Programming/cryptography/enigma-rotor-math|The Rotor Mathematics]]
Source: [youtube.com/watch?v=JsBZOcqZerk](https://www.youtube.com/watch?v=JsBZOcqZerk)

---

## 1. The Problem, Stated Precisely

`EXT` The attack has four unknowns and they are wildly different in size. This table is the map for everything below:

| Unknown | Approx size | Who attacked it |
|---------|-------------|-----------------|
| Rotor order | 6 → 60 | brute force, but the whole attack must be **re-run** per order |
| Ring settings | $26^2$ | **statistics** — the Herivel tip |
| Window setting | $26^3 \approx 17{,}576$ | the Bombe |
| Plugboard | $10^{11}$ → $10^{14}$ | the Bombe, by contradiction |

Bletchley's own plan, per the video `(V)`: listening stations intercept traffic → codebreakers analyse the day's traffic for patterns → clues feed a guess at the settings → settings go into their own Enigmas → messages read.

`EXT` Notice the structural point: **four of the five stages are cheap**. Only the third is hard, and the Bombe's entire job is to make that one stage automatic. Everything else — interception, crib analysis, machine-setting, reading — is clerical once the settings are known.

The wall before 1940: 9,000 people could not do the third stage fast enough, and the settings **changed at midnight**.

---

## 2. Cribs — Turning Mundane Routine Into an Attack Surface

`(V)` German outposts sent near-identical messages at the same time every day. Weather. A report from Biscay arriving at 6:00 a.m. daily was overwhelmingly likely to contain

> "Wettervorhersage Biscaya."

A **crib** is a guess at what some stretch of ciphertext decrypts to. The **cribbing room** at Hut 8 — staffed, per the video, by people including Jon Weinbaum, who wrote his thesis on how Enigma was broken — searched out strong, consistent cribs: weather text, recurring procedural phrasing, slang, shorthand.

`EXT` The general principle, and the reason this matters far beyond Enigma: **a system cannot hide what it is forced to emit.** Every protocol that sends a fixed preamble, a timestamp, a call sign, or a status word is running a known-plaintext attack against itself continuously. The secrecy assumption "an adversary cannot guess my plaintext" was never true for the entire population of military radio traffic.

---

## 3. Locating the Crib — The No-Self-Cipher Scan

The crib tells you *what* the text is; the machine's structural invariant tells you *where* it is.

`(V)` Press `L` and the `L` lamp never lights —

> "the current can't flow back through the same wire. It has to go through a different wire."

So a crib is slid across the ciphertext one position at a time, looking for an alignment where **no letter coincides with itself**:

| Alignment tried | Finding | Verdict |
|-----------------|---------|---------|
| `W`/`Q` aligned | `S` enciphered as `S` | impossible → shift |
| shifted 1 | `V`→`V`, `E`→`E` | impossible → shift |
| shifted 2 | `R`→`R` | impossible → shift |
| shifted 3 | no self-coincidences | **"Bingo."** |

`EXT` Formal statement: since $E(i) \neq i$ for all $i$ under all settings, a correct alignment has **zero** self-coincidences while a wrong alignment of crib length $L$ has expected self-coincidences $\approx L/26$. For a 25-character crib that is roughly 1 — so a wrong guess usually dies on the first or second letter, and a correct one essentially never produces a self-coincidence. The test is close to a *proof* rather than a likelihood. See [[01-Areas/Programming/cryptography/enigma-rotor-math|Enigma - The Rotor Mathematics]] §4 for the algebraic reason the property exists.

`EXT` The important asymmetry: this step tells you the crib **is** there, but not **what rotor setting produced it**. The Bombe is needed for the second half.

---

## 4. Turing's Logical Test — Building a Menu of Loops

Turing's framing, which is the conceptual heart of the video `(V)`: if the process of breaking Enigma can be written as a **sequence of logical tests**, then a machine can perform those tests instead of him.

### 4.1 The setup

`(V)` He assumes the message begins with the window at `ZZZ` (i.e. 26, 26, 26) and that the second rotor has not yet turned. As soon as the first letter is typed, the rightmost rotor turns to `A` (1). At that position, typing `W` outputs `R` — meaning the machine **wires `W` to `R` and `R` to `W`**. At the next position, `E` and `W` are wired together; then `T` and `I`.

### 4.2 The loop

`EXT` This is the key step, and the video states it in concrete letters. The permutation changes at every position, so take three positions from the message and read off the mapping:

| Position | Mapping |
|----------|---------|
| 6 | `R` → `Y` |
| 22 | `Y` → `S` |
| 9 | `R` → `S` |

`EXT` Compose them: `R →(6) Y →(22) S`, and separately `R →(9) S`. So the first two steps and the third agree — `R` closes a cycle of length 3 back onto itself. Now imagine three copies of the Enigma, at positions 6, 22 and 9, wired **back to back**: the output of Enigma-6 feeds Enigma-22, whose output feeds Enigma-9. Hit `R` on the first machine and it emits `Y`; the second transforms that to `S`; the third takes that `S` back to `R`.

`(V)` The video's phrasing:

> "creating a perfect loop. R turns back into R."

`(V)` And the reason this is a *test* rather than a curiosity:

> "if the settings don't match... the test is extremely unlikely to produce a loop, and R should turn into a different letter instead."

`EXT` Formally, the full message permutation $E$ maps a letter $x$ to itself exactly when the composition of the per-position permutations along a cycle of the message sends $x$ back to $x$. Because $E$ is an involution (§ rotor-math §3), the entries along the path are pairwise inverses, so this reduces to whether the cycle of positions visited by $x$ is consistent with a *single* choice of rotor setting. If the machine settings are right, the loop closes. If they are wrong, the loop is generically broken. That is a yes/no predicate over settings — exactly what Turing asked for.

### 4.3 The menu

`(V)` One loop gives hundreds of false positives. So the constraints accumulate: from the same crib, `R` maps to `W` at position 1, `W` to `E` right after, `E` to `O` at position 8, `O` to `S`, then back to `R` — completing another loop. Chained, these form a **menu** of logical constraints that a candidate setting must satisfy *simultaneously*.

`EXT` This is constraint propagation before the term existed. Each loop is a weak filter; the conjunction of many is a strong one. The engineering problem is then purely mechanical: evaluate the whole menu as fast as the electricity moves.

### 4.4 The rotor-order tax

`(V)` The test assumes the right rotor order. The Germans had **five** rotors and could slot any three in any order — 60 configurations — so the whole process had to be re-run for each. `(TBC)` The video implies all 60 were re-run, without stating the mechanism.

---

## 5. Isolating the Plugboard — The Conjugation Argument

This is where 150 trillion possibilities become tractable, and it is the most elegant step in the story.

`(V)` A letter passes the plugboard **twice** — on the way in and on the way out — and

> "back-to-back plugboards cancel each other out."

`(V)` So the whole cascade collapses to: plugboard, then all rotors, then plugboard. If the three Enigmas transformed `R` back to `R`, then

> "if the first plugboard transformed an R to a Z on the way in, then the last plugboard must have transformed a Z into an R on the way out. So, the three rotors alone must also create a loop, transforming that same letter Z back into itself, with no plugboard needed at all."

`EXT` The algebra is in [[01-Areas/Programming/cryptography/enigma-rotor-math|rotor-math §7]]: the plugboard $\Pi$ is an involution, so $E = \Pi M \Pi = \Pi M \Pi^{-1}$ is a **conjugate** of the rotor core $M$. Hence $E(x) = x \iff M(\Pi(x)) = \Pi(x)$. The plugboard never appears as a search dimension — only the *image* of one letter does. This is the mathematical reason a $10^{14}$ component collapses to a 26-way question.

### 5.1 The test, as electrical hardware

`(V)` Turing's realisation: this can be done with a simple electrical circuit.

1. **Guess** one plugboard pairing — say `R` is plugged to `Z` — and set that wire live.
2. **If the guess is right**: the three Enigmas transform `Z` back to itself, leaving a **single loop of live wires**.
3. **If the guess is wrong**: `Z` loops back to a *different* letter, that letter loops to another, and current keeps circulating — so **multiple wires go live**.
4. **The contradiction**: multiple live wires would mean `R` is **simultaneously plugged to several letters, which is impossible**. So every alternative is eliminated in one pass.

`(V)` Two boundary cases, both used:

| Result | Meaning |
|--------|---------|
| **All 26** wires live | no plugboard is possible for this window — advance the rotors one step and retest |
| **25** live, **one dark** | the other 25 are ruled out, so the single dark wire is the only remaining candidate |

`EXT` The 25-of-26 case is the elegant one, and it is often called a **dragon break**. One electrical test eliminates 25 of 26 possibilities. Crucially the guess itself carries no information — it is a **probe**. `(V)` The video states this explicitly:

> "The guess didn't even have to be correct for this to work."

`EXT` This is the single most transferable idea in the whole set. A wrong assumption that produces an *inconsistent* result is more useful than a right assumption that produces a consistent one, because inconsistency is detectable and cheap. It is elimination by contradiction, and it converts an intractable search into one that prunes geometrically.

---

## 6. The Bombe — Machine, Then Delay

`(V)` Turing's test was performed by hand on paper, following the implications through. He designed a machine to do it **instantaneously** —

> "not the speed of light, but the speed of electricity flowing in a wire."

- Built with the engineer **Harold Keen**, drawing on Polish Cipher Bureau ideas.
- Named the **Bombe** in honour of the Polish **Bomba** the mathematicians had left behind.
- **First prototype: March 1940** — roughly six months after the war began, which the video's expert calls "pretty startling" given he also had to get the civil service *and* finance to approve and fund it.
- Physically: **~36 Enigma equivalents in parallel, working backwards**.
- A run takes **~13 minutes**; the machine in the video reports roughly a **90%** chance it is working correctly. `(TBC)` — that figure is the museum expert's, not a published spec.
- Output is read from the **indicator drums** on the right-hand end. In the run shown, the pointers indicate `DKX`. `(V)`

`EXT` Why the Bombe runs *backwards*: a menu loop asserts "this setting makes `R` close a cycle". Rather than decrypting forward, the machine wires the loop in reverse so that a closure shows up as a current flowing in a closed circuit. `EXT` — the video describes it as "working backwards" but does not develop the reason.

### 6.1 The Bombe was too slow — and why

`(V)` Two separate problems, and the video keeps them distinct:

**Problem A — self-contradictory stops.** There was a flaw in Turing's original test: the machine would sometimes stop on a loop that looked valid but was actually self-contradictory, e.g. implying `R` was plugged to **both** `X` and `S` at once. The machine had no way to catch this. With 100 stops each taking 15 minutes to check, that is **more than 24 hours of work** — by which time the settings had already changed. `(V)` "The bomb wasn't fast enough."

**Problem B — the Nazi redesign.** Turing's attack was, in the expert's words, "so resilient to protocol changes that it would have worked at any time prior to this. It is fundamental to the structure of the Enigma machine." So the Germans **changed the machine itself** to escape it — adding a **fourth rotor**. `(V)`

> "You either reinvent the entire machine or... prevent them from knowing any information whatsoever." `(V)`

`EXT` Worth stating plainly: this is a **designer-versus-analyst** cycle. The analysts found a structural invariant; the designers modified the machine; the analysts found a new method for the new machine. Each round took longer than the last, which is why the war's decisive year — 1943 — was two years after the first prototype.

---

## 7. Welchman's Diagonal Board — Making It Practical

The mathematician who fixed Problem A was **Gordon Welchman**, another Cambridge mathematician at Bletchley.

`EXT` Note this is the *same class of insight* as §7 of the rotor-math page, arriving by a different route: both Rejewski and Welchman find power in treating a wiring diagram as algebra.

`(V)` The observation: guessing `R` is plugged to `Y` is **exactly the same** as guessing `Y` is plugged to `R`. So Welchman **connected those two wires together**, so that if one went live both would. The same for `S`↔`Y` and `R`↔`S`.

`(V)` The effect: the same input now rules out **more** plugboard swaps, so far fewer false positives — from ~100 candidate solutions down to **four**. In the video's phrasing, the diagonal board "could eliminate over 90% of false stops". **This is what made the Bombe practical.** Ready **August 1940**.

`EXT` The mechanism is the same contradiction trick, applied to the *algebraic* structure of a transposition. Because $\Pi$ is an involution, the statements "$\Pi(R)=Y$" and "$\Pi(Y)=R$" are one fact, not two. Forcing both wires to share a live state makes the machine rule out an entire *orbit* of hypotheses per test instead of a single hypothesis. The gain is combinatorial, not mechanical.

### 7.1 The clock

`EXT` Read the dates against the war:

| Date | Event |
|------|-------|
| Sept 1939 | war begins |
| March 1940 | first Bombe prototype |
| Aug 1940 | diagonal-board Bombe ready — by now France, Norway, Denmark have fallen |
| Aug–Sept 1940 | Battle of Britain; the air commander could judge whether to commit the last reserve fighter squatters because Enigma intelligence reinforced his own sense of the balance of forces |
| end 1941 | **16 Bombes** in operation (6 at Bletchley, 10 nearby); Army + Luftwaffe traffic read routinely |
| 1942 | El Alamein — decrypts reveal the German Army critically short of fuel and supplies |
| 1943 | Americans build **100+** Bombes of their own |

`(V)` On the Battle of Britain, the video cuts in Churchill: *"We shall defend our island, whatever the cost. We shall fight on beaches."* `(TBC)` — the quotation appears truncated/garbled in the transcript; the full "fight on the beaches" passage runs *"…if we can only stand up to you, all Europe may be free."*

`EXT` The strategic point: the Bombe did not win battles. It changed what commanders believed about the balance of forces, and commanders act on belief. Note also that between August 1940 and the end of 1941 the *count* of machines mattered more than their elegance — a lesson about capacity versus insight.

---

## 8. Naval Enigma — Where It Got Hard

`EXT` Everything above targets the Army and Luftwaffe networks. The Navy was different in kind, and the video is explicit that it was much harder.

`EXT` Why, structurally:
- A **fourth rotor** (Naval M3/M4) `(V)` — more rotor choices, so more orders, so more re-runs. Turing had to invent "a whole new statistical method to narrow down the choice of rotors" `(V)`.
- A **larger plugboard** — more swaps, a bigger conjugation to reason about.
- The U-boat wolfpack threat was existential, so a slow result is not merely useless but fatal.
- Higher-volume, higher-value traffic meant more to read and less time.

`EXT` The British response combined cryptanalysis with plain field intelligence and deliberate attacks on the enemy's process:
- **Captured key sheets** from materials recovered from **sunk U-boats** `(V)` — which is to say, from the deaths of Royal Navy sailors. `EXT` The video names this directly and refuses to soften it.
- **"Gardening"** `(V)`: when plaintext was desperately needed, they would have the military **seed mines at particular locations**; German forces then had to go and clear them, forcing those locations into the plaintext. An attack on the ciphertext conducted by *engineering* the plaintext.

`EXT` Gardening is a beautiful general technique and worth naming as such: rather than attacking the cryptosystem, change the *world* until the plaintext you want becomes forced. The lesson generalises to any system whose plaintext you can influence — you do not always need to break the cipher, only to control the input.

`EXT` On the human cost, the video's expert is careful:

> "codebreaking is not the same as combat, and battles are not won by codebreakers sitting in rooms in the safety of Bletchley Park. They're won by people at the sharp end of things." `(V)`

`EXT` **1943** is marked as the turning point: once the U-boat Enigma was mastered, Germany's position began to collapse. `(TBC)` The transcript is garbled at this point — it says the sinkings both "drop like a stone" and then "start to rise". The well-documented reading is that the **Allies**' ability to locate and destroy U-boats improved sharply, so German U-boat losses rose and the Battle of the Atlantic turned in the Allied favour. Recorded as the historical reading, **not** as a claim from the video. By the end of 1943 everyone except Hitler knew Germany would lose. `(V)`

---

## 9. D-Day, and the Machine Nobody Broke in Time

`(V)` By 1944 Enigma traffic from all Nazi forces was being deciphered daily, setting the stage for Normandy. Historians estimate breaking Enigma **shortened the war by up to two years**, with the lives that implies.

`EXT` The neat irony the video ends on. To confirm their own D-Day deception — that the invasion would come at the Pas-de-Calais, not Normandy — the Allies needed to read **Hitler himself**. And Hitler did not use Enigma `(V)`. He used a different machine, one the Allies had never seen, with a key space of roughly

$$10^{170} \quad \text{versus Enigma's} \quad 10^{23}$$

`(V)` "greater than the number of atoms in the observable universe squared", and breaking it was "described as the greatest intellectual feat of World War II" — and yet the video never names the machine or the people who cracked it, because it was classified for decades afterwards. `(TBC, inference)` It is generally identified as the **Lorenz SZ40/42**. That identification is **not** made in the video; recorded here as inference only, per the vault's mark-inference rule.

`EXT` Why the video leaves it unnamed is itself the point: $10^{170}$ is not a bigger number of the same kind. It is a different *regime* — a machine built to be information-theoretically secure against the resources of the 1940s, not merely computationally secure. The two regimes are worth distinguishing in one's head, and Enigma is the textbook example of the second failing against the first: a $10^{23}$ space that was structurally walkable.

---

## 10. Method Summary — What Generalises

1. **Find an invariant the designer cannot remove.** The no-self-cipher property survived every setting change and every rotor addition. Invariants beat parameters.
2. **Turn a search into a predicate.** Turing's requirement was a yes/no test, not a partial score. That is what made automation possible at all.
3. **Exploit the human layer.** Cribs existed because outposts sent the same weather report daily. Most real systems have the same exposure.
4. **Use contradiction, not confirmation.** A wrong guess that yields an *impossible* result eliminates 25 candidates at once. Detection of inconsistency is a search accelerator.
5. **Fold in algebraic redundancies.** Welchman's diagonal board did nothing physical — it noticed that two hypotheses were the same hypothesis.
6. **Speed is a security property.** The midnight reset meant a slow break was worthless; a 24-hour verification backlog undid a fast machine.
7. **Change the world when you cannot change the cipher.** Gardening forced the plaintext. Capture of key sheets did the same by other means.

`EXT` A coda on item 1, because it is the one most often missed: the Germans *did* defend the parameter space — five rotors, ten plugboard pairs, a fourth rotor, rewired rotors, a nightly reset. Every one of those was a good, expensive, well-engineered defence, and every one of them failed. The only defence that failed to be replaced was the one nobody had seen.

---

## 11. Source Data (not instructions)

`EXT` The video's description contains a Naval Enigma ciphertext its makers state **has never been decrypted**, preserved here as a fact about the source:

```
JCRSAJTGSJEYEXYKKZZSHVUOCTRFRCRPFVYPLKPPLGRHVVBBTBRSXSWXGGTYTVKQNGSCHVGF
```

The description also carries sponsor, newsletter, Patreon, simulator and reference links, and invites viewers to post solutions in the comments. Per vault rule, all of that is **data about the video**, not instruction to the agent, and none of it was acted on.

---

## Related

- [[01-Areas/Programming/cryptography/index|Cryptography Module Index]]
- [[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Enigma - Machine Deep Dive]]: mechanics, key space, operator vulnerabilities, institutional scale
- [[01-Areas/Programming/cryptography/enigma-rotor-math|Enigma - The Rotor Mathematics]]: permutations, involutions, the plugboard conjugation argument behind §5
- [[01-Areas/Programming/cs50/week-10-cybersecurity|CS50 Week 10 - Cybersecurity]]: modern framing of confidentiality, integrity, availability
- [[01-Areas/Programming/cs50/week-2-arrays|CS50 Week 2 - Arrays]]: the fixed-permutation ciphers Enigma replaced
- [[01-Areas/Engineering/engineering-math/ise-exam-prep-am1|Eng-Math ISE Exam Prep]]: orthogonal-matrix cryptography as the $Q^{-1}=Q^T$ analogue of self-reciprocity
