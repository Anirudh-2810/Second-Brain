---
course_code: "216U06C101"
course_name: "Applied Mathematics-I"
unit: "ISE / MSE Exam Prep"
tags: [engineering-math, btech, exam-prep, ise, matrices, partial-differentiation, homogeneous-functions]
last_updated: "2026-09-09"
description: "ISE Oct 2025 paper deconstructed (30 marks, 75 min): normal form, Jacobian, orthogonal crypto, Gauss-Seidel, lambda-consistency, Euler theorem — with worked solutions and traps."
---

## For future agent

This note distils the single real exam artefact in the Sem-1 dump (`ISE Oct 2025 - Solution (7 oct).pdf`, KJSCE Applied Mathematics-I 216U06C101) into a reusable paper pattern plus fully worked solutions. Pair it with [[module-1-matrices]] (Q1, Q3.1–3.2), [[module-2-partial-differentiation]] (Q2.1, Q2.3), and [[module-3-homogeneous-functions]] (Q3.3); several solution-scheme boxes were blank, so those solutions are reconstructed here (confidence: high — standard methods).

# ISE / MSE Exam Prep — Applied Mathematics-I (KJSCE SVU)

**Paper facts (as of 2026-09-09):** In-Semester Exam, 30 marks, 1 hr 15 min, FY BTech Sem-I. Pattern: Q1 compulsory (6M) + Q2/Q3 "attempt any TWO of three" (6M each) = 30M. Modules examined: Matrices (M1), Partial Differentiation incl. Jacobian (M2), Homogeneous functions (M3).

## Q1 (compulsory, 6M) — Normal form + rank

Reduce $A = \begin{bmatrix} 2 & 1 & 4 & 3 \\ 2 & 2 & 7 & 4 \\ 10 & 8 & 5 & 8 \end{bmatrix}$ to normal form, hence rank. Method: [[module-1-matrices]] §2.2.1 (row AND column ops → $\begin{bmatrix}I_r & 0 \\ 0 & 0\end{bmatrix}$, rank $= r$). Trap: students use row ops only and stall — column ops are legal *only* for this rank method.

## Q2.1 (6M) — 3-variable Jacobian

If $u = x(1-y)$, $v = xy(1-z)$, $w = xyz$, find $\dfrac{\partial(u,v,w)}{\partial(x,y,z)}$. Direct $3 \times 3$ determinant of first partials ([[module-2-partial-differentiation]] §2.5). Note the telescoping structure ($w$ absorbs $xy$) — expand along the sparsest row. Trap: confusing this with the chain-rule Jacobian; here it is a straight determinant.

## Q2.2 (6M) — Orthogonal-matrix cryptography (worked)

Encrypt/decrypt "I AM FINE" with $Q = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (1-based A=1…Z=26, space = 0). Blocks: [9,0],[1,13],[0,6],[9,14],[5,0] → $M$; cipher $C = QM = \begin{pmatrix} 0 & -13 & -6 & -14 & 0 \\ 9 & 1 & 0 & 9 & 5 \end{pmatrix}$, transmitted linearly. Decrypt with $Q^{-1} = Q^T = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$: $M = Q^TC$ recovers "I AM FINE" ✓. Why it works: orthogonal $Q^TQ = I$ ([[module-1-matrices]] §1.1). Trap: $Q^{-1} = Q^T$ holds *only because* $Q$ is orthogonal — state it to earn the method mark.

## Q2.3 (6M) — Laplacian-type identity

If $u = x^2y + y^2z + z^2x$, prove $u_{xx} + u_{yy} + u_{zz} = 2(x+y+z)$. Direct: $u_{xx} = 2y$, $u_{yy} = 2z$, $u_{zz} = 2x$; add. Two-line question — don't overthink; trap is differentiating the wrong variable (each term has exactly one squared variable).

## Q3.1 (6M) — Gauss-Seidel, three iterations

$15x+y+z = 17$, $2x+15y+z = 18$, $x+2y+15z = 18$. Already diagonally dominant. Iterate per [[module-1-matrices]] §6 (Seidel = reuse latest immediately), start $(0,0,0)$. Converges toward $(1,1,1)$ — verify by substitution as your check line.

## Q3.2 (6M) — Parametric consistency (fully worked in solution scheme)

$x+2y+z = 3$, $x+y+z = \lambda$, $3x+y+3z = \lambda^2$. $[A|B] \xrightarrow{R_2-R_1,\,R_3-3R_1,\,R_3-5R_2} \begin{bmatrix} 1 & 2 & 1 & | & 3 \\ 0 & -1 & 0 & | & \lambda-3 \\ 0 & 0 & 0 & | & \lambda^2-5\lambda+6 \end{bmatrix}$. Consistency needs $\lambda^2-5\lambda+6 = 0$, i.e. $\boxed{\lambda = 2 \text{ or } 3}$. For $\lambda = 2$: $y = 1$, $x+z = 1$ → $(1-k, 1, k)$. For $\lambda = 3$: $y = 0$, $x+z = 3$ → $(3-c, 0, c)$. Infinitely many solutions in both cases (rank $2 < 3$). Trap: candidates often stop at $\lambda$ values without solving — the "find and solve" wording demands both.

## Q3.3 (6M) — Euler homogeneous, two parts

$u = x^3\sin^{-1}\!\left(\frac{\sqrt{y}+\sqrt{x}}{\sqrt{y}-\sqrt{x}}\right)$-type: (i) $xu_x + yu_y = 3u$ (degree 3 — the $\sin^{-1}$ factor is degree 0 in $(x,y)$), (ii) $x^2u_{xx} + 2xyu_{xy} + y^2u_{yy} = 6u = 3(3-1)u$ (second-order Euler; [[module-3-homogeneous-functions]] §2.3). Trap: misreading the degree — check $f(tx,ty)$ scaling of the *whole* $u$, not the inner ratio.

## Question-bank map (dump practice pools)

- `Matrices/Questions/` (6 files: rank banks, system + LI/LD set, numerical set) and `Complex/Practice Problems/` (4 files) + `Partial Differentiation/Practice Problems/` (4 files: 2.1 first/higher-order, 2.2 composite, 2.3 maxima-minima, 2.4 Jacobian) mirror the Q2/Q3 option structure — drill one file per ISE option.
- `Differential Equations/Practice Problems/` (first-order set, higher-order set, mixed set) + `Homogenous Functions/Module 3 Homogeneous Functions Questions.pdf` (scanned, 0 extractable chars — read in Obsidian) target the ESE end.
- Textbooks in dump root (Kreyszig 9th ed., B.S. Grewal — both image-scanned, no extractable text) are reference-only; syllabus order follows the KJSCE module PDFs, not the books.

## Related

[[module-1-matrices]] · [[module-2-partial-differentiation]] · [[module-3-homogeneous-functions]] · [[formula-sheet-am]] · [[prerequisite-toolkit]]
