"""
2807. Insert Greatest Common Divisors in Linked List
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            new_node = ListNode(self.getGCD(node.val, node.next.val))
            new_node.next = node.next
            node.next = new_node
            node = node.next.next
        return head

    def getGCD(self, a, b):
        small = a if a < b else b
        while small > 0:
            if a % small == 0 and b % small == 0:
                return small
            small -= 1
