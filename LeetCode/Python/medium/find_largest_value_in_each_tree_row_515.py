"""
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        maxes = []
        self.traverse(root, 0, maxes)
        return maxes

    def traverse(self, node, depth, maxes):
        if not node:
            return
        if depth >= len(maxes):
            maxes.append(node.val)
        elif maxes[depth] < node.val:
            maxes[depth] = node.val
        self.traverse(node.left, depth + 1, maxes)
        self.traverse(node.right, depth + 1, maxes)
