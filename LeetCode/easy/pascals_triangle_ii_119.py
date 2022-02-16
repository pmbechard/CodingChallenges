"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/
"""


class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        result = [1, 1]
        counter = 1
        while True:
            if counter == rowIndex:
                return result
            result = [1] + [result[i] + result[i+1] for i in range(len(result)-1)] + [1]
            counter += 1
