// 12_pointers.c — memory addresses, pointers, pass-by-reference
#include <stdio.h>

void birthday(int *age) {   // accepts a POINTER to an int
    (*age)++;               // increment what it points to (modifies original)
}

int main() {
    // --- memory addresses ---
    int age = 30;
    printf("value of age:    %d\n", age);
    printf("address of age:  %p\n", (void*)&age);
    printf("size of age:     %zu bytes\n", sizeof(age));

    // --- pointers ---
    int *pAge = &age;                 // pAge stores the ADDRESS of age
    printf("pAge (address):  %p\n", (void*)pAge);
    printf("*pAge (value):   %d\n", *pAge);   // dereference -> 30

    *pAge = 31;                       // change age through the pointer
    printf("age now: %d\n", age);     // 31

    // --- pass-by-reference ---
    int myAge = 22;
    birthday(&myAge);                 // pass the ADDRESS
    printf("myAge after birthday: %d\n", myAge);  // 23 (actually changed!)

    // --- pointer + struct member access with ->
    struct Point { int x, y; } pt = {3, 7};
    struct Point *pPt = &pt;
    printf("pt via -> : %d, %d\n", pPt->x, pPt->y);  // arrow operator

    return 0;
}