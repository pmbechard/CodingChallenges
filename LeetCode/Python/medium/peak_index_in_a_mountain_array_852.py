"""
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while True:
            mid = l + ((r - l) // 2)
            if mid < len(arr) and arr[mid] < arr[mid + 1]:
                l = mid + 1
            elif mid > 0 and arr[mid] < arr[mid - 1]:
                r = mid - 1
            else:
                return mid
