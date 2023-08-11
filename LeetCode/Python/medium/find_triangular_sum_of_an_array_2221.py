"""
2221. Find Triangular Sum of an Array
https://leetcode.com/problems/find-triangular-sum-of-an-array/
"""


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            result = []
            for i in range(len(nums)-1):
                result.append((nums[i] + nums[i+1]) % 10)
            nums = result
        return nums[0]
