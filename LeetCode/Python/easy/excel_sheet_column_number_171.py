"""
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        for i in range(len(columnTitle)):
            val += (ord(columnTitle[i]) - 64) * 26 ** (len(columnTitle) - i - 1)
        return val
