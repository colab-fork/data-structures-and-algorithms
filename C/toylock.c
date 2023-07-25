#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("_____Welcome to Mr. Lock System_____\n");

    int password;
    int FakeInput;

    printf("\n\nPlease type your password: ");
    scanf("%d", &password);

    if (password == 2005) {
        printf("The password is correct :)\n");
        printf("Hello my close friend :)\n");
    } else {
        printf("The password is wrong :O\n");
        printf("You still have two more tries.\n");
        printf("Try again... ");
        scanf("%d", &password);
    }

    if (password == 2005) {
        printf("The password is correct :)\n");
        printf("Hello my close friend :)\n");
    } else {
        printf("The password is wrong :O\n");
        printf("You still have one more try.\n");
        printf("Try again... ");
        scanf("%d", &password);
    }

    if (password == 2005) {
        printf("The password is correct :)\n");
        printf("Hello my close friend :)\n");
    } else {
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
        printf("WRONG.\n");
    }

    scanf("%d", &FakeInput); // This line reads an integer and stores it in FakeInput.

    return 0;
}
