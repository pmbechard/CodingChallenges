"""
1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/
"""


class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result
