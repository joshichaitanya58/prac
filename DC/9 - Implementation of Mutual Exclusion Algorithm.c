// gcc file_name.c
// a.exe  or  ./a.out

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int cs = 0, pro = 0;
    char key = 0;
    time_t t1 = time(NULL) - 5;

    system("cls");
    printf("Press a key (except q) to enter a process: \nPress q at any time to exit\n");

    while (key != 'q') {
        if (kbhit()) {
            key = getch();
            if (key == 'q') break;

            if (cs && difftime(time(NULL), t1) > 5.0) {
                printf("Process %d exited critical section.\n", pro - 1);
                cs = 0;
            }

            if (!cs) {
                printf("Process %d entered critical section.\n", pro++);
                cs = 1;
                t1 = time(NULL);
            } else {
                printf("Error: Another process is currently executing!\n");
            }
        }
    }
    return 0;
}