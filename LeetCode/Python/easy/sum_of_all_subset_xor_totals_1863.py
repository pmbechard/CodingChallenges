"""
1863. Sum of All Subset XOR Totals
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
"""

import itertools


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            combs = itertools.combinations(nums, i + 1)
            for comb in combs:
                current = 0
                for num in comb:
                    current ^= num
                total += current
        return total
