"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        if len(nodes) % 2 == 0:
            return nodes[:len(nodes)//2] == nodes[len(nodes)//2:][::-1]
        else:
            return nodes[:len(nodes)//2] == nodes[len(nodes)//2+1:][::-1]
