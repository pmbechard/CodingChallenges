"""
3852. Smallest Pair With Different Frequencies
https://leetcode.com/problems/smallest-pair-with-different-frequencies/
"""


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freqs = Counter(nums)
        nums = sorted(set(nums))
        x = nums[0]
        for i in range(1, len(nums)):
            if freqs[x] != freqs[nums[i]]:
                return [x, nums[i]]
        return [-1, -1]
