"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if head:
            node = head
        else:
            return head
        while True:
            if node.next and node.next.val == node.val:
                node.next = node.next.next
            elif node.next:
                node = node.next
            else:
                break
        return head
