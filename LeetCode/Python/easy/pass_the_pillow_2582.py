"""
2582. Pass the Pillow
https://leetcode.com/problems/pass-the-pillow/
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        pos = 1
        while time > 0:
            if pos == n:
                direction = -1
            elif pos == 1:
                direction = 1
            pos += direction
            time -= 1
        return pos
