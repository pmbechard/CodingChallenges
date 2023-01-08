"""
1827. Minimum Operations to Make the Array Increasing
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                count += nums[i-1] - nums[i] + 1
                nums[i] += nums[i-1] - nums[i] + 1
        return count
