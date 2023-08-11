"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n):
        a, b = 1, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        return b
