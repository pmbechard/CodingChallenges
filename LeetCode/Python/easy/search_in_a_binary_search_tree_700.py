"""
700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while True:
            if not current:
                return None
            elif val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return current