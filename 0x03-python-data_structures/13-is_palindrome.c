#include "lists.h"

/**
 * aux_palind - This function checks if a linked list is a palindrome
 * @left: pointer to the left node
 * @right: pointer to the right node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int aux_palind(listint_t **left, listint_t *right);

/**
 * is_palindrome - This funtion check if a linked list
 * is a palindrome
 *
 * @head: A pointer to the head of the linked list
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - This function knows if it palinrome
 * @left: A pointer to the left node
 * @right: A a pointer to the right node
 * Return : 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int aux_palind(listint_t **left, listint_t *right)
{
	if (right == NULL)
		return (1);
	if (aux_palind(left, right->next) && (*left)->n == right->n)
	{
		*left = (*left)->next;
		return (1);
	}

	return (0);
}
