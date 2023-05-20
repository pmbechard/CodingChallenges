"""
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        results = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                results[c][r] = matrix[r][c]
        return results
