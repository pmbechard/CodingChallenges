"""
653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.traverse(root, k, dict())

    def traverse(self, node, target, visited):
        flag = False
        if node.left:
            flag = flag or self.traverse(node.left, target, visited)
        if node.right:
            flag = flag or self.traverse(node.right, target, visited)
        if node.val in visited:
            return True
        visited[target - node.val] = node.val
        return flag
