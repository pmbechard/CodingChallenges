"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: x == 0)
