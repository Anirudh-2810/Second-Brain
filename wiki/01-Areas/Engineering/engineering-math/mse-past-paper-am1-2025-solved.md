---
course_code: "316U06C101"
course_name: "Applied Mathematics-I"
unit: "MSE (full paper)"
tags: [btech, engineering-math, matrices, rank, jacobian, partial-differentiation, gauss-seidel, consistency, euler-theorem, exam-prep, mse, past-paper]
last_updated: "2026-10-21"
confidence: high
date: "2026-10-21"
description: "Solved walkthrough of the Aug-Nov 2025 Applied Maths-I MSE paper (midsems-pyp.pdf): normal form + rank, Jacobian, matrix encryption, Laplacian proof, Gauss-Seidel, consistency-in-lambda, Euler's theorem proof - each Q explained in easy language with worked solutions, similar problems, difficulty and yield ratings."
---

## For future agent
Full walkthrough of the actual **Augâ€“Nov 2025 AM-I MSE paper** (source: [[raw-sources/midsems-pyp.pdf|midsems-pyp.pdf]], 30 marks, 1 hr 15 min). Every question explained in plain language, solved step-by-step, with the sibling problems that always appear next to it. Deep theory lives in [[module-1-matrices]], [[module-2-partial-differentiation]], [[module-3-homogeneous-functions]]. As of 2026-10-21.

# AM-I MSE 2025 â€” Solved Paper Walkthrough

## Pattern & verdict

| Q | Type | Marks | Difficulty | Yield |
|---|------|-------|-----------|-------|
| Q1 | Normal form â†’ rank | 6 | Easy (pure algorithm) | â­â­â­ bankable |
| Q2 | Any 2 of 3 (Jacobian / cipher / Laplacian) | 6+6 | EasyÂ·MedÂ·Easy | â­â­â­ pick 1&3 |
| Q3 | Any 2 of 3 (Gauss-Seidel / Î»-consistency / Euler) | 6+6 | Med Â· Med Â· Med | â­â­ pick 1&2 |

**Verdict: easiest paper of the four.** Q1 + Q2.1 + Q2.3 + Q3.1 + Q3.2 is a pure-procedure 24/30. Drill, don't derive.

---

## Q1 (6M) â€” Reduce to Normal Form, find rank

$$A=\begin{bmatrix}2&1&4\\3&2&2\\7&4&10\\8&5&8\end{bmatrix}$$

**The idea (easy words):** "Normal form" means grinding the matrix with elementary **row** operations (swap, multiply a row by a non-zero number, add a multiple of another row) until it looks like

$$\begin{bmatrix}I_r & 0\\0 & 0\end{bmatrix}$$

where **r = the rank** = number of non-zero rows/cols left. You never need to "see" anything clever â€” just keep clearing below the leading entry.

**Worked solution.** Eliminate column 1 (3/2, 7/2, 4 = multipliers of R1):

$$R_2\to R_2-\tfrac32R_1:\ [0,\ \tfrac12,\ -4]\qquad R_3\to R_3-\tfrac72R_1:\ [0,\ \tfrac12,\ -4]\qquad R_4\to R_4-4R_1:\ [0,\ 1,\ -8]$$

Clear column 2: $R_3\to R_3-R_2:\ [0,0,0]$; $R_4\to R_4-2R_2:\ [0,0,0]$.

Two non-zero rows, two non-zero columns â†’ **rank = 2**, normal form:

$$\begin{bmatrix}1&0\\0&1\\0&0\\0&0\end{bmatrix}$$

**Trap:** the matrix is 4Ã—3 â€” the normal form is NOT a square identity. Write $[I_r\ 0;\ 0\ 0]$ sized to fit (I is 2Ã—2, zero block 2Ã—1 under it).

**Similar problems:** any "reduce to echelon/normal form + rank" â€” 2026-09-22 quiz systems â†’ [[quiz-2026-09-22-systems-consistency-rank]]; theory + 5 more matrices â†’ [[module-1-matrices]].

---

## Q2.1 (6M) â€” Jacobian âˆ‚(u,v,w)/âˆ‚(x,y,z)

u = x(1âˆ’y), v = xy(1âˆ’z), w = xyz.

**The idea:** the Jacobian is literally a determinant whose rows are "how u, v, w change when x, y, z change". Differentiate each function by each variable, arrange in a 3Ã—3 grid, take the determinant. Nothing more.

$$J=\begin{vmatrix}1-y&-x&0\\ y(1-z)&x(1-z)&-xy\\ yz&xz&xy\end{vmatrix}$$

**Worked solution.** Expand along row 1:

- Minorâ‚: $x(1-z)\cdot xy-(-xy)(xz)=x^2y(1-z)+x^2yz=x^2y$
- Minorâ‚‚: $y(1-z)\cdot xy-(-xy)\cdot yz=xy^2(1-z)+xy^2z=xy^2$

$$J=(1-y)(x^2y)+x(xy^2)=x^2y\ \boxed{}$$

The cancellations are the examiner's gift â€” if your answer has yÂ² left, re-check row 1 expansion signs.

**Similar problems:** every "u,v in terms of x,y find Jacobian" + the standard helpers: u = xÂ²y, v = x sin y type 2Ã—2; the "u=x+y, v=xy" warm-up; chain "show J(A,B)=J(A,C)Â·J(C,B)". â†’ [[module-2-partial-differentiation]].

---

## Q2.2 (6M) â€” Encrypt/decrypt "I AM FINE" with orthogonal Q

$$Q=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$

**The idea:** Hill cipher. Letters â†’ numbers (A=0 â€¦ Z=25 (one common convention; some courses use A=1 â€” check your class notes (TBC))), group the message in pairs, multiply each pair-vector by Q to encrypt. Because Q is **orthogonal**, $Q^{-1}=Q^T$, so decryption = multiply by $Q^T=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.

**Worked solution.** QÂ·(a, b)áµ€ = (âˆ’b, a)áµ€ â€” it's just a quarter-turn rotation, mod 26:

| pair | numbers | QÂ·p (mod 26) | cipher |
|------|---------|--------------|--------|
| I A | 8, 0 | (0, 8) | A I |
| M F | 12, 5 | (21, 12) | V M |
| I N | 8, 13 | (13, 8) | N I |
| E (padâ†’E X) | 4, 23 | (3, 4) | D E |

Ciphertext: **AI VM NI DE**. Decrypt the same way with $Q^T$: Qáµ€Â·(0,8)áµ€ = (8,0) = "IA" â€” back to the original. Spaces are dropped before encoding, restored after.

**Trap to memorise:** the whole point of "orthogonal matrix" in this question = free $Q^{-1}=Q^T$. If they ever give a non-orthogonal Q, you must find the inverse by adjoint/cofactor.

**Similar problems:** same cipher with Q = [[1,1],[0,1]], or 3Ã—3 cipher on "ATTACK", or "show det(Q)=Â±1 for orthogonal Q". â†’ [[module-1-matrices]].

---

## Q2.3 (6M) â€” Laplacian proof

u = xÂ²y + yÂ²z + zÂ²x. Prove âˆ‚Â²u/âˆ‚xÂ² + âˆ‚Â²u/âˆ‚yÂ² + âˆ‚Â²u/âˆ‚zÂ² = 2(x+y+z).

**Worked solution.** Second partials:

- âˆ‚Â²u/âˆ‚xÂ² = âˆ‚/âˆ‚x(2xy + zÂ²) = **2y**
- âˆ‚Â²u/âˆ‚yÂ² = âˆ‚/âˆ‚y(xÂ² + 2yz) = **2z**
- âˆ‚Â²u/âˆ‚zÂ² = âˆ‚/âˆ‚z(yÂ² + 2zx) = **2x**

Sum = 2y + 2z + 2x = **2(x+y+z)** âˆŽ

Three lines. This should be everyone's first pick in Q2 â€” zero tricks.

**Similar problems:** u = xÂ²+yÂ²+zÂ², u = e^(x+y+z), sin(mixed-terms) â€” the pattern "second-derivative soup that telescopes into a simple fact" is the whole genre (see Q3.3 for the fancy version). â†’ [[module-2-partial-differentiation]].

---

## Q3.1 (6M) â€” Gaussâ€“Seidel, 3 iterations

$$15x+y+z=17,\qquad x+15y+z=18,\qquad x+2y+15z=18$$

**The idea:** rearrange each equation so its "big" coefficient is 1, then update **one variable at a time, always using the freshest values available**. (That's the difference from Jacobi: Gaussâ€“Seidel uses the new x immediately in the y-equation.) The system is nicely **diagonally dominant** (15 is the biggest in each row) â€” that's why it converges fast, and why the examiner chose it.

**Rearranged:** x = (17âˆ’yâˆ’z)/15 Â· y = (18âˆ’xâˆ’z)/15 Â· z = (18âˆ’xâˆ’y)/15. Start x=y=z=0.

| Iter | x | y | z |
|------|------|------|------|
| 1 | 1.1333 | 1.1244 | 1.0495 |
| 2 | 0.9884 | 1.0641 | 1.0632 |
| 3 | 0.9915 | 1.0630 | 1.0630 |

**x â‰ˆ 0.99, y â‰ˆ 1.06, z â‰ˆ 1.06.** After iter 3 values barely move â€” converged.

**Write-up tip:** show every substitution raw (e.g. "y = (18 âˆ’ 1.1333 âˆ’ 1.0495)/15 = 1.1244") â€” the marks are in the substitutions, not the final answer.

**Similar problems:** 10x+2y+z=7 type sets; the 1-iteration vs 2-iteration variant; "why must the system be diagonally dominant" theory Q. â†’ [[mse-revision-am1]] Â§numerical-methods.

---

## Q3.2 (6M) â€” For which Î» is the system consistent?

$$x+2y+z=3,\qquad x+y+z=\lambda,\qquad 3x+y+3z=\lambda^2$$

**The idea:** "consistent" = system has (at least one) solution = rows of A have the same rank as rows of the augmented matrix. Practically: row-reduce and make the contradiction row vanish.

**Worked solution.** Augmented matrix, eliminate:

$$\begin{bmatrix}1&2&1&3\\1&1&1&\lambda\\3&1&3&\lambda^2\end{bmatrix}\xrightarrow{R_2-R_1,\ R_3-3R_1}\begin{bmatrix}1&2&1&3\\0&-1&0&\lambda-3\\0&-5&0&\lambda^2-9\end{bmatrix}\xrightarrow{R_3-5R_2}\begin{bmatrix}1&2&1&3\\0&-1&0&\lambda-3\\0&0&0&\lambda^2-5\lambda+6\end{bmatrix}$$

Consistent âŸº last row â‰  0=non-zero âŸº $\lambda^2-5\lambda+6=0\Rightarrow(\lambda-2)(\lambda-3)=0$: **Î» = 2 or 3.**

- **Î» = 3:** âˆ’y = 0 â†’ y = 0; both remaining equations give x + z = 3. **Infinite solutions:** x = 3âˆ’t, y = 0, z = t.
- **Î» = 2:** âˆ’y = âˆ’1 â†’ y = 1; equations both give x + z = 1. **Infinite solutions:** x = 1âˆ’t, y = 1, z = t.

Any other Î» â‡’ 0 = non-zero â‡’ inconsistent.

**Similar problems:** the exact same skeleton with RHS (k, kÂ², kÂ³) or (3, Î», Î»Â³); "discuss ranks for all Î» incl. no-solution/unique/infinite" variants. â†’ [[module-1-matrices]] Â§consistency Â· [[quiz-2026-09-22-systems-consistency-rank]] is literally this genre.

---

## Q3.3 (6M) â€” Euler's theorem proof

u = xÂ³ sinâ»Â¹(y/x) â€” the scan is hard to read; the classic companion (and the one that makes both identities true) is the homogeneous u = xÂ³ sinâ»Â¹(y/x) (inferred from the paper's âˆ‚u/âˆ‚x + âˆ‚u/âˆ‚y = 3u structure; (TBC) against the original print).

**The idea:** a function is **homogeneous of degree n** if scaling (x,y) by t scales u by tâ¿. For such u, **Euler's theorem** says xÂ·âˆ‚u/âˆ‚x + yÂ·âˆ‚u/âˆ‚y = nÂ·u. Then the "second-derivative identity" xÂ²u_xx + 2xyÂ·u_xy + yÂ²u_yy = n(nâˆ’1)u follows automatically.

**Worked solution.** Test homogeneity: replace xâ†’tx, yâ†’ty inside sinâ»Â¹(y/x): the ratio is unchanged, and the prefactor becomes tÂ³xÂ³. So u(tx,ty) = tÂ³Â·u â‡’ **degree n = 3**.

i) By Euler: xÂ·u_x + yÂ·u_y = **3u** âˆŽ (state the theorem by name in the exam â€” that's half the marks.)

ii) Differentiate Euler's equation w.r.t. x (and y), multiply and recombine (standard textbook step, no new ideas): xÂ²u_xx + 2xyÂ·u_xy + yÂ²u_yy = n(nâˆ’1)Â·u = 3Â·2Â·u = **6u** âˆŽ

**Similar problems:** u = tanâ»Â¹(y/x) â†’ degree 0; u = xÂ·f(y/x) construction checks; the "prove xy(u_xx âˆ’ u_yy) = ..." cousins all reuse the same two lines. â†’ [[module-3-homogeneous-functions]]. Skip on exam day unless Q3.1/Q3.2 feel shaky â€” this is the highest-effort 6M on the paper.

---

## Exam-day strategy for THIS paper

1. Open with Q1 (guaranteed 6M, ~8 minutes).
2. Q2: take **2.3 then 2.1**; keep 2.2 as backup.
3. Q3: take **3.1 then 3.2** (3.2's row-reduction is the same skill as Q1).
4. Total honest effort needed: ~35 min for 24M. Rest of time â†’ polish 2.2 or attempt 3.3.

**One-page formula anchors:** [[formula-sheet-am]] Â· revision pack: [[mse-revision-am1]] Â· flashcards: [[mse-flashcards-am1]] Â· recall test: [[mse-recall-test-am1]] Â· chem twin: [[mse-past-paper-chem-2025-solved]].

**Relations:** relates_to [[module-1-matrices]] Â· [[module-2-partial-differentiation]] Â· [[module-3-homogeneous-functions]] Â· source_of this: [[raw-sources/midsems-pyp.pdf|midsems-pyp.pdf]].


