"""
872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1, []) == self.get_leaves(root2, [])

    def get_leaves(self, node, leaves):
        if not node.left and not node.right:
            leaves.append(node.val)
        if node.left:
            self.get_leaves(node.left, leaves)
        if node.right:
            self.get_leaves(node.right, leaves)
        return leaves
