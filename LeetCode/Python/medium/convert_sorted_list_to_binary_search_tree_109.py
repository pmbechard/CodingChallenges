"""
109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return self.connect_nodes(nodes)

    def connect_nodes(self, lst):
        if not lst:
            return
        elif len(lst) == 1:
            return TreeNode(lst[0].val)
        elif len(lst) == 2:
            node = TreeNode(lst[1].val)
            node.left = TreeNode(lst[0].val)
            return node
        mid = len(lst) // 2
        mid_node = TreeNode(lst[mid].val)
        mid_node.left = self.connect_nodes(lst[:mid])
        mid_node.right = self.connect_nodes(lst[mid + 1:])
        return mid_node
