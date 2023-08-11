"""
1800. Maximum Ascending Subarray Sum
https://leetcode.com/problems/maximum-ascending-subarray-sum/
"""


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        counter = 0
        results = [[]]
        for i in range(len(nums)):
            results[counter].append(nums[i])
            if i == len(nums) - 1 or nums[i] >= nums[i+1]:
                counter += 1
                results.append([])
        return max([sum(x) for x in results])
