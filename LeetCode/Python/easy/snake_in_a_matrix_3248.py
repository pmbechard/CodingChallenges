"""
3248. Snake in Matrix
https://leetcode.com/problems/snake-in-matrix/
"""


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        for c in commands:
            if c == 'UP':
                y -= 1
            elif c == 'DOWN':
                y += 1
            elif c == 'LEFT':
                x -= 1
            else:
                x += 1
        return (y * n) + x
