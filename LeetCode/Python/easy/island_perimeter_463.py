"""
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += self.get_perimeter(grid, i, j)
        return perimeter

    def get_perimeter(self, grid, row, col):
        perimeter = 0
        # left
        if (col > 0 and grid[row][col - 1] == 0) or col == 0:
            perimeter += 1
        # right
        if (col < len(grid[row]) - 1 and grid[row][col + 1] == 0) or col == len(grid[row]) - 1:
            perimeter += 1
        # up
        if (row > 0 and grid[row - 1][col] == 0) or row == 0:
            perimeter += 1
        # down
        if (row < len(grid) - 1 and grid[row + 1][col] == 0) or row == len(grid) - 1:
            perimeter += 1

        return perimeter
