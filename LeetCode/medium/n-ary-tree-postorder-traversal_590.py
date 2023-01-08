"""
590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.traverse(root, [])

    def traverse(self, node, result):
        if not node:
            return result
        if not node.children:
            result.append(node.val)
        else:
            for child in node.children:
                self.traverse(child, result)
            result.append(node.val)
        return result
