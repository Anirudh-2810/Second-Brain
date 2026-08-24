// 11_structs_enums.c — structs, typedef, enums
#include <stdio.h>
#include <string.h>

// plain struct
struct Student {
    char name[50];
    float gpa;
    int age;
};

// typedef: "Student" becomes the type name (no "struct" keyword needed)
typedef struct {
    char name[50];
    float gpa;
    int age;
} Student2;

// enum of days
enum Day { SUN, MON, TUE, WED, THU, FRI, SAT };

// typedef enum: Status can be used without "enum"
typedef enum { TRUE, FALSE } Status;

int main() {
    // struct usage
    struct Student student1;
    strcpy(student1.name, "Spongebob");
    student1.gpa = 3.2;
    student1.age = 23;
    printf("%s | %.2f | %d\n", student1.name, student1.gpa, student1.age);

    // typedef struct usage — cleaner
    Student2 student2 = {"Patrick", 2.8, 24};
    printf("%s | %.2f | %d\n", student2.name, student2.gpa, student2.age);

    // array of structs
    Student2 students[2] = {{"Squidward", 3.5, 30}, {"Sandy", 4.0, 28}};
    for (int i = 0; i < 2; i++) {
        printf("%s: %.2f\n", students[i].name, students[i].gpa);
    }

    // enum
    enum Day today = WED;
    printf("WED = %d\n", today);            // 3

    switch (today) {
        case SUN: printf("Sunday\n"); break;
        case MON: printf("Monday\n"); break;
        case TUE: printf("Tuesday\n"); break;
        case WED: printf("Wednesday\n"); break;
        default:  printf("Some other day\n");
    }

    // typedef enum
    Status isOnline = TRUE;
    printf("isOnline = %d\n", isOnline);    // 1

    return 0;
}