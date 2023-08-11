"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = sorted(self.traverse(root, []))
        return lst[k - 1]

    def traverse(self, root, lst):
        if not root: return []
        lst.append(root.val)
        if root.left:
            self.traverse(root.left, lst)
        if root.right:
            self.traverse(root.right, lst)
        return lst
