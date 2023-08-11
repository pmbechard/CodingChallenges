"""
1920. Build Array from Permutation
https://leetcode.com/problems/build-array-from-permutation/
"""


class Solution:
    def buildArray(self, nums):
        result = []
        for i in nums:
            result.append(nums[i])
        return result
