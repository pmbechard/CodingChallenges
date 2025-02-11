"""
3442. Maximum Difference Between Even and Odd Frequency I
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
"""


class Solution:
    def maxDifference(self, s: str) -> int:
        ctr = Counter(s)
        maxes = sorted(ctr.values())
        evens = [i for i in maxes if i % 2 == 0]
        odds = [i for i in maxes if i % 2 == 1]
        return odds[-1] - evens[0]
