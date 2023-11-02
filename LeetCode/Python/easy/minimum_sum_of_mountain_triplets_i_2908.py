"""
2908. Minimum Sum of Mountain Triplets I
https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/
"""


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum = None
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        curr_sum = sum([nums[i], nums[j], nums[k]])
                        if min_sum == None or curr_sum < min_sum:
                            min_sum = curr_sum
        return -1 if min_sum == None else min_sum
