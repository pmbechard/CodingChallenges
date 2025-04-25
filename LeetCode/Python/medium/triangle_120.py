"""
120. Triangle
https://leetcode.com/problems/triangle/
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]], pos=(0, 0)) -> int:
        if len(triangle) == 1: return triangle[0][0]
        for row in range(len(triangle) -2, -1, -1):
            for col in range(len(triangle[row])):
                left = triangle[row + 1][col]
                right = triangle[row + 1][col + 1] if col + 1 < len(triangle[row + 1]) else None
                triangle[row][col] += left if right == None else min(left, right)
        return triangle[0][0]
