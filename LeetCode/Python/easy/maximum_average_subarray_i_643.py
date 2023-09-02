"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = max_sum = sum(nums[0:k])
        for i in range(len(nums) - k):
            current += nums[i + k]
            current -= nums[i]
            max_sum = current if current > max_sum else max_sum
        return max_sum / k
