"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        nodes = []
        while head:
            if head in nodes: return True
            elif not head.next: return False
            nodes.append(head)
            head = head.next
