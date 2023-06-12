#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int count = countNode(*head);
	int *arr = malloc(count * sizeof(int));

	if (arr == NULL)
		return (0);

	assignToArray(*head, arr, count);

	int i = 0;
	int j = count - 1;

	while (i < j)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
		i++;
		j--;
	}

	free(arr);
	return (1);
}

/**
 * countNode - counts the number of nodes in a linked list
 * @head: head of the list
 * Return: number of nodes in the list
 */
int countNode(listint_t *head)
{
	int count = 0;
	listint_t *current = head;

	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	return (count);
}

/**
 * assignToArray - assign values of list to an array
 * @head: head of the list
 * @arr: array to assign values to
 * @size: size of the array
 * Return: void
 */
void assignToArray(listint_t *head, int *arr, int size)
{
	listint_t *current = head;
	int i = 0;

	while (current != NULL && i < size)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
}
