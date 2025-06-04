"""
3467. Transform Array by Parity
https://leetcode.com/problems/transform-array-by-parity/
"""


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        evens = [num for num in nums if num % 2 == 0]
        return ([0] * len(evens)) + ([1] * (len(nums) - len(evens)))
