"""
77. Combinations
https://leetcode.com/problems/combinations/
"""


class Solution:
    def __init__(self):
        self.combs = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.traverse([], n, k)
        return self.combs

    def traverse(self, curr, n, k):
        if len(curr) == k:
            self.combs.append(curr)
            return
        options = list(range(1 if not curr else curr[-1] + 1, n + 1))
        for option in options:
            self.traverse(curr + [option], n, k)
