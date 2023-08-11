"""
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while '()' in s:
            i = s.index('()')
            s = s[:i] + s[i + 2:]
        return len(s)
