"""
1329. Sort the Matrix Diagonally
https://leetcode.com/problems/sort-the-matrix-diagonally/
"""


class Solution:
    def __init__(self):
        self.result = [[]]

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 1 or len(mat[0]) == 1: return mat
        self.result = [[0 for y in range(len(mat[0]))] for x in range(len(mat))]
        self.result[0][-1] = mat[0][-1]
        self.result[-1][-0] = mat[-1][0]
        x = 0
        y = len(mat[0]) - 2

        for i in range(1, len(mat) + len(mat[0]) - 2):
            sorted_list = self.generateList([x, y], mat)
            self.replaceItems([x, y], sorted_list)
            if y > 0:
                y -= 1
            else:
                x += 1
        return self.result

    def generateList(self, start, mat):
        x, y = start
        output = []
        while x < len(mat) and y < len(mat[0]):
            output.append(mat[x][y])
            x += 1
            y += 1
        return sorted(output)

    def replaceItems(self, start, sorted_list):
        x, y = start
        for i in range(len(sorted_list)):
            self.result[x][y] = sorted_list[i]
            x += 1
            y += 1
