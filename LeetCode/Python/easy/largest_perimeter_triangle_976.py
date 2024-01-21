"""
976. Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        for i in range(0, len(nums) - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                result = max(result, nums[i + 1] + nums[i + 2] + nums[i])
        return result
