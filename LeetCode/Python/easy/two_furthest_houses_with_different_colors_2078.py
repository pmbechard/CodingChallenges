"""
2078. Two Furthest Houses With Different Colors
https://leetcode.com/problems/two-furthest-houses-with-different-colors/
"""


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        diff = None
        for i in range(len(colors)):
            for j in range(len(colors) - 1, -1, - 1):
                if colors[i] != colors[j]:
                    if not diff or j - i > diff:
                        diff = j - i
        return diff
