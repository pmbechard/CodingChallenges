"""
3643. Flip Square Submatrix Vertically
https://leetcode.com/problems/flip-square-submatrix-vertically/
"""


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l, r = y, y + k - 1
        while l <= r:
            t, b = x, x + k - 1
            while t <= b:
                grid[t][l], grid[b][l] = grid[b][l], grid[t][l]
                t += 1
                b -= 1
            l += 1
        return grid
