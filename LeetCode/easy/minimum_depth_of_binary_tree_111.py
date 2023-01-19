"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return min(self.traverse(root, 0, [])) if root else 0

    def traverse(self, node, lvl=0, arr=[]):
        lvl += 1
        if node.left: self.traverse(node.left, lvl, arr)
        if node.right: self.traverse(node.right, lvl, arr)
        if not node.left and not node.right:
            arr.append(lvl)
        return arr
