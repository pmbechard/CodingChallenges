"""
2130. Maximum Twin Sum of a Linked List
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_items = []
        while head:
            list_items.append(head.val)
            head = head.next
        return max([list_items[i] + list_items[-1-i] for i in range(len(list_items)//2)])
