#include "lists.h"
/**
 * palindrome - searches for palindrome
 * @l: l
 * @r: r
 * Return: 1 for palindrome else 0 no palindrome
 */

int palindrome(listint_t **l, listint_t *r)
{
	int resp;

	if (r != NULL)
	{
		resp = palindrome(l, r->next);
		if (resp != 0)
		{
			resp = (r->n == (*l)->n);
			*l = (*l)->next;
			return (resp);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - determines if list is a palindrome.
 * @head: list head
 * Return: 0 No palindrome othewise 1 palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
