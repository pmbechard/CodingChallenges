"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""


class Solution:
    def runningSum(self, nums):
        running_sum = []
        for i in range(len(nums)):
            running_sum.append(sum(nums[:i+1]))
        return running_sum
