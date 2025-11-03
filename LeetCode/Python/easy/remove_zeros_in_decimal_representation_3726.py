"""
3726. Remove Zeros in Decimal Representation
https://leetcode.com/problems/remove-zeros-in-decimal-representation/
"""


class Solution:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace('0', ''))
