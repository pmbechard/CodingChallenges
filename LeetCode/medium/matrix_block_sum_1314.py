"""
1314. Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/
"""

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        results = []
        for i in range(len(mat)):
            results.append([])
            r = list(range(max(0, i - k), min(len(mat), i + k + 1)))
            for j in range(len(mat[i])):
                results[i].append(0)
                c = list(range(max(0, j - k), min(len(mat[i]), j + k + 1)))
                for row in r:
                    results[i][j] += sum([mat[row][x] for x in c])
        return results
