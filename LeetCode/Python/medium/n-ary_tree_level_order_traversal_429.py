"""
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        return self.traverse(root, [], 0)

    def traverse(self, node, lst, lvl):
        if len(lst) == lvl:
            lst.append([node.val])
        else:
            lst[lvl].append(node.val)
        for child in node.children:
            self.traverse(child, lst, lvl + 1)
        return lst
