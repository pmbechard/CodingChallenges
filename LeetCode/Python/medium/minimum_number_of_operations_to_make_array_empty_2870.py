"""
2870. Minimum Number of Operations to Make Array Empty
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        ops = 0
        for freq in freqs.values():
            if freq == 1:
                return -1
            ops += ceil(freq / 3)
        return ops
