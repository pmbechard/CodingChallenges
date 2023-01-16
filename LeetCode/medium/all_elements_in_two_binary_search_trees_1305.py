"""
1305. All Elements in Two Binary Search Trees
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1: return sorted(self.traverse(root2, []))
        elif not root2: return sorted(self.traverse(root1, []))
        else: return sorted(self.traverse(root1, []) + self.traverse(root2, []))

    def traverse(self, node: TreeNode, arr: List[int]=[]) -> List[int]:
        arr.append(node.val)
        if node.left:
            self.traverse(node.left, arr)
        if node.right:
            self.traverse(node.right, arr)
        return arr
