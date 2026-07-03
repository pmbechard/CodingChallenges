"""
3959. Check Good Integer
https://leetcode.com/problems/check-good-integer/
"""


class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        output = 0
        while n > 0:
            curr = n % 10
            n //= 10
            output += curr ** 2 - curr
        return output >= 50
