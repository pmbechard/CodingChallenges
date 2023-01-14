"""
896. Monotonic Array
https://leetcode.com/problems/monotonic-array/
"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)
