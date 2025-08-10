"""
3622. Check Divisibility by Digit Sum and Product
https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
"""


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        o = n
        s = 0
        p = 1
        while True:
            r = n % 10
            s += r
            p *= r
            n //= 10
            if not n:
                break
        return o % (s + p) == 0
