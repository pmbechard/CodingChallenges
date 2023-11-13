"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return min(set(range(1, len(nums) + 2)).difference(nums))
