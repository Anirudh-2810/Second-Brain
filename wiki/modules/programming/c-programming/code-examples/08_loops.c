// 08_loops.c — while / do while / for / nested loops
#include <stdio.h>

int main() {
    // --- while: check first ---
    int i = 1;
    while (i <= 5) {
        printf("%d ", i);
        i++;
    }
    printf("\n");   // 1 2 3 4 5

    // --- do while: runs at least once ---
    int number;
    do {
        printf("Enter a positive number: ");
        scanf("%d", &number);
    } while (number <= 0);
    printf("You entered %d\n", number);

    // --- for ---
    for (int j = 1; j <= 5; j++) {
        printf("%d ", j);
    }
    printf("\n");   // 1 2 3 4 5

    // --- break & continue ---
    for (int k = 1; k <= 10; k++) {
        if (k == 5) continue;   // skip 5
        if (k == 8) break;      // stop at 8
        printf("%d ", k);
    }
    printf("\n");   // 1 2 3 4 6 7

    // --- nested loops: multiplication table ---
    for (int r = 1; r <= 5; r++) {          // rows
        for (int c = 1; c <= 5; c++) {      // columns
            printf("%2d ", r * c);
        }
        printf("\n");
    }

    return 0;
}