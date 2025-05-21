"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        prev = self.nums[0]
        for num in self.nums[1:]:
            if num <= prev:
                return False
            prev = num
        return True

    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        self.nums.append(node.val)
        if node.right:
            self.traverse(node.right)
