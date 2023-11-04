"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
