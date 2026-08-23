---
module: "c-programming"
topic: "Solved Practice — Strings (5 problems)"
tags: [programming, c, practice, solved, strings, palindrome, strlen, exam]
last_updated: "2026-08-19"
---

# 06 · Strings — 5 Solved Problems

> String questions = arrays of characters + the hidden `\0`. Five classics: length, reverse, palindrome, vowel count, and library functions.

---

## Problem 6.1 — Predict the output (strlen & the `\0`)

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s1[] = "Hello";
    char s2[] = {'H', 'e', 'l', 'l', 'o'};
    printf("%d\n", strlen(s1));
    printf("%d\n", strlen(s2));      // surprise?
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
5
5
```
(`s2` happens to have a `\0` right after `'o'` in memory here — but that's **luck**, not guaranteed!)

| String | Contents in memory |
|---|---|
| `s1` | `H e l l o \0` — `strlen` counts until `\0` → 5 |
| `s2` | `H e l l o ?` — no `\0` written explicitly |

**Trap to remember:** a proper string **must end in `\0`**. `s2` reads past the array until it finds a zero byte — undefined behavior. Always use double quotes: `"Hello"` auto-appends `\0`.

</details>

---

## Problem 6.2 — String length WITHOUT strlen (write the program)

Write a function that finds the length of a string **without** using `strlen`.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int myStrlen(char s[]) {
    int len = 0;
    while (s[len] != '\0')   // count until the null character
        len++;
    return len;
}
int main() {
    char name[] = "Programming";
    printf("%d\n", myStrlen(name));   // 11
    return 0;
}
```

**Trace for `"ABC"`:** len=0 (s[0]='A') → 1 (s[1]='B') → 2 (s[2]='C') → 3 (s[3]='\0' → stop).

**Key idea:** the `\0` is the string's built-in "end of data" marker.

</details>

---

## Problem 6.3 — Reverse a string (write the program)

Write a program to **reverse** the string `"hello"` → `"olleh"`.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s[] = "hello";
    int n = strlen(s);
    for (int left = 0, right = n - 1; left < right; left++, right--) {
        char t = s[left]; s[left] = s[right]; s[right] = t;   // swap ends
    }
    printf("%s\n", s);   // olleh
    return 0;
}
```

| left | right | swap |
|---|---|---|
| 0 | 4 | h ↔ o → `oellh` |
| 1 | 3 | e ↔ l → `olleh` |
| 2 | 2 | stop |

**Key idea:** same two-pointer trick as the array reverse; `n-1` because the last *character* is before `\0`.

</details>

---

## Problem 6.4 — Palindrome check (write the program)

Check if a string is a **palindrome** (reads same forwards and backwards: `"madam"`, `"racecar"`).

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
#include <string.h>
int main() {
    char s[] = "madam";
    int n = strlen(s), isPal = 1;
    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - 1 - i]) { isPal = 0; break; }
    }
    if (isPal) printf("Palindrome\n");
    else       printf("Not a palindrome\n");
    return 0;
}
```

**Trace for `"madam"`:**

| i | s[i] | s[n-1-i] | match? |
|---|---|---|---|
| 0 | m | m | ✔ |
| 1 | a | a | ✔ |

**Key idea:** only check the first **half** (`i < n/2`); compare mirror characters `s[i]` vs `s[n-1-i]`. If any mismatch → not a palindrome.

</details>

---

## Problem 6.5 — Count vowels & string functions (write the program)

Count the number of **vowels** in a string.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
#include <ctype.h>       // tolower
int main() {
    char s[] = "Programming in C";
    int count = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = tolower(s[i]);        // handle uppercase too
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            count++;
    }
    printf("Vowels: %d\n", count);     // a,i,i,i = 4
}
```

**Bonus (library round-up):**

| Task | Code |
|---|---|
| copy | `strcpy(dest, src)` |
| compare | `strcmp(a, b) == 0` |
| uppercase | `strupr(s)` |
| lowercase | `strlwr(s)` |
| append | `strcat(dest, src)` |
| first n chars | `strncmp(a, b, 3)` |

**Trap:** `scanf("%s")` stops at spaces — `"Programming in C"` would read only `"Programming"`. Use `fgets`.

</details>

---

**Next:** [[c-programming/practice/07-functions-recursion|07 · Functions & recursion]] · **Index:** [[c-programming/practice/README|Problem bank]]