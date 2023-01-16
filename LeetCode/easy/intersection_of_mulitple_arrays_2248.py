"""
2248. Intersection of Multiple Arrays
https://leetcode.com/problems/intersection-of-multiple-arrays/
"""


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersections = nums[0]
        for i in range(1, len(nums)):
            intersections = set(intersections).intersection(nums[i])
        return sorted(intersections)
