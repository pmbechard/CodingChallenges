"""
2923. Find Champion I
https://leetcode.com/problems/find-champion-i/
"""


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # max_idx_sum = (-1, -1)
        # for i in range(len(grid)):
        #     if sum(grid[i]) > max_idx_sum[1]:
        #         max_idx_sum = (i, sum(grid[i]))
        # return max_idx_sum[0]

        # return sorted(grid, key=sum)[-1].index(0)

        max_idx_sum = (-1, -1)
        for i, v in enumerate([sum(x) for x in grid]):
            if v > max_idx_sum[1]:
                max_idx_sum = (i, v)
        return max_idx_sum[0]
