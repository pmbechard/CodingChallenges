"""
292. Nim Game
https://leetcode.com/problems/nim-game/
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4
