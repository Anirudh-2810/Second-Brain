// 04_input.c — scanf, fgets, and clearing the input buffer
#include <stdio.h>
#include <string.h>

int main() {
    // --- scanf: numbers and single chars ---
    int age;
    double gpa;
    char grade;

    printf("Enter your age: ");
    scanf("%d", &age);            // & = address of age

    printf("Enter your GPA: ");
    scanf("%lf", &gpa);           // %lf for double

    getchar();                    // eat the leftover newline from scanf

    printf("Enter your grade: ");
    scanf("%c", &grade);

    printf("Age: %d, GPA: %.2f, Grade: %c\n", age, gpa, grade);

    // --- fgets: whole lines (strings with spaces) ---
    getchar();                    // clear again
    char name[50];
    printf("Enter your full name: ");
    fgets(name, sizeof(name), stdin);          // read a whole line
    name[strcspn(name, "\n")] = '\0';          // strip trailing newline

    printf("Hello, %s!\n", name);

    return 0;
}