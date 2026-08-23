// 02_variables.c — variables & data types
#include <stdio.h>
#include <stdbool.h>   // for bool

int main() {
    // whole numbers
    int age = 21;
    int year = 2026;

    // decimals (float = ~7 digits precision, double = ~15)
    float price = 19.99;
    double pi = 3.141592653589793;

    // single character (single quotes) and string (double quotes)
    char grade = 'A';
    char name[] = "Bro Code";

    // boolean (true / false)
    bool isStudent = true;

    printf("Age:    %d\n", age);
    printf("Price:  %f\n", price);
    printf("Pi:     %lf\n", pi);
    printf("Grade:  %c\n", grade);
    printf("Name:   %s\n", name);
    printf("Student? %d (1=yes)\n", isStudent);

    return 0;
}