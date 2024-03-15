#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: points to linked list head
 * @number: The number to insert.
 * Return:  NULL if function is unsuccesful.
 * else point to new pode
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->N = number;
	if (node == NULL || node->N >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->N < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
