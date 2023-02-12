"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        return self.traverse(root, [])

    def traverse(self, node, lst):
        for child in node.children:
            self.traverse(child, lst)
        lst.append(node.val)
        return lst
