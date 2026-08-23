---
module: "c-programming"
topic: "C Programming — 13 Hands-on Projects"
tags: [programming, c, projects, practice]
source: "https://www.youtube.com/watch?v=xND0t1pr3KY"
last_updated: "2026-08-19"
---

# C Programming — 13 Hands-on Projects

> The course teaches by doing: 12 practice projects, ending with a working **digital clock**. Build them in order — each one reuses the previous tools. Full files live in `[[c-programming/code-examples|code-examples/]]`.

| # | Project | Reinforces |
|---|---------|-----------|
| 1 | Circle circumference | constants, `%f`, user input |
| 2 | Hypotenuse calculator | `math.h`, `sqrt`, `pow` |
| 3 | Compound interest | `math.h`, `pow`, `.2f` |
| 4 | Weight converter | `if`, comparisons |
| 5 | Temperature converter | `if/else if`, input validation |
| 6 | Calculator | `switch` |
| 7 | Swap values | temp variable trick |
| 8 | Sort array | nested loops, arrays, swaps |
| 9 | Number guessing game | `rand`, `while`, `do while` |
| 10 | Rock-paper-scissors | `rand`, `switch`, logic |
| 11 | Quiz game | arrays of strings, loops, score |
| 12 | Tic-tac-toe | 2D arrays, functions, game logic |
| 13 | **Digital clock** | `time.h`, structs, pointers, `%02d`, loops |

---

## 1. Circle circumference

```c
#include <stdio.h>
#include <math.h>

int main() {
    const double PI = 3.14159;
    double radius, circumference;

    printf("Enter the radius of a circle: ");
    scanf("%lf", &radius);

    circumference = 2 * PI * radius;

    printf("The circumference is: %.2lf\n", circumference);
    return 0;
}
```

```
Enter the radius of a circle: 5
The circumference is: 31.42
```

**Learn:** `const double PI`, `%lf` for doubles in both `scanf` and `printf`.

---

## 2. Hypotenuse calculator

```c
#include <stdio.h>
#include <math.h>

int main() {
    double sideA, sideB, hyp;

    printf("Enter the length of side A: ");
    scanf("%lf", &sideA);
    printf("Enter the length of side B: ");
    scanf("%lf", &sideB);

    hyp = sqrt(pow(sideA, 2) + pow(sideB, 2));

    printf("The hypotenuse is: %.2lf\n", hyp);
    return 0;
}
```

```
Enter the length of side A: 3
Enter the length of side B: 4
The hypotenuse is: 5.00
```

**Learn:** `sqrt` + `pow` from `<math.h>` — Pythagoras: *a² + b² = c²*.

---

## 3. Compound interest calculator

```c
#include <stdio.h>
#include <math.h>

int main() {
    double balance, rate, years, amount;

    printf("Enter the initial balance: ");
    scanf("%lf", &balance);
    printf("Enter the interest rate (%%): ");
    scanf("%lf", &rate);
    printf("Enter the number of years: ");
    scanf("%lf", &years);

    amount = balance * pow(1 + rate / 100, years);

    printf("Final amount: $%.2lf\n", amount);
    return 0;
}
```

```
Enter the initial balance: 1000
Enter the interest rate (%): 5
Enter the number of years: 2
Final amount: $1102.50
```

**Learn:** compound-interest formula `A = P(1 + r/n)^(nt)` (yearly: `A = P(1 + r)^t`). Note `%%` prints a literal percent sign.

---

## 4. Weight conversion calculator

```c
#include <stdio.h>

int main() {
    char unit;
    double weight;

    printf("Is your weight in (k)g or (l)bs? ");
    scanf("%c", &unit);
    printf("Enter your weight: ");
    scanf("%lf", &weight);

    if (unit == 'k') {
        printf("Weight in lbs: %.2lf\n", weight * 2.2);
    } else if (unit == 'l') {
        printf("Weight in kg: %.2lf\n", weight / 2.2);
    } else {
        printf("Invalid unit.\n");
    }
    return 0;
}
```

**Learn:** a single `char` input branching with `if/else if`.

---

## 5. Temperature converter

```c
#include <stdio.h>

int main() {
    char unit;
    double temp;

    printf("Is the temperature in (C)elsius or (F)ahrenheit? ");
    scanf(" %c", &unit);
    printf("Enter the temperature: ");
    scanf("%lf", &temp);

    if (unit == 'C') {
        double f = (temp * 9 / 5) + 32;
        printf("The temperature in Fahrenheit is: %.1lf\n", f);
    } else if (unit == 'F') {
        double c = (temp - 32) * 5 / 9;
        printf("The temperature in Celsius is: %.1lf\n", c);
    } else {
        printf("Invalid unit.\n");
    }
    return 0;
}
```

```
Is the temperature in (C)elsius or (F)ahrenheit? C
Enter the temperature: 100
The temperature in Fahrenheit is: 212.0
```

**Learn:** conversion formulas; note the **leading space** `" %c"` in `scanf` to skip leftover newlines.

---

## 6. Calculator (switch)

```c
#include <stdio.h>

int main() {
    char op;
    double a, b;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &op);
    printf("Enter two numbers: ");
    scanf("%lf %lf", &a, &b);

    switch (op) {
        case '+': printf("%.2lf\n", a + b); break;
        case '-': printf("%.2lf\n", a - b); break;
        case '*': printf("%.2lf\n", a * b); break;
        case '/':
            if (b == 0) printf("Cannot divide by zero.\n");
            else        printf("%.2lf\n", a / b);
            break;
        default: printf("Invalid operator.\n");
    }
    return 0;
}
```

**Learn:** `switch` for dispatch + the divide-by-zero guard.

---

## 7. Swap values

```c
#include <stdio.h>

int main() {
    int a = 5, b = 10;
    printf("Before: a=%d b=%d\n", a, b);

    int temp = a;
    a = b;
    b = temp;

    printf("After:  a=%d b=%d\n", a, b);
    return 0;
}
```

```
Before: a=5 b=10
After:  a=10 b=5
```

**Learn:** you need a **third temporary variable** — otherwise the first assignment destroys the data you need.

---

## 8. Sort array (selection sort)

```c
#include <stdio.h>

void selectionSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[i]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int array[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int size = sizeof(array) / sizeof(array[0]);

    selectionSort(array, size);

    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");   // 1 1 2 3 4 5 6 9
    return 0;
}
```

**Learn:** nested loops + the swap trick inside a function (arrays auto-pass-by-pointer, so sorting inside the function changes the original).

---

## 9. Number guessing game

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int answer = (rand() % 100) + 1;   // 1..100
    int guess = 0;
    int tries = 0;

    printf("Number Guessing Game!\n");

    while (guess != answer) {
        printf("Guess a number between 1 and 100: ");
        scanf("%d", &guess);
        tries++;

        if (guess < answer) {
            printf("Too low!\n");
        } else if (guess > answer) {
            printf("Too high!\n");
        }
    }

    printf("You guessed it in %d tries!\n", tries);
    return 0;
}
```

**Learn:** `srand(time(NULL))` + `rand() % 100 + 1`, and a `while` loop driven by the answer comparison. (Pro tip from the course: use a **binary search** strategy — always guess the middle.)

---

## 10. Rock, paper, scissors

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int player, computer = (rand() % 3) + 1;   // 1=rock 2=paper 3=scissors

    printf("Rock, Paper, Scissors!\n");
    printf("1) Rock\n2) Paper\n3) Scissors\n");
    printf("Your choice: ");
    scanf("%d", &player);

    // name what was chosen
    char *cName, *pName;
    switch (computer) {
        case 1: cName = "rock";     break;
        case 2: cName = "paper";    break;
        default: cName = "scissors"; break;
    }
    switch (player) {
        case 1: pName = "rock";     break;
        case 2: pName = "paper";    break;
        case 3: pName = "scissors"; break;
        default: printf("Invalid choice.\n"); return 1;
    }

    printf("You chose %s. Computer chose %s.\n", pName, cName);

    if (player == computer) {
        printf("It's a draw!\n");
    } else if ((player == 1 && computer == 3) ||
               (player == 2 && computer == 1) ||
               (player == 3 && computer == 2)) {
        printf("You win!\n");
    } else {
        printf("You lose!\n");
    }
    return 0;
}
```

**Learn:** `rand()` for the computer + `switch` to map numbers to names + win-condition logic (rock beats scissors, paper beats rock, scissors beats paper).

---

## 11. Quiz game

```c
#include <stdio.h>
#include <ctype.h>

int main() {
    char questions[][50] = {
        "What is the largest planet in our solar system?",
        "What is the capital of France?",
        "How many bones are in the adult human body?"
    };
    char options[][50] = {
        "A. Earth", "B. Jupiter", "C. Mars", "D. Saturn",
        "A. Paris", "B. Berlin", "C. Rome", "D. Madrid",
        "A. 106",  "B. 176",     "C. 206",  "D. 306"
    };
    char answers[] = {'B', 'A', 'C'};
    int score = 0, numQ = 3;
    char guess;

    for (int i = 0; i < numQ; i++) {
        printf("\n%s\n", questions[i]);
        for (int j = i * 4; j < i * 4 + 4; j++) {
            printf("%s\n", options[j]);
        }
        printf("Your answer: ");
        scanf(" %c", &guess);
        guess = toupper(guess);

        if (guess == answers[i]) {
            printf("Correct!\n");
            score++;
        } else {
            printf("Wrong! Correct answer: %c\n", answers[i]);
        }
    }
    printf("\nFinal score: %d/%d\n", score, numQ);
    return 0;
}
```

**Learn:** arrays of strings (`questions[][50]`, `options[][50]`), indexing rows of a 2D array (`options[j]` with `j = i*4 .. i*4+3`), `toupper`, and score accumulation.

---

## 12. Tic-tac-toe

```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

char board[3][3];
const char PLAYER = 'X', COMPUTER = 'O';

void resetBoard() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = ' ';
}

void printBoard() {
    printf("\n %c | %c | %c \n", board[0][0], board[0][1], board[0][2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[1][0], board[1][1], board[1][2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[2][0], board[2][1], board[2][2]);
}

int checkFreeSpaces() {
    int spaces = 0;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ' ') spaces++;
    return spaces;
}

void playerMove() {
    int x, y;
    do {
        printf("Enter row (1-3): ");  scanf("%d", &x);
        printf("Enter col (1-3): ");  scanf("%d", &y);
        x--; y--;
    } while (x < 0 || x > 2 || y < 0 || y > 2 || board[x][y] != ' ');
    board[x][y] = PLAYER;
}

void computerMove() {
    int x, y;
    do {
        x = rand() % 3;
        y = rand() % 3;
    } while (board[x][y] != ' ');
    board[x][y] = COMPUTER;
}

char checkWinner() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return board[i][0];                     // row win
        if (board[0][i] != ' ' && board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return board[0][i];                     // column win
    }
    if (board[0][0] != ' ' && board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return board[0][0];                         // main diagonal
    if (board[0][2] != ' ' && board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return board[0][2];                         // anti diagonal
    return ' ';                                     // no winner yet
}

int main() {
    srand(time(NULL));
    resetBoard();
    char winner = ' ';
    int turn = 1;

    while (winner == ' ' && checkFreeSpaces() > 0) {
        printBoard();
        if (turn == 1) { playerMove();   turn = 0; }
        else           { computerMove(); turn = 1; }
        winner = checkWinner();
    }

    printBoard();
    if (winner == PLAYER)   printf("You win!\n");
    else if (winner == COMPUTER) printf("You lose!\n");
    else                    printf("It's a draw!\n");
    return 0;
}
```

**Learn:** a **2D array** as the game board, **functions** for each responsibility (reset/print/move/check), validation loops, and win-checking (rows, columns, diagonals).

---

## 13. Digital clock (final project)

```c
#include <stdio.h>
#include <time.h>
#ifdef _WIN32
  #include <windows.h>
#else
  #include <unistd.h>
#endif

int main() {
    time_t rawTime;              // seconds since the "epoch" (Jan 1 1970)
    struct tm *pTime;            // readable breakdown (hours, minutes, ...)
    int isRunning = 1;

    while (isRunning) {
        rawTime = time(NULL);            // update the raw seconds
        pTime = localtime(&rawTime);     // convert to a time struct

        // %02d zero-pads; \r = carriage return → updates in place
        printf("%02d:%02d:%02d\r",
               pTime->tm_hour, pTime->tm_min, pTime->tm_sec);
        fflush(stdout);

#ifdef _WIN32
        Sleep(1000);                     // Windows: 1000 MILLIseconds
#else
        sleep(1);                        // Linux/Mac: 1 SECOND
#endif
    }
    return 0;
}
```

**Learn (capstone ideas):**
- `time_t` / `time(NULL)` — seconds since Jan 1, 1970 (~1.7 billion).
- `localtime()` returns a **pointer to a `struct tm`** with `tm_hour`, `tm_min`, `tm_sec`.
- The **arrow operator `->`** dereferences a struct pointer and accesses a member.
- `%02d` zero-pads (`07:05:09`), `\r` carriage return makes the clock **update in place**.
- `Sleep(1000)` (Windows, milliseconds) vs `sleep(1)` (Unix, seconds) via `#ifdef _WIN32`.
- `while (isRunning)` gives an explicit exit switch (`isRunning = false`).

---

## Practice checklist

- [ ] Project 1–3 compile and run correctly
- [ ] 4–6 handle invalid input gracefully
- [ ] 7–8: trace the swap/sort by hand on paper before running
- [ ] 9–10: can you predict what `rand() % 3 + 1` can produce?
- [ ] 11–12: modify the quiz questions / board size
- [ ] 13: make the clock print 12-hour format with AM/PM as a stretch goal

**Next steps:** try [[cs50/index|CS50x]] problem sets, or the exam-style drills in [[SPM/c-programming-master-study-guide|the C master study guide]].