#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @L: int
 * @next: points towards upcoming node
 */

typedef struct listint_s
{
	int L;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
int is_palindrome(listint_t **head);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int L);

#endif /* LISTS_H */
