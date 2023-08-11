"""
1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0, '')

    def traverse(self, node, total, curr):
        curr += str(node.val)
        if node.left:
            total = self.traverse(node.left, total, curr)
        if node.right:
            total = self.traverse(node.right, total, curr)
        if not node.right and not node.left:
            total += int(curr, 2)
        return total
