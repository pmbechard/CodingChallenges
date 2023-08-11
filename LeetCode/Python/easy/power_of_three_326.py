"""
326. Power of Three
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        elif n == 1: return True
        i = 3
        while i != n:
            if i == n: return True
            elif i > n: return False
            i *= 3
        return True
