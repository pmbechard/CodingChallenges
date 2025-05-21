"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
        for row in rows:
            matrix[row] = [0 for i in range(len(matrix[row]))]
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
