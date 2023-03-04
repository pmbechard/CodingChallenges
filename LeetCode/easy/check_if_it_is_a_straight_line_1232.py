"""
1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = False
        for i in range(len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]
            if x2 - x1 == 0:
                current_slope = None
            else:
                current_slope = (y2 - y1) / (x2 - x1)
            if slope == False:
                slope = current_slope
            elif current_slope != slope:
                return False
        return True
