"""
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        for i in range(0, len(node_list), 2):
            if i == len(node_list) - 1: break
            node_list[i], node_list[i+1] = node_list[i+1], node_list[i]
        for i in range(len(node_list)):
            if i == len(node_list) - 1: node_list[i].next = None
            else: node_list[i].next = node_list[i+1]
        return node_list[0]
