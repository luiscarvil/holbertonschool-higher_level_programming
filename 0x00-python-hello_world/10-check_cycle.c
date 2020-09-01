#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: pointer to struct list.
 * Return: 1 if is a cycle or 0 if isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *move;

	if ((!list) || (!list->next))
		return (0);
	temp = list;
	move = list;
	while (move->next && move->next->next)
	{
		temp = temp->next;
		move = move->next->next;
		if (temp == move)
			return (1);
	}
	return (0);
}
