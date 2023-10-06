"""
1496. Path Crossing
https://leetcode.com/problems/path-crossing/
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        x = y = 0
        visited = {(x, y)}
        for direction in path:
            dx, dy = directions[direction]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
