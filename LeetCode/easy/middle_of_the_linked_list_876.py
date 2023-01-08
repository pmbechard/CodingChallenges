"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        while True:
            arr.append(node)
            if not node.next:
                break
            node = node.next
        return arr[len(arr) // 2]
