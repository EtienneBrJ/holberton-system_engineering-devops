#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 * Return: 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - create that create 5 zombies process
 * Return: 0 if success or 1 if it fail
 */

int main(void)
{
    pid_t zpid;
    int i;

    for (i = 0; i < 5; i++)
    {
        if ((zpid = fork()) == 0)
            exit(EXIT_FAILURE);
        printf("Zombie process created, PID: %d\n", zpid);
    }
    infinite_while();
}