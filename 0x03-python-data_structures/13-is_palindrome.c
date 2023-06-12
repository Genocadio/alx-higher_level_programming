#include "lists.h"
/**
 * reverse_listint - reverses a list
 * @head: pointer to head of list
 * Return: pointer to reversed list head
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 else
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *reversed = reverse_listint(head);

	while (tmp != NULL && reversed != NULL)
	{
		if (tmp->n != reversed->n)
			return (0);

		tmp = tmp->next;
		reversed = reversed->next;
	}
	return (1);
}
