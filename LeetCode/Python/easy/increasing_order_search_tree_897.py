"""
897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        arr = sorted(self.extract_list(root, []), key=lambda x: x.val)
        for i in range(len(arr) - 1):
            arr[i].right = arr[i + 1]
            arr[i].left = None
        arr[-1].right = None
        arr[-1].left = None
        return arr[0]

    def extract_list(self, node, arr=[]):
        arr.append(node)
        if node.left: self.extract_list(node.left, arr)
        if node.right: self.extract_list(node.right, arr)
        return arr
