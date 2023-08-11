"""
1779. Find Nearest Point That Has the Same X or Y Coordinate
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
"""


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        results = [i for i in points if i[0] == x or i[1] == y]
        if len(results) == 0: return -1
        closest, diff = -1, -1
        for i in results:
            curr = abs(i[0] - x) + abs(i[1] - y)
            if diff == -1 or curr < diff:
                diff = curr
                closest = i
        return points.index(closest)
