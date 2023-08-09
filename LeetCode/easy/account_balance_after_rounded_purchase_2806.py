"""
2806. Account Balance After Rounded Purchase
https://leetcode.com/problems/account-balance-after-rounded-purchase/
"""


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = purchaseAmount / 10
        if rounded - int(rounded) == 0.5:
            rounded += 0.1
        return 100 - round(rounded) * 10
