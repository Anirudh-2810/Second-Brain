---
date: 2026-09-28
description: "Cryptography module hub - cipher history, the polyalphabetic breakthrough, and a full worked study of the Enigma machine: mechanics, permutation theory, and the Turing/Welchman codebreaking attack."
tags: [programming, cryptography, ciphers, index, module-hub, enigma, permutation-theory, codebreaking]
last_updated: "2026-09-28"
type: [module-index]
relations:
  relates_to: "[[01-Areas/Programming/cryptography/enigma-machine-deep-dive|Enigma - Machine Deep Dive]]"
  relates_to: "[[01-Areas/Programming/cryptography/enigma-rotor-math|Enigma - The Rotor Mathematics]]"
  relates_to: "[[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking|Enigma - The Bombe & Codebreaking]]"
---

## For future agent
**MODULE SCOPE**: classical/modern cryptography, ciphers, cryptanalysis, and cipher history → scan `wiki/01-Areas/Programming/cryptography/**`. Current contents: one deep study (Enigma), split three ways because the material genuinely has three distinct jobs.

Placement rule: a **cipher's design and mathematics** belongs here. A **hash function** is better placed at [[01-Areas/Programming/cs50/week-10-cybersecurity|CS50 week 10]] where the vault already has the integrity/availability framing. **ML model internals** go to `wiki/01-Areas/AI-Data/`, never here.

**Entry points by question:**

| Question | Page |
|----------|------|
| "how did Enigma work / why was it broken" | [[01-Areas/Programming/cryptography/enigma-machine-deep-dive\|Machine Deep Dive]] |
| "why is Enigma a permutation / is it linear" | [[01-Areas/Programming/cryptography/enigma-rotor-math\|The Rotor Mathematics]] |
| "how did the Bombe work / what is a crib" | [[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking\|The Bombe & Codebreaking]] |
| "Caesar / substitution / polyalphabetic basics" | [[01-Areas/Programming/cs50/week-2-arrays\|CS50 Week 2 §7]] |
| "hash functions, modern security model" | [[01-Areas/Programming/cs50/week-10-cybersecurity\|CS50 Week 10]] |

Staleness caveat: the mathematics is settled and will not change. What may age: institutional detail, museum attributions, and any `TBC`-marked item.

# Cryptography — Module Index

Ciphers, cryptanalysis, and the engineering of secrecy. Enter here for "how does encryption work" and "how has it been broken".

---

## 1. Pages

| Page | Covers |
|------|--------|
| [[01-Areas/Programming/cryptography/enigma-machine-deep-dive\|Enigma — Machine Deep Dive]] | Origins (Scherbius 1918, commercial not military), the signal path, the odometer, key-space arithmetic, self-reciprocity, key sheets, operator vulnerabilities (sillies, Herivel tip), the on-camera crack, Bletchley Park, consequences, Turing's later years |
| [[01-Areas/Programming/cryptography/enigma-rotor-math\|Enigma — The Rotor Mathematics]] | Rotor as a permutation of $S_{26}$, composition and the stack, involution/self-reciprocity, the no-self-cipher theorem, mixed-radix odometer arithmetic, key-space products (re-derived), plugboard-as-conjugation, linear-algebra bridge to orthogonal-matrix crypto |
| [[01-Areas/Programming/cryptography/enigma-bombe-and-codebreaking\|Enigma — The Bombe & Codebreaking]] | Cribs and the cribbing room, locating a crib by no-self-cipher scan, Turing's loop/menu test, plugboard isolation by contradiction, dragon breaks, the Bombe machine, its too-slow flaw, Welchman's diagonal board, Naval Enigma, gardening, D-Day |

**Source:** Veritasium, *"The Insane Real Engineering of the Nazi Enigma Machine"*, 47:41 — [youtube.com/watch?v=JsBZOcqZerk](https://www.youtube.com/watch?v=JsBZOcqZerk). Raw transcript + metadata in `raw-sources/` (gitignored, local only).

---

## 2. Reading Order

**Narrative first:** Deep Dive (1) → Bombe & Codebreaking (2) → Rotor Mathematics (3)

**Technical first:** Rotor Mathematics (§2–4) → Bombe (§3–5) → Deep Dive for context

**Exam-relevant first:** Rotor Mathematics §4 (no-self-cipher), §7 (conjugation), §8 (linear-algebra bridge) — the derivable parts

---

## 3. The One-Paragraph Summary

A **substitution cipher** maps letters by a fixed rule, so a plaintext letter always yields the same ciphertext letter and frequency analysis breaks it. A **polyalphabetic cipher** changes the rule per character, defeating that analysis. Enigma was a *mechanical* polyalphabetic cipher: three scrambled rotors (permutations of the alphabet) stepped like a base-26 odometer on every keystroke, with a reflector forcing self-reciprocity, and a plugboard conjugating the whole thing. That bought a key space above $10^{23}$. It still fell, for two independent reasons. First, the operators were lazy: predictable "random" indicators (girlfriends' names, home cities) and minimal rotor shuffling leaked the ring settings statistically. Second, and fatally, the machine had a **structural invariant** no setting could change — *no letter ever encrypts to itself* — which let a codebreaker locate a guessed plaintext inside the real ciphertext, after which Turing's Bombe converted "does this setting close these loops?" into an electrical yes/no test, and Welchman's diagonal board cut the false positives by 90%. The deeper lesson, stated plainly in the source: *the weakest part of any encryption device is not the device, it is the human operating it.*

---

## 4. Cross-Domain Bridges

- **Engineering-math:** [[01-Areas/Engineering/engineering-math/ise-exam-prep-am1|ISE exam prep Q2.2]] works an orthogonal-matrix cipher ($Q^{-1}=Q^T$, the self-reciprocity analogue) · [[01-Areas/Engineering/engineering-math/module-1-matrices|Module 1 - Matrices]] (composition/invertibility of linear maps) · [[01-Areas/Engineering/engineering-math/module-5-complex-numbers|Module 5 - Complex Numbers]] (roots of unity → NTT in crypto)
- **CS50:** [[01-Areas/Programming/cs50/week-2-arrays|Week 2 §7]] (Caesar + substitution, the fixed-rule baseline) · [[01-Areas/Programming/cs50/week-10-cybersecurity|Week 10]] (hash functions, modern security model)
- **Programming meta:** [[01-Areas/Programming/math-for-programming|Why Programming Needs Math]] (why linear algebra is non-negotiable in crypto) · [[01-Areas/Programming/yt info|YT source metadata]]
- **History/ethics:** the Bletchley Park material intersects with computing history and with questions about state secrecy — no page in the vault covers this yet

---

## 5. Self-Checks

When using these pages, verify:
- Claims tagged `(V)` are traceable to the transcript in `raw-sources/`
- Claims tagged `(EXT)` are NOT attributed to the video
- `(TBC)` items are unresolved (the Lorenz machine identification; the 1943 U-boat phrasing; the $26^2$ ring count; the Churchill quotation)
- Key-space figures re-derive from their components (§5 of Rotor Mathematics) — they should, every time
