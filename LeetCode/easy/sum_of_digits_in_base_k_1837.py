"""
1837. Sum of Digits in Base K
https://leetcode.com/problems/sum-of-digits-in-base-k
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        return sum([int(s) for s in self.changeBase(n, k)])

    def changeBase(self, num: int, base: int) -> str:
        div = num // base
        rem = num % base
        if num == 0:
            return '0'
        elif div == 0:
            return str(rem)
        return self.changeBase(div, base) + str(rem)
