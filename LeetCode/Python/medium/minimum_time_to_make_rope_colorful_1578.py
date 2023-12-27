"""
1578. Minimum Time to Make Rope Colorful
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        i = 0
        while i < len(colors):
            j = 1
            while i + j < len(colors) and colors[i] == colors[i + j]:
                j += 1
            if j > 1:
                time += sum(sorted(neededTime[i: i + j])[:-1])
            i += j
        return time
