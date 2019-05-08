#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse_list - a function reverses the second half linked list
 * @h: a double pointer of head
 * Return: return the head pointer
 */

void reverse_list(listint_t **h)
{
	listint_t *result = NULL;
	listint_t *current = *h;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = result;
		result = current;
		current = next;
	}
	*h = result;
}

/**
 * is_palindrome - a function checks whether the list is palindrome or not
 * @head: a head pointer
 * Return: return 1 is palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *mid_last;
	int len = 0, len_half;

	current = *head;
	while (current)
	{
		len++;
		current = current->next;
	}
	len_half = (len % 2 == 0) ? len / 2 : len / 2 + 1;
	current = *head;
	while (--len_half)
		current = current->next;
	mid_last = current;
	current = current->next;
	reverse_list(&current);
	mid_last->next = current;
	current = *head;
	mid_last = mid_last->next;
	while (mid_last != NULL)
	{
		if (current->n != mid_last->n)
			return (0);
		current = current->next;
		mid_last = mid_last->next;
	}
	return (1);
}
