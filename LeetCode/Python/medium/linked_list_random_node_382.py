"""
382. Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.nodes = []
        while head:
            self.nodes.append(head)
            head = head.next

    def getRandom(self) -> int:
        return self.nodes[randint(0, len(self.nodes) - 1)].val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
