"""
1038. Binary Search Tree to Greater Sum Tree
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, node):
        if node.right:
            self.traverse(node.right)
        self.total += node.val
        node.val = self.total
        if node.left:
            self.traverse(node.left)