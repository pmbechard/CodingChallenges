"""
2373. Largest Local Values in a Matrix
https://leetcode.com/problems/largest-local-values-in-a-matrix/
"""


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # output = [[] for i in range(len(grid) - 2)]
        # for i in range(len(grid) - 2):
        #     for j in range(len(grid) - 2):
        #         output[i].append(self.getLocalMax([i, j], grid))
        # return output
        return [[self.getLocalMax([i, j], grid) for j in range(len(grid) - 2)] for i in range(len(grid) - 2)]

    def getLocalMax(self, point, grid):
        return max(max(grid[point[0]][point[1]:point[1] + 3]),
                   max(grid[point[0] + 1][point[1]:point[1] + 3]),
                   max(grid[point[0] + 2][point[1]:point[1] + 3]))
