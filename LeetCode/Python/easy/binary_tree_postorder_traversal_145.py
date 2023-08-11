"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.traverse(root, [])

    def traverse(self, node, arr=[]):
        if node.left:
            arr += self.traverse(node.left, [])
        if node.right:
            arr += self.traverse(node.right, [])
        arr.append(node.val)
        return arr
