"""
1957. Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string/
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        stack = s[:2]
        for c in s[2:]:
            if c == stack[-1] == stack[-2]:
                continue
            stack += c
        return stack
