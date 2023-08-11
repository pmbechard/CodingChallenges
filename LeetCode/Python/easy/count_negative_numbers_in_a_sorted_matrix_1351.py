"""
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        for i in grid:
            for j in i:
                if j < 0:
                    result += 1
        return result
