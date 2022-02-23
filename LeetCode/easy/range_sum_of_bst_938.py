"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
"""


class Solution:
    def rangeSumBST(self, root, low, high):
        self.nums_range = list(range(low, high + 1))
        self.node_sum = 0
        self.traverse(root)
        return self.node_sum

    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)
        if node.val in self.nums_range:
            self.node_sum += node.val