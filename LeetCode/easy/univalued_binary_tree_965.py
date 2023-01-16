"""
965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return all(self.traverse(root, root.val, []))

    def traverse(self, node, unival, arr):
        arr.append(node.val == unival)
        if node.left:
            self.traverse(node.left, unival, arr)
        if node.right:
            self.traverse(node.right, unival, arr)
        return arr
