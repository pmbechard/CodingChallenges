"""
1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next
        node_list[k-1], node_list[-k] = node_list[-k], node_list[k-1]
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i+1]
        node_list[-1].next = None
        return node_list[0]
