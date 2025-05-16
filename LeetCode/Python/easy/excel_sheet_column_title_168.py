"""
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            rem = columnNumber % 26
            if rem == 0:
                rem = 26
                columnNumber -= 1
            columnNumber //= 26
            result = chr(rem + 64) + result
        return result
