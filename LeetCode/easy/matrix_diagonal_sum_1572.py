"""
1572. Matrix Diagonal Sum
https://leetcode.com/problems/matrix-diagonal-sum/
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l_index = 0
        r_index = len(mat[0]) - 1
        diagonal_sum = 0

        for i in range(len(mat)):
            if l_index == r_index:
                diagonal_sum += mat[i][l_index]
            else:
                diagonal_sum += mat[i][l_index] + mat[i][r_index]
            l_index += 1
            r_index -= 1

        return diagonal_sum