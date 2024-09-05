"""
874. Walking Robot Simulation
https://leetcode.com/problems/walking-robot-simulation/
"""


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = ([0, 1], [1, 0], [0, -1], [-1, 0])
        dir_i = 0
        current = (0, 0)
        furthest = 0
        obstacles = set([tuple(i) for i in obstacles])
        for c in commands:
            if 1 <= c <= 9:
                for _ in range(c):
                    new_pos = (current[0] + dirs[dir_i][0], current[1] + dirs[dir_i][1])
                    if new_pos in obstacles:
                        break
                    current = new_pos
                furthest = max(furthest, sum([i ** 2 for i in current]))
            elif c == -1:
                dir_i = (dir_i + 1) % 4
            elif c == -2:
                dir_i = (dir_i - 1) % 4
        return furthest
