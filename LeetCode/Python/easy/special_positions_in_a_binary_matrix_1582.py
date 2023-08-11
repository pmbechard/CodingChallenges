"""
1582. Special Positions in a Binary Matrix
https://leetcode.com/problems/special-positions-in-a-binary-matrix/
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        output = 0
        for r in range(len(mat)):
            if mat[r].count(1) == 1:
                output += 1 if self.check_column(mat, mat[r].index(1)) else 0
        return output

    def check_column(self, mat, col):
        count = 0
        for row in mat:
            if row[col] == 1:
                count += 1
        return count == 1
