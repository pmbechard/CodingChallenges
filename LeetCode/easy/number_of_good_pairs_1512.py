"""
1512. Number of Good Pairs
https://leetcode.com/problems/number-of-good-pairs/
"""


class Solution:
    def numIdenticalPairs(self, nums):
        result = 0
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x < y and nums[x] == nums[y]:
                    result += 1
        return result