"""
3174. Clear Digits
https://leetcode.com/problems/clear-digits/
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = ''
        for c in s:
            if c.isnumeric():
                stack = stack[:-1]
            else:
                stack += c
        return stack
