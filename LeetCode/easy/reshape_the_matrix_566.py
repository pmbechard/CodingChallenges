"""
566. Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]): return mat
        ri, ci = 0, 0
        result = []
        for i in range(r):
            result.append([])
            for j in range(c):
                result[i].append(mat[ri][ci])
                ci += 1
                if ci >= len(mat[0]):
                    ci = 0
                    ri += 1
        return result
