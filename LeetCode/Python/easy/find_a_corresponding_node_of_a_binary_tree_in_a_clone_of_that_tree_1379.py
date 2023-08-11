"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.cloned_target = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.traverse(cloned, target)
        return self.cloned_target

    def traverse(self, node, target):
        if node.val == target.val:
            self.cloned_target = node
            return
        if node.left:
            self.traverse(node.left, target)
        if node.right:
            self.traverse(node.right, target)
