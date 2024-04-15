"""
129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, '')
        return self.sum

    def traverse(self, node, s):
        s += str(node.val)
        if not node.left and not node.right:
            self.sum += int(s)
            return
        if node.right:
            self.traverse(node.right, s)
        if node.left:
            self.traverse(node.left, s)
