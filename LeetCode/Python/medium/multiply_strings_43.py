"""
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = '0123456789'
        first = second = 0
        for i in range(len(num1)):
            first += nums.index(num1[i]) * 10 ** (len(num1) - i - 1)
        for i in range(len(num2)):
            second += nums.index(num2[i]) * 10 ** (len(num2) - i - 1)
        return str(first * second)
