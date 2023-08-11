"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num = '{:032d}'.format(int(bin(n)[2:]))
        return int(bin_num[::-1], 2)
