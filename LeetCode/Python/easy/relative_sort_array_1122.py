"""
1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {k: v for v, k in enumerate(arr2)}
        return sorted(arr1, key=lambda n: dic.get(n, len(arr1) + n))
