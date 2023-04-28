"""
2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            count += grid.count(col)
        return count
