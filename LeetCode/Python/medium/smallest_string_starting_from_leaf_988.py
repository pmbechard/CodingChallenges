"""
988. Smallest String Starting From Leaf
https://leetcode.com/problems/smallest-string-starting-from-leaf
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        results = []
        self.traverse(root, '', results)
        return min(results)

    def traverse(self, node, current, results):
        current = chr(node.val + 97) + current
        if not node.left and not node.right:
            results.append(current)
            return
        if node.left:
            self.traverse(node.left, current, results)
        if node.right:
            self.traverse(node.right, current, results)
