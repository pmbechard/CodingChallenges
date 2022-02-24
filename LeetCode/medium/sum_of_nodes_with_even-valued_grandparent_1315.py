"""
1315. Sum of Nodes with Even-Valued Grandparent
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
"""


class Solution:
    def sumEvenGrandparent(self, root):
        self.parent = None
        self.node_sum = 0
        self.traverse(root)
        return self.node_sum

    def traverse(self, node):
        if self.parent and self.parent.val % 2 == 0:
            if node.left:
                self.node_sum += node.left.val
            if node.right:
                self.node_sum += node.right.val
        if node.left:
            self.parent = node
            self.traverse(node.left)
        if node.right:
            self.parent = node
            self.traverse(node.right)
