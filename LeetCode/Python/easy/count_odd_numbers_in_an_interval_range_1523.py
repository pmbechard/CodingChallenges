"""
1523. Count Odd Numbers in an Interval Range
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return low % 2
        high += high % 2
        return (high - low) - (high - low) // 2
