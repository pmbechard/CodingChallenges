"""
2924. Find Champion II
https://leetcode.com/problems/find-champion-ii/
"""


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        strongest = set(list(range(n))).difference([x[1] for x in edges])
        return strongest.pop() if len(strongest) == 1 else -1
