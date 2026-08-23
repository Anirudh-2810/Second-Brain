// 06_strings.c — the <string.h> library
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "Bro";
    char big[50];

    printf("strlen(\"Hello\") = %d\n", strlen(str1));   // 5

    strcpy(big, str1);            // copy str1 into big
    printf("copy: %s\n", big);    // Hello

    strcat(big, " ");
    strcat(big, str2);            // append
    printf("cat:  %s\n", big);    // Hello Bro

    printf("strcmp equal?  %d\n", strcmp("abc", "abc")); // 0
    printf("strcmp a<b?    %d\n", strcmp("abc", "abd")); // negative
    printf("strcmp a>b?    %d\n", strcmp("abd", "abc")); // positive

    strcpy(big, "MiXeD CaSe");
    strlwr(big);
    printf("lower: %s\n", big);   // mixed case
    strupr(big);
    printf("upper: %s\n", big);   // MIXED CASE

    // strncpy / strncat / strncmp compare only the first n chars
    printf("first3 cmp: %d\n", strncmp("abcdef", "abcXYZ", 3)); // 0

    return 0;
}