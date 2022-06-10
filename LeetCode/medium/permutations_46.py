"""
46. Permutations
https://leetcode.com/problems/permutations/
"""

import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [i for i in itertools.permutations(nums, len(nums))]
