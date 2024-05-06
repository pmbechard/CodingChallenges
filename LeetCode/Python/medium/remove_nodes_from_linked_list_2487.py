"""
2487. Remove Nodes From Linked List
https://leetcode.com/problems/remove-nodes-from-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case for single node
        if not head.next:
            return head
        # O(n) - Convert to list
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        # O(1) - Get second last index
        prev = nodes[-1]
        i = len(nodes) - 2
        # O(n) - Connect increasing nodes (right to left)
        while i >= 0:
            if nodes[i].val >= prev.val:
                nodes[i].next = prev
                prev = nodes[i]
            i -= 1
        # Total: O(n)
        return prev
