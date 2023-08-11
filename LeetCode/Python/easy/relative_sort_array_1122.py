"""
1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            result += [i] * arr1.count(i)

        leftovers = []
        for i in arr1:
            if i not in result:
                leftovers.append(i)

        return result + sorted(leftovers)
