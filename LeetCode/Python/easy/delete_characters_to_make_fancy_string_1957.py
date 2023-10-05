"""
1957. Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string/
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        result = s[:2]
        for i in range(2, len(s)):
            if not (result[-1] == result[-2] == s[i]):
                result += s[i]
        return result
