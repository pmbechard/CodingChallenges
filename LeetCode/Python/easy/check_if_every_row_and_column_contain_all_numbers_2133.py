"""
2133. Check if Every Row and Column Contains All Numbers
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
"""


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix[0])
        cols = []
        for i in range(n):
            if len(set(matrix[i])) != n:
                return False
            for j in range(len(matrix[i])):
                if i == 0:
                    cols.append([])
                cols[j].append(matrix[i][j])
        for i in range(n):
            if len(set(cols[i])) != n:
                return False
        return True
