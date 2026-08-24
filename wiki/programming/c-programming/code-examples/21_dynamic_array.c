// 21_dynamic_array.c — Dynamic array (growable) using realloc
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Create a dynamic array that starts with capacity 2
    int *arr = malloc(2 * sizeof(int));
    if (arr == NULL) {
        printf("initial allocation failed\n");
        return 1;
    }
    
    size_t capacity = 2;   // current allocated capacity
    size_t size = 0;       // how many elements we've used
    
    // Function to ensure capacity, growing if needed
    // This is a simplified vector push_back
    #define PUSH(val) do { \
        if (size >= capacity) { \
            capacity *= 2; \
            int *tmp = realloc(arr, capacity * sizeof(int)); \
            if (tmp == NULL) { \
                printf("realloc failed at element %zu\n", size); \
                free(arr); \
                return 1; \
            } \
            arr = tmp; \
        } \
        arr[size] = val; \
        size++; \
    } while(0)
    
    // Add elements 1 through 8
    PUSH(10);
    PUSH(20);
    PUSH(30);
    PUSH(40);
    PUSH(50);
    PUSH(60);
    PUSH(70);
    PUSH(80);
    
    printf("Dynamic array has %zu elements:\n", size);
    for (size_t i = 0; i < size; i++) {
        printf("%d ", arr[i]);  // 10 20 30 40 50 60 70 80
    }
    printf("\n");
    
    printf("Allocated capacity: %zu (may be larger than used)\n", capacity);
    
    // Free when done
    free(arr);
    arr = NULL;
    
    return 0;
}