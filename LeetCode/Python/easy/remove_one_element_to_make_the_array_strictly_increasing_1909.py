"""
1909. Remove One Element to Make the Array Strictly Increasing
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
"""


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            curr = nums[:i] + nums[i + 1:]
            if curr == sorted(set(curr)):
                return True
        return False
