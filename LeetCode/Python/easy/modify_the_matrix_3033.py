"""
3033. Modify the Matrix
https://leetcode.com/problems/modify-the-matrix/
"""


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for col in range(len(matrix[0])):
            largest = -1
            to_replace = []
            for row in range(len(matrix)):
                if matrix[row][col] == -1:
                    to_replace.append([row, col])
                largest = max(matrix[row][col], largest)
            for r in to_replace:
                matrix[r[0]][r[1]] = largest
        return matrix
