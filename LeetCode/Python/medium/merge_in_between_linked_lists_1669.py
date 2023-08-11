"""
1669. Merge In Between Linked Lists
https://leetcode.com/problems/merge-in-between-linked-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1

        # get merge point at list1
        merge1 = list1
        for i in range(a - 1):
            merge1 = merge1.next

        # get second merge point at list1
        merge2 = list1
        for i in range(b + 1):
            merge2 = merge2.next

        # complete first merge
        merge1.next = list2

        # get merge point at list2
        while list2.next:
            list2 = list2.next

        # complete second merge
        list2.next = merge2

        return head
