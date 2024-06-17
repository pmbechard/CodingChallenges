"""
633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l <= r:
            total = l ** 2 + r ** 2
            if total == c:
                return True
            elif total > c:
                r -= 1
            else:
                l += 1
        return False
