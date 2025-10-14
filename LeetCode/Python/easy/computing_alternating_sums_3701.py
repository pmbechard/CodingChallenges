"""
3701. Compute Alternating Sum
https://leetcode.com/problems/compute-alternating-sum/
"""


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                output += nums[i]
            else:
                output -= nums[i]
        return output
