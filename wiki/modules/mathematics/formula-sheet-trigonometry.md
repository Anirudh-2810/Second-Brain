---
module: "mathematics"
topic: "Trigonometry Formula Sheet — Complete Reference (JEE Advanced)"
tags: [mathematics, trigonometry, formulas, jee, identities, equations]
last_updated: "2026-08-11"
source: "/raw-sources/math/TRIGNOMETRIC-Formulas.pdf, Kota notes"
---

# Trigonometry Formula Sheet — Complete Reference

> Specialized trigonometry formula compendium. Every identity, transformation, and equation-solving technique for JEE Advanced.

---

## 📐 Basic Ratios & Reciprocals

| Function | Definition | Reciprocal |
|----------|------------|------------|
| $\sin\theta$ | $\frac{\text{opp}}{\text{hyp}}$ | $\csc\theta = \frac{1}{\sin\theta}$ |
| $\cos\theta$ | $\frac{\text{adj}}{\text{hyp}}$ | $\sec\theta = \frac{1}{\cos\theta}$ |
| $\tan\theta$ | $\frac{\sin\theta}{\cos\theta}$ | $\cot\theta = \frac{1}{\tan\theta}$ |

**Pythagorean Identities:**
- $\sin^2\theta + \cos^2\theta = 1$
- $1 + \tan^2\theta = \sec^2\theta$
- $1 + \cot^2\theta = \csc^2\theta$

---

## 📐 Standard Angles

| $\theta$ | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
|----------|-----------|------------|------------|------------|------------|-------------|-------------|-------------|
| $\sin\theta$ | $0$ | $1/2$ | $1/\sqrt{2}$ | $\sqrt{3}/2$ | $1$ | $0$ | $-1$ | $0$ |
| $\cos\theta$ | $1$ | $\sqrt{3}/2$ | $1/\sqrt{2}$ | $1/2$ | $0$ | $-1$ | $0$ | $1$ |
| $\tan\theta$ | $0$ | $1/\sqrt{3}$ | $1$ | $\sqrt{3}$ | $\infty$ | $0$ | $\infty$ | $0$ |

---

## 📐 Compound Angle Formulas

### Sum & Difference
| Formula | Expression |
|---------|------------|
| $\sin(A+B)$ | $\sin A\cos B + \cos A\sin B$ |
| $\sin(A-B)$ | $\sin A\cos B - \cos A\sin B$ |
| $\cos(A+B)$ | $\cos A\cos B - \sin A\sin B$ |
| $\cos(A-B)$ | $\cos A\cos B + \sin A\sin B$ |
| $\tan(A+B)$ | $\frac{\tan A + \tan B}{1 - \tan A\tan B}$ |
| $\tan(A-B)$ | $\frac{\tan A - \tan B}{1 + \tan A\tan B}$ |
| $\cot(A+B)$ | $\frac{\cot A\cot B - 1}{\cot A + \cot B}$ |
| $\cot(A-B)$ | $\frac{\cot A\cot B + 1}{\cot B - \cot A}$ |

### Transformations (Sum-to-Product)
| Formula | Expression |
|---------|------------|
| $\sin C + \sin D$ | $2\sin\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| $\sin C - \sin D$ | $2\cos\frac{C+D}{2}\sin\frac{C-D}{2}$ |
| $\cos C + \cos D$ | $2\cos\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| $\cos C - \cos D$ | $-2\sin\frac{C+D}{2}\sin\frac{C-D}{2}$ |

### Product-to-Sum
| Formula | Expression |
|---------|------------|
| $2\sin A\cos B$ | $\sin(A+B) + \sin(A-B)$ |
| $2\cos A\sin B$ | $\sin(A+B) - \sin(A-B)$ |
| $2\cos A\cos B$ | $\cos(A+B) + \cos(A-B)$ |
| $2\sin A\sin B$ | $\cos(A-B) - \cos(A+B)$ |

---

## 📐 Multiple & Sub-Multiple Angles

### Double Angle
| Formula | Expression |
|---------|------------|
| $\sin 2A$ | $2\sin A\cos A = \frac{2\tan A}{1+\tan^2 A}$ |
| $\cos 2A$ | $\cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A = \frac{1-\tan^2 A}{1+\tan^2 A}$ |
| $\tan 2A$ | $\frac{2\tan A}{1-\tan^2 A}$ |
| $\cot 2A$ | $\frac{\cot^2 A - 1}{2\cot A}$ |

### Triple Angle
| Formula | Expression |
|---------|------------|
| $\sin 3A$ | $3\sin A - 4\sin^3 A$ |
| $\cos 3A$ | $4\cos^3 A - 3\cos A$ |
| $\tan 3A$ | $\frac{3\tan A - \tan^3 A}{1 - 3\tan^2 A}$ |

### Half Angle
| Formula | Expression |
|---------|------------|
| $\sin A$ | $2\sin\frac{A}{2}\cos\frac{A}{2} = \frac{2\tan\frac{A}{2}}{1+\tan^2\frac{A}{2}}$ |
| $\cos A$ | $2\cos^2\frac{A}{2} - 1 = 1 - 2\sin^2\frac{A}{2} = \frac{1-\tan^2\frac{A}{2}}{1+\tan^2\frac{A}{2}}$ |
| $\tan A$ | $\frac{2\tan\frac{A}{2}}{1-\tan^2\frac{A}{2}}$ |
| $\sin\frac{A}{2}$ | $\pm\sqrt{\frac{1-\cos A}{2}}$ |
| $\cos\frac{A}{2}$ | $\pm\sqrt{\frac{1+\cos A}{2}}$ |
| $\tan\frac{A}{2}$ | $\pm\sqrt{\frac{1-\cos A}{1+\cos A}} = \frac{1-\cos A}{\sin A} = \frac{\sin A}{1+\cos A}$ |

---

## 📐 Trigonometric Equations — General Solutions

### Basic Equations
| Equation | General Solution | Principal Solution |
|----------|------------------|-------------------|
| $\sin x = \sin \alpha$ | $x = n\pi + (-1)^n \alpha$ | $x = \alpha$ or $\pi - \alpha$ |
| $\cos x = \cos \alpha$ | $x = 2n\pi \pm \alpha$ | $x = \pm \alpha$ |
| $\tan x = \tan \alpha$ | $x = n\pi + \alpha$ | $x = \alpha$ |
| $\sin^2 x = \sin^2 \alpha$ | $x = n\pi \pm \alpha$ | $x = \pm \alpha$ |
| $\cos^2 x = \cos^2 \alpha$ | $x = n\pi \pm \alpha$ | $x = \pm \alpha$ |
| $\tan^2 x = \tan^2 \alpha$ | $x = n\pi \pm \alpha$ | $x = \pm \alpha$ |
| $\sin x = 0$ | $x = n\pi$ | $x = 0, \pi$ |
| $\cos x = 0$ | $x = (2n+1)\pi/2$ | $x = \pi/2, 3\pi/2$ |
| $\tan x = 0$ | $x = n\pi$ | $x = 0, \pi$ |

### Standard Values
| Equation | Solution |
|----------|----------|
| $\sin x = a$ ($|a| \le 1$) | $x = n\pi + (-1)^n \sin^{-1} a$ |
| $\cos x = a$ ($|a| \le 1$) | $x = 2n\pi \pm \cos^{-1} a$ |
| $\tan x = a$ | $x = n\pi + \tan^{-1} a$ |

### Quadratic in Trig Functions
Solve for $\sin x$, $\cos x$, or $\tan x$ using quadratic formula, then apply general solutions.

**Example:** $2\sin^2 x + 3\sin x - 2 = 0 \implies \sin x = \frac{1}{2}, -2 (\text{reject}) \implies x = n\pi + (-1)^n \frac{\pi}{6}$

---

## 📐 Conditional Identities (If $A+B+C = \pi$)

### Sum of Angles
- $\sin(A+B) = \sin C$
- $\cos(A+B) = -\cos C$
- $\tan(A+B) = -\tan C$

### Sine/Cosine of Sum
- $\sin 2A + \sin 2B + \sin 2C = 4\sin A \sin B \sin C$
- $\cos 2A + \cos 2B + \cos 2C = -1 - 4\cos A \cos B \cos C$
- $\sin A + \sin B + \sin C = 4\cos\frac{A}{2}\cos\frac{B}{2}\cos\frac{C}{2}$
- $\cos A + \cos B + \cos C = 1 + 4\sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2}$

### Tangent
- $\tan A + \tan B + \tan C = \tan A \tan B \tan C$
- $\cot A \cot B + \cot B \cot C + \cot C \cot A = 1$

### Half Angles
- $\sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2} \le \frac{1}{8}$
- $\cos\frac{A}{2}\cos\frac{B}{2}\cos\frac{C}{2} \le \frac{3\sqrt{3}}{8}$

---

## 📐 Inverse Trigonometric Functions

### Principal Values
| Function | Domain | Range (Principal) |
|----------|--------|-------------------|
| $\sin^{-1} x$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ |
| $\cos^{-1} x$ | $[-1, 1]$ | $[0, \pi]$ |
| $\tan^{-1} x$ | $\mathbb{R}$ | $(-\pi/2, \pi/2)$ |
| $\cot^{-1} x$ | $\mathbb{R}$ | $(0, \pi)$ |
| $\sec^{-1} x$ | $|x| \ge 1$ | $[0, \pi] \setminus \{\pi/2\}$ |
| $\csc^{-1} x$ | $|x| \ge 1$ | $[-\pi/2, \pi/2] \setminus \{0\}$ |

### Properties
| Property | Formula |
|----------|---------|
| $\sin^{-1}(-x)$ | $-\sin^{-1} x$ |
| $\cos^{-1}(-x)$ | $\pi - \cos^{-1} x$ |
| $\tan^{-1}(-x)$ | $-\tan^{-1} x$ |
| $\sin^{-1} x + \cos^{-1} x$ | $\pi/2$ |
| $\tan^{-1} x + \cot^{-1} x$ | $\pi/2$ |
| $\sec^{-1} x + \csc^{-1} x$ | $\pi/2$ |
| $\tan^{-1} x + \tan^{-1} y$ | $\tan^{-1}\frac{x+y}{1-xy}$ (if $xy<1$) |
| $\tan^{-1} x - \tan^{-1} y$ | $\tan^{-1}\frac{x-y}{1+xy}$ |
| $2\tan^{-1} x$ | $\sin^{-1}\frac{2x}{1+x^2} = \cos^{-1}\frac{1-x^2}{1+x^2} = \tan^{-1}\frac{2x}{1-x^2}$ |

### Important Formulas
- $\sin^{-1} x + \sin^{-1} y = \sin^{-1}[x\sqrt{1-y^2} + y\sqrt{1-x^2}]$
- $\cos^{-1} x + \cos^{-1} y = \cos^{-1}[xy - \sqrt{1-x^2}\sqrt{1-y^2}]$
- $2\sin^{-1} x = \sin^{-1}[2x\sqrt{1-x^2}]$
- $2\cos^{-1} x = \cos^{-1}[2x^2-1]$

---

## 📐 Properties of Triangles

### Sine Rule
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

### Cosine Rule
$$a^2 = b^2 + c^2 - 2bc\cos A$$
$$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$$

### Projection Rule
$$a = b\cos C + c\cos B$$
$$b = c\cos A + a\cos C$$
$$c = a\cos B + b\cos A$$

### Napier's Analogy
$$\tan\frac{B-C}{2} = \frac{b-c}{b+c}\cot\frac{A}{2}$$
$$\tan\frac{A-B}{2} = \frac{a-b}{a+b}\cot\frac{C}{2}$$

### Area
$$\Delta = \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B = \frac{1}{2}ab\sin C$$
$$\Delta = \sqrt{s(s-a)(s-b)(s-c)} \quad (\text{Heron's Formula})$$
$$\Delta = \frac{abc}{4R} = rs = (s-a)r_1 = (s-b)r_2 = (s-c)r_3$$

### Radii
| Radius | Formula |
|--------|---------|
| Circumradius $R$ | $R = \frac{abc}{4\Delta} = \frac{a}{2\sin A}$ |
| Inradius $r$ | $r = \frac{\Delta}{s} = 4R\sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2}$ |
| Exradius $r_1$ | $r_1 = \frac{\Delta}{s-a} = 4R\sin\frac{A}{2}\cos\frac{B}{2}\cos\frac{C}{2}$ |

### Half-Angle Formulas
$$\sin\frac{A}{2} = \sqrt{\frac{(s-b)(s-c)}{bc}}$$
$$\cos\frac{A}{2} = \sqrt{\frac{s(s-a)}{bc}}$$
$$\tan\frac{A}{2} = \sqrt{\frac{(s-b)(s-c)}{s(s-a)}} = \frac{r}{s-a} = \frac{\Delta}{s(s-a)}$$

### Other Useful Formulas
- $r = 4R\sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2}$
- $r_1 + r_2 + r_3 - r = 4R$
- $\frac{1}{r_1} + \frac{1}{r_2} + \frac{1}{r_3} = \frac{1}{r}$
- $r_1 r_2 r_3 = r s^2$
- $\cot\frac{A}{2} = \frac{s-a}{r}$

---

## 📐 Trigonometric Inequalities & Bounds

| Expression | Range |
|------------|-------|
| $a\sin\theta + b\cos\theta$ | $[-\sqrt{a^2+b^2}, \sqrt{a^2+b^2}]$ |
| $a\sin\theta + b\cos\theta + c$ | $[c-\sqrt{a^2+b^2}, c+\sqrt{a^2+b^2}]$ |
| $\sin\theta \cos\theta$ | $[-1/2, 1/2]$ |
| $\sin^n\theta + \cos^n\theta$ ($n>2$) | $[2^{1-n/2}, 1]$ |
| $\sin A + \sin B + \sin C$ ($A+B+C=\pi$) | $\le \frac{3\sqrt{3}}{2}$ |
| $\cos A + \cos B + \cos C$ ($A+B+C=\pi$) | $\le \frac{3}{2}$ |
| $\tan A \tan B \tan C$ ($A+B+C=\pi$, acute) | $\ge 3\sqrt{3}$ |

---

## 📐 Complex Numbers & Trigonometry

### Euler's Formula
$$e^{i\theta} = \cos\theta + i\sin\theta$$

### De Moivre's Theorem
$$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$$

### Roots of Unity
- $z^n = 1 \implies z = e^{2\pi i k/n}$, $k = 0,1,\dots,n-1$
- Sum of all $n$-th roots $= 0$
- Product $= (-1)^{n-1}$

### Trigonometric via Complex
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$$
$$\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$
$$\tan\theta = \frac{e^{i\theta} - e^{-i\theta}}{i(e^{i\theta} + e^{-i\theta})}$$

### Summation Series
$$\sum_{k=1}^n \cos k\theta = \frac{\sin(n\theta/2)\cos((n+1)\theta/2)}{\sin(\theta/2)}$$
$$\sum_{k=1}^n \sin k\theta = \frac{\sin(n\theta/2)\sin((n+1)\theta/2)}{\sin(\theta/2)}$$

---

## 🎯 Problem-Solving Shortcuts

### 1. Converting Product to Sum
**Always use:** $2\sin A\cos B = \sin(A+B) + \sin(A-B)$ when you see products of trig functions.

### 2. Symmetric Sums
If expression is symmetric in $A,B,C$ with $A+B+C=\pi$, use $\tan A + \tan B + \tan C = \tan A\tan B\tan C$.

### 3. Range Questions
For $a\sin\theta + b\cos\theta$, max $= \sqrt{a^2+b^2}$, min $= -\sqrt{a^2+b^2}$.

### 4. Inverse Trig Domains
Always check domain before applying identities. $\sin^{-1}(\sin x) = x$ only if $x \in [-\pi/2, \pi/2]$.

### 5. Multiple Angle Factorization
- $\sin 3A = 3\sin A - 4\sin^3 A$ (cubic in $\sin A$)
- $\cos 3A = 4\cos^3 A - 3\cos A$ (cubic in $\cos A$)

---

*Specialized trigonometry reference — use alongside master formula sheet and topic-wise notes.*