#include "lists.h"

/**
 * check_cycle - function to check if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle or else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
		while (slow != fast)
	{
		if (!fast || !fast->next)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
