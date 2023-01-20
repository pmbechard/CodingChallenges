"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))[:k]
