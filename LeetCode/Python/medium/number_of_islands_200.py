"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.flood(i, j, grid)
                    islands += 1
        return islands

    def flood(self, i, j, grid):
        stack = [[i, j]]
        while stack:
            current = stack.pop()
            grid[current[0]][current[1]] = '2'

            if current[1] > 0 and grid[current[0]][current[1] - 1] == '1':
                stack.append([current[0], current[1] - 1])

            if current[1] < len(grid[current[0]]) - 1 and grid[current[0]][current[1] + 1] == '1':
                stack.append([current[0], current[1] + 1])

            if current[0] > 0 and grid[current[0] - 1][current[1]] == '1':
                stack.append([current[0] - 1, current[1]])

            if current[0] < len(grid) - 1 and grid[current[0] + 1][current[1]] == '1':
                stack.append([current[0] + 1, current[1]])
