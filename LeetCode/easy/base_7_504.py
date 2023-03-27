"""
504. Base 7
https://leetcode.com/problems/base-7/
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        isNegative = False
        if num < 0:
            num *= -1
            isNegative = True
        output = ''
        while num > 0:
            output = str(num % 7) + output
            num //= 7
        return output if not isNegative else '-' + output
