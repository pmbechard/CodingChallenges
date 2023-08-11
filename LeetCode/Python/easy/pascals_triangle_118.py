"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""


class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
        counter = 2
        while True:
            if counter == numRows:
                return result
            result += [[1] + [result[-1][i] + result[-1][i+1] for i in range(len(result[-1])-1)] + [1]]
            counter += 1
