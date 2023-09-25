"""
2864. Maximum Odd Binary Number
https://leetcode.com/problems/maximum-odd-binary-number/
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        return '1' * (one_count - 1) + '0' * (len(s) - one_count) + '1'
