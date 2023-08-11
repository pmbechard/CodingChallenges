"""
2331. Evaluate Boolean Binary Tree
https://leetcode.com/problems/evaluate-boolean-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return eval(self.traverse(root))

    def traverse(self, node):
        result = ''
        if node.left:
            val = self.traverse(node.left)
            if val: result += val
        result += self.convertVal(node.val)
        if node.right:
            val = self.traverse(node.right)
            if val: result += val
        if node.left and node.right:
            return f'{eval(result)} '
        return result

    def convertVal(self, val):
        if val == 0:
            return 'False '
        elif val == 1:
            return 'True '
        elif val == 2:
            return 'or '
        elif val == 3:
            return 'and '
