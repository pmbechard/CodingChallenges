"""
445. Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = ''
        while l1 or l2:
            if l1:
                num1 += str(l1.val)
                l1 = l1.next
            if l2:
                num2 += str(l2.val)
                l2 = l2.next
        sum_str = str(int(num1) + int(num2))
        prev = None
        head = None
        for digit in sum_str:
            node = ListNode(int(digit))
            if prev:
                prev.next = node
            else:
                head = node
            prev = node
        return head
