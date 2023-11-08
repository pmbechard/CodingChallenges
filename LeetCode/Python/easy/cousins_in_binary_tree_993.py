"""
993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        targets = self.traverse(root, x, y, 0, [], None)
        return targets[0][0] == targets[1][0] and targets[0][1] != targets[1][1]

    def traverse(self, node, target1, target2, depth, targetInfo, parent) -> List[int]:
        if node.val == target1 or node.val == target2:
            targetInfo.append([depth, parent.val if parent else None])
        if len(targetInfo) == 2:
            return targetInfo

        if node.right:
            self.traverse(node.right, target1, target2, depth + 1, targetInfo, node)
        if node.left:
            self.traverse(node.left, target1, target2, depth + 1, targetInfo, node)
        return targetInfo
