// 23_goto_cleanup.c — goto cleanup pattern for error handling
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Demonstrates the "goto cleanup" pattern:
// Ensures every error path frees resources properly.
// Order: free in reverse order of allocation (LIFO).

int process_files(const char *path1, const char *path2) {
    FILE *f1 = NULL;
    FILE *f2 = NULL;
    char *buffer1 = NULL;
    char *buffer2 = NULL;
    int result = -1;
    
    // Open first file for reading
    f1 = fopen(path1, "r");
    if (!f1) { perror("fopen path1"); goto cleanup; }
    
    // Open second file for reading
    f2 = fopen(path2, "r");
    if (!f2) { perror("fopen path2"); goto cleanup; }
    
    // Allocate buffers
    fseek(f1, 0, SEEK_END);
    long size1 = ftell(f1);
    fseek(f1, 0, SEEK_SET);
    buffer1 = malloc(size1 + 1);  // +1 for null terminator
    if (!buffer1) { perror("malloc buffer1"); goto cleanup; }
    
    fseek(f2, 0, SEEK_END);
    long size2 = ftell(f2);
    fseek(f2, 0, SEEK_SET);
    buffer2 = malloc(size2 + 1);
    if (!buffer2) { perror("malloc buffer2"); goto cleanup; }
    
    // Read files
    if (fread(buffer1, 1, size1, f1) != (size_t)size1) {
        perror("fread path1"); goto cleanup;
    }
    if (fread(buffer2, 1, size2, f2) != (size_t)size2) {
        perror("fread path2"); goto cleanup;
    }
    
    buffer1[size1] = '\0';
    buffer2[size2] = '\0';
    
    // Success! Set result and fall through to cleanup
    result = 0;
    
    // (In a real program, we'd process the buffers here,
    // then fall through to cleanup, or return early with a flag)
    
cleanup:
    // Reverse order of allocation (LIFO — last allocated, first freed)
    free(buffer2);
    free(buffer1);
    if (f2) fclose(f2);
    if (f1) fclose(f1);
    
    return result;
}

int main(void) {
    int status;
    
    // Success case
    status = process_files("test1.txt", "test2.txt");
    if (status == 0) {
        printf("Both files processed successfully\n");
    } else {
        printf("Error processing files (one or both may not exist)\n");
    }
    
    // If path1 doesn't exist, all resources are still freed correctly
    // thanks to the goto cleanup pattern
    
    return 0;
}