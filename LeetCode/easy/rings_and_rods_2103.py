"""
2103. Rings and Rods
https://leetcode.com/problems/rings-and-rods/
"""

class Solution:
    def countPoints(self, rings: str) -> int:
        output = 0
        results = dict()

        for i in range(1, len(rings), 2):
            if results.get(rings[i]):
                results[rings[i]].add(rings[i - 1])
            else:
                results[rings[i]] = {rings[i - 1]}

        for v in results.values():
            if len(v) == 3:
                output += 1

        return output
