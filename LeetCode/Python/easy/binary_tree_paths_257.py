"""
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.traverse(root, '', [])

    def traverse(self, node, current_path, completed_paths):
        if current_path:
            current_path += f'->{node.val}'
        else:
            current_path = f'{node.val}'

        if node.left:
            self.traverse(node.left, current_path, completed_paths)
        if node.right:
            self.traverse(node.right, current_path, completed_paths)
        if not node.left and not node.right:
            completed_paths.append(current_path)

        return completed_paths
