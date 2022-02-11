"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                if y != x and nums[x] + nums[y] == target:
                           return [x, y]
