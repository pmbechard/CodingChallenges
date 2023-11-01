"""
2913. Subarrays Distinct Element Sum of Squares I
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
"""


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                total += len(set(nums[i:j])) ** 2
        return total
