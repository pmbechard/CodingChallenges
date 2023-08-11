"""
2022. Convert 1D Array Into 2D Array
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        return [original[i:i+n] for i in range(0, len(original), n)]
