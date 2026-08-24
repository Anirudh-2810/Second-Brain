// 01_hello_world.c — your very first C program
// Compile:  gcc 01_hello_world.c -o hello
// Run:      ./hello   (Windows: hello.exe)

#include <stdio.h>

int main()
{
    // printf = print formatted; \n = new line
    printf("Hello, world!\n");
    printf("I like pizza!\n");

    // escape sequences
    printf("\"I like pizza!\"\n");   // escaped double quotes
    printf("It's really good!\n");   // apostrophe is fine
    printf("1\t2\t3\n");             // tabs

    return 0;
}