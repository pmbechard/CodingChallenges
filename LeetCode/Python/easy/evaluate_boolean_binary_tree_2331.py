"""
2331. Evaluate Boolean Binary Tree
https://leetcode.com/problems/evaluate-boolean-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)

    def traverse(self, node):
        if node.val == 2:
            return self.traverse(node.left) or self.traverse(node.right)
        elif node.val == 3:
            return self.traverse(node.left) and self.traverse(node.right)
        return True if node.val == 1 else False
