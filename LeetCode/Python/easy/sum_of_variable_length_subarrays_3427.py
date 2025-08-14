"""
3427. Sum of Variable Length Subarrays
https://leetcode.com/problems/sum-of-variable-length-subarrays/
"""


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        i = 0
        while i < len(nums):
            start = max(0, i - nums[i])
            total += sum(nums[start: i + 1])
            i += 1
        return total
