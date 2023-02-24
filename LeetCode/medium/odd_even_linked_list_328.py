"""
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        node = head
        even_list = []
        odd_list = []
        i = 0
        while node:
            if i % 2 == 0:
                even_list.append(node)
            else:
                odd_list.append(node)
            i += 1
            node = node.next
        node_list = even_list + odd_list
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        node_list[-1].next = None
        return node_list[0]
