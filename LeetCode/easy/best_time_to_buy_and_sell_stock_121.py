"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices):
        left = 0
        right = 1
        result = 0
        while right < len(prices):
            if prices[right] - prices[left] > result:
                result = prices[right] - prices[left]
            elif prices[right] < prices[left]:
                left = right
            right += 1
        return result
