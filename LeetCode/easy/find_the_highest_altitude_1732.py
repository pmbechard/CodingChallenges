"""
1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        for i in range(1, len(gain)+1):
            if sum(gain[:i]) > highest:
                highest = sum(gain[:i])
        return highest
