"""
507. Perfect Number
https://leetcode.com/problems/perfect-number/
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1
        if num == 1: return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                total += i + num // i
            if total > num:
                return False
        return total == num
