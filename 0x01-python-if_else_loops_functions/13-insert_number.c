#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"
/**
 * insert_node - a function that inserts a number into a sorted linked list
 * @head: a double pointer of head address of a linked list
 * @number: a inserted number
 *
 * Return: return new node address on success, otherwise return NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, dummy;

	current = &dummy;
	dummy.next = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;
	*head = dummy.next;
	return (new);
}
