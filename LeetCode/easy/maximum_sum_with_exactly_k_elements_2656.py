"""
2656. Maximum Sum With Exactly K Elements
https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
"""


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        num = max(nums)
        result = 0
        for i in range(k):
            result += num
            num += 1
        return result
