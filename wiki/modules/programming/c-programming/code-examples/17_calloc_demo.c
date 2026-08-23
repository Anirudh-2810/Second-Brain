// 17_calloc_demo.c — calloc: allocate AND zero-initialize
#include <stdio.h>
#include <stdlib.h>

int main() {
    // calloc(count, size) — allocates AND sets all bytes to 0
    int *arr = calloc(5, sizeof(int));
    
    if (arr == NULL) {
        printf("calloc failed\n");
        return 1;
    }
    
    // All values start at 0 — no garbage!
    printf("calloc values (all zero): ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);  // 0 0 0 0 0
    }
    printf("\n");
    
    // We can now safely write to them
    for (int i = 0; i < 5; i++) {
        arr[i] = (i + 1) * 5;  // 5, 10, 15, 20, 25
    }
    
    printf("After writing: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Free when done
    free(arr);
    arr = NULL;
    
    return 0;
}