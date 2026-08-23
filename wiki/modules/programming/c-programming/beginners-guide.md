---
module: "c-programming"
topic: "C Programming — Beginner's Guide"
tags: [programming, c, beginner, setup, tutorial]
source: "https://www.youtube.com/watch?v=xND0t1pr3KY"
last_updated: "2026-08-19"
---

# C Programming — Beginner's Guide

> Everything you need to go from zero to *"I ran my first C program"* — with zero jargon. Follow the steps in order.

---

## 1. What do you need to write C?

Exactly **two things**:

1. **An IDE** — *Integrated Development Environment*. A workspace (like a fancy notepad) where you write your code.
2. **A C compiler** — a program that **translates your C code into machine code** (0s and 1s) so the computer can actually run it.

> Think of it like cooking: the IDE is your kitchen and utensils, the compiler is the oven that turns your raw ingredients (source code) into a finished meal (running program).

---

## 2. Install an IDE (Visual Studio Code)

1. Go to `code.visualstudio.com` and click the blue **Download** button.
2. Choose the download for your operating system (Windows / Mac / Linux).
3. Open the installer, read the license, accept it, and click **Next → Next → Install → Finish**.
4. VS Code opens. Now create a project folder:
   - Left toolbar → **Explorer** (top icon) → **Open Folder** (or create a new one).
   - Pick a location, create a folder (e.g. `coding`), select it.
5. Create your first C file:
   - In the Explorer, click **New File**, name it **`main.c`** (the name `main` is a convention — it holds the *main* body of your program).
6. Install two extensions (left toolbar → **Extensions**):
   - **C/C++ extension pack** — gives autocomplete, syntax highlighting, etc.
   - **Code Runner** — lets you run your program with one click.

### Code Runner settings (recommended)

File → Preferences → Settings → search `code runner`:

- ✔ **Clear Previous Output** — clears old output before each run.
- ✔ **Save File Before Run** — no manual saving before running.

---

## 3. Install a C compiler

### Check if you already have one

Open the terminal inside VS Code: **Terminal → New Terminal**, then type:

| OS | Command |
|---|---|
| Windows | `gcc --version` |
| Mac | `clang --version` |
| Linux | `gcc -v` |

If you see an error like *"gcc is not recognized"*, you need to install one.

### Windows → MSYS2 (the easy way)

1. Download the **MSYS2** installer from `msys2.org`.
2. Run it: **Next → Next → Install → Finish**. (Requires 64-bit Windows 10+.)
3. In the MSYS2 terminal, copy-paste this command (yes it's long — just copy it):

   ```
   pacman -S mingw-w64-ucrt-x86_64-gcc
   ```

   - `pacman` = the **pa**cka**g**e **man**ager (not the arcade game!)
   - `-S` = **S**ync (download and install)
   - Press **Y** to proceed.
4. Verify: type `gcc --version` — you should see the compiler version.
5. **Add it to your PATH** so VS Code can find it:
   - Copy the path `C:\msys64\ucrt64\bin` (or wherever MSYS2 installed).
   - Windows → search "environment variables" → Edit the **Path** variable → **New** → paste the path → OK. **Restart VS Code** afterward.

> ⚠️ This PATH step is the #1 cause of "gcc is not recognized" after installing MSYS2. Do not skip it.

### Mac

Run `xcode-select --install` in the terminal. This installs `clang`, the C compiler, plus dev tools.

### Linux (Debian/Ubuntu)

```bash
sudo apt-get update          # refresh the package list
sudo apt-get install build-essential gdb   # installs compiler, make, and debugger
```

---

## 4. Your very first program

Type this into `main.c`:

```c
#include <stdio.h>

int main()
{
    printf("Hello, world!\n");
    return 0;
}
```

**Line by line (for beginners):**

| Line | What it does |
|------|--------------|
| `#include <stdio.h>` | Pulls in the **standard input/output** library so we can use `printf` (print formatted). |
| `int main()` | Defines the **main function** — the entry point of every C program. Without it, the program won't run. |
| `{ ... }` | The curly braces mark the **body** of the function — the code that runs. |
| `printf("...");` | **Prints** text to the screen. `\n` means *new line* (like pressing Enter). |
| `return 0;` | Tells the operating system the program finished successfully. |
| `;` | Every **statement** in C ends with a semicolon. Forget it → compiler error! |

### Run it!

- **Code Runner:** click the ▶ **Run** button (top-right) or press `Ctrl+Alt+N`.
- **Terminal (manual):**
  ```bash
  gcc main.c -o main     # compile: main.c → executable named "main"
  ./main                 # run it (Windows: main.exe)
  ```

You should see: `Hello, world!`

---

## 5. Compile vs. run (the mental model)

```
 main.c (you write this)
    │
    │  1. COMPILE  gcc main.c -o main
    ▼
 main.exe / main   (machine code the computer understands)
    │
    │  2. RUN      ./main
    ▼
  OUTPUT printed to the screen
```

> **Fix-as-you-go rule:** compile often. A compiler error is the computer *helping* you — it tells you the exact line and what's wrong.

---

## 6. The 3 most common beginner errors (and fixes)

| Error message | Cause | Fix |
|---|---|---|
| `error: expected ';' ...` | Forgot the semicolon | Add `;` at the end of the statement |
| `error: 'main' must return int` / `undefined reference to main` | No `main()` function, or typo | Make sure you typed `int main()` exactly |
| `'gcc' is not recognized...` | Compiler not installed / not on PATH | Do the MSYS2 + PATH steps above, restart VS Code |
| `error: unknown type name 'bool'` | Missing `stdbool.h` | Add `#include <stdbool.h>` |
| Everything works but output is cut off | No `\n` at the end | Add `\n` inside the `printf` string |

---

## 7. Your first practice challenge

Write a program that prints **three lines**:

```
Hello Bro Code!
Your favorite food is ...
Your favorite number is ...
```

Then modify it to print **your name**, **your age**, and **your email** each on its own line.

> **Hint:** you only need three `printf` statements and `\n` after each line.

---

## 8. Where to go next

1. Read the [[c-programming/detailed-notes|detailed notes]] for every concept in order.
2. Build the [[c-programming/projects|projects]] — start with the circle circumference calculator.
3. Use the [[c-programming/flowcharts|flowcharts]] to visualize each idea before coding it.
4. Try the practice problems in [[cs50/index|CS50x]] to test yourself.