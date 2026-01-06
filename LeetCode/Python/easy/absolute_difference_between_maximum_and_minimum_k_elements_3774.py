"""
3774. Absolute Difference Between Maximum and Minimum K Elements
https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/
"""


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        for i in range(k):
            total += nums[len(nums) - 1 - i] - nums[i]
        return total
