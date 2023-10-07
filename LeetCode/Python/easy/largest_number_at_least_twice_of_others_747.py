"""
747. Largest Number At Least Twice of Others
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        return nums.index(nums_sorted[-1]) if nums_sorted[-1] >= nums_sorted[-2] * 2 else -1
