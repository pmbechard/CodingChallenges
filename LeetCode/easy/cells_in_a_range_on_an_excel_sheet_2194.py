"""
2194. Cells in a Range on an Excel Sheet
https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
"""

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        results = []
        row = int(start[1])
        col = start[0]
        while col <= end[0]:
            while row <= int(end[1]):
                results.append(f'{col}{row}')
                row += 1
            row = int(start[1])
            col = chr(ord(col)+1)
        return results
