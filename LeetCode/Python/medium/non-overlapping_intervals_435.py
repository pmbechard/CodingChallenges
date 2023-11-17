"""
435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output = sorted(set([tuple(x) for x in intervals]))
        i = 0
        removed = len(intervals) - len(output)
        while i < len(output) - 1:
            if output[i][1] <= output[i + 1][0]:
                i += 1
            elif output[i + 1][1] < output[i][1]:
                del output[i]
                removed += 1
            else:
                del output[i + 1]
                removed += 1
        return removed
