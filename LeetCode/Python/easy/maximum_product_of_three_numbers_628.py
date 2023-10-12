"""
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
