"""
3536. Maximum Product of Two Digits
https://leetcode.com/problems/maximum-product-of-two-digits/
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        nums = sorted([int(i) for i in str(n)])
        return nums[-1] * nums[-2]
