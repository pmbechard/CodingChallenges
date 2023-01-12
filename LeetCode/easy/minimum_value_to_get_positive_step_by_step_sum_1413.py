"""
1413. Minimum Value to Get Positive Step by Step Sum
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        smallest_sum = min([sum(nums[:i+1]) for i in range(len(nums))])
        return abs(smallest_sum) + 1 if smallest_sum < 1 else 1
