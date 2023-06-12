#include "lists.h"
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	listint_t *prev = NULL;

	while (slow != NULL)
	{
		listint_t *next = slow->next;

		slow->next = prev;
		prev = slow;
		slow = next;
	}

	listint_t *p1 = *head;
	listint_t *p2 = prev;

	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1);
}
