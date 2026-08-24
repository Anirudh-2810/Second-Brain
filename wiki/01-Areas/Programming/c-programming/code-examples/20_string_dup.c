// 20_string_dup.c — Duplicate a string using malloc (common pattern)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *original = "Hello, world!";
    
    // 1. Determine length (strlen excludes null terminator)
    size_t len = strlen(original);
    
    // 2. Allocate memory for the string + null terminator
    char *copy = malloc((len + 1) * sizeof(char));
    if (copy == NULL) {
        printf("malloc failed\n");
        return 1;
    }
    
    // 3. Copy the string content (strcpy includes null terminator)
    strcpy(copy, original);
    
    // 4. Now we can modify copy independently
    // For example, make it uppercase (strlwr/strupr not standard, so do manually):
    for (size_t i = 0; i < len; i++) {
        if (copy[i] >= 'a' && copy[i] <= 'z') {
            copy[i] = copy[i] - 'a' + 'A';
        }
    }
    
    printf("Original: %s\n", original);
    printf("Modified: %s\n", copy);
    
    // 5. Free both when done (they are independent allocations)
    free(original);   // if original was also malloc'd
    free(copy);
    
    return 0;
}