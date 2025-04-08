"""
3498. Reverse Degree of a String
https://leetcode.com/problems/reverse-degree-of-a-string/
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum([(i + 1) * abs(ord(s[i]) - 123) for i in range(len(s))])