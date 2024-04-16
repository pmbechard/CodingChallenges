"""
623. Add One Row to Tree
https://leetcode.com/problems/add-one-row-to-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        self.traverse(root, val, 1, depth, False)
        return root

    def traverse(self, node, val, current_depth, target_depth, is_left):
        if current_depth == target_depth - 1:
            new_left = TreeNode(val)
            new_right = TreeNode(val)
            new_left.left = node.left
            new_right.right = node.right
            node.left = new_left
            node.right = new_right
            return
        if node.left:
            self.traverse(node.left, val, current_depth + 1, target_depth, True)
        if node.right:
            self.traverse(node.right, val, current_depth + 1, target_depth, False)
