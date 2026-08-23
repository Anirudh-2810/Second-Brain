---
module: "c-programming"
topic: "C Programming — Flowcharts & Visuals"
tags: [programming, c, flowcharts, mermaid, visuals]
source: "https://www.youtube.com/watch?v=xND0t1pr3KY"
last_updated: "2026-08-19"
---

# C Programming — Flowcharts & Visuals

> Every core concept as a picture. Mermaid diagrams render natively in Obsidian (`Ctrl/Cmd+Shift+P` → "Preview"); ASCII versions work anywhere.

---

## 1. Compile & run pipeline

```mermaid
flowchart LR
    A[You write main.c] --> B[gcc main.c -o main]
    B --> C{Compiler errors?}
    C -- yes --> A
    C -- no --> D[main.exe machine code]
    D --> E[./main runs it]
    E --> F[Output on screen]
```

```
 main.c ──► gcc main.c -o main ──► main.exe ──► ./main ──► OUTPUT
   ▲                                │
   └────────── (fix errors) ◄───────┘
```

---

## 2. The program lifecycle — `main()` to `return 0`

```mermaid
flowchart TB
    A[START] --> B[OS loads program]
    B --> C[Find entry point: int main]
    C --> D[Statements run top-to-bottom]
    D --> E[printf / scanf / logic]
    E --> F{more statements?}
    F -- yes --> D
    F -- no --> G[return 0]
    G --> H[OS frees resources]
    H --> I[END]
```

---

## 3. Data types decision tree

```mermaid
flowchart TD
    A[What value am I storing?] --> B{Number?}
    B -- no --> C{One character?}
    C -- yes --> D[char  %c  'A']
    C -- no --> E[String: char[]  %s  &quot;Hi&quot;]
    B -- yes --> F{Decimal point?}
    F -- no --> G[int  %d  25]
    F -- yes --> H{Need precision?}
    H -- no --> I[float  %f  19.99]
    H -- yes --> J[double  %lf  3.14159]
    B -- bool --> K[bool  true/false  <stdbool.h>]
```

---

## 4. `if / else if / else` — decision flowchart

```mermaid
flowchart TD
    A[condition 1] --> B{true?}
    B -- yes --> C[Block 1]
    B -- no --> D{condition 2}
    D -- yes --> E[Block 2]
    D -- no --> F[else block]
    C --> G[continue program]
    E --> G
    F --> G
```

```
if (cond1) { … }        cond1? ──true──► Block1 ─┐
else if (cond2) { … }        │false              │
else { … }                   ▼                   ▼
                         cond2? ──true──► Block2 ─┤──► continue
                              │false              │
                              ▼                   ▼
                           Block3 ────────────────┘
```

---

## 5. Nested `if` (movie-ticket discounts)

```mermaid
flowchart TD
    S{isStudent?} -- yes --> A[price *= 0.9]
    A --> T{isSenior?}
    T -- yes --> B[price *= 0.8 → 30% total]
    T -- no --> C[10% only]
    S -- no --> U{isSenior?}
    U -- yes --> D[price *= 0.8 → 20%]
    U -- no --> E[full price]
    B --> P[print $price]
    C --> P
    D --> P
    E --> P
```

---

## 6. `switch` — dispatch by value

```mermaid
flowchart TD
    A[value to test] --> B{case A?} --yes--> C[Block A] --> Z[break]
    B --no--> D{case B?} --yes--> E[Block B] --> Y[break]
    D --no--> F{case C?} --yes--> G[Block C] --> X[break]
    F --no--> H[default block] --> W[done]
    Z --> W
    Y --> W
    X --> W
```

---

## 7. Ternary — one-line branch

```
condition ? X : Y

   condition?
      │
   yes▼    no▼
     X      Y
```

---

## 8. `while` loop — check first

```mermaid
flowchart TD
    A[init counter] --> B{condition?}
    B -- false --> E[EXIT loop]
    B -- true --> C[run body]
    C --> D[update counter i++]
    D --> B
```

> Risk: forget the update → condition never false → **infinite loop**.

## 9. `do while` loop — body runs once minimum

```mermaid
flowchart TD
    A[run body] --> B[update counter]
    B --> C{condition?}
    C -- true --> A
    C -- false --> D[EXIT loop]
```

> Perfect for **menus & validation**: prompt the user, then ask "is the input valid?".

---

## 10. `for` loop — three parts, one line

```
for ( int i = 1 ; i <= 5 ; i++ )
       ▲           ▲        ▲
      start     condition  update
       │           │        │
       ▼           ▼        ▼
     runs ONCE  checked     runs AFTER
                EVERY run   each body run
       ┌───────────────────────┐
       │        body           │
       └───────────┬───────────┘
                   ▼
              condition false → exit
```

---

## 11. Nested loops — rows × columns (2D grid)

```
OUTER i = 1    i = 2    i = 3
   ┌─────────┐ ┌─────┐ ┌─────┐
   │ j=1,2,3 │ │j=…  │ │j=…  │   outer = rows
   └─────────┘ └─────┘ └─────┘
    inner loop = columns inside each row
```

```mermaid
flowchart TD
    A[i=1] --> B{i <= 3?}
    B -- false --> E[DONE]
    B -- true --> C[j=1]
    C --> D{j <= 3?}
    D -- false --> U[i++, newline] --> B
    D -- true --> F[print i x j] --> G[j++] --> D
```

---

## 12. Function call — pass by value vs. pointer

```mermaid
flowchart LR
    subgraph main
      X[x = 22]
    end
    subgraph func
      Y[copy of x]
    end
    X -->|by value: copies value| Y
```

```mermaid
flowchart LR
    subgraph main
      A[age = 22]
      P[&age]
    end
    subgraph func
      Q[pointer → points at age]
    end
    A <--> P
    P -->|by reference: passes address| Q
```

> **By value:** function gets a copy — original unchanged.
> **By pointer:** function gets the address — it can modify the original (like `scanf`).

---

## 13. 2D array — address & index map

```
numbers[3][3]        col 0    col 1    col 2
              row 0  [ 1 ]    [ 2 ]    [ 3 ]
              row 1  [ 4 ]    [ 5 ]    [ 6 ]
              row 2  [ 7 ]    [ 8 ]    [ 9 ]

numbers[2][1]  =  row 2, col 1  =  8
numbers[0][0]  =  row 0, col 0  =  1
```

---

## 14. Pointers — the star-shaped key

```
  memory (RAM)
  ┌──────────────┐
  │  age = 30    │  address 0x7ffd12
  └──────────────┘
        ▲
        │
  ┌─────┴──────┐
  │ pAge = 0x7ffd12 │  pAge points AT age
  └────────────┘

  &age   → 0x7ffd12   (address of age)
  *pAge  → 30         (dereference: the value age holds)
```

```mermaid
flowchart LR
    P[pAge] -->|&age| A[age = 30]
    A -->|*pAge| V[value 30]
```

---

## 15. File I/O lifecycle

```mermaid
flowchart TD
    A[fopen path, mode] --> B{pFile == NULL?}
    B -- yes --> E[print error + return 1]
    B -- no --> C{read or write}
    C -- write --> F[fprintf pFile, data]
    C -- read --> G[fgets line until EOF]
    F --> H[fclose pFile]
    G --> H
    H --> D[DONE - file closed, resources freed]
```

---

## 16. Dynamic memory — malloc → use → free

```mermaid
flowchart TD
    A[Determine bytes needed] --> B[malloc / calloc / realloc]
    B --> C{returned NULL?}
    C -- yes --> D[handle failure, exit]
    C -- no --> E[use like an array]
    E --> F[free pointer]
    F --> G[set pointer = NULL to avoid dangling]
    G --> H[DONE]
```

---

## 17. Project logic flowcharts

### A. Circle circumference

```mermaid
flowchart TD
    A[PI = 3.14159] --> B[ask radius r]
    B --> C[circumference = 2 * PI * r]
    C --> D[print result]
```

### B. Hypotenuse calculator

```mermaid
flowchart TD
    A[ask side A] --> B[ask side B]
    B --> C[hyp = sqrt A^2 + B^2]
    C --> D[print hyp]
```

### C. Number guessing game

```mermaid
flowchart TD
    A[srand time NULL] --> B[answer = rand 1-100]
    B --> C[guess = 0, tries = 0]
    C --> D{guess != answer?}
    D -- no --> E[print &quot;You guessed it!&quot;]
    D -- yes --> F[prompt guess, tries++]
    F --> G{guess < answer?}
    G -- yes --> H[print Too low]
    G -- no --> I{guess > answer?}
    I -- yes --> J[print Too high]
    I -- no --> D
    H --> D
    J --> D
```

### D. Rock-paper-scissors

```mermaid
flowchart TD
    A[player picks 1/2/3] --> B[computer = rand 1-3]
    B --> C{map 1→rock 2→paper 3→scissors}
    C --> D{decide winner}
    D -- tie --> E[print Draw]
    D -- player wins --> F[print You win]
    D -- computer wins --> G[print You lose]
```

### E. Digital clock (final project)

```mermaid
flowchart TD
    A[isRunning = true] --> B{isRunning?}
    B -- no --> Z[END]
    B -- yes --> C[rawTime = time NULL]
    C --> D[pTime = localtime rawTime]
    D --> E[print %02d:%02d:%02d with carriage return]
    E --> F[fflush stdout]
    F --> G[sleep 1 sec / Sleep 1000 ms]
    G --> B
```

---

## 18. Beginner's debugging flowchart

```mermaid
flowchart TD
    A[Program won't compile] --> B{Read the FIRST error}
    B --> C{Missing ; or { }?}
    C -- yes --> D[add it, recompile]
    C -- no --> E{undefined main?}
    E -- yes --> F[check spelling: int main]
    E -- no --> G{unknown type?}
    G -- yes --> H[add missing #include e.g. stdbool.h]
    G -- no --> I[google the exact error text]
    D --> J{compiles now?}
    F --> J
    H --> J
    I --> J
    J -- no --> A
    J -- yes --> K[Wrong output? add printf debug lines]
    K --> L[compare against expected values]
```

---

**Companion pages:** [[c-programming/detailed-notes|Detailed notes]] · [[c-programming/projects|Projects]] · [[c-programming/beginners-guide|Beginner's guide]]