"""
143. Reorder List
https://leetcode.com/problems/reorder-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next

        l = 0
        r = len(nodes) - 1
        results = []
        while l <= r:
            results.append(nodes[l])
            if l != r:
                results.append(nodes[r])
            l += 1
            r -= 1

        for i in range(len(results) - 1):
            results[i].next = results[i + 1]
        results[-1].next = None
