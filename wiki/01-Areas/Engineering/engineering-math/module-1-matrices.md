---
module: "engineering-math"
topic: "Module 1: Matrices — Rank, Systems, Eigenvalues & Cayley-Hamilton"
tags: [matrices, linear-algebra, eigenvalues, eigenvectors, cayley-hamilton, rank, echelon, normal-form]
last_updated: "2026-08-18"
prerequisites: ["Basic Algebra", "Determinants"]
---

# Module 1: Matrices — Rank, Systems, Eigenvalues & Cayley-Hamilton

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.1 Matrix Types Reference Table

| # | Type | Notation | Defining Property |
|---|------|----------|-------------------|
| 1 | **Square** | A ∈ ℝⁿˣⁿ | Number of rows = number of columns (m = n) |
| 2 | **Rectangular** | A ∈ ℝᵐˣⁿ | m ≠ n |
| 3 | **Diagonal** | D = diag(d₁, d₂, …, dₙ) | aᵢⱼ = 0 for all i ≠ j |
| 4 | **Scalar** | S = kI | All diagonal entries equal to constant k; off-diagonal = 0 |
| 5 | **Identity** | Iₙ | Diagonal matrix with all diagonal entries = 1 |
| 6 | **Zero (Null)** | Oₙ or 0ₘₓₙ | All entries are zero |
| 7 | **Symmetric** | Aᵀ = A | aᵢⱼ = aⱼᵢ for all i, j |
| 8 | **Skew-symmetric** | Aᵀ = −A | aᵢⱼ = −aⱼᵢ for all i, j (diagonal entries must be 0) |
| 9 | **Hermitian** | Aᴴ = A | aᵢⱼ = āⱼᵢ (complex conjugate transpose equals itself) |
| 10 | **Skew-Hermitian** | Aᴴ = −A | aᵢⱼ = −āⱼᵢ |
| 11 | **Orthogonal** | AᵀA = I = AAᵀ | Columns (and rows) form orthonormal set; det(A) = ±1 |
| 12 | **Unitary** | AᴴA = I = AAᴴ | Complex analogue of orthogonal; A⁻¹ = Aᴴ |
| 13 | **Idempotent** | A² = A | Matrix equals its own square (projection matrices) |
| 14 | **Nilpotent** | Aᵏ = O for some k ∈ ℕ | Some power yields the zero matrix; smallest such k is the index |
| 15 | **Involutory** | A² = I | Matrix is its own inverse (A = A⁻¹) |
| 16 | **Upper Triangular** | aᵢⱼ = 0 for i > j | All entries below the main diagonal are zero |
| 17 | **Lower Triangular** | aᵢⱼ = 0 for i < j | All entries above the main diagonal are zero |
| 18 | **Sparse** | Most entries = 0 | Fraction of nonzero entries is small (structure-dependent) |
| 19 | **Dense** | Most entries ≠ 0 | Fraction of nonzero entries is high (opposite of sparse) |

**Key Symbol Reference:**

| Symbol | Meaning |
|--------|---------|
| Aᵀ | Transpose of matrix A |
| Aᴴ (or A*) | Conjugate transpose (Hermitian transpose) of A |
| Iₙ | n × n identity matrix |
| O | Zero matrix |
| aᵢⱼ | Entry in row i, column j of matrix A |
| ā | Complex conjugate of scalar a |
| det(A) | Determinant of A |
| k | Scalar constant |

---

### 1.2 Row Echelon Form & Reduced Row Echelon Form — Gaussian Elimination Algorithm

```
┌─────────────────────────────────────────────────────────────────┐
│              GAUSSIAN ELIMINATION ALGORITHM                     │
│              (Row Echelon Form → Reduced Row Echelon Form)      │
└─────────────────────────────────────────────────────────────────┘

        ┌──────────────────────────┐
        │   START: Augmented       │
        │   Matrix [A | b]         │
        │   of size m × (n+1)      │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Set current_row = 1    │
        │   Set current_col = 1    │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   LOOP: Are all rows     │──── YES ──→ GO TO RREF PHASE
        │   below current_row      │            (if desired)
        │   all zeros?             │
        └────────────┬─────────────┘
                     │ NO
                     ▼
        ┌──────────────────────────┐
        │   Find leftmost nonzero  │
        │   entry in current_col   │
        │   at or below current_row│
        │   (the PIVOT column)     │
        └────────────┬─────────────┘
                     │
                     ▼
              ┌──────────────┐
              │ Pivot found? │
              └──────┬───────┘
                YES  │  NO
                │    │    │
                │    │    ▼
                │    │  ┌───────────────────────┐
                │    │  │ Increment current_col  │
                │    │  │ Go back to LOOP        │
                │    │  └───────────────────────┘
                ▼    │
  ┌───────────────────────────┐
  │ Is pivot row ≠            │
  │ current_row?              │
  └───────────┬───────────────┘
          YES │    │ NO
          │   │    │
          ▼   │    │
  ┌──────────────┐    │
  │ SWAP rows so │    │
  │ pivot is in  │    │
  │ current_row  │    │
  └──────┬───────┘    │
         │            │
         ▼            ▼
  ┌───────────────────────────┐
  │ SCALE pivot row so        │
  │ pivot entry = 1           │
  │ (divide row by pivot)     │
  └───────────┬───────────────┘
              │
              ▼
  ┌───────────────────────────┐
  │ ELIMINATE: For each row   │
  │ below current_row:        │
  │   subtract (pivot_coeff)  │
  │   × current_row from that │
  │   row to make entry = 0   │
  └───────────┬───────────────┘
              │
              ▼
  ┌───────────────────────────┐
  │ current_row += 1          │
  │ current_col += 1          │
  │ Go back to LOOP           │
  └───────────────────────────┘

         ═══════════════════════════════
         ║   RESULT: ROW ECHELON FORM  ║
         ═══════════════════════════════
                     │
                     │ (Optional)
                     ▼
  ┌───────────────────────────────────┐
  │   RREF PHASE (Back Substitution) │
  │                                   │
  │  For each pivot row (bottom-up):  │
  │    For each row ABOVE pivot row:  │
  │      Subtract (entry_above) ×     │
  │      pivot_row from that row      │
  │      to zero out ABOVE the pivot  │
  └───────────────┬───────────────────┘
                  │
                  ▼
         ═══════════════════════════════
         ║ REDUCED ROW ECHELON FORM    ║
         ║ (RREF) — Every pivot = 1,   ║
         ║ pivots are only nonzero     ║
         ║ entries in their columns    ║
         ═══════════════════════════════
```

**REF Properties:**
- All zero rows are at the bottom
- The first nonzero entry (pivot) of each row is to the right of the pivot in the row above
- All entries below each pivot are zero

**RREF Additional Properties:**
- Every pivot equals 1
- Every pivot is the only nonzero entry in its column
- RREF is unique for a given matrix

**Elementary Row Operations (EROs):**

| Operation | Symbol | Description |
|-----------|--------|-------------|
| Rᵢ ↔ Rⱼ | Swap | Interchange row i and row j |
| kRᵢ → Rᵢ | Scale | Multiply row i by nonzero scalar k |
| Rᵢ + kRⱼ → Rᵢ | Replacement | Add k times row j to row i |

---

### 1.3 Rank Determination Flowchart

```
┌─────────────────────────────────────────────────────────────┐
│                    RANK DETERMINATION                       │
└─────────────────────────────────────────────────────────────┘

        ┌──────────────────────────┐
        │   INPUT: Matrix A        │
        │   of size m × n          │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Is A a SQUARE matrix?  │
        │   (m = n?)               │
        └────────────┬─────────────┘
              YES    │    NO
              │      │     │
              ▼      │     │
  ┌──────────────────┐│     │
  │ Compute det(A)   ││     │
  └────────┬─────────┘│     │
           │          │     │
           ▼          │     │
     ┌──────────┐     │     │
     │det(A)≠ 0?│     │     │
     └────┬─────┘     │     │
    YES   │   NO      │     │
    │     │    │      │     │
    ▼     │    │      │     │
 ┌──────┐ │    │      │     │
 │rank =│ │    │      │     │
 │  n   │ │    │      │     │
 │(FULL)│ │    │      │     │
 └──────┘ │    ▼      │     ▼
          │  ┌──────────────────────┐
          │  │  REDUCE TO ROW       │
          │  │  ECHELON FORM (REF)  │
          │  │  using Gaussian      │
          │  │  Elimination         │
          │  └──────────┬───────────┘
          │             │
          │             ▼
          │  ┌──────────────────────┐
          │  │  COUNT nonzero rows  │
          │  │  in the REF          │
          │  │  (rows with at least │
          │  │   one nonzero entry) │
          │  └──────────┬───────────┘
          │             │
          │             ▼
          │  ┌──────────────────────┐
          │  │  rank(A) = number    │
          │  │  of nonzero rows     │
          │  └──────────────────────┘
          │
          ▼
  ┌────────────────────────────────┐
  │  VERIFICATION:                 │
  │  rank(A) = rank(Aᵀ)           │
  │  0 ≤ rank(A) ≤ min(m, n)      │
  └────────────────────────────────┘
```

**Rank — Quick Reference Summary:**

| Matrix Size | Full Rank | Rank Deficient |
|-------------|-----------|----------------|
| n × n square | rank = n | rank < n |
| m × n (m > n) | rank = n | rank < n |
| m × n (m < n) | rank = m | rank < m |

---

### 1.4 System of Linear Equations Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│          SYSTEM OF LINEAR EQUATIONS: AX = B                    │
│          Decision Tree for Classification & Solution            │
└─────────────────────────────────────────────────────────────────┘

        ┌──────────────────────────────┐
        │  START: Write augmented      │
        │  matrix [A | B]              │
        │  A is m×n, B is m×1         │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │  Reduce [A|B] to Row         │
        │  Echelon Form using          │
        │  Gaussian Elimination        │
        └──────────────┬───────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────┐
        │  CHECK: Is there any row of the form     │
        │  [0 0 ... 0 | bᵢ] where bᵢ ≠ 0 ?       │
        └──────────────────┬───────────────────────┘
                  YES     │      NO
                  │       │       │
                  ▼       │       │
  ┌───────────────────┐   │       │
  │  INCONSISTENT     │   │       │
  │  NO SOLUTION      │   │       │
  │  (System has      │   │       │
  │   contradictory   │   │       │
  │   equations)      │   │       │
  │                   │   │       │
  │  Example:         │   │       │
  │  0x + 0y + 0z = 5 │   │       │
  └───────────────────┘   │       │
                          │       │
                          ▼       │
        ┌──────────────────────────┐      │
        │  CONSISTENT SYSTEM       │      │
        │  Count number of         │      │
        │  pivots (r)              │      │
        └──────────────┬───────────┘      │
                       │                  │
            ┌──────────┼──────────┐       │
            │          │          │       │
            ▼          ▼          ▼       │
     ┌──────────┐ ┌─────────┐ ┌────────────────┐
     │ r = n    │ │ r < n   │ │ Special case   │
     │ (pivots  │ │(pivots <│ │: homogeneous   │
     │ = number │ │ unknowns│ │ AX = 0 always  │
     │ of       │ │         │ │ has trivial    │
     │ unknowns)│ │         │ │ solution X = 0 │
     └────┬─────┘ └────┬────┘ └────────────────┘
          │            │
          ▼            ▼
  ┌──────────────┐ ┌──────────────────────────┐
  │   UNIQUE     │ │   INFINITELY MANY        │
  │   SOLUTION   │ │   SOLUTIONS              │
  │              │ │                          │
  │  Solve by    │ │  (n − r) free variables  │
  │  back-       │ │                          │
  │  substitution│ │  Express pivots in terms │
  │  or inverse: │ │  of free variables       │
  │  X = A⁻¹B   │ │                          │
  └──────────────┘ │  Parametric form:        │
                   │  X = Xₚ + t₁V₁ + t₂V₂   │
                   │  + ... + tₙ₋ᵣVₙ₋ᵣ       │
                   │                          │
                   │  Xₚ = particular solution│
                   │  Vᵢ = direction vectors  │
                   │  tᵢ = free parameters    │
                   └──────────────────────────┘
```

**Rouché–Capelli Theorem (Consistency Condition):**

> The system AX = B is consistent **if and only if** rank(A) = rank([A|B]).

| Condition | rank(A) vs rank([A|B]) | rank vs n | Result |
|-----------|------------------------|-----------|--------|
| Inconsistent | rank(A) < rank([A|B]) | — | No solution |
| Unique solution | rank(A) = rank([A|B]) | rank = n | One solution |
| Infinite solutions | rank(A) = rank([A|B]) | rank < n | n − r free parameters |

**Symbol Reference:**

| Symbol | Meaning |
|--------|---------|
| A | Coefficient matrix (m × n) |
| X | Unknown column vector (n × 1) |
| B | Constants column vector (m × 1) |
| [A\|B] | Augmented matrix (m × (n+1)) |
| r | rank(A) = rank([A\|B]) |
| n | Number of unknowns (columns of A) |
| tᵢ | Free parameters |

---

### 1.5 Eigenvalue / Eigenvector Algorithm Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│         EIGENVALUE & EIGENVECTOR COMPUTATION                   │
└─────────────────────────────────────────────────────────────────┘

        ┌──────────────────────────┐
        │  START: Matrix A ∈ ℝⁿˣⁿ │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  Form the matrix         │
        │  (A − λI) where I is     │
        │  the n×n identity matrix │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  Compute the             │
        │  CHARACTERISTIC POLYNOMIAL│
        │  p(λ) = det(A − λI)     │
        │  This is a degree-n      │
        │  polynomial in λ         │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  SET p(λ) = 0            │
        │  Solve the characteristic│
        │  equation for λ          │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  ROOTS λ₁, λ₂, ..., λₙ  │
        │  are the EIGENVALUES     │
        │  of matrix A             │
        │                          │
        │  May be real or complex  │
        │  May have repetitions    │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  FOR EACH eigenvalue λᵢ: │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  Solve the homogeneous   │
        │  system:                 │
        │  (A − λᵢI) X = 0        │
        │                          │
        │  Row-reduce [A−λᵢI | 0]  │
        │  Find the null space     │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  NONZERO solutions X     │
        │  are the EIGENVECTORS    │
        │  corresponding to λᵢ     │
        │                          │
        │  Form the eigenspace:    │
        │  E(λᵢ) = null(A − λᵢI)  │
        └────────────┬─────────────┘
                     │
                     ▼
        ┌──────────────────────────────────────────┐
        │  CHECK DIAGONALIZABILITY:                │
        │                                          │
        │  For each λᵢ:                            │
        │    Algebraic mult. (aᵢ) = multiplicity   │
        │      of λᵢ as root of p(λ) = 0           │
        │    Geometric mult. (gᵢ) = dim(E(λᵢ))    │
        │      = n − rank(A − λᵢI)                 │
        │                                          │
        │  Condition: aᵢ = gᵢ for ALL eigenvalues  │
        │  → A is DIAGONALIZABLE                   │
        └──────────────┬───────────────────────────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
  ┌───────────────────┐ ┌────────────────────────┐
  │  DIAGONALIZABLE   │ │  NOT DIAGONALIZABLE    │
  │                   │ │  (use Jordan form)     │
  │  Form P = [X₁|X₂ │ │                        │
  │          |...|Xₙ] │ │  Some eigenvalues have │
  │                   │ │  gᵢ < aᵢ               │
  │  Then:            │ │                        │
  │  D = P⁻¹AP       │ │                        │
  │  D = diag(λ₁,...) │ │                        │
  └───────────────────┘ └────────────────────────┘
```

---

### 1.6 Properties of Eigenvalues — Summary Table

Let A be an n × n matrix with eigenvalues λ₁, λ₂, …, λₙ (counted with algebraic multiplicity).

| # | Property | Formula / Statement |
|---|----------|---------------------|
| 1 | **Trace relation** | tr(A) = λ₁ + λ₂ + ⋯ + λₙ = Σᵢλᵢ |
| 2 | **Determinant relation** | det(A) = λ₁ · λ₂ · ⋯ · λₙ = Πᵢλᵢ |
| 3 | **Eigenvalues of Aᵏ** | If λ is eigenvalue of A, then λᵏ is eigenvalue of Aᵏ |
| 4 | **Eigenvalues of A⁻¹** | If λ ≠ 0 is eigenvalue of A, then 1/λ is eigenvalue of A⁻¹ |
| 5 | **Eigenvalues of A + kI** | If λ is eigenvalue of A, then λ + k is eigenvalue of A + kI |
| 6 | **Eigenvalues of kA** | If λ is eigenvalue of A, then kλ is eigenvalue of kA |
| 7 | **Characteristic polynomial** | p(λ) = det(A − λI) = (−1)ⁿλⁿ + cₙ₋₁λⁿ⁻¹ + ⋯ + c₀ |
| 8 | **p(0) = det(A)** | The constant term of p(λ) |
| 9 | **Coefficients of p(λ)** | cₙ₋₁ = −tr(A), c₀ = (−1)ⁿ det(A) |
| 10 | **Eigenvalues of similar matrices** | If B = P⁻¹AP, then A and B have the same eigenvalues |
| 11 | **Eigenvalues of Aᴴ** | λ̄ (complex conjugate) is eigenvalue of Aᴴ if λ is eigenvalue of A |
| 12 | **Real eigenvalues** | Symmetric real matrices always have real eigenvalues |
| 13 | **Eigenvalues of orthogonal A** | All eigenvalues have modulus \|λ\| = 1 (|λ|² = 1) |
| 14 | **Positive definite** | A is positive definite iff all eigenvalues > 0 |
| 15 | **Singular matrix** | A is singular iff λ = 0 is an eigenvalue |

---

## 2. MATHEMATICAL FORMULATION & CORE THEOREMS

### 2.1 Rank — Definitions and Fundamental Theorems

**Definition 1 (Row Rank):** The row rank of a matrix A is the maximum number of linearly independent rows of A.

**Definition 2 (Column Rank):** The column rank of a matrix A is the maximum number of linearly independent columns of A.

**Theorem (Row Rank = Column Rank):** For any matrix A ∈ ℝᵐˣⁿ, row rank(A) = column rank(A). This common value is called the **rank** of A, denoted rank(A).

**Definition 3 (Rank via Minors):** The rank of A equals the order of the largest non-vanishing minor of A. Equivalently, rank(A) = r if and only if A has at least one non-zero minor of order r and all minors of order r+1 are zero.

**Definition 4 (Rank via REF):** The rank of A equals the number of nonzero rows in any row echelon form of A.

**Theorem (Rank and Nullity — Dimension Theorem):** For A ∈ ℝᵐˣⁿ:
```
rank(A) + nullity(A) = n
```
where nullity(A) = dim(null space of A) = dim({X : AX = 0}).

**Theorem (Rank and Row Operations):** Elementary row operations do not change the rank of a matrix.

**Theorem (Sylvester's Rank Inequality):** For A ∈ ℝᵐˣⁿ and B ∈ ℝⁿˣᵖ:
```
rank(AB) ≥ rank(A) + rank(B) − n
```
where n is the number of columns of A (= number of rows of B).

**Theorem (Frobenius Rank Inequality):** For matrices A, B, C of compatible sizes:
```
rank(AB) + rank(BC) ≤ rank(B) + rank(ABC)
```

**Theorem (Rank of Product):** rank(AB) ≤ min(rank(A), rank(B)).

**Theorem (Rank and Inverse):** A square matrix A is invertible (nonsingular) if and only if rank(A) = n.

**Symbol Reference:**

| Symbol | Meaning |
|--------|---------|
| rank(A) | Rank of matrix A |
| nullity(A) | Dimension of the null space of A |
| A ∈ ℝᵐˣⁿ | Matrix A with m rows and n columns |
| AB | Matrix product of A and B |
| X | Column vector |
| O | Zero matrix |
| I | Identity matrix |
| min(a,b) | Minimum of a and b |

---

### 2.2 Echelon Form — Formal Properties

**Definition (Row Echelon Form):** A matrix is in **row echelon form (REF)** if:

1. All rows consisting entirely of zeros are at the bottom.
2. The first nonzero entry (called the **pivot** or **leading entry**) in each nonzero row is strictly to the right of the pivot in the row above it.
3. All entries below a pivot are zero.

**Definition (Reduced Row Echelon Form):** A matrix is in **reduced row echelon form (RREF)** if, in addition to the REF conditions:

4. Every pivot equals 1.
5. Every pivot is the only nonzero entry in its column.

**Theorem (Uniqueness of RREF):** Every matrix has a unique reduced row echelon form. The REF is not unique (depends on the elimination strategy), but RREF is.

**Theorem (Rank from Echelon Form):** The number of nonzero rows in any REF of A equals rank(A).

**Gaussian Elimination Computational Cost:**

For an n × n matrix:
- Forward elimination (to REF): approximately (2/3)n³ operations
- Back substitution: approximately n² operations
- Total: O(n³)

---

### 2.2.1 Normal Form (Canonical Form) — the row-and-column method (MU exam standard)

**Definition (Normal Form):** A matrix $A$ of rank $r$ can be reduced by a **sequence of elementary row AND column operations** to its normal form:

$$A \sim \begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}$$

where $I_r$ is the $r \times r$ identity block and zeros fill every other block. **The number of 1s on the diagonal of the normal form equals $\mathrm{rank}(A) = r$.**

**Why column operations are allowed here (but not in REF):** column operations multiply $A$ on the *right* by an invertible matrix — elementary matrices are always invertible, so both row ops (left) and column ops (right) preserve rank. Hence $\mathrm{rank}(A) = \mathrm{rank}\bigl(\begin{bmatrix}I_r & 0 \\ 0 & 0\end{bmatrix}\bigr) = r$. This is the only rank method that uses column operations.

**Reduction algorithm (exam procedure):**

1. Pick a nonzero pivot — target position (1,1). If $a_{11} = 0$, bring a nonzero element to (1,1) by a row or column interchange.
2. **Row ops with $R_1$** — clear column 1 below the pivot: $R_i \to R_i - \frac{a_{i1}}{a_{11}} R_1$ for all $i \geq 2$.
3. **Column ops with $C_1$** — clear row 1 right of the pivot: $C_j \to C_j - \frac{a_{1j}}{a_{11}} C_1$ for all $j \geq 2$.
4. Repeat steps 1–3 on the remaining $(m-1) \times (n-1)$ submatrix (rows 2…m, cols 2…n).
5. **Stop** when the leftover block is all zeros (then scale each pivot row to get leading 1s if you want the literal $I_r$ block).

**Exam shortcut:** you may stop the moment the unprocessed block is all zeros — you do *not* need to build a literal identity matrix. Count the leading 1s: that is the rank. (Worked example: Problem 1b below.)

**Normal form vs REF — when to use which:**

| Method | Operations | Result | Rank read-off |
|--------|-----------|--------|---------------|
| Row echelon form | row ops only | triangular echelon | nonzero rows |
| Normal form | row AND column ops | $\begin{bmatrix}I_r & 0 \\ 0 & 0\end{bmatrix}$ | number of 1s on diagonal |

Normal form is the fastest when the matrix is nowhere near echelon form and the biggest-minor computation would be tedious (e.g., 4×4+ with proportional rows).

---

### 2.3 Systems of Linear Equations

**Matrix Form:** A system of m linear equations in n unknowns can be written as:

```
AX = B
```

where:
- A ∈ ℝᵐˣⁿ is the coefficient matrix
- X = [x₁, x₂, …, xₙ]ᵀ is the column vector of unknowns
- B = [b₁, b₂, …, bₘ]ᵀ is the column vector of constants

**Augmented Matrix:** The system is equivalently represented by the augmented matrix:

```
[A | B] = [a₁₁  a₁₂  ...  a₁ₙ | b₁ ]
          [a₂₁  a₂₂  ...  a₂ₙ | b₂ ]
          [ ...                    ... ]
          [aₘ₁  aₘ₂  ...  aₘₙ | bₘ ]
```

**Cramer's Rule:** When A is square (m = n) and det(A) ≠ 0, the unique solution is:

```
xᵢ = det(Aᵢ) / det(A)     for i = 1, 2, …, n
```

where Aᵢ is the matrix obtained from A by replacing its i-th column with B.

**Consistency — Rouché–Capelli Theorem:**

The system AX = B is consistent if and only if:

```
rank(A) = rank([A | B])
```

**Solution Classification Table:**

| Case | rank(A) | rank([A\|B]) | rank vs n | Solution |
|------|---------|--------------|-----------|----------|
| Unique | r | r | r = n | One solution: X = A⁻¹B (if square) |
| Infinite | r | r | r < n | n − r free parameters |
| None | r | r+1 | — | Inconsistent (no solution) |

where n = number of unknowns.

**Homogeneous System (B = 0):**
- Always consistent (trivial solution X = 0 always exists)
- If rank(A) = n → only trivial solution
- If rank(A) < n → infinitely many solutions with n − r free parameters

---

### 2.4 Eigenvalues and Eigenvectors — Complete Formulation

**Definition:** Let A be an n × n matrix. A scalar λ is called an **eigenvalue** of A if there exists a nonzero vector X ∈ ℂⁿ such that:

```
AX = λX,    X ≠ 0
```

The nonzero vector X is called an **eigenvector** of A corresponding to eigenvalue λ. Equivalently:

```
(A − λI)X = 0,    X ≠ 0
```

**Characteristic Equation:** The eigenvalues are the roots of:

```
p(λ) = det(A − λI) = 0
```

This is a polynomial of degree n in λ, called the **characteristic polynomial**.

**Expanding for a 2 × 2 matrix:**

For A = [[a, b], [c, d]]:
```
det(A − λI) = (a − λ)(d − λ) − bc = λ² − (a+d)λ + (ad − bc) = 0
```
which is:
```
λ² − tr(A)·λ + det(A) = 0
```

**Expanding for a 3 × 3 matrix:**

For A = [[a, b, c], [d, e, f], [g, h, i]]:
```
det(A − λI) = −λ³ + (a+e+i)λ² − (ae+ai+ei−bf−cg−dh)λ + det(A) = 0
```
which is:
```
λ³ − tr(A)·λ² + S₂·λ − det(A) = 0
```
where S₂ = sum of all 2 × 2 principal minors of A.

**Eigenspace:** For eigenvalue λ, the eigenspace is:

```
E(λ) = null(A − λI) = {X : (A − λI)X = 0}
```

**Geometric multiplicity:** g(λ) = dim(E(λ)) = n − rank(A − λI)

**Algebraic multiplicity:** a(λ) = multiplicity of λ as root of p(λ) = 0

**Key Inequality:** For every eigenvalue λ:
```
1 ≤ g(λ) ≤ a(λ)
```

---

#### Cayley-Hamilton Theorem — Statement and Proof

**Theorem (Cayley-Hamilton):** Every square matrix satisfies its own characteristic equation. That is, if p(λ) = det(A − λI) is the characteristic polynomial of A, then:

```
p(A) = 0
```

where the zero on the right is the n × n zero matrix.

**Step-by-Step Proof:**

**Step 1: Express (A − λI)⁻¹ using the adjugate.**

By the definition of the adjugate (classical adjoint):
```
(A − λI) · adj(A − λI) = det(A − λI) · I = p(λ) · I        ... (1)
```

**Step 2: Expand adj(A − λI) as a matrix polynomial.**

The adjugate adj(A − λI) is an n × n matrix whose entries are cofactors of (A − λI). Each cofactor is a determinant of an (n−1) × (n−1) submatrix of (A − λI), which is a polynomial in λ of degree at most n−1. Therefore, we can write:

```
adj(A − λI) = Bₙ₋₁λⁿ⁻¹ + Bₙ₋₂λⁿ⁻² + ⋯ + B₁λ + B₀      ... (2)
```

where B₀, B₁, …, Bₙ₋₁ are n × n matrices with scalar entries (independent of λ).

**Step 3: Expand det(A − λI).**

```
p(λ) = det(A − λI) = (−1)ⁿλⁿ + aₙ₋₁λⁿ⁻¹ + ⋯ + a₁λ + a₀    ... (3)
```

where a₀, a₁, …, aₙ₋₁ are scalars.

**Step 4: Substitute (2) and (3) into (1).**

```
(A − λI)(Bₙ₋₁λⁿ⁻¹ + Bₙ₋₂λⁿ⁻² + ⋯ + B₁λ + B₀)
    = (−1)ⁿλⁿI + aₙ₋₁λⁿ⁻¹I + ⋯ + a₁λI + a₀I
```

**Step 5: Expand the left side and collect powers of λ.**

Left side expanded:
```
ABₙ₋₁λⁿ⁻¹ + ABₙ₋₂λⁿ⁻² + ⋯ + AB₁λ + AB₀
− Bₙ₋₁λⁿ   − Bₙ₋₂λⁿ⁻¹ − ⋯ − B₁λ² − B₀λ
```

Collecting coefficients of each power of λ (from λⁿ down to λ⁰):

- **Coefficient of λⁿ:**  −Bₙ₋₁ = (−1)ⁿI
- **Coefficient of λⁿ⁻¹:**  ABₙ₋₁ − Bₙ₋₂ = aₙ₋₁I
- **Coefficient of λⁿ⁻²:**  ABₙ₋₂ − Bₙ₋₃ = aₙ₋₂I
- **⋮**
- **Coefficient of λ¹:**  AB₁ − B₀ = a₁I
- **Coefficient of λ⁰:**  AB₀ = a₀I

**Step 6: Multiply each equation by successive powers of A and sum.**

Multiply the λⁿ⁻¹ equation by Aⁿ⁻¹, the λⁿ⁻² equation by Aⁿ⁻², …, the λ¹ equation by A, and the λ⁰ equation by I, then sum all equations:

```
Aⁿ(−Bₙ₋₁) + Aⁿ⁻¹(ABₙ₋₁ − Bₙ₋₂) + Aⁿ⁻²(ABₙ₋₂ − Bₙ₋₃) + ⋯ + A(AB₁ − B₀) + AB₀
```

This is a **telescoping sum**. After cancellation:

```
(−1)ⁿAⁿ + aₙ₋₁Aⁿ⁻¹ + ⋯ + a₁A + a₀I = 0
```

But this is exactly p(A) = 0, where p(λ) = (−1)ⁿλⁿ + aₙ₋₁λⁿ⁻¹ + ⋯ + a₁λ + a₀. ∎

**Practical Consequence — Finding A⁻¹ Using Cayley-Hamilton:**

If A is nonsingular (det(A) ≠ 0, so a₀ ≠ 0), then from p(A) = 0:

```
(−1)ⁿAⁿ + aₙ₋₁Aⁿ⁻¹ + ⋯ + a₁A + a₀I = 0
```

Multiply both sides by A⁻¹:

```
(−1)ⁿAⁿ⁻¹ + aₙ₋₁Aⁿ⁻² + ⋯ + a₁I + a₀A⁻¹ = 0
```

Solving for A⁻¹:

```
A⁻¹ = −(1/a₀)[(−1)ⁿAⁿ⁻¹ + aₙ₋₁Aⁿ⁻² + ⋯ + a₁I]
```

---

### 2.5 Diagonalization

**Definition:** A matrix A ∈ ℝⁿˣⁿ is said to be **diagonalizable** if there exists an invertible matrix P and a diagonal matrix D such that:

```
A = PDP⁻¹      or equivalently      D = P⁻¹AP
```

**Theorem (Diagonalization Criterion):** A ∈ ℝⁿˣⁿ is diagonalizable if and only if A has n linearly independent eigenvectors.

**Construction:**
1. Find all eigenvalues λ₁, λ₂, …, λₙ of A.
2. For each λᵢ, find a basis for the eigenspace E(λᵢ).
3. If the total number of linearly independent eigenvectors equals n, form:
   - P = [X₁ | X₂ | ⋯ | Xₙ] (matrix whose columns are eigenvectors)
   - D = diag(λ₁, λ₂, …, λₙ) (diagonal matrix of corresponding eigenvalues)

**Key Property:** Once A = PDP⁻¹, computing powers becomes trivial:

```
Aᵏ = PDᵏP⁻¹ = P · diag(λ₁ᵏ, λ₂ᵏ, …, λₙᵏ) · P⁻¹
```

**Theorem (Spectral Theorem for Real Symmetric Matrices):** If A is a real symmetric matrix (A = Aᵀ), then:
1. A is always diagonalizable.
2. All eigenvalues of A are real.
3. There exists an orthogonal matrix Q (Q⁻¹ = Qᵀ) such that:
   ```
   A = QDQᵀ
   ```
   where D = diag(λ₁, …, λₙ).

**Symbol Reference:**

| Symbol | Meaning |
|--------|---------|
| A | n × n square matrix |
| λᵢ | i-th eigenvalue of A |
| Xᵢ | Eigenvector corresponding to λᵢ |
| P | Matrix of eigenvectors (invertible) |
| D | Diagonal matrix of eigenvalues |
| Q | Orthogonal matrix of eigenvectors (for symmetric A) |
| E(λᵢ) | Eigenspace of λᵢ |
| a(λᵢ) | Algebraic multiplicity of λᵢ |
| g(λᵢ) | Geometric multiplicity of λᵢ |
| Aᴴ | Conjugate transpose of A |
| Aᵏ | A raised to the k-th power |
| A⁻¹ | Inverse of A |
| tr(A) | Trace of A (sum of diagonal entries) |
| det(A) | Determinant of A |

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: Find the Rank of a 4×3 Matrix

**Problem:** Find the rank of the matrix:

```
        [ 1   2   3 ]
   A =  [ 2   4   6 ]
        [ 1   3   5 ]
        [ 3   5   7 ]
```

using (a) row reduction and (b) minors.

---

**Solution (a): Row Reduction Method**

**Step 1:** Write the matrix.

```
        [ 1   2   3 ]
   A =  [ 2   4   6 ]
        [ 1   3   5 ]
        [ 3   5   7 ]
```

**Step 2:** R₂ → R₂ − 2R₁ (eliminate below pivot in column 1).

```
R₂ = [2 4 6] − 2[1 2 3] = [2−2, 4−4, 6−6] = [0 0 0]

        [ 1   2   3 ]
   A ~  [ 0   0   0 ]
        [ 1   3   5 ]
        [ 3   5   7 ]
```

**Step 3:** R₃ → R₃ − R₁.

```
R₃ = [1 3 5] − [1 2 3] = [0 1 2]

        [ 1   2   3 ]
   A ~  [ 0   0   0 ]
        [ 0   1   2 ]
        [ 3   5   7 ]
```

**Step 4:** R₄ → R₄ − 3R₁.

```
R₄ = [3 5 7] − 3[1 2 3] = [3−3, 5−6, 7−9] = [0 −1 −2]

        [ 1   2   3 ]
   A ~  [ 0   0   0 ]
        [ 0   1   2 ]
        [ 0  −1  −2 ]
```

**Step 5:** Swap R₂ ↔ R₃ to bring nonzero row up.

```
        [ 1   2   3 ]
   A ~  [ 0   1   2 ]
        [ 0   0   0 ]
        [ 0  −1  −2 ]
```

**Step 6:** R₄ → R₄ + R₃ (where R₃ is now [0 1 2]).

```
R₄ = [0 −1 −2] + [0 1 2] = [0 0 0]

        [ 1   2   3 ]
   A ~  [ 0   1   2 ]
        [ 0   0   0 ]
        [ 0   0   0 ]
```

This is in row echelon form.

**Count nonzero rows:** 2 nonzero rows.

**rank(A) = 2** ✓

---

**Solution (b): Minor Method**

**Step 1:** Check the largest possible minors (3 × 3 minors, since A is 4 × 3).

Compute det of the top 3 × 3 submatrix:

```
| 1  2  3 |
| 2  4  6 | = 1(4·6 − 6·6) − 2(2·6 − 6·3) + 3(2·6 − 4·3)
| 1  3  5 |   = 1(24−36) − 2(12−18) + 3(12−12)
            = 1(−12) − 2(−6) + 3(0)
            = −12 + 12 + 0
            = 0
```

All 3 × 3 minors are zero (since the two rows [1 2 3] and [2 4 6] are proportional, any 3 × 3 minor containing both is 0; and direct computation confirms the remaining 3 × 3 minors also vanish).

**Step 2:** Check 2 × 2 minors.

```
| 1  2 | = 1·4 − 2·2 = 0    (rows proportional)
| 2  4 |

| 1  2 | = 1·3 − 2·1 = 1 ≠ 0
| 1  3 |
```

Since we found a nonzero 2 × 2 minor, rank ≥ 2. Since all 3 × 3 minors are zero, rank < 3.

**rank(A) = 2** ✓

---

### Problem 1b: Find the Rank via Normal (Canonical) Form

**Problem:** Reduce the matrix below to normal form and state its rank:

```
        [ 1   2   3   4 ]
   A =  [ 2   4   6   8 ]
        [ 1   1   1   1 ]
```

Note: $R_2 = 2R_1$, so the rank is ≤ 2 — a warning flag before any elimination.

---

**Solution: Normal Form Method**

**Step 1:** $a_{11} = 1 \neq 0$ → pivot in place. Clear column 1 with row ops:

```
R2 → R2 − 2R1 = [2 4 6 8] − 2[1 2 3 4] = [0 0 0 0]
R3 → R3 − R1  = [1 1 1 1] − [1 2 3 4]  = [0 −1 −2 −3]

        [ 1   2   3   4 ]
   A ~  [ 0   0   0   0 ]
        [ 0  −1  −2  −3 ]
```

**Step 2:** Clear row 1 with column ops ($C_2 \to C_2 - 2C_1$, $C_3 \to C_3 - 3C_1$, $C_4 \to C_4 - 4C_1$):

```
C2: (2, 0, −1) − 2(1, 0, 0) = (0, 0, −1)
C3: (3, 0, −2) − 3(1, 0, 0) = (0, 0, −2)
C4: (4, 0, −3) − 4(1, 0, 0) = (0, 0, −3)

        [ 1   0   0   0 ]
   A ~  [ 0   0   0   0 ]
        [ 0  −1  −2  −3 ]
```

**Step 3:** Descend to submatrix (rows 2–3, cols 2–4). Swap $R_2 \leftrightarrow R_3$ to bring a nonzero into position (2,2):

```
        [ 1   0   0   0 ]
   A ~  [ 0  −1  −2  −3 ]
        [ 0   0   0   0 ]
```

**Step 4:** Pivot $a_{22} = -1$. Clear row 2 with column ops ($C_3 \to C_3 - 2C_2$, $C_4 \to C_4 - 3C_2$):

```
C3: (0, −2, 0) − 2(0, −1, 0) = (0, 0, 0)
C4: (0, −3, 0) − 3(0, −1, 0) = (0, 0, 0)

        [ 1   0   0   0 ]
   A ~  [ 0  −1   0   0 ]
        [ 0   0   0   0 ]
```

**Step 5:** Scale $R_2 \to (-1) R_2$ to make the pivot +1:

```
        [ 1   0   0   0 ]
   A ~  [ 0   1   0   0 ]   =   [ I₂  0 ]
        [ 0   0   0   0 ]       [ 0   0 ]
```

This is the normal form $\begin{bmatrix} I_2 & 0 \\ 0 & 0 \end{bmatrix}$.

**Count the 1s on the diagonal:** 2 → **rank(A) = 2** ✓

(Cross-check via Problem 1 methods: REF gives 2 nonzero rows; largest nonzero minor is 2×2.)

---

### Problem 2: Solve System Using Gaussian Elimination (Unique Solution)

**Problem:** Solve the system:
```
  x + 2y +  z =  9
 2x + 5y + 3z = 24
  x +  y + 4z = 16
```

---

**Solution:**

**Step 1:** Write the augmented matrix.

```
        [ 1   2   1 |  9 ]
[A|B] = [ 2   5   3 | 24 ]
        [ 1   1   4 | 16 ]
```

**Step 2:** R₂ → R₂ − 2R₁.

```
R₂ = [2 5 3 | 24] − 2[1 2 1 | 9] = [2−2, 5−4, 3−2 | 24−18] = [0 1 1 | 6]

        [ 1   2   1 |  9 ]
       [ 0   1   1 |  6 ]
        [ 1   1   4 | 16 ]
```

**Step 3:** R₃ → R₃ − R₁.

```
R₃ = [1 1 4 | 16] − [1 2 1 | 9] = [0 −1 3 | 7]

        [ 1   2   1 |  9 ]
       [ 0   1   1 |  6 ]
        [ 0  −1   3 |  7 ]
```

**Step 4:** R₃ → R₃ + R₂.

```
R₃ = [0 −1 3 | 7] + [0 1 1 | 6] = [0 0 4 | 13]

        [ 1   2   1 |  9 ]
       [ 0   1   1 |  6 ]
        [ 0   0   4 | 13 ]
```

This is in row echelon form. 3 pivots, 3 unknowns → unique solution.

**Step 5:** Back substitution.

**From Row 3:**
```
4z = 13  →  z = 13/4
```

**From Row 2:**
```
y + z = 6
y + 13/4 = 6
y = 6 − 13/4 = 24/4 − 13/4 = 11/4
```

**From Row 1:**
```
x + 2y + z = 9
x + 2(11/4) + 13/4 = 9
x + 22/4 + 13/4 = 9
x + 35/4 = 9
x = 9 − 35/4 = 36/4 − 35/4 = 1/4
```

**Verification:**
```
Eq 1: 1/4 + 2(11/4) + 13/4 = 1/4 + 22/4 + 13/4 = 36/4 = 9  ✓
Eq 2: 2(1/4) + 5(11/4) + 3(13/4) = 2/4 + 55/4 + 39/4 = 96/4 = 24  ✓
Eq 3: 1/4 + 11/4 + 4(13/4) = 1/4 + 11/4 + 52/4 = 64/4 = 16  ✓
```

**The unique solution is x = 1/4, y = 11/4, z = 13/4.** ✓

---

### Problem 3: Solve System with Infinite Solutions (Parametric Form)

**Problem:** Solve the system:
```
 x +  y +  z =  6
2x + 3y +  z = 13
3x + 4y + 2z = 19
```

---

**Solution:**

**Step 1:** Write the augmented matrix.

```
        [ 1   1   1 |  6 ]
[A|B] = [ 2   3   1 | 13 ]
        [ 3   4   2 | 19 ]
```

**Step 2:** R₂ → R₂ − 2R₁.

```
R₂ = [2 3 1 | 13] − 2[1 1 1 | 6] = [0 1 −1 | 1]

        [ 1   1   1 |  6 ]
       [ 0   1  −1 |  1 ]
        [ 3   4   2 | 19 ]
```

**Step 3:** R₃ → R₃ − 3R₁.

```
R₃ = [3 4 2 | 19] − 3[1 1 1 | 6] = [0 1 −1 | 1]

        [ 1   1   1 |  6 ]
       [ 0   1  −1 |  1 ]
        [ 0   1  −1 |  1 ]
```

**Step 4:** R₃ → R₃ − R₂.

```
R₃ = [0 1 −1 | 1] − [0 1 −1 | 1] = [0 0 0 | 0]

        [ 1   1   1 |  6 ]
       [ 0   1  −1 |  1 ]
        [ 0   0   0 |  0 ]
```

Row echelon form achieved. The third row is all zeros → consistent.

**Step 5:** Rank analysis.

rank(A) = rank([A|B]) = 2 (two nonzero rows).
Number of unknowns n = 3.
Since rank < n (2 < 3), there are n − r = 3 − 2 = **1 free variable**.

**Step 6:** Express pivot variables in terms of the free variable.

Let z = t (free parameter, t ∈ ℝ).

**From Row 2:**
```
y − z = 1
y = 1 + z = 1 + t
```

**From Row 1:**
```
x + y + z = 6
x + (1 + t) + t = 6
x = 6 − 1 − t − t = 5 − 2t
```

**Step 7:** Write the solution in parametric form.

```
X = [ x ]   [ 5 − 2t ]   [ 5 ]       [ −2 ]
    [ y ] = [ 1 + t  ] = [ 1 ] + t · [  1 ]
    [ z ]   [   t    ]   [ 0 ]       [  1 ]
```

**Verification (for any t):**

Take t = 0: x = 5, y = 1, z = 0.
```
Eq 1: 5 + 1 + 0 = 6  ✓
Eq 2: 10 + 3 + 0 = 13  ✓
Eq 3: 15 + 4 + 0 = 19  ✓
```

Take t = 1: x = 3, y = 2, z = 1.
```
Eq 1: 3 + 2 + 1 = 6  ✓
Eq 2: 6 + 6 + 1 = 13  ✓
Eq 3: 9 + 8 + 2 = 19  ✓
```

**The solution is x = 5 − 2t, y = 1 + t, z = t for any real parameter t.** ✓

---

### Problem 4: Eigenvalues and Eigenvectors of a 3×3 Matrix

**Problem:** Find the eigenvalues and eigenvectors of:

```
        [ 2   1   0 ]
   A =  [ 0   2   1 ]
        [ 0   0   3 ]
```

---

**Solution:**

**Step 1:** Form (A − λI).

```
A − λI = [ 2−λ    1      0   ]
         [  0    2−λ     1   ]
         [  0      0    3−λ  ]
```

**Step 2:** Compute det(A − λI).

Since A − λI is an upper triangular matrix, the determinant is the product of diagonal entries:

```
det(A − λI) = (2 − λ)(2 − λ)(3 − λ) = (2 − λ)²(3 − λ)
```

**Step 3:** Solve det(A − λI) = 0.

```
(2 − λ)²(3 − λ) = 0
```

**Eigenvalues:**
```
λ₁ = 2  (algebraic multiplicity a₁ = 2)
λ₂ = 3  (algebraic multiplicity a₂ = 1)
```

---

**Step 4:** Find eigenvectors for λ₁ = 2.

Solve (A − 2I)X = 0:

```
A − 2I = [ 0   1   0 ]
         [ 0   0   1 ]
         [ 0   0   1 ]
```

Row reduce:

```
R₃ → R₃ − R₂:

[ 0   1   0 ]
[ 0   0   1 ]
[ 0   0   0 ]
```

The system is:
```
0·x₁ + 1·x₂ + 0·x₃ = 0  →  x₂ = 0
0·x₁ + 0·x₂ + 1·x₃ = 0  →  x₃ = 0
```

x₁ is free. Let x₁ = t.

```
X = t [ 1 ]
      [ 0 ]
      [ 0 ]
```

**Eigenvector for λ₁ = 2:** X₁ = [1, 0, 0]ᵀ

**Geometric multiplicity:** g(2) = 1 (one free variable, one independent eigenvector).

**Note:** g(2) = 1 < a(2) = 2, so A is **NOT diagonalizable**.

---

**Step 5:** Find eigenvectors for λ₂ = 3.

Solve (A − 3I)X = 0:

```
A − 3I = [ −1   1   0 ]
         [  0  −1   1 ]
         [  0   0   0 ]
```

The system is:
```
−x₁ + x₂ = 0       →  x₂ = x₁
−x₂ + x₃ = 0       →  x₃ = x₂ = x₁
```

Let x₁ = t. Then x₂ = t, x₃ = t.

```
X = t [ 1 ]
      [ 1 ]
      [ 1 ]
```

**Eigenvector for λ₂ = 3:** X₂ = [1, 1, 1]ᵀ

**Geometric multiplicity:** g(3) = 1 = a(3). ✓

---

**Summary:**

| Eigenvalue | Algebraic Mult. | Geometric Mult. | Eigenvector |
|------------|-----------------|-----------------|-------------|
| λ = 2 | 2 | 1 | [1, 0, 0]ᵀ |
| λ = 3 | 1 | 1 | [1, 1, 1]ᵀ |

**The eigenvalues are λ = 2 (with eigenvector [1,0,0]ᵀ) and λ = 3 (with eigenvector [1,1,1]ᵀ). Since geometric multiplicity < algebraic multiplicity for λ = 2, the matrix is not diagonalizable.** ✓

---

### Problem 5: Verify Cayley-Hamilton Theorem and Find A⁻¹

**Problem:** For the matrix:

```
        [ 1   2   1 ]
   A =  [ 0   1   2 ]
        [ 1   0   1 ]
```

(a) Verify the Cayley-Hamilton theorem.
(b) Find A⁻¹ using the Cayley-Hamilton theorem.

---

**Solution (a): Verify Cayley-Hamilton**

**Step 1:** Compute the characteristic polynomial p(λ) = det(A − λI).

```
A − λI = [ 1−λ    2      1   ]
         [  0    1−λ     2   ]
         [  1      0    1−λ  ]
```

**Step 2:** Expand det(A − λI) along the first column.

```
det(A − λI) = (1−λ) · det[ 1−λ   2  ]  −  0  +  1 · det[  2     1  ]
                              [  0  1−λ ]                    [ 1−λ   2  ]

= (1−λ)[(1−λ)(1−λ) − 2·0] + 1[2·2 − 1·(1−λ)]

= (1−λ)(1−λ)² + [4 − 1 + λ]

= (1−λ)³ + (3 + λ)

= (1 − 3λ + 3λ² − λ³) + (3 + λ)

= −λ³ + 3λ² − 3λ + 1 + 3 + λ

= −λ³ + 3λ² − 2λ + 4
```

So:
```
p(λ) = −λ³ + 3λ² − 2λ + 4 = 0
```

Or equivalently (multiplying by −1):
```
λ³ − 3λ² + 2λ − 4 = 0
```

**Step 3:** According to Cayley-Hamilton, p(A) = 0, i.e.:

```
−A³ + 3A² − 2A + 4I = 0
```

**Step 4:** Compute A² and A³.

**Computing A²:**
```
A² = A · A = [ 1  2  1 ] [ 1  2  1 ]
             [ 0  1  2 ] [ 0  1  2 ]
             [ 1  0  1 ] [ 1  0  1 ]

Row 1: [1·1+2·0+1·1,  1·2+2·1+1·0,  1·1+2·2+1·1]
      = [0+0+1,       2+2+0,        1+4+1      ]  (wait, let me redo)

Row 1 × Col 1: 1·1 + 2·0 + 1·1 = 1 + 0 + 1 = 2
Row 1 × Col 2: 1·2 + 2·1 + 1·0 = 2 + 2 + 0 = 4
Row 1 × Col 3: 1·1 + 2·2 + 1·1 = 1 + 4 + 1 = 6

Row 2 × Col 1: 0·1 + 1·0 + 2·1 = 0 + 0 + 2 = 2
Row 2 × Col 2: 0·2 + 1·1 + 2·0 = 0 + 1 + 0 = 1
Row 2 × Col 3: 0·1 + 1·2 + 2·1 = 0 + 2 + 2 = 4

Row 3 × Col 1: 1·1 + 0·0 + 1·1 = 1 + 0 + 1 = 2
Row 3 × Col 2: 1·2 + 0·1 + 1·0 = 2 + 0 + 0 = 2
Row 3 × Col 3: 1·1 + 0·2 + 1·1 = 1 + 0 + 1 = 2
```

```
A² = [ 2  4  6 ]
     [ 2  1  4 ]
     [ 2  2  2 ]
```

**Computing A³ = A² · A:**
```
A³ = [ 2  4  6 ] [ 1  2  1 ]
     [ 2  1  4 ] [ 0  1  2 ]
     [ 2  2  2 ] [ 1  0  1 ]

Row 1 × Col 1: 2·1 + 4·0 + 6·1 = 2 + 0 + 6 = 8
Row 1 × Col 2: 2·2 + 4·1 + 6·0 = 4 + 4 + 0 = 8
Row 1 × Col 3: 2·1 + 4·2 + 6·1 = 2 + 8 + 6 = 16

Row 2 × Col 1: 2·1 + 1·0 + 4·1 = 2 + 0 + 4 = 6
Row 2 × Col 2: 2·2 + 1·1 + 4·0 = 4 + 1 + 0 = 5
Row 2 × Col 3: 2·1 + 1·2 + 4·1 = 2 + 2 + 4 = 8

Row 3 × Col 1: 2·1 + 2·0 + 2·1 = 2 + 0 + 2 = 4
Row 3 × Col 2: 2·2 + 2·1 + 2·0 = 4 + 2 + 0 = 6
Row 3 × Col 3: 2·1 + 2·2 + 2·1 = 2 + 4 + 2 = 8
```

```
A³ = [ 8   8  16 ]
     [ 6   5   8 ]
     [ 4   6   8 ]
```

**Step 5:** Verify −A³ + 3A² − 2A + 4I.

```
−A³ = [ −8  −8  −16 ]
      [ −6  −5   −8 ]
      [ −4  −6   −8 ]

3A²  = [  6  12  18 ]
       [  6   3  12 ]
       [  6   6   6 ]

−2A  = [ −2  −4  −2 ]
       [  0  −2  −4 ]
       [ −2   0  −2 ]

4I   = [  4   0   0 ]
       [  0   4   0 ]
       [  0   0   4 ]
```

**Summing element by element:**

**Row 1:**
- (1,1): −8 + 6 − 2 + 4 = 0 ✓
- (1,2): −8 + 12 − 4 + 0 = 0 ✓
- (1,3): −16 + 18 − 2 + 0 = 0 ✓

**Row 2:**
- (2,1): −6 + 6 + 0 + 0 = 0 ✓
- (2,2): −5 + 3 − 2 + 4 = 0 ✓
- (2,3): −8 + 12 − 4 + 0 = 0 ✓

**Row 3:**
- (3,1): −4 + 6 − 2 + 0 = 0 ✓
- (3,2): −6 + 6 + 0 + 0 = 0 ✓
- (3,3): −8 + 6 − 2 + 4 = 0 ✓

```
−A³ + 3A² − 2A + 4I = [ 0  0  0 ]
                       [ 0  0  0 ]
                       [ 0  0  0 ]  = O  ✓
```

**The Cayley-Hamilton theorem is verified: p(A) = 0.** ✓

---

**Solution (b): Find A⁻¹ Using Cayley-Hamilton**

**Step 1:** From p(A) = 0:
```
−A³ + 3A² − 2A + 4I = 0
```

**Step 2:** Check det(A) ≠ 0. From the characteristic polynomial, p(0) = det(A) = 4 ≠ 0, so A is invertible. ✓

**Step 3:** Multiply both sides of p(A) = 0 by A⁻¹:
```
−A² + 3A − 2I + 4A⁻¹ = 0
```

**Step 4:** Solve for A⁻¹:
```
4A⁻¹ = A² − 3A + 2I
```

**Step 5:** Compute the right side.

```
A²  = [ 2  4  6 ]
      [ 2  1  4 ]
      [ 2  2  2 ]

−3A  = [ −3  −6  −3 ]
       [  0  −3  −6 ]
       [ −3   0  −3 ]

2I   = [ 2   0   0 ]
       [ 0   2   0 ]
       [ 0   0   2 ]
```

```
A² − 3A + 2I = [ 2−3+2    4−6+0    6−3+0 ]   [ 1  −2   3 ]
               [ 2+0+2    1−3+2    4−6+0 ] = [ 4  −2  −2 ]
               [ 2−3+2    2+0+0    2−3+2 ]   [ 1   2   1 ]
```

**Step 6:** Divide by 4:

```
A⁻¹ = (1/4) [ 1  −2   3 ]
             [ 4  −2  −2 ]
             [ 1   2   1 ]
```

```
A⁻¹ = [ 1/4   −1/2    3/4 ]
       [   1   −1/2   −1/2 ]
       [ 1/4    1/2    1/4 ]
```

**Step 7:** Verification — Check A · A⁻¹ = I.

```
A · A⁻¹ = [ 1  2  1 ] [ 1/4  −1/2   3/4 ]
           [ 0  1  2 ] [  1   −1/2  −1/2 ]
           [ 1  0  1 ] [ 1/4   1/2   1/4 ]

Row 1 × Col 1: 1·(1/4) + 2·1 + 1·(1/4) = 1/4 + 2 + 1/4 = 5/2 + 1/4 ... 

Let me redo this more carefully.

Row 1 × Col 1: 1·(1/4) + 2·(1) + 1·(1/4) = 1/4 + 2 + 1/4 = 1/4 + 8/4 + 1/4 = 10/4 = 5/2

Hmm, that's not 1. Let me recheck the computation.
```

Let me recheck A².

```
A = [ 1  2  1 ]
    [ 0  1  2 ]
    [ 1  0  1 ]
```

```
A² = A·A:

(1,1): 1·1 + 2·0 + 1·1 = 2      ✓
(1,2): 1·2 + 2·1 + 1·0 = 4      ✓
(1,3): 1·1 + 2·2 + 1·1 = 6      ✓
(2,1): 0·1 + 1·0 + 2·1 = 2      ✓
(2,2): 0·2 + 1·1 + 2·0 = 1      ✓
(2,3): 0·1 + 1·2 + 2·1 = 4      ✓
(3,1): 1·1 + 0·0 + 1·1 = 2      ✓
(3,2): 1·2 + 0·1 + 1·0 = 2      ✓
(3,3): 1·1 + 0·2 + 1·1 = 2      ✓
```

A² is correct. Now recheck A² − 3A + 2I:

```
A² = [ 2  4  6 ]
     [ 2  1  4 ]
     [ 2  2  2 ]

3A  = [ 3  6  3 ]
      [ 0  3  6 ]
      [ 3  0  3 ]

2I  = [ 2  0  0 ]
      [ 0  2  0 ]
      [ 0  0  2 ]

A² − 3A + 2I:
(1,1): 2 − 3 + 2 = 1
(1,2): 4 − 6 + 0 = −2
(1,3): 6 − 3 + 0 = 3
(2,1): 2 − 0 + 0 = 2
(2,2): 1 − 3 + 2 = 0
(2,3): 4 − 6 + 0 = −2
(3,1): 2 − 3 + 0 = −1
(3,2): 2 − 0 + 0 = 2
(3,3): 2 − 3 + 2 = 1
```

I made an error before. Let me redo:

```
A² − 3A + 2I = [ 1  −2   3 ]
               [ 2   0  −2 ]
               [ −1  2   1 ]
```

So:
```
A⁻¹ = (1/4) [ 1  −2   3 ]
             [ 2   0  −2 ]
             [ −1  2   1 ]
```

Let me verify A · A⁻¹:

```
A · A⁻¹ = [ 1  2  1 ] [ 1  −2   3 ] × (1/4)
           [ 0  1  2 ] [ 2   0  −2 ]
           [ 1  0  1 ] [ −1  2   1 ]

(1,1): 1·1 + 2·2 + 1·(−1) = 1 + 4 − 1 = 4
(1,2): 1·(−2) + 2·0 + 1·2 = −2 + 0 + 2 = 0
(1,3): 1·3 + 2·(−2) + 1·1 = 3 − 4 + 1 = 0

(2,1): 0·1 + 1·2 + 2·(−1) = 0 + 2 − 2 = 0
(2,2): 0·(−2) + 1·0 + 2·2 = 0 + 0 + 4 = 4
(2,3): 0·3 + 1·(−2) + 2·1 = 0 − 2 + 2 = 0

(3,1): 1·1 + 0·2 + 1·(−1) = 1 + 0 − 1 = 0
(3,2): 1·(−2) + 0·0 + 1·2 = −2 + 0 + 2 = 0
(3,3): 1·3 + 0·(−2) + 1·1 = 3 + 0 + 1 = 4
```

```
A · A⁻¹ = (1/4) [ 4  0  0 ]   [ 1  0  0 ]
                [ 0  4  0 ] = [ 0  1  0 ] = I  ✓
                [ 0  0  4 ]   [ 0  0  1 ]
```

**The inverse using Cayley-Hamilton theorem is:**

```
A⁻¹ = (1/4) [ 1  −2   3 ]
             [ 2   0  −2 ]
             [ −1  2   1 ]
```

or equivalently:

```
A⁻¹ = [  1/4   −1/2    3/4 ]
       [  1/2     0   −1/2 ]
       [ −1/4    1/2    1/4 ]
```

**This is verified by A · A⁻¹ = I.** ✓

---

## 4. ENGINEERING APPLICATIONS MAP

### Eigenvalues and Eigenvectors in Engineering

| Application Domain | Eigenvalues | Eigenvectors |
|-------------------|-------------|--------------|
| **Structural Dynamics** | Natural frequencies (ωₙ = √λ) of vibrating structures — determine resonance conditions | Mode shapes — the spatial pattern of vibration at each natural frequency |
| **Principal Stress/Strain** | Principal stresses σ₁, σ₂, σ₃ — maximum and minimum normal stresses at a point | Principal directions — orientations along which shear stress vanishes |
| **Control Theory** | Poles of transfer function — determine system stability and transient response | Controllability/observability modes — directions in state space |
| **Quantum Mechanics** | Energy levels of quantum systems (Ĥψ = Eψ) | Quantum states (wavefunctions) of the system |
| **Vibration Analysis** | Critical speeds of rotating machinery — avoid resonance | Deflection shapes at critical speeds |
| **Google PageRank** | Importance scores of web pages | Steady-state distribution of random web surfer |

### Matrix Rank in Engineering

| Application Domain | Role of Rank |
|-------------------|--------------|
| **Control Systems** | rank of controllability matrix C = [B AB A²B … Aⁿ⁻¹B] determines if system is controllable |
| **Observability** | rank of observability matrix O = [C; CA; CA²; …; CAⁿ⁻¹] determines if system state can be estimated |
| **Structural Engineering** | rank of stiffness matrix K determines if a structure is statically determinate or indeterminate |
| **Signal Processing** | rank of data covariance matrix indicates number of independent signal sources |
| **Mechanics** | rank of the Jacobian of constraint equations determines degrees of freedom of a mechanism |
| **Data Science** | rank of feature matrix indicates intrinsic dimensionality of the dataset |

### Systems of Linear Equations in Engineering

| Application Domain | Description |
|-------------------|-------------|
| **Circuit Analysis (Nodal Analysis)** | Kirchhoff's Current Law at each node gives a linear equation — solve GV = I for node voltages |
| **Circuit Analysis (Mesh Analysis)** | Kirchhoff's Voltage Law around each mesh gives a linear equation — solve ZI = V for mesh currents |
| **Structural Analysis (FEM)** | Finite Element Method assembles element stiffness matrices into global system KU = F — solve for displacements U |
| **Heat Transfer** | Steady-state temperature distribution satisfies Laplace equation — discretized to linear system |
| **Fluid Mechanics** | Incompressible flow potential — velocity potential satisfies linear PDE, discretized to linear system |
| **Power Systems** | Load flow analysis — nonlinear system linearized to solve for bus voltages and power flows |
| **Economics** | Leontief Input-Output model — (I − A)X = D solves for production levels X given demand D |

### Diagonalization in Engineering

| Application Domain | How Diagonalization Helps |
|-------------------|---------------------------|
| **Coupled Oscillations** | Decouples n-DOF system Mẍ + Kx = 0 into n independent single-DOF equations via modal analysis X = Φq |
| **Differential Equations** | Converts ẋ = Ax to ẏ = Dy (uncoupled) where y = P⁻¹x — solve each independently |
| **Control Theory** | Modal decomposition separates fast and slow dynamics for controller design |
| **Data Compression** | Principal Component Analysis (PCA) diagonalizes covariance matrix — finds directions of maximum variance |
| **Stability Analysis** | Eigenvalues of A determine stability of ẋ = Ax: stable iff all Re(λᵢ) < 0 |

### Cayley-Hamilton Theorem in Engineering

| Application Domain | How Cayley-Hamilton Helps |
|-------------------|---------------------------|
| **System Response** | Compute eᴬᵗ without diagonalization — express eᴬᵗ as polynomial in A of degree ≤ n−1 using C-H |
| **Matrix Powers** | Compute Aᵏ for large k (e.g., A¹⁰⁰) by reducing to polynomial in A of degree ≤ n−1 |
| **Control Theory** | Derive state transition matrix Φ(t) = eᴬᵗ using inverse Laplace: (sI − A)⁻¹ = adj(sI−A)/det(sI−A) |
| **Structural Dynamics** | Free vibration response: x(t) = eᴬᵗx₀ where A is the system matrix |
| **Power Systems** | Transient stability analysis — compute matrix exponentials efficiently |
| **Signal Processing** | Recursive filter implementation — compute system matrix powers for FIR/IIR filter design |

### Summary: Quick Reference for Engineering Applications

```
┌────────────────────────────────────────────────────────────────────┐
│               ENGINEERING APPLICATIONS SUMMARY                    │
├─────────────────────┬──────────────────────────────────────────────┤
│  EIGENVALUE λ       │  • Natural frequency ωₙ = √λ               │
│                     │  • System pole → stability                   │
│                     │  • Energy level (quantum)                    │
│                     │  • Critical speed (rotor dynamics)           │
│                     │  • PageRank importance score                 │
├─────────────────────┼──────────────────────────────────────────────┤
│  EIGENVECTOR X      │  • Mode shape (vibration pattern)           │
│                     │  • Principal stress/strain direction         │
│                     │  • Controllability/observability mode        │
│                     │  • Quantum state                             │
│                     │  • Principal component (PCA)                 │
├─────────────────────┼──────────────────────────────────────────────┤
│  MATRIX RANK        │  • Controllability: rank(C) = n?            │
│                     │  • Observability: rank(O) = n?               │
│                     │  • Structural determinacy                     │
│                     │  • Data dimensionality                       │
│                     │  • Mechanism DOF                              │
├─────────────────────┼──────────────────────────────────────────────┤
│  LINEAR SYSTEMS     │  • Circuit analysis (KCL/KVL)               │
│  AX = B             │  • FEM structural analysis                   │
│                     │  • Steady-state heat transfer                │
│                     │  • Leontief economics model                  │
│                     │  • Power flow analysis                       │
├─────────────────────┼──────────────────────────────────────────────┤
│  DIAGONALIZATION    │  • Modal analysis (decouple vibrations)     │
│  A = PDP⁻¹         │  • Solve coupled ODEs                       │
│                     │  • PCA / data compression                   │
│                     │  • Stability analysis                       │
│                     │  • Controller design                         │
├─────────────────────┼──────────────────────────────────────────────┤
│  CAYLEY-HAMILTON    │  • Compute eᴬᵗ for system response         │
│  p(A) = 0          │  • Efficient matrix power computation        │
│                     │  • State transition matrix                   │
│                     │  • Recursive filter design                   │
│                     │  • Transient analysis                        │
└─────────────────────┴──────────────────────────────────────────────┘
```

---

## APPENDIX: KEY FORMULAS QUICK REFERENCE

### Rank Formulas

| Formula | Statement |
|---------|-----------|
| Row rank = Column rank | rank(A) = rank(Aᵀ) |
| Rank–Nullity | rank(A) + nullity(A) = n |
| Sylvester | rank(AB) ≥ rank(A) + rank(B) − n |
| Frobenius | rank(AB) + rank(BC) ≤ rank(B) + rank(ABC) |
| Product bound | rank(AB) ≤ min(rank(A), rank(B)) |
| Sum bound | rank(A + B) ≤ rank(A) + rank(B) |
| Invertibility | A is invertible ⟺ rank(A) = n |

### Eigenvalue Formulas

| Formula | Statement |
|---------|-----------|
| Trace | tr(A) = Σλᵢ |
| Determinant | det(A) = Πλᵢ |
| Aᵏ eigenvalues | λᵢᵏ |
| A⁻¹ eigenvalues | 1/λᵢ (λᵢ ≠ 0) |
| A + kI eigenvalues | λᵢ + k |
| kA eigenvalues | kλᵢ |
| Similar matrices | Same eigenvalues |
| Aᴴ eigenvalues | λ̄ᵢ |

### System Solution Conditions

| Condition | rank(A) vs rank([A\|B]) | rank vs n | Solution |
|-----------|-------------------------|-----------|----------|
| Unique | r = r | r = n | One solution |
| Infinite | r = r | r < n | n − r parameters |
| Inconsistent | r < r+1 | — | No solution |

### Diagonalization Conditions

| Condition | Status |
|-----------|--------|
| A has n distinct eigenvalues | Diagonalizable |
| All a(λ) = g(λ) | Diagonalizable |
| A is real symmetric | Always diagonalizable (orthogonally) |
| A is real symmetric | All eigenvalues are real |
| g(λ) < a(λ) for any λ | NOT diagonalizable |

### Cayley-Hamilton Applications

| Use | Formula |
|-----|---------|
| Direct verification | p(A) = 0 |
| Find A⁻¹ | A⁻¹ = −(1/a₀)[(−1)ⁿAⁿ⁻¹ + aₙ₋₁Aⁿ⁻² + ⋯ + a₁I] |
| Find Aᵏ (for k ≥ n) | Express Aᵏ as polynomial of degree ≤ n−1 using p(A) = 0 |
| Compute eᴬᵗ | Express eᴬᵗ as polynomial in A of degree ≤ n−1 |

---

## CROSS-REFERENCES

- [[engineering-math/module-2-partial-differentiation|Module 2: Partial Differentiation]] — The Jacobian matrix (Module 2, §2.5) is built from partial derivatives arranged as a matrix; eigenvalue analysis of the Hessian (Module 2, §2.6) classifies critical points. Matrix methods from this module provide the computational engine behind the Jacobian and Hessian frameworks.
- [[engineering-math/module-4-linear-differential-equations|Module 4: Linear Differential Equations]] — Systems of linear ODEs are solved using the matrix eigenvalue method: ẋ = Ax is decoupled via diagonalization (A = PDP⁻¹) into independent scalar equations. The characteristic polynomial of a matrix parallels the auxiliary equation in ODEs.
- [[engineering-math/module-3-homogeneous-functions|Module 3: Homogeneous Functions]] — Euler's theorem for homogeneous functions uses partial derivatives in a linear combination analogous to matrix-vector products; the degree of homogeneity connects to eigenvalue relationships.
- [[engineering-math/module-5-complex-numbers|Module 5: Complex Numbers]] — Complex eigenvalues arise when the characteristic polynomial has negative discriminant, leading to oscillatory solutions (e^{αx}(cos βx + i sin βx)) in systems of DEs.

*Module 1 of 5 — [[engineering-math/module-5-complex-numbers|← Module 5]] | [[engineering-math/module-2-partial-differentiation|Module 2 →]]*

*End of Module 1: Matrices — Rank, Systems, Eigenvalues & Cayley-Hamilton*

---

*Revision: every formula from this module is on [[formula-sheet-am]].*
