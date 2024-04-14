"""
3024. Type of Triangle
https://leetcode.com/problems/type-of-triangle
"""


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[2] >= nums[0] + nums[1]:
            return 'none'
        nums = set(nums)
        if len(nums) == 1:
            return 'equilateral'
        elif len(nums) == 2:
            return 'isosceles'
        return 'scalene'
