"""
3386. Button with Longest Push Time
https://leetcode.com/problems/button-with-longest-push-time/
"""


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        result = events[0]
        prev = result[:]
        for event in events[1:]:
            if event[1] - prev[1] > result[1] or (event[1] - prev[1] == result[1] and event[0] < result[0]):
                result = [event[0], event[1] - prev[1]]
            prev = event[:]
        return result[0]
