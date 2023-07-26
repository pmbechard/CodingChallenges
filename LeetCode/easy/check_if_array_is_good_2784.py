"""
2784. Check if Array is Good
https://leetcode.com/problems/check-if-array-is-good/
"""


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return sorted(nums) == [i for i in range(1, len(nums))] + [len(nums) - 1]
