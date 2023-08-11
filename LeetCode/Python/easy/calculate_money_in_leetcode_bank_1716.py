"""
1716. Calculate Money in Leetcode Bank
https://leetcode.com/problems/calculate-money-in-leetcode-bank/
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        total, counter = 0, 0
        for i in range(1, n+1):
            total += i % 7 + counter
            if i >= 7 and i % 7 == 0:
                total += 7
                counter += 1
        return total
