"""
2500. Delete Greatest Value in Each Row
https://leetcode.com/problems/delete-greatest-value-in-each-row
"""


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        while len(grid[0]) > 0:
            all_rows_max = -1
            for row in grid:
                row.sort()
                row_max = row.pop()
                if row_max > all_rows_max:
                    all_rows_max = row_max
            result += all_rows_max
        return result
