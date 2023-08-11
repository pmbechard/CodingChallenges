"""
2558. Take Gifts From the Richest Pile
https://leetcode.com/problems/take-gifts-from-the-richest-pile/
"""
from math import *


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort()
            gifts[-1] = floor(sqrt(gifts[-1]))
        return sum(gifts)
