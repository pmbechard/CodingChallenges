"""
3550. Smallest Index With Digit Sum Equal to Index
https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
"""


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = 0
            for s in str(nums[i]):
                val += int(s)
            if val == i:
                return i
        return -1
