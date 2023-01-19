"""
112. Path Sum
https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return targetSum in self.traverse(root, 0, []) if root else False

    def traverse(self, node, count, arr):
        count += node.val
        if node.left: self.traverse(node.left, count, arr)
        if node.right: self.traverse(node.right, count, arr)
        if not node.left and not node.right:
            arr.append(count)
        return arr
