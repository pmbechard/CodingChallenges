"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        count = 2
        prev = 0
        curr = 1
        while True:
            if count == n:
                return prev + curr
            curr, prev = prev + curr, curr
            count += 1
