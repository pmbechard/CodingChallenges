"""
2264. Largest 3-Same-Digit Number in String
https://leetcode.com/problems/largest-3-same-digit-number-in-string/
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if f'{i}{i}{i}' in num:
                return f'{i}{i}{i}'
        return ''
