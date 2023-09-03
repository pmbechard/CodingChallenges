"""
2487. Remove Nodes From Linked List
https://leetcode.com/problems/remove-nodes-from-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        return stack[0]
