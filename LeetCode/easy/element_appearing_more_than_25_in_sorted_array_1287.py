"""
1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        set_arr = set(arr)
        for i in set_arr:
            if arr.count(i) / len(arr) > 0.25:
                return i
