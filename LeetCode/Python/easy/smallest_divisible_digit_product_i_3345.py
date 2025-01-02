"""
3345. Smallest Divisible Digit Product I
https://leetcode.com/problems/smallest-divisible-digit-product-i/
"""


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(10):
            prod = ((n + i) // 10) * ((n + i) % 10) if (n + i) >= 10 else n + i
            if prod % t == 0:
                return n + i
