"""
1325. Delete Leaves With a Given Value
https://leetcode.com/problems/delete-leaves-with-a-given-value/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.traverse(root, target)
        if root.val == target and self.is_leaf(root):
            return None
        return root

    def traverse(self, node, target):
        if node.left:
            self.traverse(node.left, target)
        if node.right:
            self.traverse(node.right, target)

        if node.left and node.left.val == target and self.is_leaf(node.left):
            node.left = None
        if node.right and node.right.val == target and self.is_leaf(node.right):
            node.right = None

    def is_leaf(self, node):
        return not node.left and not node.right
