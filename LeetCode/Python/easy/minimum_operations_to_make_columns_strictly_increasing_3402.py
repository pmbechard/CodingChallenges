"""
3402. Minimum Operations to Make Columns Strictly Increasing
https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/
"""


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        prevs = grid[0]
        count = 0
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] <= prevs[j]:
                    prevs[j] = prevs[j] + 1
                    count += prevs[j] - grid[i][j]
                else:
                    prevs[j] = grid[i][j]
        return count

