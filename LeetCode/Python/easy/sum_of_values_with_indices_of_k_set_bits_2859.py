"""
2859. Sum of Values at Indices With K Set Bits
https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/
"""


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            if bin(i)[2:].count('1') == k:
                output += nums[i]
        return output
