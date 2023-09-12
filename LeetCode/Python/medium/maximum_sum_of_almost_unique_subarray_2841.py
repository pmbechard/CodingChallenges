"""
2841. Maximum Sum of Almost Unique Subarray
https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/
"""


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        result = 0
        for i in range(len(nums) - k + 1):
            if len(set(nums[i:i + k])) >= m and sum(nums[i:i + k]) > result:
                result = sum(nums[i:i + k])
        return result
