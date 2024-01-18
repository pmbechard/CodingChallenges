"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def __init__(self):
        self.memo = dict()

    def climbStairs(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 3:
            return n
        output = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if not n in self.memo:
            self.memo[n] = output
        return output
