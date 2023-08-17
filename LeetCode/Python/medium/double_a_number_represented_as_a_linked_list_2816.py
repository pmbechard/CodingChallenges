"""
2816. Double a Number Represented as a Linked List
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
"""

import sys

sys.set_int_max_str_digits(0)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        num = 0
        while node:
            num = num * 10 + node.val
            node = node.next
        num = str(num * 2)

        node = head
        for i in range(len(num)):
            node.val = int(num[i])
            if not node.next and i < len(num) - 1:
                node.next = ListNode()
            node = node.next
        return head
