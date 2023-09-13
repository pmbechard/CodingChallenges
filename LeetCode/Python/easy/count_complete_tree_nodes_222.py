"""
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)

    def traverse(self, node, count):
        if not node:
            return count
        if node.left:
            count = self.traverse(node.left, count)
        if node.right:
            count = self.traverse(node.right, count)
        return count + 1
