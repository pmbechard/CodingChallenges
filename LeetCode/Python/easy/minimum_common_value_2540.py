"""
2540. Minimum Common Value
https://leetcode.com/problems/minimum-common-value/
"""


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            left, right = nums1[ptr1], nums2[ptr2]
            if left == right:
                return left
            elif left < right:
                ptr1 += 1
            else:
                ptr2 += 1
        return -1
