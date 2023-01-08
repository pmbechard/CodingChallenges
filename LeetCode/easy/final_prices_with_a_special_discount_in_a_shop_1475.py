"""
1475. Final Prices With a Special Discount in a Shop
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        results = prices[:]
        for i in range(len(prices) - 1):
            results[i] -= self.get_next_lowest(i, prices)
        return results

    def get_next_lowest(self, start, arr):
        for i in range(start + 1, len(arr)):
            if arr[i] <= arr[start]:
                return arr[i]
