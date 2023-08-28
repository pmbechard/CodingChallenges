"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = []
        while headA:
            visited_nodes.append(headA)
            headA = headA.next
        while headB:
            if headB in visited_nodes:
                return headB
            headB = headB.next
        return None
