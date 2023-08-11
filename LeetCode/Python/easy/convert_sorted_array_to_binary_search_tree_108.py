"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traverse(nums)

    def traverse(self, nums):
        mid_index = len(nums) // 2
        mid_node = TreeNode(nums[mid_index])
        if mid_index > 0:
            mid_node.left = self.traverse(nums[:mid_index])
        if mid_index < len(nums) - 1:
            mid_node.right = self.traverse(nums[mid_index + 1:])
        return mid_node
