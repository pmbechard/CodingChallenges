"""
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ''
        rows_result = []
        for i in range(numRows):
            rows_result.append([])
        moving_down = True
        current_row = 1
        current_index = 0
        for i in range(len(s)):
            rows_result[current_row - 1].append(s[current_index])
            if current_row == numRows:
                moving_down = False
            elif current_row == 1:
                moving_down = True
            current_row = current_row + 1 if moving_down else current_row - 1
            current_index += 1
        for arr in rows_result:
            result += ''.join(arr)
        return result
