"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x):
        x = str(x)
        y = ''
        for i in x[::-1]:
            if i != '-':
                y += i
        y = int(y)
        if '-' in x:
            y *= -1
        if -2**31 <= y <= 2**31 - 1:
            return y
        return 0
