"""
1685. Sum of Absolute Differences in a Sorted Array
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        total = r = sum(nums)
        l = 0

        for i in range(n):
            result[i] = i * nums[i] - l + r - (n - i) * nums[i]
            l += nums[i]
            r -= nums[i]
        return result
