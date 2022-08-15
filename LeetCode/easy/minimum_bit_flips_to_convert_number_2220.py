"""
2220. Minimum Bit Flips to Convert Number
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = format(start, 'b')
        goal_bin = format(goal, 'b')

        if len(start_bin) < len(goal_bin):
            start_bin = "0" * (len(goal_bin) - len(start_bin)) + start_bin
        elif len(start_bin) > len(goal_bin):
            goal_bin = "0" * (len(start_bin) - len(goal_bin)) + goal_bin

        counter = 0
        for i in range(len(start_bin)):
            if goal_bin[i] != start_bin[i]:
                counter += 1
        return counter
