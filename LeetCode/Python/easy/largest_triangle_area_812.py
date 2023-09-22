"""
812. Largest Triangle Area
https://leetcode.com/problems/largest-triangle-area/
"""


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    area = 0.5 * abs(
                        points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (points[k][1] - points[i][1]) +
                        points[k][0] * (points[i][1] - points[j][1]))
                    if area > max_area:
                        max_area = area
        return max_area
