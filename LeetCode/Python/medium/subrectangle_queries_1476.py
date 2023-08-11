"""
1476. Subrectangle Queries
https://leetcode.com/problems/subrectangle-queries/
"""


class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for x in range(row1, row2 + 1):
            for y in range(col1, col2 + 1):
                self.rectangle[x][y] = newValue

    def getValue(self, row, col):
        return self.rectangle[row][col]
