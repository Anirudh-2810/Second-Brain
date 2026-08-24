// 07_conditionals.c — if / nested if / switch / ternary
#include <stdio.h>
#include <stdbool.h>

int main() {
    // --- if / else if / else ---
    int age = 21;
    if (age >= 18) {
        printf("Adult\n");
    } else if (age >= 13) {
        printf("Teenager\n");
    } else {
        printf("Child\n");
    }

    // --- logical operators ---
    bool isSunny = true, isRaining = false;
    if (isSunny && !isRaining) printf("Let's go outside!\n");

    int temp = 35;
    if (temp < 0 || temp > 40) printf("Stay inside.\n");

    // --- nested if (movie tickets: 10% student, 20% senior, 30% both) ---
    double price = 10.00;
    bool isStudent = true, isSenior = true;

    if (isStudent) {
        price *= 0.9;
        if (isSenior) {
            price *= 0.8;                 // total 30% -> $7, not $7.20
        }
    } else if (isSenior) {
        price *= 0.8;
    }
    printf("Ticket price: $%.2f\n", price);

    // --- switch ---
    char grade = 'B';
    switch (grade) {
        case 'A': printf("Excellent!\n"); break;
        case 'B': printf("Good job.\n");  break;
        case 'C': printf("Okay.\n");      break;
        default:  printf("Invalid\n");
    }

    // --- ternary ---
    int x = 10, y = 5;
    int max = (x > y) ? x : y;
    printf("max = %d\n", max);

    return 0;
}