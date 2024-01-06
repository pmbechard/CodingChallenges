"""
2335. Minimum Amount of Time to Fill Cups
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
"""


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0
        while sum(amount) > 0:
            amount.sort()
            amount[2] = max(0, amount[2] - 1)
            amount[1] = max(0, amount[1] - 1)
            count += 1
        return count
