"""
136. Single Number
https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num
