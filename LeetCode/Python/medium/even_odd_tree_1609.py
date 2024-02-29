"""
1609. Even Odd Tree
https://leetcode.com/problems/even-odd-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, 0, {})

    def traverse(self, node, lvl, lvl_map):
        if lvl % 2 == node.val % 2 or (lvl % 2 == 0 and lvl_map.get(lvl) and lvl_map.get(lvl)[-1] >= node.val) or (
                lvl % 2 == 1 and lvl_map.get(lvl) and lvl_map.get(lvl)[-1] <= node.val):
            return False
        lvl_map[lvl] = lvl_map.get(lvl, []) + [node.val]
        if node.left and not self.traverse(node.left, lvl + 1, lvl_map):
            return False
        if node.right and not self.traverse(node.right, lvl + 1, lvl_map):
            return False
        return True
