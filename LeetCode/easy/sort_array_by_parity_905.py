"""
905. Sort Array by Parity
https://leetcode.com/problems/sort-array-by-parity/
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
