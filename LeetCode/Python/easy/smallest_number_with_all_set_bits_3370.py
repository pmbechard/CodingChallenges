"""
3370. Smallest Number With All Set Bits
https://leetcode.com/problems/smallest-number-with-all-set-bits/
"""


class Solution:
    def smallestNumber(self, n: int) -> int:
        # return int(bin(n)[2:].replace('0', '1'), 2)
        return int('1' * (len(bin(n)) - 2), 2)
