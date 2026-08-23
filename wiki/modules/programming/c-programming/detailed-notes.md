---
module: "c-programming"
topic: "C Programming — Detailed Notes (every topic)"
tags: [programming, c, notes, reference]
source: "https://www.youtube.com/watch?v=xND0t1pr3KY"
last_updated: "2026-08-19"
---

# C Programming — Detailed Notes

> The complete course, topic by topic, in course order. Each section has the *idea*, the *syntax*, a *runnable example*, and *gotchas*. All code lives in `[[c-programming/code-examples|code-examples/]]`.

---

## 1. Program structure & printing

### The `main` function — every program's entry point

```c
#include <stdio.h>   // pulls in printf, scanf, etc.

int main()           // the entry point; C looks for this first
{
    // your code goes here
    return 0;        // 0 = success to the operating system
}
```

- `#include` **copies** a library (header file) into your program. `<stdio.h>` = **sta**ndard **d**evice **io** — input/output functions.
- Every statement ends with **`;`**.
- `main` is the **entry point**: the computer always starts running your program here.

### `printf` — print formatted text

```c
printf("Hello, world!\n");
```

| Format | Meaning | Example output |
|---|---|---|
| `\n` | new line | moves cursor to next line |
| `\t` | tab (8-space indent) | `A    B` |
| `\"` | double quote inside string | `He said "hi"` |
| `\'` | single quote | `it\'s` |
| `\\` | backslash | `C:\users` |

```c
printf("I like pizza!\n");
printf("It's really good!\n");      // ' is fine, no escape needed
printf("\"I like pizza!\"\n");       // quotes need \"
printf("1\t2\t3\n");                // tabs
```

### Comments — notes to yourself (ignored by compiler)

```c
// single-line comment

/* multi-line
   comment */
```

> **Beginner habit:** comment *what* a tricky block does *before* writing it.

---

## 2. Variables & data types

A **variable** is a named container that stores a value in memory.

```c
int age = 21;                 // whole numbers:  -2,147,483,648 .. 2,147,483,647
float price = 19.99;          // decimal, ~7 digits precision
double pi = 3.141592653589793;// decimal, double precision (more memory, more accurate)
char grade = 'A';             // ONE character, in SINGLE quotes
char name[] = "Bro Code";     // string = array of characters, in DOUBLE quotes
bool isStudent = true;        // true/false  (needs #include <stdbool.h>)
```

| Data type | Size (typical) | Stores | Format specifier |
|---|---|---|---|
| `int` | 4 bytes | whole numbers | `%d` |
| `float` | 4 bytes | decimals (~7 digits) | `%f` |
| `double` | 8 bytes | decimals (~15 digits) | `%lf` / `%f` |
| `char` | 1 byte | one character | `%c` |
| `char[]` | n bytes | a string of characters | `%s` |
| `bool` | 1 byte | `true` / `false` | (print as `%d`) |

> **`char` vs `char[]`:** single quotes `'A'` = one character; double quotes `"AB"` = a string (many characters). A string in C is **an array of characters**.

```c
#include <stdio.h>

int main() {
    int age = 21;
    float price = 19.99;
    char grade = 'A';
    char name[] = "Bro";
    printf("Age: %d\n", age);
    printf("Price: %f\n", price);
    printf("Grade: %c\n", grade);
    printf("Name: %s\n", name);
    return 0;
}
```

**Naming rules:** letters, digits, underscores; can't start with a digit; can't be a keyword (`int`, `return`, ...). Be descriptive: `studentCount`, not `x`.

---

## 3. Format specifiers — full control over output

A **format specifier** = `%` + letter (+ optional modifiers). It tells `printf` *what type* a variable is and *how* to display it.

### The basics

| Specifier | Type |
|---|---|
| `%d` | `int` (decimal) |
| `%f` | `float` |
| `%f` or `%lf` | `double` (use `%lf` for consistency with input) |
| `%c` | `char` |
| `%s` | string (`char[]`) |
| `%ld` | `long` int |
| `%x` | `int` in hexadecimal |

### Width — minimum characters to print

```c
int num1 = 1, num2 = 10, num3 = 100;
printf("%d\n", num1);   // 1
printf("%d\n", num2);   // 10
printf("%d\n", num3);   // 100

printf("%3d\n", num1);  //   1   (padded with 2 spaces to width 3)
printf("%3d\n", num2);  //  10
printf("%3d\n", num3);  // 100   (already 3 wide, no change)
```

### Precision — digits after the decimal

```c
double pi = 3.14159;
printf("%.2f\n", pi);   // 3.14  (2 decimal places)
printf("%.1f\n", pi);   // 3.1
printf("%.4f\n", pi);   // 3.1416 (rounds!)
```

### Combined width.precision

```c
printf("%8.2f\n", price);   // 8 chars wide, 2 decimals → "   19.99"
printf("%02d\n", 7);        // zero-padding → "07" (used for the digital clock!)
printf("%-10d|\n", 42);     // left-align → "42        |"
```

> **Big idea:** width pads with spaces, precision controls decimals, `0` pads with zeros, `-` left-aligns. The **digital clock** project uses `%02d` to show `07:05:09`.

---

## 4. Constants & arithmetic operators

### Constants — values that never change

```c
const float PI = 3.14159;   // can't be reassigned later
PI = 5;   // ❌ ERROR: PI is const
```

### Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | addition | `7 + 3` | `10` |
| `-` | subtraction | `7 - 3` | `4` |
| `*` | multiplication | `7 * 3` | `21` |
| `/` | division | `7 / 3` | `2` (integer division!) |
| `/` | division | `7.0 / 3` | `2.333...` (float division) |
| `%` | modulus (remainder) | `7 % 3` | `1` |

> ⚠️ **Integer division gotcha:** `7 / 3` = `2`, not `2.33`. C truncates. To get decimals, make at least one operand a float/double: `7 / 3.0` or `7.0 / 3`.

```c
int x = 10;
int y = 3;
printf("%d\n", x / y);   // 3  (10/3 truncated)
printf("%.1f\n", x / (float)y);  // 3.3
```

### Operator precedence

```
1. ( )  parentheses
2. *  /  %   (left to right)
3. +  -
```

`x + y * z` → multiply first. Use parentheses when in doubt.

### Augmented assignment operators — shortcut math

| Operator | Means |
|---|---|
| `x += 5` | `x = x + 5` |
| `x -= 5` | `x = x - 5` |
| `x *= 5` | `x = x * 5` |
| `x /= 5` | `x = x / 5` |
| `x %= 5` | `x = x % 5` |
| `x++` | `x = x + 1` (increment) |
| `x--` | `x = x - 1` (decrement) |

```c
int x = 10;
x++;        // 11
x += 5;     // 16
x *= 2;     // 32
```

---

## 5. User input — scanf & fgets

### `scanf` — read typed values (numbers, single chars)

```c
#include <stdio.h>

int main() {
    int age;
    double gpa;
    char grade;

    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter your GPA: ");
    scanf("%lf", &gpa);

    printf("Enter your grade: ");
    scanf(" %c", &grade);          // note the leading space

    printf("Age: %d, GPA: %.2f, Grade: %c\n", age, gpa, grade);
    return 0;
}
```

**Rules that trip up beginners:**

1. **`&` = address-of.** `scanf` needs the *address* of the variable (`&age`), not the value. Strings are the exception — `char name[]` needs **no** `&`.
2. **Match the type:** `double` → `%lf` in `scanf` (float → `%f`, int → `%d`, char → `%c`).
3. **Leading space `" %c"`:** when reading a single character after other input, the leftover newline is still in the buffer. The space tells `scanf` to skip it.
4. **The buffer problem:** after `scanf` for a number, pressing Enter leaves `'\n'` in the input buffer. That leftover newline will be immediately swallowed by the next `scanf("%c")`.

### Clearing the input buffer

```c
int age;
char grade;
printf("Enter age: ");
scanf("%d", &age);
getchar();                  // eat the leftover newline
printf("Enter grade: ");
scanf(" %c", &grade);
```

> `getchar()` reads and discards **one** character. Call it after a `scanf` to flush the stray `'\n'`.

### `fgets` — read a whole line (strings with spaces)

```c
#include <stdio.h>
#include <string.h>

int main() {
    char name[50];
    printf("Enter your full name: ");
    fgets(name, sizeof(name), stdin);   // fgets = "file get string"; stdin = keyboard
    name[strcspn(name, "\n")] = '\0';   // strip the trailing newline
    printf("Hello, %s!\n", name);
    return 0;
}
```

- **Why not `scanf("%s")`?** `scanf` stops at the first space, so `"Bro Code"` would only read `"Bro"`.
- `fgets(name, size, stdin)` reads **up to `size` characters** (or until Enter). `sizeof(name)` auto-computes the size.
- `fgets` **keeps the `\n`** at the end — strip it with `name[strcspn(name, "\n")] = '\0';` or by overwriting the last character.

---

## 6. Math library — `<math.h>`

| Function | Does | Example |
|---|---|---|
| `sqrt(x)` | square root | `sqrt(9)` → `3` |
| `pow(x, y)` | x raised to y | `pow(2, 10)` → `1024` |
| `ceil(x)` | round up | `ceil(3.1)` → `4` |
| `floor(x)` | round down | `floor(3.9)` → `3` |
| `round(x)` | round nearest | `round(3.5)` → `4` |
| `fabs(x)` | absolute value | `fabs(-5)` → `5` |
| `log(x)` | natural log | `log(1)` → `0` |
| `sin(x)` / `cos(x)` / `tan(x)` | trig (x in **radians**) | `sin(0)` → `0` |
| `fmax(a,b)` / `fmin(a,b)` | bigger/smaller of two | `fmax(3,7)` → `7` |

```c
#include <stdio.h>
#include <math.h>

int main() {
    double x = 3.99;
    printf("%f\n", sqrt(9));    // 3.000000
    printf("%.0f\n", ceil(x));  // 4
    printf("%.0f\n", floor(x)); // 3
    printf("%.0f\n", round(x)); // 4
    printf("%f\n", pow(2, 10)); // 1024.000000
    printf("%f\n", fabs(-5));   // 5.000000
    return 0;
}
```

> ⚠️ **Windows note:** sometimes you must compile with `-lm` to link the math library: `gcc main.c -o main -lm`.

---

## 7. String library — `<string.h>`

| Function | Does | Example |
|---|---|---|
| `strlen(s)` | length (excludes `\0`) | `strlen("Hello")` → `5` |
| `strcpy(dest, src)` | copy source into dest | `strcpy(x, y)` |
| `strncpy(dest, src, n)` | copy up to n chars | `strncpy(x, y, 5)` |
| `strcat(dest, src)` | append src to dest | `strcat(x, y)` |
| `strncat(dest, src, n)` | append up to n chars | `strncat(x, y, 2)` |
| `strcmp(a, b)` | compare; 0 if equal | `strcmp(x, y) == 0` |
| `strncmp(a, b, n)` | compare first n chars | `strncmp(x, y, 3)` |
| `strlwr(s)` | to lowercase | `strlwr(x)` |
| `strupr(s)` | to uppercase | `strupr(x)` |

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "Bro";

    printf("%d\n", strlen(str1));        // 5

    strcpy(str1, str2);                  // str1 becomes "Bro"
    printf("%s\n", str1);                // Bro

    strcat(str1, str2);                  // str1 becomes "BroBro"
    printf("%s\n", str1);

    printf("%d\n", strcmp("abc", "abc")); // 0 (equal)
    printf("%d\n", strcmp("abc", "abd")); // negative (a<b)

    strlwr(str2); strupr(str2);
    return 0;
}
```

> **String comparison gotcha:** never use `==` on strings (`str1 == str2` compares *addresses*, not text). Always use `strcmp`.

---

## 8. Decisions — `if`, nested `if`, `switch`, ternary

### `if / else if / else`

```c
int age;
printf("Enter your age: ");
scanf("%d", &age);

if (age >= 18) {
    printf("You are an adult.\n");
} else if (age >= 13) {
    printf("You are a teenager.\n");
} else {
    printf("You are a child.\n");
}
```

### Comparison & logical operators

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal |
| `<`, `>`, `<=`, `>=` | comparisons |
| `&&` | AND (both true) |
| `\|\|` | OR (at least one true) |
| `!` | NOT (flips true/false) |

```c
if (isSunny && !isRaining) printf("Let's go outside!\n");
if (temp < 0 || temp > 40) printf("Stay inside.\n");
```

### Nested `if` — if inside an if

**Example (movie tickets):** students get 10% off, seniors 20%, students *and* seniors 30%.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    double price = 10.00;
    bool isStudent = true;
    bool isSenior = true;

    if (isStudent) {
        price *= 0.9;               // 10% off
        printf("You get a student discount of 10%%.\n");
        if (isSenior) {            // NESTED check
            price *= 0.8;          // total 30% off → $7, not $7.20
            printf("You get a senior discount of 20%%.\n");
        }
    } else if (isSenior) {
        price *= 0.8;
        printf("You get a senior discount of 20%%.\n");
    }

    printf("The price of a ticket is $%.2f\n", price);
    return 0;
}
```

> **The trap:** two *separate* `if`s would apply the senior 20% on top of the discounted $9 → $7.20. Nesting (or else-if) ensures discounts stack on the original price correctly.

### `switch` — many choices, one variable

```c
char grade;
printf("Enter your grade (A/B/C/F): ");
scanf("%c", &grade);

switch (grade) {
    case 'A': printf("Excellent!\n"); break;
    case 'B': printf("Good job.\n");  break;
    case 'C': printf("Okay.\n");      break;
    case 'F': printf("Failed.\n");    break;
    default:  printf("Invalid grade.\n");
}
```

- `switch` compares one value against many `case` labels — cleaner than a chain of `else if`s for *equality* checks.
- **`break` is required** — without it, execution *falls through* to the next case.
- `default` runs if no case matches.

### Ternary operator — one-line if/else

```c
condition ? value_if_true : value_if_false;
```

```c
int x = 10;
int y = 5;
int max = (x > y) ? x : y;     // max = 10
printf("%d\n", max);
```

---

## 9. Loops — `while`, `do while`, `for`, nested

### `while` — check FIRST, maybe run 0 times

```c
int i = 1;
while (i <= 5) {
    printf("%d ", i);
    i++;
}
// 1 2 3 4 5
```

> ⚠️ If you forget `i++`, the condition never becomes false → **infinite loop**.

### `do while` — run at least ONCE, then check

```c
int i = 1;
do {
    printf("%d ", i);
    i++;
} while (i <= 5);
// runs the body, then asks "again?" — perfect for menus & games
```

```c
int number;
do {
    printf("Enter a positive number: ");
    scanf("%d", &number);
} while (number <= 0);     // keep asking until valid
```

### `for` — counter-controlled loop

```c
for (start; condition; update) {
    // body
}
for (int i = 1; i <= 5; i++) {
    printf("%d ", i);
}
// 1 2 3 4 5
```

- `start` runs once.
- `condition` is checked *before* each run (like `while`).
- `update` runs *after* each body run.

### `break` & `continue`

- `break` — jump **out** of the loop entirely.
- `continue` — skip to the **next** iteration (jump back to the condition/update).

```c
for (int i = 1; i <= 10; i++) {
    if (i == 5) continue;    // skip 5
    if (i == 8) break;       // stop at 8
    printf("%d ", i);        // 1 2 3 4 6 7
}
```

### Nested loops — a loop inside a loop (grids & tables)

```c
for (int i = 1; i <= 3; i++) {        // outer loop (rows)
    for (int j = 1; j <= 3; j++) {    // inner loop (columns)
        printf("%d%d ", i, j);
    }
    printf("\n");
}
```

```
11 12 13
21 22 23
31 32 33
```

**Multiplication table (course example):** outer loop prints each row, inner loop prints the products — a 10×10 grid of `i * j`.

> **Convention:** use `i` for the outer loop, `j` for the inner loop (never reuse `i` for both — the inner loop would reset it!).

---

## 10. Functions

A **function** is a reusable block of code you can *call* from anywhere.

### Basic function (no parameters, no return)

```c
#include <stdio.h>

void hello() {                 // void = returns nothing
    printf("Hello!\n");
}

int main() {
    hello();                    // call it
    hello();
    return 0;
}
```

### With parameters & return value

```c
#include <stdio.h>

double square(double x) {
    double result = x * x;
    return result;              // sends a value back
}

int main() {
    double answer = square(4.5);
    printf("Answer: %.2f\n", answer);   // Answer: 20.25
    return 0;
}
```

### Full example: greetings with an age

```c
#include <stdio.h>

void hello(char name[], int age) {
    printf("Hello %s, you are %d years old.\n", name, age);
}

int main() {
    hello("Spongebob", 30);
    hello("Patrick", 35);
    return 0;
}
```

**Vocabulary:** `name[]` and `age` are **parameters** (the "placeholders"); `"Spongebob", 30` are **arguments** (the actual values passed in). C passes arguments **by value** — the function gets a *copy*.

### Function prototypes — declare before you use

If a function is defined *after* `main`, the compiler hasn't seen it yet and errors. Fix with a **prototype** (a forward declaration):

```c
#include <stdio.h>

void hello(char[], int);        // prototype: name, types, semicolon

int main() {
    hello("Spongebob", 30);     // now this works!
    return 0;
}

void hello(char name[], int age) {   // actual definition
    printf("Hello %s, you are %d years old.\n", name, age);
}
```

> Or simply **define the function before `main`** — same effect, less syntax.

---

## 11. Arrays

### 1D arrays — a list of the same type

```c
double prices[] = {5.0, 10.0, 15.0, 25.0, 20.0};
// index:         0     1     2     3     4

printf("%.2f\n", prices[0]);   // 5.00 (first element)
printf("%.2f\n", prices[4]);   // 20.00 (last element)

prices[2] = 99.99;             // change a value

for (int i = 0; i < 5; i++) {
    printf("%.2f\n", prices[i]);   // loop through all
}
```

- **Indexes start at 0.** `prices[0]` is the first element.
- You must declare the size up front (either via the values or `int arr[10];`).
- If you use `sizeof`: `int size = sizeof(prices) / sizeof(prices[0]);`

### 2D arrays — a grid (array of arrays)

```c
int numbers[3][3] = {
    {1, 2, 3},     // row 0
    {4, 5, 6},     // row 1
    {7, 8, 9}      // row 2
};
//           col 0  col 1  col 2

printf("%d\n", numbers[0][0]);   // 1  (row 0, col 0)
printf("%d\n", numbers[2][1]);   // 8  (row 2, col 1)
```

- **Syntax rule:** when initializing a 2D array, you **must give the number of columns** — C needs it to know where each row ends:
  ```c
  int numbers[][3] = { {1,2,3}, {4,5,6} };   // ✔ row count optional
  int numbers[3][] = ...                       // ✘ error
  ```
- Loop through with **nested loops** (row × column).

### Array of strings

```c
char cars[][10] = {"Mustang", "Corvette", "Camaro"};
// each row is a string; [10] = max chars per string

for (int i = 0; i < 3; i++) {
    printf("%s\n", cars[i]);
}
```

> Think: *array of character arrays*. Great for menus and lists of names.

### Swap two values (the classic)

```c
int a = 5, b = 10;
int temp = a;     // temp = 5
a = b;            // a = 10
b = temp;         // b = 5
// now a=10, b=5
```

> You need a **third temporary variable** — you can't just do `a = b; b = a;` (both would become 10).

### Sort an array (selection sort)

```c
int array[] = {3, 1, 4, 1, 5, 9, 2, 6};
int size = sizeof(array) / sizeof(array[0]);

for (int i = 0; i < size - 1; i++) {
    for (int j = i + 1; j < size; j++) {
        if (array[j] < array[i]) {       // found smaller → swap
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
}
// 1 1 2 3 4 5 6 9
```

---

## 12. Structs, typedef & enums

### Structs — bundle different types together

```c
#include <stdio.h>
#include <string.h>

struct Student {
    char name[50];
    float gpa;
    int age;
};

int main() {
    struct Student student1;
    strcpy(student1.name, "Spongebob");
    student1.gpa = 3.2;
    student1.age = 23;

    printf("%s\n", student1.name);
    printf("%.2f\n", student1.gpa);
    printf("%d\n", student1.age);
    return 0;
}
```

- A struct is a **user-defined data type** — it groups related data (name, gpa, age) into one unit.
- Access members with the **dot operator** `.`.
- Copy strings with `strcpy` (can't assign `student1.name = "..."` directly).
- You can have an **array of structs**: `struct Student students[100];`

### typedef — give types nicknames

```c
typedef struct {
    char name[50];
    float gpa;
    int age;
} Student;                 // now "Student" is the type name

int main() {
    Student student1;      // no "struct" keyword needed!
    ...
}
```

`typedef int Pair;` also works for primitive types — it just creates an alias.

### Enums — named constants

```c
#include <stdio.h>

enum Day { SUN, MON, TUE, WED, THU, FRI, SAT };   // SUN=0, MON=1, ...

int main() {
    enum Day today = TUE;
    printf("%d\n", today);   // 2
    return 0;
}
```

- **Enums = enumerations** — a set of named integer constants.
- The tags automatically get values 0, 1, 2, ... (you can override: `enum Day { SUN=1, MON=2, ... };`).
- **Typedef trick** — skip the `enum` keyword every time:

```c
typedef enum { TRUE, FALSE } Status;   // TRUE=0, FALSE=1

Status isOnline = TRUE;                // cleaner
```

**Real-world use:** enum for days of the week + `switch` to print a friendly name, or game states (`PLAYING`, `PAUSED`, `GAME_OVER`).

---

## 13. Random numbers — `rand`, `srand`, `time`

```c
#include <stdio.h>
#include <stdlib.h>      // rand, srand
#include <time.h>        // time

int main() {
    srand(time(NULL));   // seed once — makes numbers differ each run

    int num1 = rand();                       // 0 .. RAND_MAX (usually 32767)
    int num2 = rand() % 6;                   // 0 .. 5      (dice roll!)
    int num3 = rand() % 6 + 1;               // 1 .. 6      (proper dice)
    int num4 = (rand() % 20) + 1;            // 1 .. 20
    printf("%d\n", num3);
    return 0;
}
```

- `rand()` alone gives the **same sequence every run** — boring for games.
- `srand(time(NULL))` seeds it with the current time (seconds since Jan 1, 1970) so it's different each run.
- **Range formula:** `rand() % (max - min + 1) + min`.

> **Why `rand()` is "pseudo-random":** it's a deterministic formula, but seeding with time makes it look random — good enough for games.

---

## 14. Memory addresses & pointers

### Memory addresses — where variables live

Every variable lives at an address in RAM. Get it with `&`:

```c
int age = 30;
printf("%p\n", (void*)&age);   // e.g. 0x7ffe1234 — the memory address
printf("%p\n", (void*)&age);   // same address — &age = "address of age"
```

- Memory is like a giant street with numbered houses (bytes).
- **Hex (`0x...`)** is just base-16, the human-friendly way to show addresses.
- `sizeof(age)` → `4` bytes for an int. Every variable owns a block of consecutive bytes; `&age` is the address of the *first* byte.

### Pointers — variables that store addresses

> **The mental model (from the course):** a pointer is like a **star-shaped key** — it doesn't hold the value itself, it holds the *location* of the value.

```c
int age = 30;
int *pAge = &age;        // pAge = "address of age" (pointer to int)

printf("%p\n", (void*)pAge);   // 0x...  the address
printf("%d\n", *pAge);         // 30  (dereference: follow the key to the value)

*pAge = 31;                    // change age THROUGH the pointer
printf("%d\n", age);           // 31
```

| Symbol | Meaning |
|---|---|
| `*` in declaration | "this is a pointer to..." (`int *pAge`) |
| `&` | address-of operator (`&age`) |
| `*` in use | dereference — follow the address to the value (`*pAge`) |

### Passing pointers to functions (pass-by-reference)

```c
#include <stdio.h>

void birthday(int *age) {   // accept a POINTER
    (*age)++;               // increment what it points to
}

int main() {
    int age = 22;
    birthday(&age);         // pass the ADDRESS
    printf("%d\n", age);    // 23  ← main's variable was actually changed
    return 0;
}
```

- Passing **by value** copies — the function can't change the caller's variable.
- Passing a **pointer (by reference)** lets the function modify the original.
- This is exactly why `scanf("%d", &age)` uses `&` — it modifies your variable from inside the library.

> **Why pointers matter:** passing a huge struct by value copies the *entire* struct (e.g. 24 bytes). Passing a pointer copies just one address — fast. Linked lists, dynamic memory, and file I/O all build on pointers.

---

## 15. File I/O — read & write files

### Writing to a file

```c
#include <stdio.h>

int main() {
    FILE *pFile = fopen("output.txt", "w");   // open for WRITING

    if (pFile == NULL) {                      // always check!
        printf("Unable to open file\n");
        return 1;
    }

    fprintf(pFile, "This is my first file.\n");
    fprintf(pFile, "Line 2 here.\n");

    fclose(pFile);                            // always close!
    printf("File written successfully.\n");
    return 0;
}
```

### Reading from a file

```c
#include <stdio.h>

int main() {
    FILE *pFile = fopen("output.txt", "r");   // open for READING

    if (pFile == NULL) {
        printf("File not found\n");
        return 1;
    }

    char line[100];
    while (fgets(line, sizeof(line), pFile) != NULL) {
        printf("%s", line);                    // print each line
    }

    fclose(pFile);
    return 0;
}
```

| Mode | Meaning |
|---|---|
| `"w"` | write (creates or overwrites) |
| `"r"` | read (file must exist) |
| `"a"` | append (add to the end) |

**The 3 golden rules:**

1. `FILE *pFile = fopen("name", "mode");` — a file pointer.
2. **Always check** `if (pFile == NULL)` before using it.
3. **Always `fclose(pFile)`** when done — release the resources.

> Paths can be relative (`"output.txt"` = same folder) or absolute (`"C:\\Users\\me\\Desktop\\out.txt"`).

---

## 16. Dynamic memory — `malloc`, `calloc`, `realloc`, `free`

Normally array sizes are fixed at compile time. Dynamic memory lets you ask the OS for exactly the amount you need **while the program runs** — and return it.

### `malloc` — allocate memory

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *grades = malloc(sizeof(int) * 5);   // room for 5 ints on the heap

    if (grades == NULL) {                    // allocation failed?
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        grades[i] = i * 10;                  // use it like an array
    }
    for (int i = 0; i < 5; i++) {
        printf("%d\n", grades[i]);
    }

    free(grades);                            // give the memory BACK
    grades = NULL;                           // avoid a "dangling pointer"
    return 0;
}
```

### `calloc` — allocate AND zero-init

```c
int *scores = calloc(5, sizeof(int));   // 5 ints, all starting at 0
// same usage; free(scores); scores = NULL;
```

- `calloc(count, size)` → zero-initialized memory.
- `malloc(size)` → uninitialized memory (may contain garbage).

### `realloc` — resize memory

```c
int *prices = malloc(sizeof(int) * 5);
// ... use it ...
prices = realloc(prices, sizeof(int) * 10);   // grow to 10 ints
// ... use the bigger block ...
free(prices); prices = NULL;
```

- `realloc(ptr, newSize)` moves the data to a bigger block if needed, then returns the new pointer.

### Why `free` + `NULL`?

| Problem | What happens |
|---|---|
| Forgot to `free` | **Memory leak** — your program hoards RAM forever |
| `free` then still using the pointer | **Dangling pointer** — a pointer to memory that's been returned; using it = undefined behavior (can crash) |
| `grades = NULL` after `free` | Safety — dereferencing NULL is a detectable error, dereferencing a dangling pointer is chaos |

> **Memory regions mental model:** your variables live on the **stack** (fast, auto-cleaned). `malloc`/`calloc`/`realloc` allocate on the **heap** (bigger, but *you* must clean up with `free`).

---

## 17. The digital clock (final project preview)

The course's capstone puts *everything* together — `while` loop, `time.h`, structs, pointers, and formatting:

```c
#include <stdio.h>
#include <time.h>
#ifdef _WIN32
  #include <windows.h>
#else
  #include <unistd.h>
#endif

int main() {
    time_t rawTime;
    struct tm *pTime;
    int isRunning = 1;

    while (isRunning) {
        rawTime = time(NULL);              // seconds since Jan 1, 1970
        pTime = localtime(&rawTime);       // convert to a readable struct

        printf("%02d:%02d:%02d\r",         // \r = carriage return (update in place!)
               pTime->tm_hour, pTime->tm_min, pTime->tm_sec);
        fflush(stdout);

#ifdef _WIN32
        Sleep(1000);                       // Windows: 1000 MILLIseconds
#else
        sleep(1);                          // Unix: 1 SECOND
#endif
    }
    return 0;
}
```

**Key ideas:** `time(NULL)` returns a huge `time_t` (seconds since 1970 — the "epoch"); `localtime()` converts it into a `struct tm` with `tm_hour`, `tm_min`, `tm_sec`; `pTime->` is pointer-arrow access to struct members; `%02d` zero-pads; `\r` returns the cursor to the line start so the clock **updates in place**; `Sleep(1000)` (Windows, ms) vs `sleep(1)` (Linux/Mac, seconds) paces the loop.

---

## Quick-reference cheat sheet

```
COMPILE & RUN        gcc main.c -o main && ./main
PRINT                printf("text %d\n", num);
READ NUMBER          scanf("%d", &x);        (double → %lf, float → %f)
READ LINE            fgets(buf, sizeof buf, stdin);
MAIN FORMATS         %d int · %f float · %lf double · %c char · %s string
PRECISION/WIDTH      %.2f · %3d · %02d · %-10s
MATH                 sqrt pow ceil floor round fabs log sin cos tan  (<math.h>)
STRINGS              strlen strcpy strcat strcmp strlwr strupr       (<string.h>)
DECIDE               if/else · switch · cond ? a : b
LOOPS                while(cond) · do{}while(cond) · for(;;) · nested
ARRAY 1D             int a[5];  a[0] ... a[4]
ARRAY 2D             int g[3][3]; g[r][c]  (must state column count)
STRUCT               struct Tag { ... };  tag.member
TYPEDEF              typedef struct {...} Name;
ENUM                 enum Tag { A, B, C };
RANDOM               srand(time(NULL)); rand() % range + min
POINTER              int *p = &x;  *p (deref), &x (address)
FILES                FILE *f = fopen(p, mode); fprintf/fgets; fclose(f);
DYNAMIC              malloc/calloc/realloc(ptr, bytes) + free(ptr); ptr = NULL;
```

See the [[c-programming/flowcharts|flowcharts]] for visual versions of every concept, and [[c-programming/projects|projects]] for the full programs.