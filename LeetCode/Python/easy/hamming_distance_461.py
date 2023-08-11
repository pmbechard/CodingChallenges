"""
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        longer = len(x) if len(x) > len(y) else len(y)
        x, y = x.zfill(longer), y.zfill(longer)
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
        return count
