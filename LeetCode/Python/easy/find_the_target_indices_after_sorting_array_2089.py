"""
2089. Find Target Indices After Sorting Array
https://leetcode.com/problems/find-target-indices-after-sorting-array/
"""


class Solution:
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        return [i for i in (range(len(nums))) if nums[i] == target]
