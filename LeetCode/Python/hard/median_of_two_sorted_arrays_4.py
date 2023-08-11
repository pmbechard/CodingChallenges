"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/872985879/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combinedList = nums1 + nums2
        combinedList.sort()
        if len(combinedList) % 2 == 1:
            return combinedList[(len(combinedList)) // 2]
        else:
            return (combinedList[len(combinedList) // 2] + combinedList[(len(combinedList) // 2) - 1]) / 2