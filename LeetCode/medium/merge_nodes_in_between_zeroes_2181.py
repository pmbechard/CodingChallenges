"""
2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/
"""


class Solution:
    def mergeNodes(self, head):
        current = head
        sum_node = head
        while True:
            if current.val == 0 and current is not head:
                sum_node.next = current
                sum_node = current
            else:
                sum_node.val += current.val
            current = current.next
            if not current.next:
                sum_node.next = None
                break
        return head
