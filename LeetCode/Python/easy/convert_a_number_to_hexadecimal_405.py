"""
405. Convert a Number to Hexadecimal
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num = 2 ** 32 + num
        elif num == 0:
            return '0'

        output = ''
        while num > 0:
            r = num % 16
            if r > 9:
                r = chr(87 + r)
            output = str(r) + output
            num //= 16
        return output
