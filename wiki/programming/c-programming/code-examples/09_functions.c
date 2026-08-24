// 09_functions.c — functions, parameters, return, prototypes
#include <stdio.h>

// function defined BEFORE main -> no prototype needed
void hello(char name[], int age) {
    printf("Hello %s, you are %d years old.\n", name, age);
}

double square(double x) {
    return x * x;
}

// prototype: declared before main, defined after
int add(int a, int b);

int main() {
    hello("Spongebob", 30);
    hello("Patrick", 35);

    double answer = square(4.5);
    printf("Answer: %.2f\n", answer);   // 20.25

    printf("3 + 7 = %d\n", add(3, 7));  // 10 (works thanks to prototype)
    return 0;
}

// definition AFTER main — the prototype above makes it legal
int add(int a, int b) {
    return a + b;
}