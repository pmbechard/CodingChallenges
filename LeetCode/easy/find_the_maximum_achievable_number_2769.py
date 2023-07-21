"""
2769. Find the Maximum Achievable Number
https://leetcode.com/problems/find-the-maximum-achievable-number/
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t
