"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.traverse(root)
        return root

    def traverse(self, node):
        node.left, node.right = node.right, node.left
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)
