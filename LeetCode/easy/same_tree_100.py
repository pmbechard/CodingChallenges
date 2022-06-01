"""
100. Same Tree
https://leetcode.com/problems/same-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.original = []
        self.other = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        self.traverse(p, self.original)
        self.traverse(q, self.other)
        return self.original == self.other

    def traverse(self, node, results):
        results.append(node.val)
        if node.left:
            self.traverse(node.left, results)
        else:
            results.append(None)
        if node.right:
            self.traverse(node.right, results)
        else:
            results.append(None)
