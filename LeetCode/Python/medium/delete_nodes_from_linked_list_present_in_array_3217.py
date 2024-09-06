"""
3217. Delete Nodes From Linked List Present in Array
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        while head and head.val in nums:
            head = head.next
        if not head:
            return None

        prev = head
        node = head.next
        while node:
            if node.val in nums:
                prev.next = node.next
            else:
                prev = prev.next
            node = node.next
        return head
