"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.traverse(root, [])

    def traverse(self, current, traversal_list):
        if current.left:
            self.traverse(current.left, traversal_list)
        traversal_list.append(current.val)
        if current.right:
            self.traverse(current.right, traversal_list)
        return traversal_list
