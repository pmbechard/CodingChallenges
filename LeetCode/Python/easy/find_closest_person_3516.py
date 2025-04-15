"""
3516. Find Closest Person
https://leetcode.com/problems/find-closest-person/
"""


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z - x) < abs(y - z): return 1
        elif abs(z - x) > abs(y - z): return 2
        else: return 0