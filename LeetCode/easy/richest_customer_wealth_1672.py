"""
1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            if sum(i) > wealth:
                wealth = sum(i)
        return wealth
