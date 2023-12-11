"""
1287. Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common()[0][0]
