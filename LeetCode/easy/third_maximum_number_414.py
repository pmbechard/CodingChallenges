"""
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        return sorted(list(nums))[-3]
