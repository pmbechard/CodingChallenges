"""
530. Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        self.traverse(root, vals)
        vals.sort()
        min_diff = vals[1] - vals[0]
        for i in range(2, len(vals)):
            diff = vals[i] - vals[i - 1]
            min_diff = min(diff, min_diff)
        return min_diff

    def traverse(self, node, vals):
        vals.append(node.val)
        if node.left:
            self.traverse(node.left, vals)
        if node.right:
            self.traverse(node.right, vals)
