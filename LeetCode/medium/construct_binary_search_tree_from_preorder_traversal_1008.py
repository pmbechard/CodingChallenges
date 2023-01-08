"""
1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        preorder.pop(0)

        for val in preorder:
            self.add_node(root, val)

        return root

    def add_node(self, root, val):
        current = root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    return
                else:
                    current = current.right
