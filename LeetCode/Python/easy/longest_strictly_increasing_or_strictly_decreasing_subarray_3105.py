"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray
"""


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        highest = current = 1
        prev = nums[0]
        increasing = nums[0] < nums[1]
        for num in nums[1:]:
            if prev < num:
                current = current + 1 if increasing else 2
            elif prev > num:
                current = current + 1 if not increasing else 2
            else:
                current = 1

            if current > highest:
                highest = current

            increasing = prev < num
            prev = num
        return highest
