"""
2057. Smallest Index With Equal Value
https://leetcode.com/problems/smallest-index-with-equal-value/
"""


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1
