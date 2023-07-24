"""
1252. Cells with Odd Values in a Matrix
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[False for i in range(n)] for j in range(m)]

        for index in indices:
            for col in range(n):
                mat[index[0]][col] = not mat[index[0]][col]
            for row in range(m):
                mat[row][index[1]] = not mat[row][index[1]]

        count = 0
        for i in range(m):
            count += mat[i].count(True)
        return count
