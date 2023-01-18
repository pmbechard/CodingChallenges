"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.traverse(root, [])

    def traverse(self, node, result):
        result.append(node.val)
        if node.left:
            result += self.traverse(node.left, [])
        if node.right:
            result += self.traverse(node.right, [])
        return result
