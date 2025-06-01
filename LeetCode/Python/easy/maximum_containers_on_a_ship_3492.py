"""
3492. Maximum Containers on a Ship
https://leetcode.com/problems/maximum-containers-on-a-ship/
"""


class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(maxWeight // w, n * n)
