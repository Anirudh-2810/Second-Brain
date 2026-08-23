// 10_arrays.c — 1D arrays, 2D arrays, array of strings, swap, sort
#include <stdio.h>

void selectionSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[i]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    // --- 1D array ---
    double prices[] = {5.0, 10.0, 15.0, 25.0, 20.0};
    printf("First: %.2f, Last: %.2f\n", prices[0], prices[4]);
    prices[2] = 99.99;
    for (int i = 0; i < 5; i++) printf("%.2f ", prices[i]);
    printf("\n");

    // --- swap two values (need a temp!) ---
    int a = 5, b = 10;
    int temp = a;
    a = b;
    b = temp;
    printf("After swap: a=%d b=%d\n", a, b);

    // --- 2D array (must state column count) ---
    int numbers[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    printf("numbers[0][0]=%d numbers[2][1]=%d\n", numbers[0][0], numbers[2][1]);

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) printf("%d ", numbers[r][c]);
        printf("\n");
    }

    // --- array of strings ---
    char cars[][10] = {"Mustang", "Corvette", "Camaro"};
    for (int i = 0; i < 3; i++) printf("%s\n", cars[i]);

    // --- sort ---
    int array[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int size = sizeof(array) / sizeof(array[0]);
    selectionSort(array, size);
    for (int i = 0; i < size; i++) printf("%d ", array[i]);
    printf("\n");   // 1 1 2 3 4 5 6 9

    return 0;
}