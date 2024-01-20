"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short, long = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        current = ''
        for i in range(1, len(short) + 1):
            if self.is_divisible(short[:i], short) and self.is_divisible(short[:i], long):
                current = short[:i]
        return current

    def is_divisible(self, short, long):
        if not short:
            return False
        return short * (len(long) // len(short)) == long
