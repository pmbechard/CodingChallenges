"""
3232. Find if Digit Game Can Be Won
https://leetcode.com/problems/find-if-digit-game-can-be-won/
"""


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            count = count + num if num > 9 else count - num
        return count != 0
