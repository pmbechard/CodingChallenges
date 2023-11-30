"""
2946. Matrix Similarity After Cyclic Shifts
https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
"""


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        for row in mat:
            if row[-k:] + row[:-k] != row:
                return False
        return True
