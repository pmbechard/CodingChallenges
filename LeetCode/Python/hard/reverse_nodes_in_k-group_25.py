"""
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        node_list = []
        while node:
            node_list.append(node)
            node = node.next
        rev_list = []
        for i in range(0, len(node_list), k):
            if i + k > len(node_list):
                rev_list += node_list[i:]
            else:
                rev_list += node_list[i:i + k][::-1]
        for i in range(len(rev_list)):
            if i == len(rev_list) - 1:
                rev_list[i].next = None
            else:
                rev_list[i].next = rev_list[i + 1]
        return rev_list[0]
