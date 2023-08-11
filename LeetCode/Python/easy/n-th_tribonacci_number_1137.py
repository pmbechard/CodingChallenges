"""
1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1

        a = 0
        b = 1
        c = 1
        d = 0

        for i in range(3, n + 1):
            d = a + b + c
            a = b
            b = c
            c = d
        return d
