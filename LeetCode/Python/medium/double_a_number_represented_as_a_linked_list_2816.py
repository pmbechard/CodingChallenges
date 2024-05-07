"""
2816. Double a Number Represented as a Linked List
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = node = head
        prev = None
        while node:
            new_val = node.val * 2
            if new_val > 9:
                node.val = new_val % 10
                if prev:
                    prev.val += 1
                else:
                    prev = ListNode(1, node)
                    new_head = prev
            else:
                node.val = new_val
            prev = node
            node = node.next
        return new_head
