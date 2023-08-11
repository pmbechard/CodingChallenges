"""
1636. Sort Array by Increasing Frequency
https://leetcode.com/problems/sort-array-by-increasing-frequency/
"""


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse=True), key=lambda x: nums.count(x))
