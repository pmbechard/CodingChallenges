"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = self.getTreeList(root.left, {}, 1)
        right = self.getTreeList(root.right, {}, 1)
        print(left, right)
        for k, v in left.items():
            if right[k][::-1] != v:
                return False
        return True

    def getTreeList(self, node, node_list, depth):
        if not node:
            if node_list.get(depth):
                node_list[depth].append(None)
            else:
                node_list[depth] = [None]
            return node_list
        if node_list.get(depth):
            node_list[depth].append(node.val)
        else:
            node_list[depth] = [(node.val)]
        self.getTreeList(node.left, node_list, depth + 1)
        self.getTreeList(node.right, node_list, depth + 1)
        return node_list
