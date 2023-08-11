"""
2482. Difference Between Ones and Zeros in Row and Column
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column
"""


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        num_spaces = len(grid) + len(grid[0])
        row_sums = [sum(r) for r in grid]
        col_sums = [sum(c) for c in zip(*grid)]
        for i in range(len(grid)):
            result.append([])
            for j in range(len(grid[i])):
                result[i].append(row_sums[i] + col_sums[j] - (num_spaces - (row_sums[i] + col_sums[j])))
        return result
