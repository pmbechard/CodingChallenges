"""
593. Valid Square
https://leetcode.com/problems/valid-square/
"""


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        coords = [p1, p2, p3, p4]
        for i in range(3):
            if coords[i] in coords[i + 1:]:
                return False
        distances = set()
        distances.add(sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2))
        distances.add(sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2))
        distances.add(sqrt((p4[0] - p1[0]) ** 2 + (p4[1] - p1[1]) ** 2))
        distances.add(sqrt((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2))
        distances.add(sqrt((p4[0] - p2[0]) ** 2 + (p4[1] - p2[1]) ** 2))
        distances.add(sqrt((p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2))
        return len(distances) == 2
