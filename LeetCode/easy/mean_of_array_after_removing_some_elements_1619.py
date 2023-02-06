"""
1619. Mean of Array After Removing Some Elements
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
"""


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        length = len(arr)
        arr = arr[length//20:-length//20]
        return sum(arr)/len(arr)
