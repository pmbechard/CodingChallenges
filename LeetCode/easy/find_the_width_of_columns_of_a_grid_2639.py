"""
2639. Find the Width of Columns of a Grid
https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/
"""


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        result = []
        for col in range(len(grid[0])):
            max_len = 0
            for row in range(len(grid)):
                curr_len = len(str(grid[row][col]))
                if curr_len > max_len:
                    max_len = curr_len
            result.append(max_len)
        return result
