"""
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def __init__(self):
        self.num = 0
        self.results = ""

    def intToRoman(self, num):
        self.num = num
        self.results = ""
        self._getRom(1000, "M", "V", "X")
        self._getRom(100, "C", "D", "M")
        self._getRom(10, "X", "L", "C")
        self._getRom(1, "I", "V", "X")
        return self.results

    def _getRom(self, base_10, one_symbol, five_symbol, ten_symbol):
        result = ""
        value = self.num // base_10
        if value == 0:
            return
        if value == 9:
            result += one_symbol + ten_symbol
        elif value >= 5:
            result += five_symbol + one_symbol * (value - 5)
        elif value == 4:
            result += one_symbol + five_symbol
        else:
            result += one_symbol * value
        self.num -= value * base_10
        self.results += result
