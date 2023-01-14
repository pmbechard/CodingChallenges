"""
1556. Thousand Seperator
https://leetcode.com/problems/thousand-separator/
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        return "{:,}".format(n).replace(',', '.')
