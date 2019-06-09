#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

/**
 * main - main function
 * Return: return 0 on success
 */
int main(void)
{
	char *s;
	unsigned long int i = 0;

	s = strdup("Holberton");
	if (!s)
	{
		fprintf(stderr, "Can't allocate memory with malloc\n");
		return (EXIT_FAILURE);
	}
	while (s)
	{
		printf(" [%lu] %s (%p)\n", i, s, (void *)s);
		sleep(3);
		i++;
	}
	return (EXIT_SUCCESS);
}

