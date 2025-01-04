"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = 0
        self.arr = []
        self.traverse(root)
        self.len = len(self.arr)

    def next(self) -> int:
        self.curr += 1
        return self.arr[self.curr - 1]

    def hasNext(self) -> bool:
        return self.curr < self.len

    def traverse(self, node) -> None:
        if not node:
            return
        if node.left:
            self.traverse(node.left)
        self.arr.append(node.val)
        if node.right:
            self.traverse(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()