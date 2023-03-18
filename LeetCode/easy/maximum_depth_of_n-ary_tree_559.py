"""
559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        return self.traverse(root, 1)

    def traverse(self, node, depth):
        if not node.children:
            return depth
        depths = [self.traverse(x, depth + 1) for x in node.children]
        return max(depths)
