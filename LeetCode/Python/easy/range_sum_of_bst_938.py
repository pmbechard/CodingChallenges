"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.traverse(root, low, high, 0)

    def traverse(self, node, low, high, result):
        if low <= node.val <= high:
            result += node.val
        if node.left:
            result = self.traverse(node.left, low, high, result)
        if node.right:
            result = self.traverse(node.right, low, high, result)
        return result
