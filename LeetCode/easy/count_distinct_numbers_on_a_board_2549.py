"""
2549. Count Distinct Numbers on Board
https://leetcode.com/problems/count-distinct-numbers-on-board/
"""


class Solution:
    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1
