"""
3099. Harshad Number
https://leetcode.com/problems/harshad-number
"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = sum([int(i) for i in str(x)])
        return digit_sum if x % digit_sum == 0 else -1
