#include "lists.h"
/**
 *insert_node - a function that insert a node in a sorted linked list
 *@head: double pointer to head
 *@number: number to be inserted @ head
 *
 *Return: new head or null if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = NULL;
listint_t *new_node = NULL;
current = *head;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}
new_node->n = number;
new_node->next = NULL;
if (*head == NULL || number <= (*head)->n)
{
new_node->next = *head;
*head = new_node;
}
else
{
while ((current->next != NULL) && (number > current->next->n))
{
current = current->next;
}
new_node->next = current->next;
current->next = new_node;
}
return (new_node);
}
