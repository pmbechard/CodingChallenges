"""
807. Max Increase to Keep City Skyline
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sum = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                sum += min(max(grid[r]), max([r[c] for r in grid])) - grid[r][c]
        return sum
