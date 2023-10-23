"""
1089. Duplicate Zeros
https://leetcode.com/problems/duplicate-zeros/
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = arr[:]
        i1 = i2 = 0
        while i1 < len(arr):
            arr[i1] = queue[i2]
            if arr[i1] == 0 and i1 != len(arr) - 1:
                i1 += 1
                arr[i1] = queue[i2]
            i1 += 1
            i2 += 1
        return arr
