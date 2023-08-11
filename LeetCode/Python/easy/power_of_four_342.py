"""
342. Power of Four
https://leetcode.com/problems/power-of-four/submissions/878960707/
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        for i in range(n + 1):
            if 4 ** i == n:
                return True
            elif 4 ** i > n:
                return False
