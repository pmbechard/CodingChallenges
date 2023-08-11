"""
389. Find the Difference
https://leetcode.com/problems/find-the-difference/
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            index = s.find(i)
            if index == -1:
                return i
            s = s[:index] + s[index+1:]
        return s
