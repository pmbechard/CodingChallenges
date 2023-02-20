"""
2190. Most Frequent Number Following Key In an Array
https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
"""


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        indices = [nums[i + 1] for i in range(len(nums) - 1) if nums[i] == key]
        return sorted(indices, key=lambda x: indices.count(x))[-1]
