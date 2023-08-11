"""
1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/
"""


class Solution:
    def deepestLeavesSum(self, root):
        self.deepest_row = 0
        self.deepest_node_sum = self.traverse(root, 0)
        return self.deepest_row_sum

    def traverse(self, node, row):
        if node.left:
            self.traverse(node.left, row + 1)
        if node.right:
            self.traverse(node.right, row + 1)
        else:
            if row > self.deepest_row:
                self.deepest_row = row
                self.deepest_row_sum = node.val
            elif row == self.deepest_row:
                self.deepest_row_sum += node.val
