"""
1009. Complement of Base 10 Integer
https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)[2:]
        complement = ''
        for i in bin_n:
            complement += '0' if i == '1' else '1'
        return int(complement, 2)
