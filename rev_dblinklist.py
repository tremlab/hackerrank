# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

def reverse(head):

    if head == None:
        return head

    current = head
    prev = None
    next = current.next

    while current.next:
        current.prev = next
        current.next = prev
        prev = current
        current = next
        next = current.next


    current.next = prev
    current.prev = None

    return current
