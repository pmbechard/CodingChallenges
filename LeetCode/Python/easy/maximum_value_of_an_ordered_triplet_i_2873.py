"""
2873. Maximum Value of an Ordered Triplet I
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
"""


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    max_val = max(max_val, (nums[i] - nums[j]) * nums[k])
        return max_val
