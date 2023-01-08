"""
2485. Find the Pivot Integer
https://leetcode.com/problems/find-the-pivot-integer
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n, 0, -1):
            if sum(range(1, i + 1)) == sum(range(i, n + 1)):
                return i
        return -1
