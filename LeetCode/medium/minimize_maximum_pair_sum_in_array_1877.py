"""
1877. Minimize Maximum Pair Sum in Array
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
"""


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        greatest_sum = 0
        for i in range(len(nums)//2):
            if nums[i] + nums[-1-i] > greatest_sum:
                greatest_sum = nums[i] + nums[-1-i]
        return greatest_sum
