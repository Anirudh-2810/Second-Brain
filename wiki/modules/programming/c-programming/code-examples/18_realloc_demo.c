// 18_realloc_demo.c — realloc: resize existing allocation
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Start with 5 integers
    int *nums = malloc(5 * sizeof(int));
    if (nums == NULL) {
        printf("initial malloc failed\n");
        return 1;
    }
    
    // Initialize
    for (int i = 0; i < 5; i++) {
        nums[i] = (i + 1) * 10;  // 10, 20, 30, 40, 50
    }
    
    printf("Original (5 elements): ");
    for (int i = 0; i < 5; i++) printf("%d ", nums[i]);
    printf("\n");
    
    // Grow to 10 integers — realloc preserves old data, adds new uninitialized space
    int *tmp = realloc(nums, 10 * sizeof(int));
    if (tmp == NULL) {
        // realloc failed — original block is still valid, don't free nums!
        printf("realloc failed — keeping original size\n");
        free(nums);
        return 1;
    }
    
    nums = tmp;  // success — update pointer
    
    // New spots (5-9) are uninitialized — initialize them
    for (int i = 5; i < 10; i++) {
        nums[i] = (i + 1) * 10;  // 60, 70, 80, 90, 100
    }
    
    printf("After realloc to 10: ");
    for (int i = 0; i < 10; i++) printf("%d ", nums[i]);
    printf("\n");
    
    // Set nums[9] explicitly as shown in course
    nums[9] = 99;
    
    printf("nums[9] = %d\n", nums[9]);
    
    // Free both when done
    free(nums);
    nums = NULL;
    
    return 0;
}