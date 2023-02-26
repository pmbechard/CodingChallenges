"""
86. Partition List
https://leetcode.com/problems/partition-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        nodes.sort(key=lambda i: i.val >= x)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]
