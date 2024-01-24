"""
1457. Pseudo-Palindromic Paths in a Binary Tree
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = 0

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.get_paths(root, 0)
        return self.paths

    def get_paths(self, node, bitmask):
        bitmask ^= (1 << node.val)  # Toggle the bit for the current node value
        if not node.left and not node.right:
            if bitmask & (bitmask - 1) == 0:  # Check if only one bit is set (palindromic condition)
                self.paths += 1
        if node.left:
            self.get_paths(node.left, bitmask)
        if node.right:
            self.get_paths(node.right, bitmask)
