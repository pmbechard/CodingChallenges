"""
67. Add Binary
https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a, b):
        a = self.to_int(a)
        b = self.to_int(b)
        return str((bin(a+b)))[2:]

    def to_int(self, x):
        x = [x for x in reversed(x)]
        sum_x = [(2 * int(x[i])) ** i for i in range(len(x))]
        if x[0] == '0':
            sum_x[0] = 0
        return sum(sum_x)
