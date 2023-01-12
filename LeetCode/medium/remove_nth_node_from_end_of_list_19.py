"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        node_list = []
        while node:
            node_list.append(node)
            node = node.next
        len_nl = len(node_list)
        to_remove = len_nl - n

        if to_remove > len_nl - 1:
            return head
        elif len_nl == 1:
            return None
        elif to_remove == 0:
            head = head.next
            return head
        elif to_remove == len_nl - 1:
            node_list[to_remove - 1].next = None
        else:
            node_list[to_remove - 1].next = node_list[to_remove - 1].next.next

        return head
