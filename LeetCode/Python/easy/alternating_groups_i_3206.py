"""
3206. Alternating Groups I
https://leetcode.com/problems/alternating-groups-i/
"""


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        result = 0
        colors = [colors[-1]] + colors + [colors[0]]
        for i in range(1, len(colors) - 1):
            if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                result += 1
        return result
