"""
1828. Queries on Number of Points Inside a Circle
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
"""


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        results = [0] * len(queries)
        for q in range(len(queries)):
            for p in points:
                if sqrt((queries[q][0] - p[0]) ** 2 + (queries[q][1] - p[1]) ** 2) <= queries[q][2]:
                    results[q] += 1
        return results
