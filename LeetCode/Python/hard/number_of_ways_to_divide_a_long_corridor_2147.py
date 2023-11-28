"""
2147. Number of Ways to Divide a Long Corridor
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
"""
from functools import reduce


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') % 2 != 0:
            return 0
        s_count = 0
        count = 0
        outputs = []
        i = 0
        while i < len(corridor):
            if s_count == 2:
                count += 1
                if corridor[i] == 'S':
                    s_count = 1
                    outputs.append(count)
                    count = 0
            elif corridor[i] == 'S':
                s_count += 1
            i += 1
        if s_count == 2:
            outputs.append(1)
        if len(outputs) <= 1:
            return sum(outputs) % (10 ** 9 + 7)
        return reduce(lambda a, b: a * b, outputs) % (10 ** 9 + 7)
