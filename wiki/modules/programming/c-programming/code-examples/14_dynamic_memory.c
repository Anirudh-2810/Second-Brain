// 14_dynamic_memory.c — malloc, calloc, realloc, free
#include <stdio.h>
#include <stdlib.h>

int main() {
    // ---- malloc: allocate, contents uninitialized ----
    int *grades = malloc(sizeof(int) * 5);
    if (grades == NULL) {
        printf("Allocation failed.\n");
        return 1;
    }
    for (int i = 0; i < 5; i++) grades[i] = i * 10;
    for (int i = 0; i < 5; i++) printf("%d ", grades[i]);
    printf("\n");

    // ---- calloc: allocate, zero-initialized ----
    int *scores = calloc(5, sizeof(int));     // all zeros
    if (scores == NULL) {
        printf("Allocation failed.\n");
        free(grades);
        return 1;
    }
    for (int i = 0; i < 5; i++) printf("%d ", scores[i]);
    printf("\n");

    // ---- realloc: resize ----
    scores = realloc(scores, sizeof(int) * 10);   // grow to 10
    if (scores == NULL) {
        printf("Reallocation failed.\n");
        free(grades);
        return 1;
    }
    scores[9] = 99;
    printf("scores[9] = %d\n", scores[9]);

    // ---- free + set to NULL (avoid dangling pointers) ----
    free(grades);
    grades = NULL;
    free(scores);
    scores = NULL;

    printf("Memory freed.\n");
    return 0;
}