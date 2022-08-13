"""
654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build_tree(TreeNode(), nums)

    def build_tree(self, node, nums):
        if nums:
            node.val = max(nums)
            node.left = self.build_tree(TreeNode(), nums[:nums.index(max(nums))])
            node.right = self.build_tree(TreeNode(), nums[nums.index(max(nums)) + 1:])
            return node
