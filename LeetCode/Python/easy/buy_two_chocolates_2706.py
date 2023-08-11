"""
2706. Buy Two Chocolates
https://leetcode.com/problems/buy-two-chocolates/
"""


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cost = sum(sorted(prices)[:2])
        return money - cost if cost <= money else money
