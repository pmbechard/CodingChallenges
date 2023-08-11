"""
617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        elif not root1: return root2
        elif not root2: root1
        return self.traverse(root1, root2, None)

    def traverse(self, node1, node2, merged):
        merged = TreeNode()
        merged.val += node1.val if node1 else 0
        merged.val += node2.val if node2 else 0
        if (node1 and node1.left) or (node2 and node2.left):
            merged.left = self.traverse(node1.left if node1 else node1, node2.left if node2 else node2, merged.left)
        if (node1 and node1.right) or (node2 and node2.right):
            merged.right = self.traverse(node1.right if node1 else node1, node2.right if node2 else node2, merged.right)
        return merged
