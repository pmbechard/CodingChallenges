"""
1382. Balance a Binary Search Tree
https://leetcode.com/problems/balance-a-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_list = sorted(self.extract_list(root, []), key=lambda x: x.val)
        return self.generate_BST(node_list)

    def extract_list(self, node, arr=[]):
        if node.left: arr += self.extract_list(node.left, [])
        if node.right: arr += self.extract_list(node.right, [])
        arr.append(node)
        return arr

    def generate_BST(self, arr):
        if not arr: return
        if len(arr) == 1:
            arr[0].left = None
            arr[0].right = None
            return arr[0]
        mid = arr[len(arr) // 2]
        mid.left = self.generate_BST(arr[:len(arr) // 2])
        mid.right = self.generate_BST(arr[len(arr) // 2 + 1:])
        return mid
