// 05_math.c — the <math.h> library
// NOTE: on some Windows setups compile with:  gcc 05_math.c -o math -lm
#include <stdio.h>
#include <math.h>

int main() {
    double x = 3.99;
    double a = 3.0, b = 4.0;

    printf("sqrt(9)   = %.1f\n", sqrt(9));      // 3
    printf("pow(2,10) = %.1f\n", pow(2, 10));   // 1024
    printf("ceil(3.1) = %.0f\n", ceil(3.1));    // 4
    printf("floor     = %.0f\n", floor(x));     // 3
    printf("round(3.5)= %.0f\n", round(3.5));   // 4
    printf("fabs(-5)  = %.1f\n", fabs(-5));     // 5
    printf("log(1)    = %.1f\n", log(1));       // 0
    printf("sin(0)    = %.1f\n", sin(0));       // 0
    printf("fmax      = %.0f\n", fmax(a, b));   // 4
    printf("hypot     = %.1f\n", sqrt(pow(a,2) + pow(b,2)));  // 5

    return 0;
}