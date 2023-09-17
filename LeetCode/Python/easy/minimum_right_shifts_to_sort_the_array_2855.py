"""
2855. Minimum Right Shifts to Sort the Array
https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/
"""


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums == sorted(nums):
                return i
            nums = nums[-1:] + nums[:-1]
        return -1
