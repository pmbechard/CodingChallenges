"""
790. Domino and Tromino Tiling
https://leetcode.com/problems/domino-and-tromino-tiling/
"""


class Solution:
    def numTilings(self, n: int, memo=dict()) -> int:
        if n in memo: return memo[n]
        if n <= 2: return max(0, n)
        if n == 3: return 5
        memo[n] = (self.numTilings(n - 1, memo) * 2 + self.numTilings(n - 3, memo)) % (10**9 + 7)
        return memo[n]
