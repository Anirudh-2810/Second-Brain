---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Lab Write-up Guides — EXP1, EXP7, EXP8 (CO1 + CO4)"
tags: [spm, btech, c, lab, experiments, structures, unions, pointers, viva, writeup]
last_updated: "2026-09-09"
description: "SPM lab write-up guides for EXP1 (algorithms, types, operators), EXP7 (structures/unions record system) and EXP8 (pointers-only marks manager) with C skeletons and viva answers."
---

## For future agent

This note gives executable lab write-ups for three SPM experiments, distilled from the small `SPM Lab/*.docx` templates (Exp7/Exp8 fully extracted; Exp1 extracted except one long table). It covers what [[lab-ca-and-experiments]] lists but does not solve: aim, theory gist, exact problem statements, C skeletons, and viva Q&A. Use it to answer "how do I write EXP1/7/8?" Rubric/timeline stay in [[lab-ca-and-experiments]] and [[lesson-plan-2026-27]]; theory depth in [[module-1-spm-c-basics]] and [[module-4-structures-unions-pointers]].

# SPM Lab Write-up Guides — EXP1, EXP7, EXP8

> Sources: `SPM Lab/SPM Exp 1.docx` (EXP1, CO1) · `SPM Lab/SPM_Exp7.docx` (EXP7 structures/unions, CO4) · `SPM Lab/SPM_Exp8.docx` (EXP8 pointers, CO4) · remaining 11 lab files cataloged by name only (`Exp 1/2/3/4/7/8 M1-21 Dhruv Jaiswal` PDFs + `SPM EXP 5/6/Exp2/3/4 M21` docx — same template, not opened).
> Lab catalog: 14 files total (6 student PDFs + 8 blank templates). Full list: [[lab-ca-and-experiments#6-list-of-experiments--10-items-exp1-8--2-assignments]].

## EXP1 — Problem Definition, Algorithms, Data Types & Operators (CO1, W3)

**Aim (template wording):** define a problem clearly, devise an algorithm, represent it through a flowchart, and work with data types and operators in C.

**Theory gist:** structured programming = sequence + selection + iteration, no `goto`; promotes clarity/debugging. Example algorithm pattern (pos/neg/zero): `INPUT number → IF >0 DISPLAY positive → ELSE IF <0 DISPLAY negative → ELSE DISPLAY zero`. Data types: `int` (2/4 B), `float` (4 B), `double` (8 B), `char` (1 B) — sizes via `sizeof`; operators: arithmetic/relational/logical/bitwise + precedence. Depth: [[module-1-spm-c-basics]].

**Problem statements (verbatim gist):** (a) *pseudo-code:* stationery-shop billing — input item count, loop items (name, qty, price), total, discount, net; algorithm steps Start → input n → per-item input → accumulate → discount → print. (b) *C code:* area + circumference of any shape (circle/triangle/rectangle menu). **Post-lab:** algorithm + pseudo-code for student final-grade calculator. **Conclusion line:** "formulated a problem statement and developed logic (algorithm/flowchart)".

```c
// EXP1 skeleton — shape area/circumference menu (covers both problem asks)
#include <stdio.h>
#define PI 3.1416
int main(void) {
    int ch; float a, c;
    printf("1 circle 2 triangle(b,h) 3 rectangle: "); scanf("%d", &ch);
    if (ch == 1) { float r; scanf("%f", &r); a = PI*r*r; c = 2*PI*r; }
    else if (ch == 2) { float b,h; scanf("%f%f",&b,&h); a = 0.5*b*h; c = -1; }
    else { float l,w; scanf("%f%f",&l,&w); a = l*w; c = 2*(l+w); }
    printf("area=%.2f circ=%.2f", a, c);
    return 0;
}
```

**Write-up must contain:** handwritten algorithm/pseudocode + flowchart + faculty signature (L4 per [[lab-ca-and-experiments#2-laboratory-experiments--assignments-15-marks--rubric]]), else capped at L3.

## EXP7 — Structures and Unions (CO4, W12)

**Aim:** write a program to demonstrate structures and unions. **CO:** CO4 (modular programs with functions + structures).

**Theory gist (from template):** `struct` groups different-typed members under one name (`struct Student { char name[50]; int age; float grade; };`); init at declaration or per-member (`strcpy` for strings); access via `.`, via `->` through pointers; array of structs (`struct Student s[3]`) looped with `for`. Union = same syntax, shared memory (one live member). Depth: [[module-4-structures-unions-pointers]].

**Problem statement (verbatim gist):** *Student Academic Record Management Using Structures and Unions* — common fields ID(int), name, age, course; type-specific via **union** (UG: semester int + CGPA float; PG: thesis string + research score float) with **enum** {UG, PG}; array of structs; menu: input / display-all / search-by-ID / update-or-delete.

```c
// EXP7 skeleton — struct + union + enum record (core of the problem ask)
#include <stdio.h>
#include <string.h>
typedef enum { UG, PG } SType;
typedef union { struct { int sem; float cgpa; } ug; struct { char thesis[60]; float score; } pg; } Extra;
typedef struct { int id, age; char name[50], course[30]; SType type; Extra ex; } Student;
int main(void) {
    Student s[3]; int n = 0, id, i, f = -1;
    // input one UG record (extend to loop + menu for full marks)
    s[0].id = 1; strcpy(s[0].name, "Asha"); s[0].type = UG;
    s[0].ex.ug.sem = 2; s[0].ex.ug.cgpa = 8.5; n = 1;
    scanf("%d", &id);
    for (i = 0; i < n; i++) if (s[i].id == id) f = i;
    if (f >= 0) printf("%s sem %d cgpa %.1f", s[f].name, s[f].ex.ug.sem, s[f].ex.ug.cgpa);
    else printf("not found");
    return 0;
}
```

**Viva (template):** *"structure vs union?"* — struct: all members have separate memory (`sizeof` = sum + padding); union: all share one block (`sizeof` = largest member); access same syntax; use struct for simultaneous fields, union for alternatives (memory saving). Examinable in ESE Q4b per [[assessment-guide-ese-ost-quiz]].

## EXP8 — Pointers (CO4, W14)

**Aim:** write a program to demonstrate pointers. **CO:** CO4.

**Theory gist (from template):** pointer = address-holder (`int *ptr; ptr = &x; y = *ptr;`); `ptr++` scales by `sizeof`; arrays decay so `*(p+i)` ≡ `p[i]`; strings via dynamic allocation. Depth: [[module-4-structures-unions-pointers#3-pointers]].

**Problem statement (verbatim gist):** *Student Marks Management Using Pointers* — **no array indexing allowed**: input n marks via pointers, display via pointers, pointer-loop average, pointer-traversal min/max, update one mark via pointer arithmetic, menu-driven, functions taking pointer params, commented traversal.

```c
// EXP8 skeleton — pointers-only marks manager (indexing-free per problem req.)
#include <stdio.h>
void input(int *p, int n) { for (int *q = p; q < p + n; q++) scanf("%d", q); }
void show(int *p, int n) { for (int *q = p; q < p + n; q++) printf("%d ", *q); }
int main(void) {
    int m[50], n, sum = 0, hi, lo, idx;
    scanf("%d", &n); input(m, n);
    int *e = m + n;
    hi = lo = *m;
    for (int *q = m; q < e; q++) { sum += *q; if (*q > hi) hi = *q; if (*q < lo) lo = *q; }
    show(m, n);
    printf("\navg=%.2f hi=%d lo=%d", (float)sum / n, hi, lo);
    scanf("%d", &idx); *(m + idx) += 5; // modify via arithmetic
    show(m, n);
    return 0;
}
```

**Viva MCQ (template, 8 Q — answers):** 1 pointer=address-holder (b) · 2 address-of=`&` (b) · 3 `*`=dereference (b) · 4 null-deref=crash/UB (b) · 5 `*ptr` prints 10 (a) · 6 leak=alloc-without-free (b) · 7 dangling=points-to-freed (a) · 8 `printf("%d",*NULL)`=runtime error (c).

**Rubric reminder:** logic 35 + debug 15 + write-up 30 (handwritten algorithm + signature) + timely 20; submit in lab week (EXP7 W12, EXP8 W14) per [[lesson-plan-2026-27]]; TW bound by 08 Dec.

*Related:* [[syllabus-316U06C107]] · [[c-programming-master-study-guide]] · [[formula-sheet-spm]] · [[spm-pic-question-bank]]
