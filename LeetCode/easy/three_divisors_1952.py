"""
1952. Three Divisors
https://leetcode.com/problems/three-divisors/
"""


class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(2, n):
            if n % i == 0:
                count += 1
        return count == 1
