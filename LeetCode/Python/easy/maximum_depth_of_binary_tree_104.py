"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.traverse(root, 1)

    def traverse(self, current, depth):
        if current.left:
            self.traverse(current.left, depth + 1)
        if current.right:
            self.traverse(current.right, depth + 1)
        if depth > self.depth:
            self.depth = depth
        return self.depth
