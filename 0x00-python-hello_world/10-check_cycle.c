#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - This function checks of a singly-linked list contains a cycle.
 * @list: The name of singly-linked list
 *
 * Return: 0 if there is no cycle
 *         1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *weak, *quick;

	if (list == NULL || list->next == NULL)
		return (0);

	weak = list->next;
	quick = list->next->next;

	while (weak && quick && quick && quick->next)
	{
		if (weak == quick)
			return (1);

		weak = weak->next;
		quick = quick->next->next;
	}
	return (0);
}
