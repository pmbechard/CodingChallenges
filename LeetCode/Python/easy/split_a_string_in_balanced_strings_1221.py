"""
1221. Split a String in Balanced Strings
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "R":
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                result += 1
        return result
