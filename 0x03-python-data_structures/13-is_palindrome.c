#include "lists.h"
/**
 *reverseList - a function that reverses a linked list
 *@head: a head pointer to a list
 *
 *Return: head of reversed list
 */
listint_t* reverseList(listint_t* head) {
listint_t *prev = NULL, *current = head, *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}
/**
 *is_palindrome - a function that checkes if a linked list palindrome
 *@head: head double pointer to a list input
 *
 *Return: 0 if not a palindrome and 1 if is
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}
slow = reverseList(slow);
while (slow != NULL)
{
if ((*head)->n != slow->n)
{
return (0);
}
*head = (*head)->next;
slow = slow->next;
}
return (1);
}
