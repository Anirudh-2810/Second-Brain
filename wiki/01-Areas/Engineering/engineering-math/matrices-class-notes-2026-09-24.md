---
date: 2026-09-24
description: "Class-taught matrices companion (DocScanner 24 Sept 2026, 5 pp): Hermitian/Skew-Hermitian split with exam method, orthogonal/unitary quick defs, echelon rank, homogeneous and augmented consistency, linear dependence, Gauss-Jacobi first iteration."
tags: [btech, engineering-math, matrices, hermitian, rank, homogeneous-system, gauss-jacobi, class-notes]
module: "engineering-math"
topic: "Matrices class notes — Hermitian split, rank/consistency, Gauss-Jacobi"
last_updated: "2026-09-24"
confidence: high
source: "[[raw-sources/DocScanner 24 Sept 2026 2-46 pm]]"
prerequisites: ["Determinants", "Complex conjugates"]
---

## For future agent

Verbatim-class distillation of the 5-page handwritten scan `[[raw-sources/DocScanner 24 Sept 2026 2-46 pm]]` (matrices, 24 Sept 2026). Full theory (proofs, Cayley-Hamilton, eigen) already lives in [[module-1-matrices]] — do NOT duplicate it here. This note keeps only the class-taught layer: the Hermitian/Skew-Hermitian decomposition table with the exam answer method, one echelon-rank reduction, the homogeneous-solution rule, one augmented-matrix consistency check, and the Gauss-Jacobi opening iteration (the sole topic with no home in [[module-1-matrices]]). Handwriting-ambiguous digits are marked (TBC).

# Matrices Class Notes (24 Sept 2026)

> Source scan: `[[raw-sources/DocScanner 24 Sept 2026 2-46 pm]]` (5 pp, handwritten) · Theory home: [[module-1-matrices]] · Quiz drill: [[quiz-2026-09-22-systems-consistency-rank]]

## 1. Hermitian matrix ($A^\theta = A$)

$A^\theta = [(\bar A)]^T$ (conjugate-transpose). Conditions: (i) $A^\theta = A$, (ii) $a_{ij} = \bar a_{ji}$.

- **Diagonal elements are real** — imaginary part is zero (class proof sketch: $a_{ii} = \bar a_{ii} \Rightarrow 2i\beta = 0 \Rightarrow \beta = 0$).

## 2. Skew-Hermitian matrix ($A^\theta = -A$)

Conditions: (i) $A^\theta = -A$, (ii) $a_{ij} = -\bar a_{ji}$.

- **Diagonal elements are purely imaginary** — real part is zero.

## 3. Splitting theorem + exam method

Every square matrix splits uniquely:

| Matrix $A$ | Expressed as | Unique representation |
|---|---|---|
| Square | Hermitian + Skew-Hermitian | $A = \tfrac{1}{2}(A + A^\theta) + \tfrac{1}{2}(A - A^\theta)$ |
| Square $A = P + iQ$, $P,Q$ Hermitian | $P + iQ$ | same split as above |
| Hermitian $A = P + iQ$ | $P$ real symmetric, $Q$ real skew-symmetric | $A = \tfrac{1}{2}(A + \bar A) + i\left[\tfrac{1}{2i}(A - \bar A)\right]$ |
| Skew-Hermitian $A = P + iQ$ | $P$ real skew-symmetric, $Q$ real symmetric | $A = \tfrac{1}{2}(A + \bar A) + i\left[\tfrac{1}{2i}(A - \bar A)\right]$ |

**Method of writing the answer in exam** (as taught): Statement $\to$ set $A = P + Q$ $\to$ compute $P = \tfrac{1}{2}(A + A^\theta)$, $Q = \tfrac{1}{2}(A - A^\theta)$ $\to$ find $A^\theta$ first $\to$ evaluate.

## 4. Orthogonal vs Unitary (quick defs)

- **Orthogonal:** $A A^T = I$ and $A^T A = I$. Then $|A|^2 = 1 \Rightarrow |A| = \pm 1$; $A^{-1} = A^T$.
- **Unitary:** $A A^\theta = I$ and $A^\theta A = I$. Then $|A| = 1$ (TBC — properly $|\det A| = 1$); $A^{-1} = A^\theta$.
- Full table + proofs: [[module-1-matrices#11-conceptual-architecture--ascii-flowcharts]].

## 5. Echelon form $\to$ rank (class example)

Row transformations only $\to$ upper-triangular (echelon) form. **Rank = number of non-zero rows.**

Class reduction (as taught, result): $3 \times 3$ matrix $\xrightarrow{R_2 \to R_2 + 2R_1}$ $\xrightarrow{R_3 \to R_3 - 2R_2}$ (TBC — handwriting ambiguous) $\to \begin{bmatrix} 1 & -2 & 3 \\ 0 & 0 & 5 \\ 0 & 0 & 0 \end{bmatrix}$ $\Rightarrow$ **rank $= 2$**.

## 6. Homogeneous system $AX = 0$

Always has at least the **zero solution** ($x_1 = x_2 = \dots = x_n = 0$).

1. Reduce $A$ to echelon form, find rank $r$ ($n$ = unknowns).
2. If $r = n$ (square: $|A| \neq 0$) → **only zero solution**.
3. If $r < n$ (square: $|A| = 0$) → **$(n - r)$ linearly independent solutions**.

## 7. Augmented matrix $[A \mid B]$ (class example)

$\rho(AB)$ = rank of the full $3 \times 4$ matrix; $\rho(A)$ = rank of the $3 \times 3$ coefficient block (cover the RHS column with a finger).

- $\rho(AB) = \rho(A)$ → **consistent**, solution exists (unique if $r = n$, else $n - r$ parameters).
- $\rho(AB) \neq \rho(A)$ → **inconsistent**, no solution.

Class example reduced to $\begin{bmatrix} 2 & 6 & 0 & -11 \\ 0 & -2 & 16 & -3 \\ 0 & 0 & 0 & -91 \end{bmatrix}$ (constants TBC) — bottom row $0 = -91$ $\Rightarrow$ $\rho(AB) = 3 \neq \rho(A) = 2$ $\Rightarrow$ **inconsistent**. Rouché–Capelli statement: [[module-1-matrices#13-system-of-linear-equations-decision-tree]].

## 8. Linear dependence / independence

$k_1x_1 + k_2x_2 + k_3x_3 = 0$ (as taught, one line): only-trivial-$k$ solution $\Rightarrow$ independent; non-trivial $k$ exist $\Rightarrow$ dependent. (TBC — class line only, see [[module-1-matrices#21-rank--definitions-and-fundamental-theorems]] for rank–nullity.)

## 9. Iterative methods — Gauss-Jacobi (NEW vs Module-1)

Start from a guessed (initial) solution, feed previous iterate into rearranged equations to get the next values. **Convergence condition (as taught): diagonal coefficients must dominate** (diagonally dominant system).

Class example (constants TBC):

$$\begin{bmatrix} 20 & 1 & -2 \\ 3 & 20 & 1 \\ 2 & -3 & 20 \end{bmatrix} \Rightarrow \begin{cases} 20x + y - 2z = 17 \\ 3x + 20y + z = -18 \\ 2x - 3y + 20z = 25 \end{cases}$$

Rearrange each row for its diagonal unknown:

$$x = \tfrac{1}{20}(17 - y + 2z), \quad y = \tfrac{1}{20}(-18 - 3x - z), \quad z = \tfrac{1}{20}(25 + 3y - 2x)$$

Start $(x_0, y_0, z_0) = (0, 0, 0)$: $x_1 = 17/20 = 0.85$, $y_1 = -18/20 = -0.9$, $z_1 = 25/20 = 1.25$. Feed back for iteration 2, repeat to tolerance.

## Self-check (from the scan)

1. $A^\theta = A$ forces what on diagonal entries, and why?
2. Write the Hermitian/Skew-Hermitian split of a general square $A$.
3. Rank-2 $3 \times 3$ homogeneous system in 3 unknowns: zero-only or $(n-r)$ solutions?
4. Bottom echelon row $[0\ 0\ 0 \mid -91]$: consistent or not?
5. Jacobi first iterate of the §9 system from $(0,0,0)$ — reproduce $0.85, -0.9, 1.25$.

## See also

- [[module-1-matrices]] — full Module-1 theory (rank theorems, normal form, eigen, Cayley-Hamilton)
- [[quiz-2026-09-22-systems-consistency-rank]] — 9-Q consistency/rank drill
- [[formula-sheet-am]] — AM-1 formula sheet
- [[prerequisite-toolkit]] — complex-conjugate prerequisites
