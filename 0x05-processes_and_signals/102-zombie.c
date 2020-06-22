#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: always 0
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
 * main - 5 zombies
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zom;

	for (i = 0; i < 5; i++)
	{
		zom = fork();
		if (!zom)
			return (0);
		printf("Zombie process created, PID: %d\n", zom);
	}

	infinite_while();
	return (0);
}
