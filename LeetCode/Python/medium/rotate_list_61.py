"""
61. Rotate List
https://leetcode.com/problems/rotate-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next

        for i in range(k % len(nodes)):
            nodes = nodes[-1:] + nodes[:-1]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None

        return nodes[0]
