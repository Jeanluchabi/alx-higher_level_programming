#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - This function inserts a number into
 * a sorted singly-linked list.
 *
 * @head: A pointer the head o
 * @number: The number to be inserted.
 *
 * Return: NULL, If the function fails.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodeName = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;

	if (nodeName == NULL || nodeName->n >= number)
	{
		newNode->next = nodeName;
		*head = newNode;
		return (newNode);
	}
	while (nodeName && nodeName->next && nodeName->next->n < number)
		nodeName = nodeName->next;

	newNode->next = nodeName->next;
	nodeName->next = newNode;

	return (newNode);
}

