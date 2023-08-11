"""
589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        return self.traverse(root, [])

    def traverse(self, node, lst):
        lst.append(node.val)
        for child in node.children:
            self.traverse(child, lst)
        return lst
