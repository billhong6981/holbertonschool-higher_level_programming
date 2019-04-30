#include "lists.h"

/**
 * check_cycle - a function that checks the linked list whether cycle or not
 * @list: linked list head pointer
 * Return: return 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		if (current->next == list)
			return (1);
		if (current->next == NULL)
			return (0);
		current = current->next;
	}
	return (0);
}
