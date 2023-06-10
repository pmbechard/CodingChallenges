"""
2717. Semi-Ordered Permutation
https://leetcode.com/problems/semi-ordered-permutation/
"""


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        dist_l = nums.index(1)
        dist_r = len(nums) - 1 - nums.index(len(nums))
        if dist_l <= nums.index(len(nums)):
            return dist_l + dist_r
        else:
            return dist_l + dist_r - 1
