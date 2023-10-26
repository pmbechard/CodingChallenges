"""
783. Minimum Distance Between BST Nodes
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lst = []
        self.traverse(root, lst)
        lst.sort()
        diff = abs(lst[0] - lst[1])
        for i in range(1, len(lst) - 1):
            diff = min(diff, abs(lst[i] - lst[i + 1]))
        return diff

    def traverse(self, node, lst):
        lst.append(node.val)
        if node.left:
            self.traverse(node.left, lst)
        if node.right:
            self.traverse(node.right, lst)
        return dist
