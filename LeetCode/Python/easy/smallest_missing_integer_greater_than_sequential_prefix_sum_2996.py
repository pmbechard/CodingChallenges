"""
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum
"""


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        output = sum(nums[:i])
        while output in set(nums):
            output += 1
        return output
