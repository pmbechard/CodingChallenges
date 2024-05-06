"""
2483. Minimum Penalty for a Shop
https://leetcode.com/problems/minimum-penalty-for-a-shop
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current = score = hour = 0
        for i, c in enumerate(customers):
            current += 1 if c == 'Y' else -1
            if current > score:
                score = current
                hour = i + 1
        return hour
