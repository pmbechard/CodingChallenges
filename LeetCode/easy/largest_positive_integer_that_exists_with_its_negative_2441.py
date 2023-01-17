"""
2441. Largest Positive Integer That Exists With Its Negative
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in sorted(nums, reverse=True):
            if i < 1: break
            elif -i in nums: return i
        return -1
