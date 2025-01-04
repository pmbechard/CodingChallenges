"""
3127. Make a Square with the Same Color
https://leetcode.com/problems/make-a-square-with-the-same-color/
"""


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        squares = [
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            [[1, 0], [1, 1], [2, 0], [2, 1]],
            [[0, 1], [0, 2], [1, 1], [1, 2]],
            [[1, 1], [1, 2], [2, 1], [2, 2]],
        ]
        for coords in squares:
            bw = 0
            for coord in coords:
                if grid[coord[0]][coord[1]] == 'B':
                    bw += 1
                else:
                    bw -= 1
            if abs(bw) >= 2:
                return True
        return False
