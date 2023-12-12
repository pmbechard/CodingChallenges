"""
2956. Find Common Elements Between Two Arrays
https://leetcode.com/problems/find-common-elements-between-two-arrays/
"""


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter, nums2_counter = Counter(nums1), Counter(nums2)
        a = 0
        for i in set(nums2):
            a += nums1_counter[i]
        b = 0
        for i in set(nums1):
            b += nums2_counter[i]
        return [a, b]
