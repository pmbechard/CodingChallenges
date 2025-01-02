"""
3300. Minimum Element After Replacement With Digit Sum
https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
"""


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([self.digit_sum(n) for n in nums])

    def digit_sum(self, n):
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total
