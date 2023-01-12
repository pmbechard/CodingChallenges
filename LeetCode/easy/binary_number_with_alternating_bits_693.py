"""
693. Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits/
"""


import re
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        bin_num = bin(n)[2:]
        return re.fullmatch(r'(10)+1?', bin_num) or re.fullmatch(r'(01)+0?', bin_num)
