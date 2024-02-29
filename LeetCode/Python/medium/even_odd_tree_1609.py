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
        lvl_map = {}
        self.traverse(root, 0, lvl_map)
        i = 0
        while True:
            if not lvl_map.get(i):
                break
            if i % 2 == 0:
                if not all([x % 2 == 1 for x in lvl_map[i]]) or not sorted(lvl_map[i]) == lvl_map[i] or not len(
                        set(lvl_map[i])) == len(lvl_map[i]):
                    return False
            else:
                if not all([x % 2 == 0 for x in lvl_map[i]]) or not sorted(lvl_map[i], reverse=True) == lvl_map[
                    i] or not len(set(lvl_map[i])) == len(lvl_map[i]):
                    return False
            i += 1
        return True

    def traverse(self, node, lvl, lvl_map):
        lvl_map[lvl] = lvl_map.get(lvl, []) + [node.val]
        if node.left:
            self.traverse(node.left, lvl + 1, lvl_map)
        if node.right:
            self.traverse(node.right, lvl + 1, lvl_map)
