/*
 * File: 102-zombie.c
 * This code must be betty compliance
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - This functon Run an infinite while loop.
 *
 * Return: Always 0.
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
 * main - This function Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pids;
	char count = 0;

	while (count < 5)
	{
		pids = fork();
		if (pids > 0)
		{
			printf("Zombie process created, PID: %d\n", pids);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
