"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x, lower=0, upper=(2**31)**0.5, previous=None):
        mid = (lower+upper)/2
        check = int(mid ** 2)
        if previous == check:
            return int(mid)
        if x > check:
            return self.mySqrt(x, lower=mid, upper=upper, previous=check)
        elif x < check:
            return self.mySqrt(x, lower=lower, upper=mid, previous=check)
        else:
            return int(mid)
