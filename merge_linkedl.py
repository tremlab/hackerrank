# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = None

        if not l1:
            if not l2:
                return None
            else:
                return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            new_head = ListNode(l1.val)
            l1 = l1.next
        else:
            new_head = ListNode(l2.val)
            l2 = l2.next

        current = new_head

        while l1 and l2:

            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next


        if l1:
            current.next = l1

        if l2:
            current.next = l2

        return new_head
