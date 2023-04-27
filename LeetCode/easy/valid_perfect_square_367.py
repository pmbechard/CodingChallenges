"""
367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square_of = 1
        result = 1
        while result <= num:
            if result == num:
                return True
            square_of += 1
            result = square_of * square_of
        return False
