// 16_malloc_basic.c — Basic malloc usage with NULL check
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocate memory for 5 integers on the heap
    int *p = malloc(5 * sizeof(int));
    
    // Always check if allocation succeeded
    if (p == NULL) {
        printf("malloc failed — out of memory\n");
        return 1;
    }
    
    // Use like an array (indices 0-4)
    for (int i = 0; i < 5; i++) {
        p[i] = (i + 1) * 10;  // 10, 20, 30, 40, 50
    }
    
    // Print all values
    printf("malloc allocated values: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", p[i]);
    }
    printf("\n");
    
    // ALWAYS free when done — return memory to the heap
    free(p);
    p = NULL;  // prevent dangling pointer
    
    printf("Memory freed and pointer set to NULL\n");
    return 0;
}