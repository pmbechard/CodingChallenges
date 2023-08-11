"""
501. Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vals = self.traverse(root, [])
        vals_set = set(vals)
        modes = []
        max_count = 0
        for val in vals_set:
            current_count = vals.count(val)
            if current_count > max_count:
                max_count = current_count
                modes = [val]
            elif current_count == max_count:
                modes.append(val)
        return modes

    def traverse(self, node, lst):
        if node.right:
            lst = self.traverse(node.right, lst)
        if node.left:
            lst = self.traverse(node.left, lst)
        lst.append(node.val)
        return lst
