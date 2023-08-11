"""
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        del nodes[len(nodes) // 2]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if not nodes: return None
        nodes[-1].next = None
        return nodes[0]
