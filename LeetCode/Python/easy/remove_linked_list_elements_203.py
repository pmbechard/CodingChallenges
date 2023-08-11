"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node_list = []
        while head:
            if head.val != val:
                node_list.append(head)
            head = head.next
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        if len(node_list) > 0:
            node_list[-1].next = None
            return node_list[0]
        return None
