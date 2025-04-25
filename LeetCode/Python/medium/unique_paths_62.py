"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int, memo=dict()) -> int:
        if (m, n) in memo: return memo[(m, n)]
        if (m == 1 or n == 1): return 1
        count = 0
        count += self.uniquePaths(m - 1, n, memo)
        count += self.uniquePaths(m, n - 1, memo)
        memo[(m, n)] = count
        return count
