---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 10
topic: "Cybersecurity on the Internet & the Final Project"
tags: [programming, computer-science, cs50, harvard, cybersecurity, encryption, phishing, malware, passwords, passkeys, final-project]
last_updated: "2026-08-11"
---

# Week 10 — Cybersecurity (and the Final Project)

> **Goal of the week:** put a security lens over *everything* the course built — from Week 4's buffer overflows to Week 7's injection to Week 9's sessions — then synthesize the whole course into **your own Final Project**.
> This is the *least code*, *most judgement* week of CS50.

---

## 1. What "Security" Means — The CIA Triad

| Goal | Meaning | Course example |
|---|---|---|
| **Confidentiality** | only the intended people read data | encryption; password hashing |
| **Integrity** | data isn't tampered with | signed messages; hashes; HTTPS |
| **Availability** | systems stay up when attacked | DDoS mitigations; load balancing |

Master question to ask about any attack: **which of the three does it break?**

---

## 2. The Threat Landscape (know the players)

- **Phishing** — deceptive messages that con a human into handing over credentials. *Soften the target, click the link.* Counter = skepticism + verifying the sender.
- **Password attacks** — brute force (try every guess) vs **credential stuffing** (reuse of leaked passwords across sites). Counter = **long, unique passwords + a password manager**.
- **Malware** — viruses, worms, trojans, ransomware. One click can own a machine (Week 4 said "validate input"; *the human is the largest attack surface*).
- **DDoS** — flood a server with requests until *availability* dies.

---

## 3. Passwords Done Right — Hashing, Not Encrypting

- **Never store plaintext.** Store a **hash** (one-way). On login, hash the user's guess and compare hashes, not passwords.
- Hash functions: fast to compute, infeasible to reverse, avalanche in output — the *same* hash idea as Week 5's hash table, but cryptographic.
- **Add a salt** (random per-user data) before hashing → defeats rainbow-table lookups and identical-password spraying.
- **Password managers** solve the tension: one master password, a unique strong password per service.

---

## 4. Encryption — Secrecy That Works Both Ways

| Scheme | Key usage | Use | Analogy |
|---|---|---|---|
| **Symmetric** | one shared key encrypts *and* decrypts | speed, bulk data | same key for the lock and the unlock |
| **Asymmetric** | a public key encrypts, a private key decrypts | TLS/HTTPS, signatures | padlock you hand out; only you keep the key |

- **HTTPS/TLS** wraps HTTP in encryption — "the tiny lock in the address bar," integrity *and* confidentiality.
- **Passkeys** (public-key) remove the shared-secret problem entirely: your device signs, the server verifies with the public key; nothing reusable leaks on a server breach.

---

## 5. The Course's Security Post-Mortem (paste the dots together)

| Week | Technique learned | Security meaning |
|---|---|---|
| 2 | validate keys / inputs | untrusted input is the root of most exploits |
| 4 | buffer overflows, `valgrind`, `strcpy` | writing past memory = hijack primitives |
| 5 | hash tables | hashing (with salt) *is* password storage |
| 7 | parameterized SQL / injection | never splice user text into a command |
| 9 | sessions, cookies, POST/redirect | auth state must be server-side and fresh |

> **The one-liner:** *Trust nothing from the outside; verify at every boundary — input, memory, SQL, browsers.*

---

## 6. The Final Project — Where the Course Points

- **Your own idea**, a week or two of work, any stack (Flask, Python, JS, C, Scratch — all on the table).
- **Health & independence first**, then: scope small, document, share. The department wants *something you chose* — not a copy of a PSet.
- **Checklists the course teaches for any project:**
  1. Plan (Week 0's pseudocode/design-first habit).
  2. Build in small, runnable increments (Week 2's "run often").
  3. Validate input + secure the plumbing (Weeks 2/7/10).
  4. Ship visibly and iterate (the [[winning-in-tech-art-of-winning]] loop).

> **The Exit Message:** CS50 is *not* about C or Python — it's about *problem-solving habits*: represent, abstract, decompose, and prove things work. Everything later (AI/ML, quant, systems) is downstream of the mental tools this week you now own.

---

## 7. Vocabulary to Master

- CIA (confidentiality/integrity/availability) · phishing · brute force · credential stuffing · malware/ransomware · DDoS · hash (one-way) · salt · rainbow table · symmetric vs asymmetric encryption · TLS/HTTPS · passkey · 2FA · security checklist.

## 8. Cross-Links

- [[cs50/week-7-sql]] — injection defenses, revisited with fear.
- [[cs50/week-4-memory]] — the pointer/overflow roots.
- [[cs50/week-5-data-structures]] — hash tables become hashing.
- [[cs50/week-9-flask]] — sessions & auth the security chapter defends.
- [[cs50/problem-sets]] — the Final Project is the real PSet 10.
- [[winning-in-tech-art-of-winning]] — ship it, show it, iterate.