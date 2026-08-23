// 03_formatting.c — format specifiers: width, precision, flags
#include <stdio.h>

int main() {
    // basic specifiers
    int age = 25;
    float price = 19.99;
    double pi = 3.1415926535;
    char currency = '$';
    char name[] = "Bro";

    printf("%d\n", age);          // %d = decimal int
    printf("%f\n", price);        // %f = float
    printf("%lf\n", pi);          // %lf = double
    printf("%c\n", currency);     // %c = char
    printf("%s\n", name);         // %s = string

    // WIDTH: minimum number of characters
    int num1 = 1, num2 = 10, num3 = 100;
    printf("%3d\n", num1);        // "  1"
    printf("%3d\n", num2);        // " 10"
    printf("%3d\n", num3);        // "100"

    // PRECISION: digits after the decimal
    printf("%.2f\n", price);      // 19.99
    printf("%.1f\n", pi);         // 3.1
    printf("%.4f\n", pi);         // 3.1416

    // width + precision combined
    printf("%8.2f\n", price);     // "   19.99"

    // zero padding + left-align
    printf("%02d\n", 7);          // "07"
    printf("%-10d|\n", 42);       // "42        |"

    return 0;
}