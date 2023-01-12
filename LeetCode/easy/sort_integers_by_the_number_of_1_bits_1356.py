"""
1356. Sort Integers by The Number of 1 Bits
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda x: bin(x).count('1'))
