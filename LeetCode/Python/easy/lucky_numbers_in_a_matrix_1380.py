"""
1380. Lucky Numbers in a Matrix
https://leetcode.com/problems/lucky-numbers-in-a-matrix/
"""


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        for c in range(len(matrix[0])):
            max_el = matrix[0][c]
            max_row = 0
            for r in range(1, len(matrix)):
                if matrix[r][c] > max_el:
                    max_el = matrix[r][c]
                    max_row = r
            if min(matrix[max_row]) == max_el:
                result.append(max_el)
        return result
