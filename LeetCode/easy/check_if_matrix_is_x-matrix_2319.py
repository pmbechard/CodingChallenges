"""
2319. Check if Matrix Is X-Matrix
https://leetcode.com/problems/check-if-matrix-is-x-matrix/
"""


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if r == c or len(grid[r]) - 1 - c == r:
                    if grid[r][c] == 0:
                        return False
                elif grid[r][c] != 0:
                    return False
        return True
