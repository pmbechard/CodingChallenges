"""
415. Add Strings
https://leetcode.com/problems/add-strings/
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(num1 + "+" + num2))
