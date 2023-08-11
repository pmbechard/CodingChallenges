"""
404. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0, False);

    def traverse(self, node, count, isLeft):
        if isLeft and not node.right and not node.left:
            count += node.val
        if node.right:
            count = self.traverse(node.right, count, False)
        if node.left:
            count = self.traverse(node.left, count, True)
        return count
