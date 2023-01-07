"""
1637. Widest Vertical Area Between Two Points Containing No Points
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_values = [point[0] for point in points]
        x_values.sort()
        widest = 0
        for i in range(len(x_values) - 1):
            if x_values[i+1] - x_values[i] > widest:
                widest = x_values[i+1] - x_values[i]
        return widest
