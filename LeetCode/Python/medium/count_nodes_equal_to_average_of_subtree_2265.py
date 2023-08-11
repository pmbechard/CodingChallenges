"""
2265. Count Nodes Equal to Average of Subtree
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

    def traverse(self, node, output=0):
        avg = self.getAvg(node)
        avg = avg[0] // avg[1]
        if avg == node.val:
            output += 1
        if node.left:
            output = self.traverse(node.left, output)
        if node.right:
            output = self.traverse(node.right, output)
        return output

    def getAvg(self, node, sum=0, children=1):
        sum += node.val
        if node.left:
            sum, children = self.getAvg(node.left, sum, children + 1)
        if node.right:
            sum, children = self.getAvg(node.right, sum, children + 1)
        return sum, children
