"""
1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def __init__(self):
        self.memo = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        else:
            result = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            self.memo[n] = result
            return result
