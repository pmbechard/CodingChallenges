"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        stack = []
        while current:
            stack.append(current.val)
            current = current.next
        new_head = ListNode(stack.pop())
        result = new_head
        for i in range(len(stack)):
            result.next = ListNode(stack.pop())
            result = result.next
        return new_head
