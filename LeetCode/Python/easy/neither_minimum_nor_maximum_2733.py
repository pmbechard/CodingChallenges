"""
2733. Neither Minimum nor Maximum
https://leetcode.com/problems/neither-minimum-nor-maximum/
"""


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return -1 if len(nums) <= 2 else sorted(nums)[1]
