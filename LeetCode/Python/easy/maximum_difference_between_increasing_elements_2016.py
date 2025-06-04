"""
2016. Maximum Difference Between Increasing Elements
https://leetcode.com/problems/maximum-difference-between-increasing-elements/
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        sm, lg = None, -1
        diff = -1
        for num in nums:
            if sm is None or num <= sm:
                sm = num
                lg = None
            elif lg is None or num > lg:
                lg = num
                diff = max(diff, lg - sm)
        return diff
