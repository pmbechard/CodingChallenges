"""
148. Sort List
https://leetcode.com/problems/sort-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next
        node_list.sort(key=lambda x: x.val)
        for i in range(len(node_list)):
            if i == len(node_list) - 1:
                node_list[i].next = None
            else:
                node_list[i].next = node_list[i+1]
        return node_list[0]
