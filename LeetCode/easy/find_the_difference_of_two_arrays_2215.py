"""
2215. Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]
