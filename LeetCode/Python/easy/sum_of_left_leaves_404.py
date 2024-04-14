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
    def __init__(self):
        self.left_sum = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left:
            if not root.left.left and not root.left.right:
                self.left_sum += root.left.val
            else:
                self.sumOfLeftLeaves(root.left)
        if root.right:
            self.sumOfLeftLeaves(root.right)
        return self.left_sum
