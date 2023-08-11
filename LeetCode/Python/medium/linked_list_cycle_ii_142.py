"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            if head not in nodes:
                nodes.append(head)
            else:
                return head
            head = head.next
        return None
