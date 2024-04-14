"""
3110. Score of a String
https://leetcode.com/problems/score-of-a-string
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        output = 0
        for i in range(1, len(s)):
            output += abs(ord(s[i - 1]) - ord(s[i]))
        return output
