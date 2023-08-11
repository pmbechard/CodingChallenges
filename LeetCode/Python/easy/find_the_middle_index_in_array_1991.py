"""
1991. Find the Middle Index in Array
https://leetcode.com/problems/find-the-middle-index-in-array/
"""


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            l_sum = sum(nums[:i])
            r_sum = sum(nums[i+1:])
            if l_sum == r_sum:
                return i
        return -1
