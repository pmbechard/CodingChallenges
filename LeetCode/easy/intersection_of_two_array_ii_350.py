"""
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        intersection = set(nums1).intersection(nums2)
        for i in intersection:
            for j in range(min(nums1.count(i), nums2.count(i))):
                results.append(i)
        return results
