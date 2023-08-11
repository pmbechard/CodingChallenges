"""
1544. Make The String Great
https://leetcode.com/problems/make-the-string-great/
"""


class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while len(s) > 0 and i != len(s) - 1:
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                s = s[:i] + s[i + 2:]
                i = 0
            else:
                i += 1
        return s
