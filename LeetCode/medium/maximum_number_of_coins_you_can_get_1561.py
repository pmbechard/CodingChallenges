"""
1561. Maximum Number of Coins You Can Get
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
"""


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        r = len(piles) - 2
        l = 0
        total = 0
        while r > l:
            total += piles[r]
            r -= 2
            l += 1
        return total
