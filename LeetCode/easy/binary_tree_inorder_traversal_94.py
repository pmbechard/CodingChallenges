"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


class Solution:
    def inorderTraversal(self, root):
        return self.traverse(root, [])

    def traverse(self, current, traversal_list):
        if not current:
            traversal_list.append(None)
            return
        if current.left:
            self.traverse(current.left, traversal_list)
        traversal_list.append(current.val)
        if current.right:
            self.traverse(current.right, traversal_list)

        return traversal_list
