// 22_arena_allocator.c — Arena allocator: batch allocate, batch free
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Simple arena allocator for many short-lived allocations
typedef struct {
    char *memory;     // start of arena buffer
    size_t capacity;  // total allocated bytes
    size_t offset;    // next free position
} Arena;

// Create a new arena with given capacity (in bytes)
Arena *arena_create(size_t capacity) {
    Arena *a = malloc(sizeof(Arena));
    if (!a) return NULL;
    
    a->memory = malloc(capacity);
    if (!a->memory) {
        free(a);
        return NULL;
    }
    
    a->capacity = capacity;
    a->offset = 0;
    return a;
}

// Allocate 'size' bytes with 'alignment' alignment from the arena
void *arena_alloc(Arena *a, size_t size, size_t alignment) {
    // Align the current offset up to the required alignment
    size_t mask = alignment - 1;
    size_t aligned = (a->offset + mask) & ~mask;
    
    // Check if we have enough space remaining
    if (aligned + size > a->capacity) {
        return NULL;  // out of space
    }
    
    // Return pointer at the aligned position
    void *ptr = a->memory + aligned;
    
    // Update offset: advance past this allocation + alignment padding
    a->offset = aligned + size;
    
    return ptr;
}

// Reset the arena — free all allocations at once (O(1) "free")
void arena_reset(Arena *a) {
    a->offset = 0;
}

// Destroy the arena — free everything in one go
void arena_destroy(Arena *a) {
    if (a->memory) free(a->memory);
    if (a) free(a);
}

// Example usage: create many objects, then free all at once
int main(void) {
    // Create a 1 KB arena
    Arena *frame = arena_create(1024);
    if (!frame) {
        printf("arena creation failed\n");
        return 1;
    }
    
    // Allocate many small objects
    for (int i = 0; i < 50; i++) {
        // Allocate an int (4 bytes) with 4-byte alignment
        int *val = arena_alloc(frame, sizeof(int), alignof(int));
        if (val == NULL) {
            printf("arena out of space at iteration %d\n", i);
            break;
        }
        *val = i * 2;  // store a value
    }
    
    // Print all allocated values
    printf("Allocated 50 ints in arena:\n");
    // Note: we can't easily iterate the arena without tracking,
    // but we demonstrate the concept by re-allocating and reading
    // In a real use case, you'd store pointers or use a tracking array
    
    // OPTIONAL: reset the arena — all memory freed instantly!
    // arena_reset(frame);  // offset = 0, all previous allocations recycled
    
    // Or destroy everything at once:
    arena_destroy(frame);
    
    printf("Arena: all memory freed in one operation\n");
    return 0;
}