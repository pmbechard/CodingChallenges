"""
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next
        left -= 1
        right -= 1
        node_list = node_list[:left] + node_list[left:right+1][::-1] + node_list[right+1:]
        for i in range(len(node_list)):
            if i == len(node_list) - 1:
                node_list[i].next = None
            else:
                node_list[i].next = node_list[i+1]
        return node_list[0]
