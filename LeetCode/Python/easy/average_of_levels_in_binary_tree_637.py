"""
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        for v in self.traverse(root, dict(), 0).values():
            output.append(sum(v) / len(v))
        return output

    def traverse(self, node, avgs, lvl):
        avgs[lvl] = avgs.get(lvl, []) + [node.val]
        if node.left:
            self.traverse(node.left, avgs, lvl + 1)
        if node.right:
            self.traverse(node.right, avgs, lvl + 1)
        return avgs
