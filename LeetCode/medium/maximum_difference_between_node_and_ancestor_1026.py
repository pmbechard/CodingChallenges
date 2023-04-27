"""
1026. Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, root.val, root.val, 0)

    def traverse(self, node, min_val, max_val, max_diff):
        if node.val > max_val:
            max_val = node.val
        elif node.val < min_val:
            min_val = node.val

        if max_val - min_val > max_diff:
            max_diff = max_val - min_val

        left_diff = right_diff = max_diff

        if node.left:
            left_diff = self.traverse(node.left, min_val, max_val, max_diff)
        if node.right:
            right_diff = self.traverse(node.right, min_val, max_val, max_diff)

        return max(max_diff, left_diff, right_diff)
