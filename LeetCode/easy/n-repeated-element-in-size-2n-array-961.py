"""
961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > 1:
                return num
