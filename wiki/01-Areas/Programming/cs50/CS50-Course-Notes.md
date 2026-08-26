---
course_code: "CS50"
course_name: "Harvard's Introduction to Computer Science"
unit: "Weeks 0-8"
tags: [cs50, programming, education, notes]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\Desktop\Anirudh\obsidian notes\Mylife101\vault\02_Dev_Notes\CS50"
description: "Complete CS50 course notes covering Weeks 0-8: binary/ASCII, compilation pipeline, memory layout, asymptotic notation, sorting algorithms, virtual memory, linked lists/hashes/tries, C-Python differences, databases, and web programming. Extracted from personal Obsidian vault notes."
---

# CS50 Course Notes — Weeks 0-8

> **Source:** `C:\Users\Vijaykumar\Desktop\Anirudh\obsidian notes\Mylife101\vault\02_Dev_Notes\CS50`
> **Course:** Harvard's CS50 (Introduction to Computer Science)
> **Scope:** Weeks 0 through 8 (binary to web programming)
> **Confidence:** high (personal notes from lectures)

---

## For future agent
This is a **complete CS50 course notes** module — all 8 weeks of lecture notes extracted from personal Obsidian vault. Covers foundational computer science concepts: binary/ASCII, compilation, memory management, algorithms, data structures, virtual memory, C/Python differences, SQL, and web programming (HTML/CSS/JS). Designed as a revision guide for the CS50 curriculum. Cross-links: [[wiki/01-Areas/Programming]], [[brain/Patterns/agent-pipeline-patterns]].

---

## Week 0 — Binary & Computational Thinking

### Number Systems
- **Binary:** Base-2 representation using digits 0 and 1
- **Decimal:** Base-10 (our everyday system)
- **Hexadecimal:** Base-16, uses digits 0-9 and A-F

### ASCII & Unicode
- **ASCII:** 7-bit character encoding (128 characters: A-Z, a-z, 0-9, punctuation, control chars)
- **Unicode:** Supports millions of characters from all writing systems; UTF-8 is the most common encoding
- **Key difference:** ASCII is a subset of Unicode

### Search Algorithms
- **Linear Search:** Check each element sequentially — O(n) time
- **Binary Search:** Requires **sorted** array; repeatedly divide search interval in half — O(log n) time

### Scratch ↔ C Mapping
| Scratch Concept | C Equivalent |
|----------------|--------------|
| Variable | `int`, `char`, `float`, `double` |
| Condition (`if`) | `if` statement |
| Loop (`repeat`) | `for`/`while` loop |
| Output (`say`) | `printf` |

---

## Week 1 — Compilation & Primitive Types

### Compilation Pipeline
1. **Pre-processing:** `#include`, `#define`, `#ifdef` → removes headers, macros
2. **Compilation:** Translates preprocessed code to assembly
3. **Assembly:** Assembly → machine code (object file)
4. **Linking:** Combines object files + libraries → executable

### Primitive Types (C)
| Type | Size | Range (typical) |
|------|------|-----------------|
| `bool` | 1 byte | 0 or 1 |
| `char` | 1 byte | -128 to 127 or 0 to 255 |
| `int` | 4 bytes | -2¹⁴⁺¹ to 2¹⁴⁻¹ |
| `long` | 8 bytes | larger range |
| `float` | 4 bytes | ~7 decimal digits precision |
| `double` | 8 bytes | ~15 decimal digits precision |
| `string` | — | Actually `char[]` (null-terminated) |

### Common Pitfalls
- **Overflow:** When value exceeds type's max (e.g., `int` max = 2,147,483,647)
- **Truncation:** Assigning a `double` to `int` drops decimal part silently
- **Floating-point imprecision:** `0.1 + 0.2 ≠ 0.3` in binary floating point

---

## Week 2 — Memory Layout & Strings

### Contiguous Memory Layout
- **Array:** Elements stored adjacent in memory, same type
- **`argc/argv`:** `argc` = argument count, `argv` = array of strings (char*)
  - `argv[0]` = program name
  - `argv[1]` = first argument, etc.
  - `argv[argc]` = `NULL` (sentinel)

### Strings in C
- **Null-terminated:** String ends with `'\0'` character
- **`strlen()`:** Returns length excluding the `'\0'`
- **`strcpy()`:** Copies including the `'\0'` — **dangerous** (buffer overflow risk)
- **`strcat()`:** Concatenates strings with buffer overflow risk

### Key Concept: `char name[]` vs `char *name`
- `char name[]` = array allocated on stack, exact size
- `char *name` = pointer, needs memory allocation (`malloc`) or string literal assignment

---

## Week 3 — Asymptotic Notation & Sorting

### Big-O, Big-Omega, Big-Theta
| Notation | Meaning |
|----------|---------|
| **Big-O (O)** | Upper bound: "worst-case" growth rate |
| **Big-Omega (Ω)** | Lower bound: "best-case" growth rate |
| **Big-Theta (Θ)** | Tight bound: both upper AND lower (average case) |

### Common Complexities (from fastest to slowest)
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

### Sorting Algorithms
| Algorithm | Best | Average | Worst | Stable? | In-place? |
|-----------|------|---------|-------|---------|-----------|
| **Selection Sort** | O(n²) | O(n²) | O(n²) | No | Yes |
| **Bubble Sort** | O(n) (optimized) | O(n²) | O(n²) | Yes | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | Yes | No (requires temp) |

### Key Insight
- **Merge Sort:** Always O(n log n) but requires auxiliary memory
- **Bubble Sort:** Optimized version can exit early if no swaps → O(n) best case
- **Selection Sort:** Always O(n²) but minimal writes (good for EEPROM/flash)

---

## Week 4 — Virtual Memory & Pointers

### Memory Layout
```
┌─────────────────────────────────────┐
│    Kernel Space (protected)         │
│   — Device drivers, OS code         │
├─────────────────────────────────────┤
│           Stack (grows down)        │
│   — Local variables, return addr   │
├─────────────────────────────────────┤
│           Heap (grows up)           │
│   — Dynamic allocation (malloc)     │
├─────────────────────────────────────┤
│    User Space (your program)        │
│   — Global/static variables         │
└─────────────────────────────────────┘
```

### Pointer Operators
- **`&` (address-of):** Returns the memory address of a variable
  - Example: `int *p = &x;` → `p` holds address of `x`
- **`*` (dereference):** Accesses the value at a memory address
  - Example: `*p = 10;` → stores 10 at the address `p` points to

### Null Pointers
- `NULL` or `0` — pointer that doesn't point to any valid memory
- **Dereferencing NULL** → Segmentation Fault (crash)
- **Best practice:** Always check `if (p != NULL)` before dereferencing

### `malloc` & `free`
```c
int *arr = (int *)malloc(n * sizeof(int));
// Use arr...
free(arr);  // Returns memory to heap
```
- **Always pair `malloc` with `free`** → prevents memory leaks
- **After `free`, set `arr = NULL`** → dangling pointer prevention

### `valgrind` Memory Error Categories
1. **Invalid read:** Accessing uninitialized or freed memory
2. **Invalid write:** Writing to uninitialized or freed memory
3. **Leaked memory:** Allocated but never freed
4. **Mismatched allocation/deallocation:** `new`/`delete` mismatch, `malloc`/`free` mismatch

---

## Week 5 — Linked Lists, Hash Tables, Tries

### Linked Lists (Singly)
```
struct node {
    int data;
    struct node *next;  // pointer to next node
};
```
- **Insert at head:** O(1)
- **Insert at tail:** O(n) unless we maintain a `tail` pointer
- **Delete:** O(n) (need predecessor pointer)
- **Search:** O(n)

### Hash Tables (Separate Chaining)
- **Hash function:** `h(k) = k % size` maps key to bucket index
- **Collision resolution:** Each bucket is a linked list
- **Load factor:** `α = n / m` (n = items, m = buckets)
- **Good hash function:** Uniform distribution, minimal collisions
- **Resize:** When α exceeds threshold, rehash into larger table

### Tries (Prefix Trees)
```
root → 'a' → 'p' → 'p' → 'l' → 'e'
```
- **Insert:** Traverse characters, create nodes as needed
- **Search:** Traverse characters, check if end node marks word end
- **Delete:** Similar to insert, remove nodes that are no longer needed
- **Space:** Can be large (each node has multiple children pointers)
- **Use case:** Auto-complete, dictionary/word lookup, IP routing

### Complexity Comparison
| Operation | Hash Table | Trie |
|-----------|------------|------|
| Insert | O(1) avg | O(k) where k = key length |
| Search | O(1) avg | O(k) |
| Delete | O(1) avg | O(k) |
| Space | O(n) | O(n × alphabet size) |

---

## Week 6 — C vs Python & Databases

### C vs Python Architectural Differences
| Aspect | C | Python |
|--------|---|--------|
| **Memory Management** | Manual (`malloc`/`free`) | Automatic (garbage collector) |
| **Data Types** | Static, declared at compile time | Dynamic, inferred at runtime |
| **Arrays** | Fixed size, contiguous memory | Lists: dynamic, heterogeneous |
| **Strings** | Null-terminated `char[]` | Immutable `str`, many built-in methods |
| **Memory Layout** | Explicit (stack/heap) | Abstracted (private heap) |
| **Performance** | Faster (close to metal) | Slower (interpreted) but more productive |

### Python Data Structures (CS50 View)
- **Lists:** Dynamic arrays (0-indexed), `append()`, `pop()`, `sort()`
- **Dictionaries:** Hash tables, `O(1)` average lookup, `key → value`
- **Sets:** Unordered, unique elements, `O(1)` membership test
- **Example:** `d = {"name": "Alice", "age": 25}` → `d["name"]` → `"Alice"`

### Safe File I/O with `with` Context Manager
```python
# Always closes file, even if error occurs
with open("filename.txt", "r") as f:
    content = f.read()
# File automatically closed here — no need for f.close()
```

---

## Week 7 — Databases (SQL)

### Normalisation & ACID Properties
- **ACID:** Atomicity, Consistency, Isolation, Durability
- **Normalisation:** Process of organizing tables to reduce redundancy
  - **1NF:** Atomic values, no repeating groups
  - **2NF:** 1NF + non-key attributes fully dependent on primary key
  - **3NF:** 2NF + no transitive dependency on primary key

### SQL Joins
| Join Type | Description |
|-----------|-------------|
| **INNER JOIN** | Rows where match exists in BOTH tables |
| **LEFT JOIN** | All from left table + matching from right (NULL if no match) |
| **RIGHT JOIN** | All from right table + matching from left (NULL if no match) |
| **FULL JOIN** | All rows from both tables (UNION of left + right) |

### SQL Aggregation
```sql
-- GROUP BY with aggregate functions
SELECT department, COUNT(*), AVG(salary)
FROM employees
GROUP BY department;

-- HAVING vs WHERE
-- WHERE: filters rows BEFORE grouping
-- HAVING: filters groups AFTER grouping
```

### SQL Injection Prevention
- **Never** concatenate user input into SQL queries
- **Use parameterized queries:**
```sql
-- Bad: "SELECT * FROM users WHERE name = '" + userInput + "'"
-- Good: "SELECT * FROM users WHERE name = ?" 
--        params = [userInput]
```

### Example Queries
```sql
-- Select users who enrolled after 2020-01-01
SELECT * FROM users WHERE enrollment_date > '2020-01-01';

-- Count courses per student
SELECT student_id, COUNT(course_id) AS courses_taken
FROM enrollments
GROUP BY student_id
HAVING courses_taken > 3;
```

---

## Week 8 — Web Programming (HTML/CSS/JS)

### HTML Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CS50 Web</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Hello, CS50!</h1>
  <script src="script.js"></script>
</body>
</html>
```

### CSS Box Model
```
┌───────────────────────────────────┐
│         margin (transparent)        │
│  ┌─────────────────────────────┐   │
│  │       border (0.5px solid)   │   │
│  │     padding (10px)          │   │
│  │  ┌──────── content ────────┐ │   │
│  │  │                         │ │   │
│  │  │       content           │ │   │
│  │  └─────────────────────────┘ │   │
│  └─────────────────────────────┘   │
└───────────────────────────────────┘
```
- **margin:** Clears area outside border (transparent)
- **border:** Edge around padding and content
- **padding:** Space between border and content
- **content:** Actual text/picture

### CSS Selectors
- **Element:** `p { color: red; }` — selects all `<p>` elements
- **Class:** `.highlight { background: yellow; }` — selects elements with `class="highlight"`
- **ID:** `#header { font-size: 20px; }` — selects element with `id="header"` (must be unique)
- **Descendant:** `div p { color: blue; }` — `<p>` inside `<div>`
- **Pseudo-class:** `:hover`, `:focus`, `:nth-child()`

### JavaScript Event Handling
```javascript
// Select element and add event listener
const button = document.querySelector("button");

button.addEventListener("click", function() {
  alert("Button clicked!");
});

// Form validation example
const form = document.querySelector("form");
form.addEventListener("submit", function(event) {
  const email = document.querySelector("#email").value;
  if (!email.includes("@")) {
    event.preventDefault();  // Stop form submission
    alert("Please enter a valid email");
  }
});
```

### DOM (Document Object Model)
- **Represents** HTML as a tree of nodes
- **`document.getElementById("id")`** — get single element
- **`document.querySelector(".class")`** — get first matching element
- **`element.innerHTML`** — get/set HTML content
- **`element.setAttribute("name", "value")`** — modify attributes

### Simple Web Page Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CS50 Calculator</title>
  <style>
    .button { padding: 10px; margin: 5px; }
  </style>
</head>
<body>
  <input type="number" id="num1" placeholder="Number 1">
  <input type="number" id="num2" placeholder="Number 2">
  <button class="button" id="add">Add</button>
  <p id="result"></p>

  <script>
    const btn = document.querySelector("#add");
    btn.addEventListener("click", () => {
      const n1 = Number(document.querySelector("#num1").value);
      const n2 = Number(document.querySelector("#num2").value);
      const sum = n1 + n2;
      document.querySelector("#result").innerHTML = "Sum: " + sum;
    });
  </script>
</body>
</html>
```

---

## Cross-References

- [[wiki/01-Areas/Programming]] — Programming domain hub
- [[brain/Patterns/agent-pipeline-patterns]] — Agent pipeline patterns (from Understand-Anything)
- [[wiki/00-Current-Projects/neural-engine]] — Neural network implementation (uses similar CS fundamentals)
- [[wiki/01-Areas/AI-Data]] — AI/ML concepts that build on CS50 foundations

---

## See Also
- [CS50 Official Website](https://cs50.harvard.edu/)
- [CS50 Lecture Videos](https://cs50.harvard.edu/x/2024/ lectures/)
- [CS50 Course Archive](https://cs50.harvard.edu/x/2020/ /2021/ /2022/ /2023/)