"""
2006. Count Number of Pairs With Absolute Difference K
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
"""


class Solution:
    def countKDifference(self, nums, k):
        counter = 0
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x == y:
                    continue
                elif abs(nums[x] - nums[y]) == k:
                    counter += 1
        return counter // 2