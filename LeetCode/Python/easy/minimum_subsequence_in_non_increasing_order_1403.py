"""
1403. Minimum Subsequence in Non-Increasing Order
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
"""


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        size = 1
        total = sum(nums)
        nums = sorted(nums, reverse=True)
        while True:
            current_sum = sum(nums[:size])
            if current_sum > total - current_sum:
                return nums[:size]
            size += 1
