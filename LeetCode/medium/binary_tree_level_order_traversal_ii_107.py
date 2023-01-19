"""
107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        return [] if not root else self.traverse(root, -1, [])[::-1]

    def traverse(self, node, lvl=-1, arr=[]):
        lvl += 1
        if lvl >= len(arr): arr.append([])
        if node.left: self.traverse(node.left, lvl, arr)
        if node.right: self.traverse(node.right, lvl, arr)
        arr[lvl].append(node.val)
        return arr
