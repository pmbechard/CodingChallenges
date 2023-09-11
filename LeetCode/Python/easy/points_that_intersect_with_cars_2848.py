"""
2848. Points That Intersect With Cars
https://leetcode.com/problems/points-that-intersect-with-cars/
"""


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for num in nums:
            points = points.union(range(num[0], num[1] + 1))
        return len(points)
