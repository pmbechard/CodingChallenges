"""
2729. Check if The Number is Fascinating
https://leetcode.com/problems/check-if-the-number-is-fascinating/
"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        return ''.join(sorted(str(n) + str(n * 2) + str(n * 3))) == '123456789'
