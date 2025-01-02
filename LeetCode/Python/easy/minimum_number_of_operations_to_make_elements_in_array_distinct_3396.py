"""
3396. Minimum Number of Operations to Make Elements in Array Distinct
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while len(set(nums)) != len(nums):
            nums = nums[3:]
            count += 1
        return count
