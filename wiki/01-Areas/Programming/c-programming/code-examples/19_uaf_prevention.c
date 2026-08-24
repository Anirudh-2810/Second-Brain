// 19_uaf_prevention.c — Use-After-Free prevention patterns
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Pattern 1: Free then NULL (the golden rule)
void pattern1(void) {
    int *p = malloc(sizeof(int));
    *p = 42;
    printf("Before free: *p = %d\n", *p);
    
    free(p);
    p = NULL;  // GOLDEN RULE: always set to NULL after free
    
    // If we accidentally dereference here, we'll get a predictable
    // crash (NULL dereference) instead of silent corruption
    if (p == NULL) {
        printf("Pointer is NULL — safe to check, but can't dereference\n");
    }
}

// Pattern 2: Copy value before free (avoid UAF)
void pattern2(void) {
    int *p = malloc(sizeof(int));
    *p = 100;
    
    int value = *p;  // copy the value BEFORE freeing
    printf("Copied value: %d\n", value);
    
    free(p);
    p = NULL;
    
    // We still have 'value' — no UAF
    printf("We still use the copied value: %d\n", value);
}

// Pattern 3: Temporary pointer for realloc safety
void pattern3(void) {
    int *p = malloc(5 * sizeof(int));
    if (!p) return;
    
    for (int i = 0; i < 5; i++) p[i] = i * 10;
    
    // realloc: assign to temp first, then update original
    int *tmp = realloc(p, 10 * sizeof(int));
    if (tmp == NULL) {
        // FAILURE: original p is STILL valid! Don't free it incorrectly.
        printf("realloc failed — original block intact\n");
        free(p);  // free the original, not tmp
        return;
    }
    
    p = tmp;  // success: now p points to the bigger block
    
    // Use and free
    free(p);
    p = NULL;
}

int main(void) {
    printf("=== Pattern 1: Free then NULL ===\n");
    pattern1();
    
    printf("\n=== Pattern 2: Copy before free ===\n");
    pattern2();
    
    printf("\n=== Pattern 3: realloc safety ===\n");
    pattern3();
    
    return 0;
}