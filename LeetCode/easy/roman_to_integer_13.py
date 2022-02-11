"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s):
        rom_num_trans = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4,
                         'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        while s:
            for k, v in rom_num_trans.items():
                if k in s:
                    result += s.count(k) * v
                    s = s.replace(k, '')
        return result
