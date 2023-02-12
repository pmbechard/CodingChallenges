"""
606. Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root, "")

    def traverse(self, node, s):
        s = f"{node.val}"
        if node.left:
            s += f"({self.traverse(node.left, s)})"
        if not node.left and node.right:
            s += "()"
        if node.right:
            s += f"({self.traverse(node.right, s)})"
        return s
