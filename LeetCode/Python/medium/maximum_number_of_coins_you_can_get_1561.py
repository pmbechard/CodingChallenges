"""
1561. Maximum Number of Coins You Can Get
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
"""


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        r = len(piles) - 2
        total = 0
        while r >= len(piles)//3:
            total += piles[r]
            r -= 2
        return total
