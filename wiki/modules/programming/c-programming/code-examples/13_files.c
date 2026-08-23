// 13_files.c — write to and read from a file
#include <stdio.h>

int main() {
    // ---- WRITE ----
    FILE *pFile = fopen("output.txt", "w");   // w = write (create/overwrite)

    if (pFile == NULL) {                      // always check!
        printf("Unable to open file for writing.\n");
        return 1;
    }

    fprintf(pFile, "This is my first file.\n");
    fprintf(pFile, "Line 2 here.\n");
    fprintf(pFile, "Pi is about %.2f\n", 3.14159);

    fclose(pFile);                            // always close!
    printf("File written successfully.\n");

    // ---- READ ----
    FILE *pRead = fopen("output.txt", "r");   // r = read (file must exist)

    if (pRead == NULL) {
        printf("File not found.\n");
        return 1;
    }

    char line[100];
    while (fgets(line, sizeof(line), pRead) != NULL) {
        printf("%s", line);                   // print each line back
    }

    fclose(pRead);
    return 0;
}