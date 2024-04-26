"""
1289. Minimum Falling Path Sum II
https://leetcode.com/problems/minimum-falling-path-sum-ii
"""


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return grid[0][0]
        (min_1, min_2) = sorted([(i, val) for i, val in enumerate(grid[0])], key=lambda x: x[1])[:2]
        for row in range(1, len(grid)):
            for col in range(len(grid[row])):
                if col != min_1[0]:
                    grid[row][col] += min_1[1]
                else:
                    grid[row][col] += min_2[1]
            (min_1, min_2) = sorted([(i, val) for i, val in enumerate(grid[row])], key=lambda x: x[1])[:2]
        return min(grid[-1])
