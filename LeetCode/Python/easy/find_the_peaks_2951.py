"""
2951. Find the Peaks
https://leetcode.com/problems/find-the-peaks/
"""


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        output = []
        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] and mountain[i + 1] < mountain[i]:
                output.append(i)
                i += 1
        return output
